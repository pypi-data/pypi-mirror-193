import shutil
from nipype.pipeline.engine import Workflow
from nipype.interfaces.dcm2nii import Dcm2niix, Dcm2niixInputSpec
from nipype.interfaces.base import InputMultiObject
from nipype.interfaces.fsl import  (SwapDimensions, BinaryMaths, UnaryMaths, ImageStats, ProbTrackX2, 
                                    ApplyWarp, BEDPOSTX5, Threshold, ApplyMask, DilateImage,Cluster,
                                    ImageMaths,MCFLIRT,ExtractROI,SliceTimer,BET,
                                    SUSAN,FLIRT,Level1Design,FEATModel,FILMGLS,SmoothEstimate)
from nipype.interfaces.fsl.dti import BEDPOSTX5InputSpec, ProbTrackX2InputSpec
from nipype.algorithms.modelgen import SpecifyModel
from nipype.algorithms.rapidart import ArtifactDetect
from nipype import Node, MapNode
from nipype.interfaces.utility import IdentityInterface
from nipype import SelectFiles
from nipype.interfaces.freesurfer import Label2Vol
from os.path import abspath
import os,glob,math
import SWANi_supplement
from nipype.interfaces.fsl.maths import KernelInput
from nipype.interfaces.fsl.base import FSLCommand, FSLCommandInputSpec
from nipype.interfaces.base import (traits, BaseInterface, BaseInterfaceInputSpec,
                                    TraitedSpec, CommandLineInputSpec, CommandLine,
                                    InputMultiPath, File, Directory,Bunch,
                                    isdefined)
from nipype.interfaces.io import DataSink
from nipype.interfaces.utility import Merge

#SERVE NEL CONNECT PER ESTRARRE UN FILE DA UNA LISTA DI OUTPUT QUANDO L'INPUT E' SINGOLO (es. aparcaseg di reconAll)
def getn (list,index):
        return list[index]

#QUESTO NODO RESTITUISCE L'ORIENTAMENTO DELLE IMMAGINI (NEUROLOGICAL/radiological)
class OrientInputSpec(FSLCommandInputSpec):
    in_file = File(exists=True, mandatory=True, argstr="%s", position="2", desc="input image")
    _options_xor=['get_orient',"swap_orient"]
    get_orient = traits.Bool(argstr="-getorient", position="1", xor=_options_xor, desc="gets FSL left-right orientation")
    swap_orient = traits.Bool(argstr="-swaporient", position="1", xor=_options_xor, desc="swaps FSL radiological and FSL neurological")

class OrientOutputSpec(TraitedSpec):
    out_file = File(exists=True, desc="image with modified orientation")
    orient = traits.Str(desc="FSL left-right orientation")

class Orient(FSLCommand):
    _cmd = 'fslorient'
    input_spec = OrientInputSpec
    output_spec = OrientOutputSpec

    def aggregate_outputs(self, runtime=None, needed_outputs=None):

        outputs = self._outputs()
        info = runtime.stdout

        # Modified file
        if isdefined(self.inputs.swap_orient):
            outputs.out_file = self.inputs.in_file

        # Get information
        if isdefined(self.inputs.get_orient):
            outputs.orient = info

        return outputs

#REIMPLEMENTAZIONE DI DCM2NIIX PER RINOMINARE I FILE CROPPATI
class Dcm2niix_moInputSpec(Dcm2niixInputSpec):
    merge_imgs = traits.Enum(
        "2",
        "1",
        "0",
        argstr="-m %s",
        usedefault=True)

class Dcm2niix_mo(Dcm2niix):

    input_spec = Dcm2niix_moInputSpec

    def _run_interface(self, runtime):
        self.inputs.args="-w 1"
        runtime = super(Dcm2niix, self)._run_interface(
            runtime, correct_return_codes=(0, 1)
        )
        self._parse_files(self._parse_stdout(runtime.stdout))
        if len(self.bids)>0:
            os.remove(self.bids[0])
            self.bids=[]
        if self.inputs.crop == True and os.path.exists(self.output_files[0]):
            os.remove(self.output_files[0])
            os.rename(self.output_files[0].replace(".nii.gz","_Crop_1.nii.gz"),self.output_files[0])
        return runtime
    
    
    
#APPLICA LA SLICE TIMING CORRECTION SE RICHIESTO
class SliceTimer_moInputSpec(BaseInterfaceInputSpec):
    in_file = File(exists=True, mandatory=True, desc='the input image')
    time_repetition = traits.Float(mandatory=True)
    slice_timing = traits.Enum(
        0, #None
        1, #Regular up
        2, #Regular down
        3, #intervealed
        usedefault=True)

class SliceTimer_moOutputSpec(TraitedSpec):
    slice_time_corrected_file = File(desc='the output image')

class SliceTimer_mo(BaseInterface):
    input_spec = SliceTimer_moInputSpec
    output_spec = SliceTimer_moOutputSpec

    def _run_interface(self, runtime):
        out_file=self._gen_outfilename()
        if self.inputs.slice_timing==0:
            shutil.copy(self.inputs.in_file,out_file)
        else:
            fMRI_timing_correction=Node(SliceTimer(),name="fMRI_timing_correction")
            fMRI_timing_correction.inputs.time_repetition=self.inputs.time_repetition
            fMRI_timing_correction.inputs.in_file=self.inputs.in_file
            fMRI_timing_correction.inputs.out_file=out_file
            if self.inputs.slice_timing==2:
                fMRI_timing_correction.inputs.index_dir=True
            elif self.inputs.slice_timing==3:
                fMRI_timing_correction.inputs.interleaved=True
            fMRI_timing_correction.run()

        return runtime

    def _gen_outfilename(self):
        out_file = os.path.basename(self.inputs.in_file)
        return abspath(out_file)
    
    def _list_outputs(self):
        outputs = self.output_spec().get()
        outputs['slice_time_corrected_file'] = self._gen_outfilename()
        return outputs

#QUESTO NODO CONVERTE LE IMMAGINI IN RADIOLOGICAL E "RL","PA","IS"
class Orient_moInputSpec(BaseInterfaceInputSpec):
    in_file = File(exists=True, mandatory=True, desc='the input image')
    out_file = File(desc='the output image')

class Orient_moOutputSpec(TraitedSpec):
    out_file = File(desc='the output image')

class Orient_mo(BaseInterface):
    input_spec = Orient_moInputSpec
    output_spec = Orient_moOutputSpec

    def _run_interface(self, runtime):
        self.inputs.out_file=self._gen_outfilename()
        shutil.copy(self.inputs.in_file,self.inputs.out_file)
        getOrient=Orient(in_file=self.inputs.out_file)
        getOrient.inputs.get_orient=True
        res=getOrient.run()
        if res.outputs.orient=="NEUROLOGICAL":
            swap_NR=SwapDimensions()
            swap_NR.inputs.in_file=self.inputs.out_file
            swap_NR.inputs.out_file=self.inputs.out_file
            swap_NR.inputs.new_dims=("-x","y","z")
            swap_NR.run()
            swapOrient=Orient(in_file=self.inputs.out_file)
            swapOrient.inputs.swap_orient=True
            swapOrient.run()
        swap_dim=SwapDimensions()
        swap_dim.inputs.in_file=self.inputs.out_file
        swap_dim.inputs.out_file=self.inputs.out_file
        swap_dim.inputs.new_dims=("RL","PA","IS")
        swap_dim.run()

        return runtime

    def _gen_outfilename(self):
        out_file = self.inputs.out_file
        if not isdefined(out_file) and isdefined(self.inputs.in_file):
            out_file = os.path.basename(self.inputs.in_file)
        return abspath(out_file)

    def _list_outputs(self):
        outputs = self.output_spec().get()
        outputs['out_file'] = self._gen_outfilename()
        return outputs

#NODO PER IL CALCOLO GENERICO DI UN ASIMMERY INDEX DATI I DUE FILE INVERTITI
class AIndexInputSpec(BaseInterfaceInputSpec):
    in_file = File(exists=True, mandatory=True, desc='the input image')
    swapped_file = File(exists=True, mandatory=True, desc='the swapped input image')
    out_file = File(desc='the output image')

class AIndexOutputSpec(TraitedSpec):
    out_file = File(desc='the output image')

class AIndex(BaseInterface):
    input_spec = AIndexInputSpec
    output_spec = AIndexOutputSpec

    def _run_interface(self, runtime):
        self.inputs.out_file=self._gen_outfilename()

        add=BinaryMaths()
        add.inputs.in_file=self.inputs.in_file
        add.inputs.operand_file=self.inputs.swapped_file
        add.inputs.operation="add"
        add.inputs.out_file=abspath("add_"+os.path.basename(self.inputs.in_file))
        add_res=add.run()

        sub=BinaryMaths()
        sub.inputs.in_file=self.inputs.in_file
        sub.inputs.operand_file=self.inputs.swapped_file
        sub.inputs.operation="sub"
        sub.inputs.out_file=abspath("sub_"+os.path.basename(self.inputs.in_file))
        sub_res=sub.run()

        div=BinaryMaths()
        div.inputs.in_file=sub_res.outputs.out_file
        div.inputs.operand_file=add_res.outputs.out_file
        div.inputs.operation="div"
        div.inputs.out_file=self.inputs.out_file
        div.run()

        return runtime

    def _gen_outfilename(self):
        out_file = self.inputs.out_file
        if not isdefined(out_file) and isdefined(self.inputs.in_file):
            out_file = "Aindex_"+os.path.basename(self.inputs.in_file)
        return abspath(out_file)

    def _list_outputs(self):
        outputs = self.output_spec().get()
        outputs['out_file'] = self._gen_outfilename()
        return outputs

#QUESTO NODO LEGGE IL NUMERO DI VOLUMI DI UN NIFTI
class fslnvolsInputSpec(FSLCommandInputSpec):
    in_file=File(exists=True, mandatory=True, argstr="%s", position="1", desc='the input image')
    force_value=traits.Int(mandatory=False, desc='value forced by user')

class fslnvolsOutputSpec(TraitedSpec):
    nvols=traits.Int(desc="Number of EPI runs")
    
class fslnvols(FSLCommand):
    _cmd = 'fslnvols'
    input_spec = fslnvolsInputSpec
    output_spec = fslnvolsOutputSpec

    def aggregate_outputs(self, runtime=None, needed_outputs=None):
        outputs = self._outputs()
        
        #se l'utente ha inserito un valore forzo quello invece del risultato della lettura automatica
        if isdefined(self.inputs.force_value) and self.inputs.force_value!=-1:
            outputs.nvols=self.inputs.force_value
            return outputs
            
        info = runtime.stdout
        try:
            outputs.nvols=int(info)
        except:
            outputs.nvols=0            

        return outputs
    

#QUESTO NODO LEGGE IL TR DI UN NIFTI
class getNiftiTRInputSpec(FSLCommandInputSpec):
    in_file=File(exists=True, mandatory=True, argstr="%s pixdim4", position="1", desc='the input image')
    force_value=traits.Float(mandatory=False, desc='value forced by user')

class getNiftiTROutputSpec(TraitedSpec):
    TR=traits.Float(desc="Repetition Time")
    
class getNiftiTR(FSLCommand):
    _cmd = 'fslval'
    input_spec = getNiftiTRInputSpec
    output_spec = getNiftiTROutputSpec

    def aggregate_outputs(self, runtime=None, needed_outputs=None):
        outputs = self._outputs()
        
        #se l'utente ha inserito un valore forzo quello invece del risultato della lettura automatica
        if isdefined(self.inputs.force_value) and self.inputs.force_value!=-1:
            outputs.TR=self.inputs.force_value
            return outputs
            
        info = runtime.stdout
        try:
            outputs.TR=float(info)
        except:
            outputs.TR=0.          

        return outputs
    
class fMRIgenSpecInputSpec(BaseInterfaceInputSpec):
    TR=traits.Float(mandatory=True, desc="Repetition Time")
    nvols=traits.Int(mandatory=True, desc="Number of EPI runs")
    taskDuration=traits.Int(mandatory=True, desc="Task duration")
    restDuration=traits.Int(mandatory=True, desc="Rest duration")
    taskName=traits.String(mandatory=False, desc="Task name")
    hpcutoff=traits.Int(mandatory=False, desc="Cutoff for highpass filtering")
    tempMean=File(exists=True,mandatory=True,desc="mean functional image")
    
class fMRIgenSpecOutputSpec(TraitedSpec):
    hpcutoff=traits.Int(desc="Cutoff for highpass filtering")
    hp_sigma_vol=traits.Float(desc="Sigma volume for highpass filtering")
    evs_run=traits.Any(desc='task events')
    hpstring=traits.String(desc="op_string for highpass filtering")
    taskName=traits.String(desc="Task name")
    contrasts=traits.List(desc="T contrast array")
    
class fMRIgenSpec(BaseInterface):
    input_spec = fMRIgenSpecInputSpec
    output_spec = fMRIgenSpecOutputSpec
    
    def _run_interface(self, runtime):
        
        if isdefined(self.inputs.hpcutoff):
            self.hpcutoff = self.inputs.hpcutoff
        else:
            self.hpcutoff = self.inputs.taskDuration+self.inputs.restDuration
            
        self.hp_sigma_vol= self.hpcutoff/(2*self.inputs.TR)
        
        self.hpstring='-bptf %f -1 -add %s' % (self.hp_sigma_vol,self.inputs.tempMean)
        
        if not isdefined(self.inputs.taskName):
            self.inputs.taskName="Task"
            
        self.contrasts = [['%s>Rest' % self.inputs.taskName, 'T', [self.inputs.taskName], [1]]]
        
        self.evs_run=Bunch(
            conditions=[self.inputs.taskName],
            onsets=[list(range(self.inputs.restDuration, int(self.inputs.TR*self.inputs.nvols), (self.inputs.taskDuration+self.inputs.restDuration)))],
            durations=[[self.inputs.taskDuration]]
            )
        
        return runtime
    
    def _list_outputs(self):
        outputs = self.output_spec().get()
        outputs['hpcutoff'] = self.hpcutoff
        outputs['hp_sigma_vol']= self.hp_sigma_vol       
        outputs['hpstring']=self.hpstring
        outputs['evs_run']=self.evs_run
        outputs['contrasts']=self.contrasts
        outputs['taskName']=self.inputs.taskName        
        return outputs


#QUESO NODO DISCRIMINA LA FASE VENOSA DA QUELLA MORFOLOGICA DELLA PHASE CONTRAST
class VenosaCheckInputSpec(BaseInterfaceInputSpec):
    in_files=InputMultiObject(File(exists=True), desc="List of splitted file")
    out_file_venosa = File(desc='the output venous image')
    out_file_modulo = File(desc='the output anatomic image')

class VenosaCheckOutputSpec(TraitedSpec):
    out_file_venosa = File(desc='the output venous image')
    out_file_modulo = File(desc='the output anatomic image')

class VenosaCheck(BaseInterface):
    input_spec = VenosaCheckInputSpec
    output_spec = VenosaCheckOutputSpec

    def _run_interface(self, runtime):
        self.inputs.out_file_venosa=abspath("venosa.nii.gz")
        self.inputs.out_file_modulo=abspath("venosa_modulo.nii.gz")
        s0=ImageStats()
        s0.inputs.in_file=self.inputs.in_files[0]
        s0.inputs.op_string="-s"
        res0=s0.run()
        s1=ImageStats()
        s1.inputs.in_file=self.inputs.in_files[1]
        s1.inputs.op_string="-s"
        res1=s1.run()
        if res0.outputs.out_stat < res1.outputs.out_stat:
            shutil.copy(self.inputs.in_files[0], self.inputs.out_file_venosa)
            shutil.copy(self.inputs.in_files[1], self.inputs.out_file_modulo)
        else:
            shutil.copy(self.inputs.in_files[1], self.inputs.out_file_venosa)
            shutil.copy(self.inputs.in_files[0], self.inputs.out_file_modulo)

        return runtime

    def _list_outputs(self):
        outputs = self.output_spec().get()
        outputs['out_file_venosa'] = abspath("venosa.nii.gz")
        outputs['out_file_modulo'] = abspath("venosa_modulo.nii.gz")
        return outputs


def create_fMRI_pipeline(y,resultDir):
    
    inputnode = Node(
        IdentityInterface(fields=['taskName', 'nvols', 'TR', 'fMRI_dir', 'slice_timing', 'taskDuration','ref_BET','restDuration']),
        name='inputnode')
    
    fMRI = Workflow_mo(name="fMRI_%d" % y,base_dir="./")
    
    #conversione dicom->nifti
    fMRI_conv = Node(Dcm2niix_mo(),name='fMRI_conv')
    fMRI_conv.inputs.out_filename ="fMRI"
    fMRI.connect(inputnode,'fMRI_dir',fMRI_conv,'source_dir')
    #TODO ci serve riorientare la dti secondo i nostri piani standard?
    
    #leggo il numero di volumi
    fMRI_nvols=Node(fslnvols(),name="fMRI_nvols")
    fMRI.connect(inputnode,'nvols',fMRI_nvols,'force_value')
    fMRI.connect(fMRI_conv,'converted_files',fMRI_nvols,'in_file')
    
    #leggo il TR
    fMRI_getTR=Node(getNiftiTR(),name="fMRI_getTR")
    fMRI.connect(inputnode,'TR',fMRI_getTR,'force_value')
    fMRI.connect(fMRI_conv,'converted_files',fMRI_getTR,'in_file')
    
    #Convert functional images to float representation.
    fMRI_img2float = Node(ImageMaths(), name="fMRI_img2float")
    fMRI_img2float.inputs.out_data_type='float'
    fMRI_img2float.inputs.op_string=''
    fMRI_img2float.inputs.suffix='_dtype'
    fMRI.connect(fMRI_conv, 'converted_files',fMRI_img2float, 'in_file')
    
    #Extract the middle volume of the first run as the reference
    fMRI_extract_ref = Node(ExtractROI(),name="fMRI_extract_ref")
    fMRI_extract_ref.inputs.t_size=1
    #SERVE NELLA FMRI PER ESTRARRE LA FASE MEDIA DA UNA RUN EPI
    def getmiddlevolume(func):
        from nibabel import load
        funcfile = func
        if isinstance(func, list):
            funcfile = func[0]
        _, _, _, timepoints = load(funcfile).shape
        middle=int(timepoints / 2) #- 1
        return middle
    fMRI.connect(fMRI_img2float, 'out_file',fMRI_extract_ref, 'in_file')
    fMRI.connect(fMRI_conv, ('converted_files', getmiddlevolume), fMRI_extract_ref, 't_min')
                
    #Realign the functional runs to the middle volume of the first run
    fMRI_motion_correct=Node(MCFLIRT(), name="fMRI_motion_correct")
    fMRI_motion_correct.inputs.save_mats=True
    fMRI_motion_correct.inputs.save_plots=True
    fMRI_motion_correct.inputs.save_rms=True
    fMRI_motion_correct.inputs.interpolation='spline'
    fMRI.connect(fMRI_img2float, 'out_file', fMRI_motion_correct, 'in_file')
    fMRI.connect(fMRI_extract_ref, 'roi_file', fMRI_motion_correct, 'ref_file')
    
    # perform slice timing correction if needed
    fMRI_timing_correction=Node(SliceTimer_mo(),name="fMRI_timing_correction")
    fMRI.connect(fMRI_getTR,'TR',fMRI_timing_correction,'time_repetition')
    fMRI.connect(fMRI_motion_correct, 'out_file', fMRI_timing_correction, 'in_file')
    fMRI.connect(inputnode, 'slice_timing', fMRI_timing_correction, 'slice_timing')                     
    
    #Extract the mean volume of the first functional run
    fMRI_meanfunc=Node(ImageMaths(),name="fMRI_meanfunc")
    fMRI_meanfunc.inputs.op_string='-Tmean'
    fMRI_meanfunc.inputs.suffix='_mean'
    fMRI.connect(fMRI_timing_correction, 'slice_time_corrected_file', fMRI_meanfunc, 'in_file')
    
    #Strip the skull from the mean functional to generate a mask
    fMRI_meanfuncmask=Node(BET(),name="fMRI_meanfuncmask")
    fMRI_meanfuncmask.inputs.mask=True
    fMRI_meanfuncmask.inputs.no_output=True
    fMRI_meanfuncmask.inputs.frac=0.3
    fMRI.connect(fMRI_meanfunc, 'out_file', fMRI_meanfuncmask, 'in_file')
    
    #Mask the functional runs with the extracted mask
    fMRI_maskfunc=Node(ImageMaths(),name="fMRI_maskfunc")
    fMRI_maskfunc.inputs.suffix='_bet'
    fMRI_maskfunc.inputs.op_string='-mas'
    fMRI.connect(fMRI_timing_correction, 'slice_time_corrected_file', fMRI_maskfunc, 'in_file')
    fMRI.connect(fMRI_meanfuncmask, 'mask_file', fMRI_maskfunc, 'in_file2')
    
    #Determine the 2nd and 98th percentile intensities of each functional run
    fMRI_getthresh=Node(ImageStats(),name="fMRI_getthresh")
    fMRI_getthresh.inputs.op_string='-p 2 -p 98'
    fMRI.connect(fMRI_maskfunc, 'out_file', fMRI_getthresh, 'in_file')
    
    #Threshold the first run of the functional data at 10% of the 98th percentile
    fMRI_threshold=Node(ImageMaths(),name="fMRI_threshold")
    fMRI_threshold.inputs.out_data_type='char'
    fMRI_threshold.inputs.suffix='_thresh'
    #Define a function to get 10% of the intensity
    def getthreshop(thresh):
        return '-thr %.10f -Tmin -bin' % (0.1 * thresh[1])
    #Determine the median value of the functional runs using the mask
    fMRI.connect(fMRI_maskfunc, 'out_file', fMRI_threshold, 'in_file')
    fMRI.connect(fMRI_getthresh, ('out_stat', getthreshop), fMRI_threshold, 'op_string')            
    
    #Determine the median value of the functional runs using the mask
    fMRI_medianval=Node(ImageStats(),name="fMRI_medianval")
    fMRI_medianval.inputs.op_string='-k %s -p 50'
    fMRI.connect(fMRI_timing_correction, 'slice_time_corrected_file', fMRI_medianval, 'in_file')
    fMRI.connect(fMRI_threshold, 'out_file', fMRI_medianval, 'mask_file')
    
    #Dilate the mask
    fMRI_dilatemask=Node(ImageMaths(),name="fMRI_dilatemask")
    fMRI_dilatemask.inputs.suffix='_dil'
    fMRI_dilatemask.inputs.op_string='-dilF'
    fMRI.connect(fMRI_threshold, 'out_file', fMRI_dilatemask, 'in_file')
    
    #Mask the motion corrected functional runs with the dilated mask
    fMRI_maskfunc2=Node(ImageMaths(),name="fMRI_maskfunc2")
    fMRI_maskfunc2.inputs.suffix='_mask'
    fMRI_maskfunc2.inputs.op_string='-mas'
    fMRI.connect(fMRI_timing_correction, 'slice_time_corrected_file', fMRI_maskfunc2, 'in_file')
    fMRI.connect(fMRI_dilatemask, 'out_file', fMRI_maskfunc2, 'in_file2')
    
    #Determine the mean image from each functional run
    fMRI_meanfunc2=Node(ImageMaths(),name="fMRI_meanfunc2")
    fMRI_meanfunc2.inputs.op_string='-Tmean'
    fMRI_meanfunc2.inputs.suffix='_mean'
    fMRI.connect(fMRI_maskfunc2, 'out_file', fMRI_meanfunc2, 'in_file')
    
    #Merge the median values with the mean functional images into a coupled list
    fMRI_mergenode=Node(Merge(2),name="fMRI_mergenode")
    #fMRI_mergenode.inputs.axis='hstack'
    fMRI.connect(fMRI_meanfunc2, 'out_file', fMRI_mergenode, 'in1')
    fMRI.connect(fMRI_medianval, 'out_stat', fMRI_mergenode, 'in2')
    
    #Smooth each run using SUSAN with the brightness threshold set to 75% of the
    #median value for each run and a mask constituting the mean functional
    fMRI_smooth=Node(SUSAN(),name="fMRI_smooth")
    fwhm_thr = 4.9996179300001655
    #Nipype uses a different algorithm to calculate it -> float(fwhm) / np.sqrt(8 * np.log(2)). Therefore, to get 2.12314225053, fwhm should be 4.9996179300001655 instead of 5
    fMRI_smooth.inputs.fwhm=fwhm_thr
    #Define a function to get the brightness threshold for SUSAN
    def getbtthresh(medianvals):
        return 0.75 * medianvals
    def getusans(x):
        return [tuple([x[0], 0.75 * x[1]])]
    fMRI.connect(fMRI_maskfunc2, 'out_file', fMRI_smooth, 'in_file')
    fMRI.connect(fMRI_medianval, ('out_stat', getbtthresh), fMRI_smooth,'brightness_threshold')
    fMRI.connect(fMRI_mergenode, ('out', getusans), fMRI_smooth, 'usans')
    
    #Mask the smoothed data with the dilated mask
    fMRI_maskfunc3=Node(ImageMaths(),name="fMRI_maskfunc3")
    fMRI_maskfunc3.inputs.suffix='_mask'
    fMRI_maskfunc3.inputs.op_string='-mas'
    fMRI.connect(fMRI_smooth, 'smoothed_file', fMRI_maskfunc3, 'in_file')
    fMRI.connect(fMRI_dilatemask, 'out_file', fMRI_maskfunc3, 'in_file2')

    #Scale each volume of the run so that the median value of the run is set to 10000
    fMRI_intnorm=Node(ImageMaths(),name="fMRI_intnorm")
    fMRI_intnorm.inputs.suffix='_intnorm'
    #Define a function to get the scaling factor for intensity normalization
    def getinormscale(medianvals):
        return '-mul %.10f' % (10000. / medianvals)
    fMRI.connect(fMRI_maskfunc3, 'out_file', fMRI_intnorm, 'in_file')
    fMRI.connect(fMRI_medianval, ('out_stat', getinormscale), fMRI_intnorm, 'op_string')
    
    #Generate a mean functional image from the first run
    fMRI_meanfunc3=Node(ImageMaths(),name="fMRI_meanfunc3")
    fMRI_meanfunc3.inputs.op_string='-Tmean'
    fMRI_meanfunc3.inputs.suffix='_mean'
    fMRI.connect(fMRI_intnorm, 'out_file', fMRI_meanfunc3, 'in_file')
    
    #genero i valori derivati
    fMRI_genSpec=Node(fMRIgenSpec(),name="fMRI_genSpec")
    fMRI.connect(inputnode,'taskDuration',fMRI_genSpec,'taskDuration')
    fMRI.connect(inputnode,'restDuration',fMRI_genSpec,'restDuration')
    fMRI.connect(inputnode,'taskName',fMRI_genSpec,'taskName')
    fMRI.connect(fMRI_getTR,"TR",fMRI_genSpec,"TR")
    fMRI.connect(fMRI_nvols,"nvols",fMRI_genSpec,"nvols")
    fMRI.connect(fMRI_meanfunc3,"out_file",fMRI_genSpec,"tempMean")
    
    #Perform temporal highpass filtering on the data
    fMRI_highpass=Node(ImageMaths(),name="fMRI_highpass")
    fMRI_highpass.inputs.suffix='_tempfilt'
    fMRI_highpass.inputs.suffix = '_hpf'
    fMRI.connect(fMRI_genSpec, 'hpstring', fMRI_highpass, 'op_string')
    fMRI.connect(fMRI_intnorm, 'out_file', fMRI_highpass, 'in_file') 
    
    #coregister the mean functional image to the structural image
    fMRI2ref=Node(FLIRT(), name="fMRI2ref")
    fMRI2ref.inputs.out_matrix_file  = "fMRI2ref.mat"
    fMRI2ref.inputs.cost = "corratio"
    fMRI2ref.inputs.searchr_x = [-90,90]
    fMRI2ref.inputs.searchr_y = [-90,90]
    fMRI2ref.inputs.searchr_z = [-90,90]
    fMRI2ref.inputs.dof = 6
    fMRI.connect(fMRI_meanfunc2, 'out_file', fMRI2ref, 'in_file')
    fMRI.connect(inputnode,'ref_BET',fMRI2ref,'reference')
    #fMRI.sink_result(resultDir,fMRI2ref,'out_file','scene.fMRI')
    
    #Use :class:`nipype.algorithms.rapidart` to determine which of the
    #images in the functional series are outliers based on deviations in
    #intensity and/or movement.
    fMRI_art=Node(ArtifactDetect(),name="fMRI_art")
    fMRI_art.inputs.use_differences=[True, False]
    fMRI_art.inputs.use_norm=True
    fMRI_art.inputs.norm_threshold=1
    fMRI_art.inputs.zintensity_threshold=3
    fMRI_art.inputs.parameter_source='FSL'
    fMRI_art.inputs.mask_type='file'
    fMRI.connect(fMRI_motion_correct,'par_file',fMRI_art,'realignment_parameters')
    fMRI.connect(fMRI_motion_correct,'out_file',fMRI_art,'realigned_files')
    #fMRI.connect(fMRI_maskfunc2,'out_file',fMRI_art,'realigned_files')
    fMRI.connect(fMRI_dilatemask,'out_file',fMRI_art,'mask_file')

    #Use :class:`nipype.algorithms.modelgen.SpecifyModel` to generate design information.
    fMRI_modelspec=Node(SpecifyModel(),name="fMRI_modelspec")
    fMRI_modelspec.inputs.input_units = 'secs'
    fMRI.connect(fMRI_genSpec,'hpcutoff',fMRI_modelspec,'high_pass_filter_cutoff')
    fMRI.connect(fMRI_genSpec,'evs_run',fMRI_modelspec,'subject_info')
    fMRI.connect(fMRI_getTR,'TR',fMRI_modelspec,'time_repetition')
    fMRI.connect(fMRI_highpass,'out_file',fMRI_modelspec,'functional_runs')
    fMRI.connect(fMRI_art,'outlier_files',fMRI_modelspec,'outlier_files')
    fMRI.connect(fMRI_motion_correct,'par_file',fMRI_modelspec,'realignment_parameters')
    
    #Use :class:`nipype.interfaces.fsl.Level1Design` to generate a run specific fsf
    #file for analysis
    fMRI_level1design=Node(Level1Design(),name="fMRI_level1design")
    fMRI_level1design.inputs.bases = {'dgamma': {'derivs': False}}
    fMRI_level1design.inputs.model_serial_correlations = True
    fMRI.connect(fMRI_genSpec, 'contrasts', fMRI_level1design, 'contrasts')
    fMRI.connect(fMRI_getTR,'TR',fMRI_level1design,'interscan_interval')
    fMRI.connect(fMRI_modelspec,'session_info',fMRI_level1design,'session_info')
    
    #Use :class:`nipype.interfaces.fsl.FEATModel` to generate a run specific mat
    #file for use by FILMGLS
    fMRI_modelgen=Node(FEATModel(),name="fMRI_modelgen")
    fMRI.connect(fMRI_level1design,'fsf_files',fMRI_modelgen,'fsf_file')
    fMRI.connect(fMRI_level1design,'ev_files',fMRI_modelgen,'ev_files')
    
    #Use :class:`nipype.interfaces.fsl.FILMGLS` to estimate a model specified by a
    #mat file and a functional run
    fMRI_modelestimate = Node(FILMGLS(),name="fMRI_modelestimate")
    fMRI_modelestimate.inputs.smooth_autocorr=True
    fMRI_modelestimate.inputs.mask_size=5
    fMRI_modelestimate.inputs.threshold=1000
    fMRI.connect(fMRI_highpass,'out_file',fMRI_modelestimate,'in_file')
    fMRI.connect(fMRI_modelgen,'design_file',fMRI_modelestimate,'design_file')
    fMRI.connect(fMRI_modelgen,'con_file',fMRI_modelestimate,'tcon_file')
    
    #get smoothness parameters
    fMRI_smoothness = Node(SmoothEstimate(), name='fMRI_smoothness')
    fMRI.connect(fMRI_modelestimate, 'residual4d', fMRI_smoothness, 'residual_fit_file')
    def dofFromFile(dofFile):
        import os
        if os.path.exists(dofFile):
            with open(dofFile, 'r') as file:
                for line in file.readlines():
                    return int(line)
    fMRI.connect(fMRI_modelestimate, ('dof_file',dofFromFile), fMRI_smoothness, 'dof')
    fMRI.connect(fMRI_dilatemask, 'out_file', fMRI_smoothness, 'mask_file')
    
    #select all result file from filmgls output folder
    fMRI_results_select = Node(SelectFiles({'cope': 'cope*.nii.gz',
                                    'pe': 'pe*.nii.gz',
                                    'tstat': 'tstat*.nii.gz',
                                    'varcope': 'varcope*.nii.gz',
                                    'zstat': 'zstat*.nii.gz'}),
                               name="fMRI_results_select")
    fMRI.connect(fMRI_modelestimate, 'results_dir', fMRI_results_select, 'base_directory')
    
    #mask zstat with the dilated mask
    fMRI_maskfunc4=Node(ImageMaths(),name="fMRI_maskfunc4")
    fMRI_maskfunc4.inputs.suffix='_mask'
    fMRI_maskfunc4.inputs.op_string='-mas'
    fMRI.connect(fMRI_results_select, 'zstat', fMRI_maskfunc4, 'in_file')
    fMRI.connect(fMRI_dilatemask, 'out_file', fMRI_maskfunc4, 'in_file2')
    
    fMRI_cluster=Node(Cluster_mo(),name="fMRI_cluster")
    fMRI_cluster.inputs.threshold=3.1
    fMRI_cluster.inputs.connectivity=26
    fMRI_cluster.inputs.pthreshold=0.05
    #fMRI_cluster.inputs.out_threshold_file="r-fMRI_cluster_%d.nii.gz" %y
    fMRI_cluster.inputs.out_localmax_txt_file=True
    def clusterFileName(taskName,y):
        return "r-fMRI_cluster_%d_%s.nii.gz" % (y,taskName)
    
    fMRI.connect([(fMRI_genSpec, fMRI_cluster, [(('taskName', clusterFileName, y),'out_threshold_file')])])
    fMRI.connect(fMRI_maskfunc4, 'out_file', fMRI_cluster, 'in_file')
    fMRI.connect(fMRI_results_select, 'cope', fMRI_cluster, 'cope_file')
    fMRI.connect(fMRI_smoothness, 'volume', fMRI_cluster, 'volume')
    fMRI.connect(fMRI_smoothness, 'dlh', fMRI_cluster, 'dlh')
    fMRI.connect(inputnode, "ref_BET", fMRI_cluster, "std_space_file")
    fMRI.connect(fMRI2ref, "out_matrix_file", fMRI_cluster, "xfm_file")
    fMRI.sink_result(resultDir,fMRI_cluster,'threshold_file','scene.fMRI')
    
    # #Determine the threshold for cluster file
    # fMRI_getclusterthresh=Node(ImageStats(),name="fMRI_getclusterthresh")
    # fMRI_getclusterthresh.inputs.op_string='-l 0.0001 -R'
    # fMRI.connect(fMRI_cluster, 'threshold_file', fMRI_getclusterthresh, 'in_file')
    
    # #combine the statistical output of the contrast estimate and a background image into one volume
    # fMRI_overlaystats = Node(Overlay(), name="fMRI_overlaystats")
    # fMRI_overlaystats.inputs.auto_thresh_bg = True
    # fMRI_overlaystats.inputs.transparency=True
    # fMRI_overlaystats.inputs.out_type="float"
    # def array2tuple(x):
    #     return tuple(x)
    # #fMRI.connect(fMRI_extract_ref, 'roi_file', fMRI_overlaystats, 'background_image')
    # fMRI.connect(inputnode, "ref_BET", fMRI_overlaystats, "background_image")
    # fMRI.connect(fMRI_cluster, 'threshold_file', fMRI_overlaystats, 'stat_image')
    # fMRI.connect(fMRI_getclusterthresh, ('out_stat', array2tuple), fMRI_overlaystats, 'stat_thresh')
    
    # #create png image from volume
    # fMRI_slicer = Node(Slicer(), name="fMRI_slicer")
    # fMRI_slicer.inputs.all_axial = True
    # fMRI_slicer.inputs.image_width = 750
    # fMRI_slicer.inputs.out_file="fMRI_%d_activation.png" % y
    # fMRI.connect(fMRI_overlaystats, 'out_file', fMRI_slicer, 'in_file')
    # fMRI.sink_result(resultDir,fMRI_slicer,'out_file','scene.fMRI')
    
    return fMRI




#IMPLEMENTAZIONE DI PROBRACKX2 IN PARALLELO
def create_probtrackx2_pipeline(name,tract_name,resultDir):

    """
    Generates a tractography workflow for the specified tract based on app defined protocol    

    Parameters
    ----------
    name : string
        the output workflow name.
    tract_name : string
        the desired tract (allowed values: ).
    resultDir : TYPE
        DESCRIPTION.

    Returns
    -------
    wf : TYPE
        DESCRIPTION.

    """
    

    inputnode = Node(
        IdentityInterface(fields=['xfm', 'inv_xfm', 'fsamples', 'mask', 'phsamples', 'thsamples', 'mni2ref_warp', 'ref']),
        name='inputnode')

    out_fields = ['fdt_paths_rh', 'fdt_paths_lh', 'waytotal_rh', 'waytotal_lh']

    outputnode = Node(
        IdentityInterface(fields=out_fields), name='outputnode')

    wf = Workflow_mo(name=name)

    sides=["lh","rh"]

    track_loop={}
    warp_loop={}
    sumTrack={}

    #GENERO I RANDOM SEED COME NODO ALTRIMENTI OGNI ESECUZIONE CAMBIA LA CACHE DEL WORKFLOW
    randomSeed = Node(randomSeedGenerator(),name='randomSeed')
    randomSeed.inputs.seeds_n=5
    wf.connect(inputnode, "mask", randomSeed, "mask")

    for side in sides:
        track_loop[side]=[None] * 5
        protocol_dir = os.path.join(SWANi_supplement.protocol_dir,tract_name+"_"+side)

        track_loop[side] = MapNode(ProbTrackX2_mo(),name="%s_track_loop_%s"%(tract_name,side),iterfield=["rseed"])
        track_loop[side].inputs.seed = os.path.join(protocol_dir,"seed.nii.gz")
        track_loop[side].inputs.onewaycondition = True
        track_loop[side].inputs.n_samples = 1000
        track_loop[side].inputs.loop_check = True
        track_loop[side].inputs.avoid_mp = os.path.join(protocol_dir,"exclude.nii.gz")
        track_loop[side].inputs.waypoints = os.path.join(protocol_dir,"target.nii.gz")
        wf.connect(inputnode, "fsamples", track_loop[side], "fsamples")
        wf.connect(inputnode, "mask", track_loop[side], "mask")
        wf.connect(inputnode, "phsamples", track_loop[side], "phsamples")
        wf.connect(inputnode, "thsamples", track_loop[side], "thsamples")
        wf.connect(inputnode, "xfm", track_loop[side], "xfm")
        wf.connect(inputnode, "inv_xfm", track_loop[side], "inv_xfm")
        wf.connect(randomSeed, "seeds", track_loop[side], "rseed")
           
        sumTrack[side] = Node(sumMultiTracks(),name='sumTrack_%s'%(side))
        sumTrack[side].inputs.out_file="%s_%s.nii.gz"%(tract_name,side)
        wf.connect(track_loop[side], "fdt_paths", sumTrack[side], "path_files")
        wf.connect(track_loop[side], "way_total", sumTrack[side], "waytotal_files")
        wf.sink_result(resultDir,sumTrack[side],'waytotal_sum','scene.dti')
        
        warp_loop[side] = Node(ApplyWarp(), name='%s_warp_%s'%(tract_name,side))
        warp_loop[side].inputs.out_file = "r-%s_%s.nii.gz"%(tract_name,side)
        wf.connect(inputnode, "ref", warp_loop[side], "ref_file")
        wf.connect(sumTrack[side], "out_file", warp_loop[side], "in_file")
        wf.connect(inputnode, "mni2ref_warp", warp_loop[side], "field_file")
        wf.sink_result(resultDir,warp_loop[side],'out_file','scene.dti')
        
        wf.connect(warp_loop[side], "out_file", outputnode, "fdt_paths_%s"%(side))
        wf.connect(sumTrack[side], "waytotal_sum", outputnode, "waytotal_%s"%(side))
        
    return wf


#IMPLEMENTAZIONE DI SEGMENT_HA
class segmentHA_moInputSpec(CommandLineInputSpec):
    subject_id = traits.Str(
        "recon_all", mandatory=True, position=0, argstr="%s", desc="subject name", usedefault=True
    )
    subjects_dir = Directory(
        exists=True,
        mandatory=True,
        position=1,
        argstr="%s",
        hash_files=False,
        desc="path to subjects directory",
        genfile=True,
    )
    num_threads = traits.Int(argstr="")

class segmentHA_moOutputSpec(TraitedSpec):
    #lh_hippoSfVolumes = File(desc="Estimated volumes of the hippocampal substructures and of the whole hippocampus")
    #lh_amygNucVolumes = File(desc="Estimated volumes of the nuclei of the amygdala and of the whole amygdala")
    lh_hippoAmygLabels = File(desc="Discrete segmentation volumes at subvoxel resolution")
    #lh_hippoAmygLabels_hierarchy = File(desc="Segmentations with the different hierarchy levels")
    #rh_hippoSfVolumes = File(desc="Estimated volumes of the hippocampal substructures and of the whole hippocampus")
    #rh_amygNucVolumes = File(desc="Estimated volumes of the nuclei of the amygdala and of the whole amygdala")
    rh_hippoAmygLabels = File(desc="Discrete segmentation volumes at subvoxel resolution")
    #rh_hippoAmygLabels_hierarchy = File(desc="Segmentations with the different hierarchy levels")


class segmentHA_mo(CommandLine):
    _cmd = 'segmentHA_T1.sh'
    input_spec = segmentHA_moInputSpec
    output_spec = segmentHA_moOutputSpec

    def _list_outputs(self):
        base=os.path.join(self.inputs.subjects_dir,self.inputs.subject_id,"mri")
        lh=''
        rh=''

        src=glob.glob(os.path.abspath(os.path.join(base,"lh.hippoAmygLabels-T1.v[0-9][0-9].mgz")))
        if len(src)==1:
            lh=src[0]

        src=glob.glob(os.path.abspath(os.path.join(base,"rh.hippoAmygLabels-T1.v[0-9][0-9].mgz")))
        if len(src)==1:
            rh=src[0]


        # Get the attribute saved during _run_interface
        # return {'lh_hippoSfVolumes':abspath(os.path.join(base,"lh.hippoSfVolumes-T1.v21.txt:")),
        #         'rh_hippoSfVolumes':abspath(os.path.join(base,"lh.hippoSfVolumes-T1.v21.txt:")),
        #         'lh_amygNucVolumes':abspath(os.path.join(base,"lh.amygNucVolumes-T1.v21.txt")),
        #         'rh_amygNucVolumes':abspath(os.path.join(base,"rh.amygNucVolumes-T1.v21.txt")),
        #         'lh_hippoAmygLabels':abspath(os.path.join(base,"lh.hippoAmygLabels-T1.v21.mgz")),
        #         'rh_hippoAmygLabels':abspath(os.path.join(base,"/rh.hippoAmygLabels-T1.v21.mgz")),
        #         'lh_hippoAmygLabels_hierarchy':abspath(os.path.join(base,"lh.hippoAmygLabels-T1.v21.[hierarchy].mgz")),
        #         'rh_hippoAmygLabels_hierarchy':abspath(os.path.join(base,"rh.hippoAmygLabels-T1.v21.[hierarchy].mgz"))
        #         }

        return {
                'lh_hippoAmygLabels':lh,
                'rh_hippoAmygLabels':rh
                }

    def _parse_inputs(self, skip=None):
        #ABILITO LA VARIABILE PER IL MULTITHREAD E IGNORO L'INPUT
        if isdefined(self.inputs.num_threads):
            skip=["num_threads"]
            self.inputs.environ["ITK_GLOBAL_DEFAULT_NUMBER_OF_THREADS"] = "%d" % self.inputs.num_threads

        parse = super(segmentHA_mo, self)._parse_inputs(skip)

        #se è rimasto il file di lock da precedente esecuzione, lo cancello
        exPath=abspath(os.path.join(self.inputs.subjects_dir,self.inputs.subject_id,"scripts/IsRunningHPsubT1.lh+rh"))

        if os.path.exists(exPath):
                os.remove(exPath)

        return parse

#REIMPLEMENTAZIONE DI BEDPOSTX PER IGNORARE STDERR E GESTIRE MULTITHREAD
class BEDPOSTX5_moInputSpec(BEDPOSTX5InputSpec):
    num_threads = traits.Int(argstr="")

class BEDPOSTX5_mo(BEDPOSTX5):
    input_spec = BEDPOSTX5_moInputSpec

    def _run_interface(self, runtime):
        from nipype.utils.filemanip import split_filename,copyfile
        from nipype.interfaces.fsl.dti import FSLXCommand
        subjectdir = abspath(self.inputs.out_dir)
        if not os.path.exists(subjectdir):
            os.makedirs(subjectdir)
        _, _, ext = split_filename(self.inputs.mask)
        copyfile(self.inputs.mask, os.path.join(subjectdir, "nodif_brain_mask" + ext))
        _, _, ext = split_filename(self.inputs.dwi)
        copyfile(self.inputs.dwi, os.path.join(subjectdir, "data" + ext))
        copyfile(self.inputs.bvals, os.path.join(subjectdir, "bvals"))
        copyfile(self.inputs.bvecs, os.path.join(subjectdir, "bvecs"))
        if isdefined(self.inputs.grad_dev):
            _, _, ext = split_filename(self.inputs.grad_dev)
            copyfile(self.inputs.grad_dev, os.path.join(subjectdir, "grad_dev" + ext))


        self._out_dir = os.getcwd()
        retval = super(FSLXCommand, self)._run_interface(runtime)


        self._out_dir = subjectdir + ".bedpostX"
        return retval

    def _parse_inputs(self, skip=None):
        #ABILITO LA VARIABILE PER IL MULTITHREAD E IGNORO L'INPUT
        if isdefined(self.inputs.num_threads):
            skip=["num_threads"]
            self.inputs.environ["FSLPARALLEL"] = "%d" % self.inputs.num_threads

        parse = super(BEDPOSTX5_mo, self)._parse_inputs(skip)
        return parse

class ProbTrackX2_moInputSpec(ProbTrackX2InputSpec):
    rseed = traits.Int(argstr="--rseed=%s", desc="random seed")

class ProbTrackX2_mo(ProbTrackX2):
    input_spec = ProbTrackX2_moInputSpec

#NODO PER KERNEL PIU' GENERICO
class DilateImage_mo(DilateImage):
    input_spec=KernelInput

#NODO PER ESTRARRE UNA ROI DA UNA SEGMENTAZIONE CON UN DATO VALORE
class thrROIInputSpec(BaseInterfaceInputSpec):
    in_file = File(exists=True, mandatory=True, desc='the input image')
    seg_val_min = traits.Float(mandatory=True, desc='the min value of interested segmentation')
    seg_val_max = traits.Float(mandatory=True, desc='the max value of interested segmentation')
    out_file = File(desc='the output image')

class thrROIOutputSpec(TraitedSpec):
    out_file = File(desc='the output image')

class thrROI(BaseInterface):
    input_spec = thrROIInputSpec
    output_spec = thrROIOutputSpec

    def _run_interface(self, runtime):
        self.inputs.out_file=self._gen_outfilename()

        below=Threshold()
        below.inputs.in_file=self.inputs.in_file
        below.inputs.direction="below"
        below.inputs.thresh=self.inputs.seg_val_min
        below.inputs.out_file=abspath("below_"+os.path.basename(self.inputs.in_file))
        below_res=below.run()

        above=Threshold()
        above.inputs.in_file=below_res.outputs.out_file
        above.inputs.direction="above"
        above.inputs.thresh=self.inputs.seg_val_max
        above.inputs.out_file=abspath("above_"+os.path.basename(self.inputs.in_file))
        above_res=above.run()

        bin=UnaryMaths()
        bin.inputs.in_file=above_res.outputs.out_file
        bin.inputs.operation="bin"
        bin.inputs.out_file=self.inputs.out_file
        bin.run()

        return runtime

    def _gen_outfilename(self):
        out_file = self.inputs.out_file
        if not isdefined(out_file) and isdefined(self.inputs.in_file):
            out_file = "ROI_"+str(self.inputs.seg_val_min)+"_"+str(self.inputs.seg_val_min)+"_"+os.path.basename(self.inputs.in_file)
        return abspath(out_file)

    def _list_outputs(self):
        outputs = self.output_spec().get()
        outputs['out_file'] = self._gen_outfilename()
        return outputs

#NODO PER CALCOLARE Z SCORE DA ROI
class ZscoreInputSpec(BaseInterfaceInputSpec):
    in_file = File(exists=True, mandatory=True, desc='the input image')
    ROI_file = File(exists=True, mandatory=True, desc='the input image')
    out_file = File(desc='the output image')

class ZscoreOutputSpec(TraitedSpec):
    out_file = File(exists=True, desc='the output image')

class Zscore(BaseInterface):
    input_spec = ZscoreInputSpec
    output_spec = ZscoreOutputSpec

    def _run_interface(self, runtime):
        self.inputs.out_file=self._gen_outfilename()

        mask=ApplyMask()
        mask.inputs.in_file=self.inputs.in_file
        mask.inputs.mask_file=self.inputs.ROI_file
        mask.inputs.out_file=abspath("mask_"+os.path.basename(self.inputs.in_file))
        res_mask=mask.run()

        mean=ImageStats()
        mean.inputs.in_file=res_mask.outputs.out_file
        mean.inputs.op_string="-M"
        mean_res=mean.run()

        sd=ImageStats()
        sd.inputs.in_file=res_mask.outputs.out_file
        sd.inputs.op_string="-S"
        sd_res=sd.run()

        sub=BinaryMaths()
        sub.inputs.in_file=self.inputs.in_file
        sub.inputs.operation="sub"
        sub.inputs.operand_value=mean_res.outputs.out_stat
        sub_res=sub.run()

        div=BinaryMaths()
        div.inputs.in_file=sub_res.outputs.out_file
        div.inputs.operation="div"
        div.inputs.operand_value=sd_res.outputs.out_stat
        div.inputs.out_file=self.inputs.out_file
        div.run()

        return runtime

    def _gen_outfilename(self):
        out_file = self.inputs.out_file
        if not isdefined(out_file) and isdefined(self.inputs.in_file):
            out_file = "zscore_"+os.path.basename(self.inputs.in_file)
        return abspath(out_file)

    def _list_outputs(self):
        outputs = self.output_spec().get()
        outputs['out_file'] = self._gen_outfilename()
        return outputs

#QUESO NODO GENERA UNA LISTA DI SEED RANDOM
class randomSeedGeneratorInputSpec(BaseInterfaceInputSpec):
    seeds_n=traits.Int(mandatory=True, desc="The number of needed seeds")
    mask=File(mandatory=True, exists=True, desc="Just for depend")

class randomSeedGeneratorOutputSpec(TraitedSpec):
    seeds = traits.List(desc='the list of seeds')

class randomSeedGenerator(BaseInterface):
    input_spec = randomSeedGeneratorInputSpec
    output_spec = randomSeedGeneratorOutputSpec
    seedlist =[]

    def _run_interface(self, runtime):
        from random import randrange
        for x in range(self.inputs.seeds_n):
            self.seedlist.append(randrange(1000))


    def _list_outputs(self):
        outputs = self.output_spec().get()
        outputs['seeds'] = self.seedlist
        return outputs

#nodo per rimozione outliers nel DOmap
class DOmap_outliers_mask_moInputSpec(BaseInterfaceInputSpec):
    in_file=File(exists=True, mandatory=True, desc='the input image')
    mask_file=File(exists=True, mandatory=True, desc='the original mask image')
    out_file = File(desc='the output mask name')

class DOmap_outliers_mask_moOutputSpec(TraitedSpec):
    out_file = File(exists=True, desc='the output image')

class DOmap_outliers_mask_mo(BaseInterface):
    input_spec = DOmap_outliers_mask_moInputSpec
    output_spec = DOmap_outliers_mask_moOutputSpec

    def _run_interface(self, runtime):
        self.inputs.out_file=self._gen_outfilename()

        mean=ImageStats()
        mean.inputs.in_file=self.inputs.in_file
        mean.inputs.op_string="-M"
        mean_res=mean.run()

        meanValue=math.trunc(mean_res.outputs.out_stat)

        if meanValue<=100:
            threshold=meanValue+1
            thr=Threshold()
            thr.inputs.in_file=self.inputs.in_file
            thr.inputs.thresh=threshold
            thr_res=thr.run()

            bin=UnaryMaths()
            bin.inputs.in_file=thr_res.outputs.out_file
            bin.inputs.operation="bin"
            bin_res=bin.run()

            sub=BinaryMaths()
            sub.inputs.in_file=self.inputs.mask_file
            sub.inputs.operation="sub"
            sub.inputs.operand_file=bin_res.outputs.out_file
            sub.inputs.out_file=self.inputs.out_file
            sub.run()
        else:
            shutil.copy(self.inputs.mask_file,self.inputs.out_file)

        return runtime

    def _gen_outfilename(self):
        out_file = self.inputs.out_file
        if not isdefined(out_file):
            out_file = "brain_cortex_mas_refined.nii.gz"
        return abspath(out_file)

    def _list_outputs(self):
        outputs = self.output_spec().get()
        outputs['out_file'] = self._gen_outfilename()
        return outputs


#SOMMA UNA LISTA DI VOLUMI
class sumMultiTracksInputSpec(BaseInterfaceInputSpec):
    path_files= InputMultiPath(File(exists=True), mandatory=True, desc="list of path file to sum togheter")
    waytotal_files= InputMultiPath(File(exists=True), mandatory=True, desc="list of waytotal files to sum togheter")
    out_file = File(desc='the output image')

class sumMultiTracksOutputSpec(TraitedSpec):
    out_file = File(exists=True, desc='the output image')
    waytotal_sum = File(exists=True, desc='the output waytotal file')

class sumMultiTracks(BaseInterface):
    input_spec = sumMultiTracksInputSpec
    output_spec = sumMultiTracksOutputSpec

    def _run_interface(self, runtime):
        self.inputs.out_file=self._gen_outfilename()
        waytotal_sum_file=self._gen_waytotal_outfilename()

        steps=len(self.inputs.path_files)-1
        sum=[None] * steps
        sum_res=[None] * steps

        waytotal_sum=0

        for x in range(steps):

            #SUM FTP_PATHS
            sum[x] = BinaryMaths()
            sum[x].inputs.operation="add"

            if x==0:
                sum[x].inputs.in_file=self.inputs.path_files[x]
            else:
                sum[x].inputs.in_file=sum_res[(x-1)].outputs.out_file

            sum[x].inputs.operand_file=self.inputs.path_files[(x+1)]

            if x==(steps-1):
                sum[x].inputs.out_file=self.inputs.out_file

            sum_res[x]=sum[x].run()

            #SUM WAYTOTAL
            if os.path.exists(self.inputs.waytotal_files[x]):
                with open(self.inputs.waytotal_files[x], 'r') as file:
                    for line in file.readlines():
                        waytotal_sum+=int(line)

        with open(waytotal_sum_file, "w") as file:
            file.write(str(waytotal_sum))

        return runtime

    def _gen_outfilename(self):
        out_file = self.inputs.out_file
        if not isdefined(out_file):
            out_file = "sum.nii.gz"
        return abspath(out_file)

    def _gen_waytotal_outfilename(self):
        out_file = os.path.basename(self.inputs.out_file)
        if not isdefined(out_file):
            out_file = "waytotal"
        else:
            out_file=out_file.replace(".nii.gz","")+"_waytotal"
        return abspath(out_file)

    def _list_outputs(self):
        outputs = self.output_spec().get()
        outputs['out_file'] = self._gen_outfilename()
        outputs['waytotal_sum'] = self._gen_waytotal_outfilename()
        return outputs


class Label2Vol_mo(Label2Vol):

        def _list_outputs(self):
            outputs=super(Label2Vol_mo, self)._list_outputs()
            outputs["vol_label_file"] = abspath(outputs["vol_label_file"])
            return outputs
        
class Cluster_mo(Cluster):
    _cmd = "fsl-cluster"

class Workflow_mo(Workflow):
    def get_node_array(self):
            """List names of all nodes in a workflow"""
            from  networkx import topological_sort

            outlist = {}
            for node in topological_sort(self._graph):
                if isinstance(node, Workflow):
                    outlist[node.name]=node.get_node_array()
                elif not isinstance(node.interface, IdentityInterface):
                        outlist[node.name]={}
            return outlist

    def sink_result(self,savePath,resultNode,resultName,subfolder,regexp_substitutions=None):

        datasink = Node(DataSink(), name='SaveResults_'+resultNode.name+"_"+resultName.replace(".","_"))
        datasink.inputs.base_directory = savePath

        if regexp_substitutions!=None:
            datasink.inputs.regexp_substitutions=regexp_substitutions

        #self.add_nodes([datasink])

        self.connect(resultNode, resultName, datasink, subfolder)
