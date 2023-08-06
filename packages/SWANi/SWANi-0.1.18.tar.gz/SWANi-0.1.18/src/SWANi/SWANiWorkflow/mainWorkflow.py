import os
from multiprocessing import cpu_count
from os.path import abspath

import SWANi_supplement
from nipype.interfaces.freesurfer import ReconAll, SampleToSurface
from nipype.interfaces.fsl import (BET, FLIRT, ConvertXFM, IsotropicSmooth, FNIRT, InvWarp,
                                   ApplyWarp, Split, ApplyMask, ExtractROI, EddyCorrect, DTIFit,
                                   ConvertWarp, BinaryMaths, FAST, ImageStats, ImageMaths)
from nipype.interfaces.utility import Merge
from nipype.pipeline.engine import Node

from ..SWANiWorkflow.SWANiLib import (Workflow_mo, create_probtrackx2_pipeline, Dcm2niix_mo, Orient_mo,
                                      SwapDimensions, segmentHA_mo, Label2Vol_mo, thrROI, AIndex, Zscore,
                                      VenosaCheck, BEDPOSTX5_mo, getn, DilateImage_mo, DOmap_outliers_mask_mo,
                                      create_fMRI_pipeline)

#TODO implementazione error manager
#todo valutare nome parlante per node
class SWANi_wf(Workflow_mo):

    #TODO forse non serve, valutare eliminazione
    def __init__(self, name, base_dir=None):
        super(SWANi_wf, self).__init__(name, base_dir)

    def add_input_folders(self, SWANiGlobalConfig, ptConfig, check_input, freesurfer):

        #SWANiGlobalConfig: configurazione globale dell'app
        #ptConfig: configurazione specifica del paziente
        #check_input dictionary che ha come key tutte le possibili serie caricabili ciascuna con valore true/false
        #freesurfer: array con 2 boleani per presenza di freesurfer e del runtime di matlab
        #todo valutare conversione di freesurfer in classe dedicata

        if not check_input['mr_t13d']:
            return

        #definizione dei boleani che saranno checkati prima della definizione dei specifici workflow
        isfreesurfer = freesurfer[0] and ptConfig.getboolean('WF_OPTION', 'freesurfer')
        isHippoAmygLabels = freesurfer[1] and ptConfig.getboolean('WF_OPTION', 'hippoAmygLabels')
        DOmap = ptConfig.getboolean('WF_OPTION', 'DOmap') and check_input['mr_flair3d']
        ai = ptConfig.getboolean('WF_OPTION', 'ai')
        tractography = ptConfig.getboolean('WF_OPTION', 'tractography')
        flair2D = SWANiGlobalConfig.getboolean('OPTIONAL_SERIES', 'mr_flair2d')

        #definizione dei core assegnati al workflow e a ciascun nodo del workflow
        self.max_cpu = SWANiGlobalConfig.getint('MAIN', 'maxPtCPU')
        if self.max_cpu > 0:
            max_node_cpu = max(int(self.max_cpu / 2), 1)
        else:
            max_node_cpu = max(int((cpu_count() - 2) / 2), 1)

        # ELABORAZIONE T1 3D
        t1 = Workflow_mo(name="t13d", base_dir="./")
        self.add_nodes([t1])

        # coversione dicom->nifti
        ref_dir = os.path.join(self.base_dir, SWANiGlobalConfig['DEFAULTFOLDERS']['default_mr_t13d_folder'])
        ref_conv = Node(Dcm2niix_mo(), name='ref_conv')
        ref_conv.inputs.source_dir = ref_dir
        ref_conv.inputs.crop = True
        ref_conv.inputs.out_filename = "ref"

        # orientamento in convenzione radiologica
        ref_reOrient = Node(Orient_mo(), name='ref_reOrient')
        t1.connect(ref_conv, "converted_files", ref_reOrient, "in_file")
        t1.sink_result(self.base_dir, ref_reOrient, 'out_file', 'scene')

        # rimozione dello scalpo
        ref_BET = Node(BET(), name='ref_BET')
        ref_BET.inputs.frac = 0.5
        ref_BET.inputs.mask = True
        ref_BET.inputs.robust = True
        ref_BET.inputs.threshold = True
        t1.connect(ref_reOrient, "out_file", ref_BET, "in_file")
        t1.sink_result(self.base_dir, ref_BET, 'out_file', 'scene')

        # REGISTRAZIONE AD ALTANTE MNI (SOLO PER I FASCI!)
        if check_input['mr_dti']:
            mni = Workflow_mo(name="mni", base_dir="./")

            # registrazione lineare
            ref2mni_FLIRT = Node(FLIRT(), name='ref2mni_FLIRT')
            mni_path = abspath(os.path.join(os.environ["FSLDIR"], 'data/standard/MNI152_T1_2mm_brain.nii.gz'))
            ref2mni_FLIRT.inputs.reference = mni_path
            ref2mni_FLIRT.inputs.cost = "mutualinfo"
            ref2mni_FLIRT.inputs.searchr_x = [-90, 90]
            ref2mni_FLIRT.inputs.searchr_y = [-90, 90]
            ref2mni_FLIRT.inputs.searchr_z = [-90, 90]
            ref2mni_FLIRT.inputs.dof = 12
            ref2mni_FLIRT.inputs.cost = "corratio"
            ref2mni_FLIRT.inputs.out_matrix_file = "ref2mni.mat"
            mni.add_nodes([ref2mni_FLIRT])
            self.connect(t1, "ref_BET.out_file", mni, "ref2mni_FLIRT.in_file")

            # registrazione non lineare
            ref2mni_FNIRT = Node(FNIRT(), name='ref2mni_FNIRT')
            ref2mni_FNIRT.inputs.ref_file = mni_path
            ref2mni_FNIRT.inputs.fieldcoeff_file = True
            mni.connect(ref2mni_FLIRT, "out_matrix_file", ref2mni_FNIRT, "affine_file")
            self.connect(t1, "ref_BET.out_file", mni, "ref2mni_FNIRT.in_file")

            # matrice inversa da atlante mni a ref
            ref2mni_INVWARP = Node(InvWarp(), name='ref2mni_INVWARP')
            mni.connect(ref2mni_FNIRT, "fieldcoeff_file", ref2mni_INVWARP, "warp")
            self.connect(t1, "ref_BET.out_file", mni, "ref2mni_INVWARP.reference")

        # REGISTRAZIONE AD ALTANTE MNI1mm (SERVE SOLO PER DOmap)
        if DOmap:
            mni1 = Workflow_mo(name="mni1", base_dir="./")

            # registrazione lineare
            ref2mni1_FLIRT = Node(FLIRT(), name='ref2mni1_FLIRT')
            mni1_path = abspath(os.path.join(os.environ["FSLDIR"], 'data/standard/MNI152_T1_1mm_brain.nii.gz'))
            ref2mni1_FLIRT.inputs.reference = mni1_path
            ref2mni1_FLIRT.inputs.cost = "mutualinfo"
            ref2mni1_FLIRT.inputs.searchr_x = [-90, 90]
            ref2mni1_FLIRT.inputs.searchr_y = [-90, 90]
            ref2mni1_FLIRT.inputs.searchr_z = [-90, 90]
            ref2mni1_FLIRT.inputs.dof = 12
            ref2mni1_FLIRT.inputs.cost = "corratio"
            ref2mni1_FLIRT.inputs.out_matrix_file = "ref2mni1.mat"
            mni1.add_nodes([ref2mni1_FLIRT])
            self.connect(t1, "ref_BET.out_file", mni1, "ref2mni1_FLIRT.in_file")

            # registrazione non lineare
            ref2mni1_FNIRT = Node(FNIRT(), name='ref2mni1_FNIRT')
            ref2mni1_FNIRT.inputs.ref_file = mni1_path
            ref2mni1_FNIRT.inputs.fieldcoeff_file = True
            mni1.connect(ref2mni1_FLIRT, "out_matrix_file", ref2mni1_FNIRT, "affine_file")
            self.connect(t1, "ref_BET.out_file", mni1, "ref2mni1_FNIRT.in_file")

            # matrice inversa da atlante mni a ref
            ref2mni1_INVWARP = Node(InvWarp(), name='ref2mni1_INVWARP')
            mni1.connect(ref2mni1_FNIRT, "fieldcoeff_file", ref2mni1_INVWARP, "warp")
            self.connect(t1, "ref_BET.out_file", mni1, "ref2mni1_INVWARP.reference")

        # REGISTRAZIONE AD ALTANTE SIMMETRICO PER EVENTUALI ASIMMETRY index
        if ai and (check_input['mr_asl'] or check_input['pet_brain']):
            sym = Workflow_mo(name="sym", base_dir="./")

            # registrazione lineare
            ref2sym_FLIRT = Node(FLIRT(), name='ref2sym_FLIRT')
            sym_template = SWANi_supplement.sym_template
            ref2sym_FLIRT.inputs.reference = sym_template
            ref2sym_FLIRT.inputs.cost = "mutualinfo"
            ref2sym_FLIRT.inputs.searchr_x = [-90, 90]
            ref2sym_FLIRT.inputs.searchr_y = [-90, 90]
            ref2sym_FLIRT.inputs.searchr_z = [-90, 90]
            ref2sym_FLIRT.inputs.dof = 12
            ref2sym_FLIRT.inputs.cost = "corratio"
            ref2sym_FLIRT.inputs.out_matrix_file = "ref2sym.mat"
            sym.add_nodes([ref2sym_FLIRT])
            self.connect(t1, "ref_BET.out_file", sym, "ref2sym_FLIRT.in_file")

            # registrazione non lineare
            ref2sym_FNIRT = Node(FNIRT(), name='ref2sym_FNIRT')
            ref2sym_FNIRT.inputs.ref_file = sym_template
            ref2sym_FNIRT.inputs.fieldcoeff_file = True
            sym.connect(ref2sym_FLIRT, "out_matrix_file", ref2sym_FNIRT, "affine_file")
            self.connect(t1, "ref_BET.out_file", sym, "ref2sym_FNIRT.in_file")

            # matrice inversa da atlante simmetrico a ref
            ref2sym_INVWARP = Node(InvWarp(), name='ref2sym_INVWARP')
            sym.connect(ref2sym_FNIRT, "fieldcoeff_file", ref2sym_INVWARP, "warp")
            self.connect(t1, "ref_BET.out_file", sym, "ref2sym_INVWARP.reference")

            # immagine ribaltata in RL del soggetto nello spazio dell'atlante simmetrico
            sym_SWAP = Node(SwapDimensions(), name='sym_SWAP')
            sym_SWAP.inputs.out_file = "sym_ref_brain_swapped.nii.gz"
            sym_SWAP.inputs.new_dims = ("-x", "y", "z")
            sym.connect(ref2sym_FNIRT, "warped_file", sym_SWAP, "in_file")

            # trasformazione lineare dell'immagine ribaltata sull'originale
            swap2sym_FLIRT = Node(FLIRT(), name='swap2sym_FLIRT')
            swap2sym_FLIRT.inputs.cost = "mutualinfo"
            swap2sym_FLIRT.inputs.searchr_x = [-90, 90]
            swap2sym_FLIRT.inputs.searchr_y = [-90, 90]
            swap2sym_FLIRT.inputs.searchr_z = [-90, 90]
            swap2sym_FLIRT.inputs.dof = 6
            swap2sym_FLIRT.inputs.interp = "trilinear"
            swap2sym_FLIRT.inputs.out_matrix_file = "swap2sym.mat"
            sym.connect(sym_SWAP, "out_file", swap2sym_FLIRT, "in_file")
            sym.connect(ref2sym_FNIRT, "warped_file", swap2sym_FLIRT, "reference")

            # trasformazione non lineare dell'immagine ribaltata sull'originale
            swap2sym_FNIRT = Node(FNIRT(), name='swap2sym_FNIRT')
            swap2sym_FNIRT.inputs.fieldcoeff_file = True
            swap2sym_FNIRT.inputs.ref_file = sym_template
            sym.connect(sym_SWAP, "out_file", swap2sym_FNIRT, "in_file")
            sym.connect(swap2sym_FLIRT, "out_matrix_file", swap2sym_FNIRT, "affine_file")
            sym.connect(ref2sym_FNIRT, "warped_file", swap2sym_FNIRT, "ref_file")

        # ELABORAZIONE FREESURFER
        if isfreesurfer:

            freesurfer = Workflow_mo(name="freesurfer", base_dir="./")

            # recon all
            reconAll = Node(ReconAll(), name='reconAll')
            reconAll.inputs.subjects_dir = self.base_dir
            reconAll.inputs.subject_id = "FS"
            reconAll.inputs.openmp = max_node_cpu
            reconAll.inputs.parallel = True
            reconAll.inputs.directive = 'all'
            freesurfer.add_nodes([reconAll])
            self.connect(t1, "ref_conv.converted_files", freesurfer, "reconAll.T1_files")
            freesurfer.sink_result(self.base_dir, reconAll, 'pial', 'scene')
            freesurfer.sink_result(self.base_dir, reconAll, 'white', 'scene')

            # sposto aparcaseg nello spazio ref
            aparaseg2Volmgz = Node(Label2Vol_mo(), name="aparaseg2Volmgz")
            aparaseg2Volmgz.inputs.vol_label_file = "./r-aparc_aseg.mgz"
            freesurfer.connect(reconAll, "rawavg", aparaseg2Volmgz, "template_file")
            freesurfer.connect([(reconAll, aparaseg2Volmgz, [(('aparc_aseg', getn, 0), 'reg_header')])])
            freesurfer.connect([(reconAll, aparaseg2Volmgz, [(('aparc_aseg', getn, 0), 'seg_file')])])
            freesurfer.connect(reconAll, "subjects_dir", aparaseg2Volmgz, "subjects_dir")
            freesurfer.connect(reconAll, "subject_id", aparaseg2Volmgz, "subject_id")
            freesurfer.sink_result(self.base_dir, aparaseg2Volmgz, 'vol_label_file', 'scene')

            aparaseg2Volnii = Node(Label2Vol_mo(), name="aparaseg2Volnii")
            aparaseg2Volnii.inputs.vol_label_file = "r-aparc_aseg.nii.gz"
            freesurfer.connect(reconAll, "rawavg", aparaseg2Volnii, "template_file")
            freesurfer.connect([(reconAll, aparaseg2Volnii, [(('aparc_aseg', getn, 0), 'reg_header')])])
            freesurfer.connect([(reconAll, aparaseg2Volnii, [(('aparc_aseg', getn, 0), 'seg_file')])])

            # estrazione ROI sostanza bianca
            lhwmROI = Node(thrROI(), name='lhwmROI')
            lhwmROI.inputs.seg_val_min = 2
            lhwmROI.inputs.seg_val_max = 2
            lhwmROI.inputs.out_file = "lhwmROI.nii.gz"
            freesurfer.connect(aparaseg2Volnii, "vol_label_file", lhwmROI, "in_file")

            rhwmROI = Node(thrROI(), name='rhwmROI')
            rhwmROI.inputs.seg_val_min = 41
            rhwmROI.inputs.seg_val_max = 41
            rhwmROI.inputs.out_file = "rhwmROI.nii.gz"
            freesurfer.connect(aparaseg2Volnii, "vol_label_file", rhwmROI, "in_file")

            wmROI = Node(BinaryMaths(), name='wmROI')
            wmROI.inputs.operation = "add"
            wmROI.inputs.out_file = "wmROI.nii.gz"
            freesurfer.connect(lhwmROI, "out_file", wmROI, "in_file")
            freesurfer.connect(rhwmROI, "out_file", wmROI, "operand_file")

            # estrazione ROI bgt
            lhbgtROI = Node(thrROI(), name='lhbgtROI')
            lhbgtROI.inputs.seg_val_min = 10
            lhbgtROI.inputs.seg_val_max = 13
            lhbgtROI.inputs.out_file = "lhbgtROI.nii.gz"
            freesurfer.connect(aparaseg2Volnii, "vol_label_file", lhbgtROI, "in_file")

            rhbgtROI = Node(thrROI(), name='rhbgtROI')
            rhbgtROI.inputs.seg_val_min = 49
            rhbgtROI.inputs.seg_val_max = 52
            rhbgtROI.inputs.out_file = "rhbgtROI.nii.gz"
            freesurfer.connect(aparaseg2Volnii, "vol_label_file", rhbgtROI, "in_file")

            bgtROI = Node(BinaryMaths(), name='bgtROI')
            bgtROI.inputs.operation = "add"
            bgtROI.inputs.out_file = "bgtROI.nii.gz"
            freesurfer.connect(lhbgtROI, "out_file", bgtROI, "in_file")
            freesurfer.connect(rhbgtROI, "out_file", bgtROI, "operand_file")

            if isHippoAmygLabels:
                # segmentazione ippocampo e amigdala
                segmentHA = Node(segmentHA_mo(), name="segmentHA_mo")
                segmentHA.inputs.num_threads = max_node_cpu
                freesurfer.connect(reconAll, "subjects_dir", segmentHA, "subjects_dir")
                freesurfer.connect(reconAll, "subject_id", segmentHA, "subject_id")
                regex_subs = [("-T1.*.mgz", ".mgz")]
                freesurfer.sink_result(self.base_dir, segmentHA, 'lh_hippoAmygLabels', 'scene.segmentHA', regex_subs)
                freesurfer.sink_result(self.base_dir, segmentHA, 'rh_hippoAmygLabels', 'scene.segmentHA', regex_subs)

        # ELABORAZIONE FLAIR
        if check_input['mr_flair3d']:
            flair = Workflow_mo(name="flair", base_dir="./")

            # conversione dicom->nifti
            flair_conv = Node(Dcm2niix_mo(), name='flair_conv')
            flair_dir = os.path.join(self.base_dir, SWANiGlobalConfig['DEFAULTFOLDERS']['default_mr_flair3d_folder'])
            flair_conv.inputs.source_dir = flair_dir
            flair_conv.inputs.crop = True
            flair_conv.inputs.out_filename = "flair"

            # orientamento in convenzione radiologica
            flair_reOrient = Node(Orient_mo(), name='flair_reOrient')
            flair.connect(flair_conv, "converted_files", flair_reOrient, "in_file")

            # rimozione scalpo
            flair_BET = Node(BET(), name='flair_BET')
            flair_BET.inputs.frac = 0.5
            flair_BET.inputs.robust = True
            flair_BET.inputs.threshold = True
            flair.connect(flair_reOrient, "out_file", flair_BET, "in_file")

            # trasformazione lineare nello spazio ref
            flair2ref_FLIRT = Node(FLIRT(), name='flair2ref_FLIRT')
            flair2ref_FLIRT.inputs.out_file = "r-flair_brain.nii.gz"
            flair2ref_FLIRT.inputs.out_matrix_file = "flair2ref.mat"
            flair2ref_FLIRT.inputs.cost = "mutualinfo"
            flair2ref_FLIRT.inputs.searchr_x = [-90, 90]
            flair2ref_FLIRT.inputs.searchr_y = [-90, 90]
            flair2ref_FLIRT.inputs.searchr_z = [-90, 90]
            flair2ref_FLIRT.inputs.dof = 6
            flair2ref_FLIRT.inputs.interp = "trilinear"
            flair.connect(flair_BET, "out_file", flair2ref_FLIRT, "in_file")
            self.connect(t1, "ref_BET.out_file", flair, "flair2ref_FLIRT.reference")
            flair.sink_result(self.base_dir, flair2ref_FLIRT, 'out_file', 'scene')

        # ELABORAZIONE script_DOmap
        if DOmap:
            DOmap = Workflow_mo(name="DOmap", base_dir="./")

            # segmentazione con fast
            DOmap_FAST = Node(FAST(), name="DOmap_FAST")
            DOmap_FAST.inputs.img_type = 1
            DOmap_FAST.inputs.number_classes = 3
            DOmap_FAST.inputs.hyper = 0.1
            DOmap_FAST.inputs.bias_lowpass = 40
            DOmap_FAST.inputs.output_biascorrected = True
            DOmap_FAST.inputs.bias_iters = 4
            DOmap.add_nodes([DOmap_FAST])
            self.connect(t1, "ref_BET.out_file", DOmap, "DOmap_FAST.in_files")

            # flair in atlante MNI1
            DOmap_flair2mni1 = Node(ApplyWarp(), name="DOmap_flair2mni1")
            DOmap_flair2mni1.inputs.ref_file = mni1_path
            DOmap.add_nodes([DOmap_flair2mni1])
            self.connect(flair, "flair_BET.out_file", DOmap, "DOmap_flair2mni1.in_file")
            self.connect(mni1, "ref2mni1_FNIRT.fieldcoeff_file", DOmap, "DOmap_flair2mni1.field_file")
            self.connect(flair, "flair2ref_FLIRT.out_matrix_file", DOmap, "DOmap_flair2mni1.premat")

            # t1_restore in atlante MNI1
            DOmap_restore2mni1 = Node(ApplyWarp(), name="DOmap_restore2mni1")
            DOmap_restore2mni1.inputs.ref_file = mni1_path
            DOmap.connect(DOmap_FAST, "restored_image", DOmap_restore2mni1, "in_file")
            self.connect(mni1, "ref2mni1_FNIRT.fieldcoeff_file", DOmap, "DOmap_restore2mni1.field_file")

            # GM in atlante MNI1
            DOmap_gm2mni1 = Node(ApplyWarp(), name="DOmap_gm2mni1")
            DOmap_gm2mni1.inputs.ref_file = mni1_path
            DOmap.connect([(DOmap_FAST, DOmap_gm2mni1, [(('partial_volume_files', getn, 1), 'in_file')])])
            self.connect(mni1, "ref2mni1_FNIRT.fieldcoeff_file", DOmap, "DOmap_gm2mni1.field_file")

            # WM in atlante MNI1
            DOmap_wm2mni1 = Node(ApplyWarp(), name="DOmap_wm2mni1")
            DOmap_wm2mni1.inputs.ref_file = mni1_path
            DOmap.connect([(DOmap_FAST, DOmap_wm2mni1, [(('partial_volume_files', getn, 2), 'in_file')])])
            self.connect(mni1, "ref2mni1_FNIRT.fieldcoeff_file", DOmap, "DOmap_wm2mni1.field_file")

            # divido FLAIR/T1
            DOmap_flairDIVref = Node(BinaryMaths(), name="DOmap_flairDIVref")
            DOmap_flairDIVref.inputs.operation = "div"
            DOmap.connect(DOmap_flair2mni1, "out_file", DOmap_flairDIVref, "in_file")
            DOmap.connect(DOmap_restore2mni1, "out_file", DOmap_flairDIVref, "operand_file")

            # outliers remove from mask
            DOmap_outliers_mask = Node(DOmap_outliers_mask_mo(), name="DOmap_outliers_mask")
            DOmap_outliers_mask.inputs.mask_file = SWANi_supplement.cortex_mas
            DOmap.connect(DOmap_flairDIVref, "out_file", DOmap_outliers_mask, "in_file")

            # rimuovo il cervelletto dalla flair/t1
            DOmap_cortexMask = Node(ApplyMask(), name="DOmap_cortexMask")
            DOmap.connect(DOmap_outliers_mask, "out_file", DOmap_cortexMask, "mask_file")
            DOmap.connect(DOmap_flairDIVref, "out_file", DOmap_cortexMask, "in_file")

            # creazione maschere gm e wn su t1_restore in MNI1
            DOmap_gmMask = Node(ApplyMask(), name="DOmap_gmMask")
            DOmap.connect(DOmap_cortexMask, "out_file", DOmap_gmMask, "in_file")
            DOmap.connect(DOmap_gm2mni1, "out_file", DOmap_gmMask, "mask_file")

            DOmap_wmMask = Node(ApplyMask(), name="DOmap_wmMask")
            DOmap.connect(DOmap_cortexMask, "out_file", DOmap_wmMask, "in_file")
            DOmap.connect(DOmap_wm2mni1, "out_file", DOmap_wmMask, "mask_file")

            # calcolo media e dev standard per gm e wm
            DOmap_gm_mean = Node(ImageStats(), name="DOmap_gm_mean")
            DOmap_gm_mean.inputs.op_string = "-M"
            DOmap.connect(DOmap_gmMask, "out_file", DOmap_gm_mean, "in_file")

            DOmap_wm_mean = Node(ImageStats(), name="DOmap_wm_mean")
            DOmap_wm_mean.inputs.op_string = "-M"
            DOmap.connect(DOmap_wmMask, "out_file", DOmap_wm_mean, "in_file")

            # DOmap_gm_std = Node(ImageStats(), name="DOmap_gm_std")
            # DOmap_gm_std.inputs.op_string="-S"
            # DOmap.connect(DOmap_gmMask,"out_file",DOmap_gm_std,"in_file")

            # DOmap_wm_std = Node(ImageStats(), name="DOmap_wm_std")
            # DOmap_wm_std.inputs.op_string="-S"
            # DOmap.connect(DOmap_wmMask,"out_file",DOmap_wm_std,"in_file")

            # maschera generata da soglia per media e dev standard su immagine divisa (perchè mai???)
            DOmap_binaryFLAIR = Node(thrROI(), name='DOmap_binaryFLAIR')
            DOmap_binaryFLAIR.inputs.out_file = "binary_flair.nii.gz"
            DOmap.connect(DOmap_cortexMask, "out_file", DOmap_binaryFLAIR, "in_file")
            DOmap.connect(DOmap_gm_mean, "out_stat", DOmap_binaryFLAIR, "seg_val_max")
            DOmap.connect(DOmap_wm_mean, "out_stat", DOmap_binaryFLAIR, "seg_val_min")

            # convolutional flair_reOrient
            DOmap_convolution_flair = Node(DilateImage_mo(), name="DOmap_convolution_flair")
            DOmap_convolution_flair.inputs.args = "-fmean"
            DOmap_convolution_flair.inputs.kernel_shape = "boxv"
            DOmap_convolution_flair.inputs.kernel_size = 5
            DOmap_convolution_flair.inputs.out_file = "convolution_flair.nii.gz"
            DOmap.connect(DOmap_binaryFLAIR, "out_file", DOmap_convolution_flair, "in_file")

            # calcolo junction e relativo zscore
            DOmap_junction = Node(BinaryMaths(), name="DOmap_junction")
            DOmap_junction.inputs.operation = "sub"
            DOmap_junction.inputs.operand_file = SWANi_supplement.mean_flair
            DOmap_junction.inputs.out_file = "junction_flair.nii.gz"
            DOmap.connect(DOmap_convolution_flair, "out_file", DOmap_junction, "in_file")

            DOmap_junctionz = Node(BinaryMaths(), name="DOmap_junctionz")
            DOmap_junctionz.inputs.operation = "div"
            DOmap_junctionz.inputs.operand_file = SWANi_supplement.std_final_flair
            DOmap_junctionz.inputs.out_file = "junctionZ_flair.nii.gz"
            DOmap.connect(DOmap_junction, "out_file", DOmap_junctionz, "in_file")

            DOmap_masked_cerebellum = Node(ApplyMask(), name="DOmap_masked_cerebellum")
            DOmap_masked_cerebellum.inputs.mask_file = SWANi_supplement.binary_cerebellum
            DOmap.connect(DOmap_restore2mni1, "out_file", DOmap_masked_cerebellum, "in_file")

            DOmap_cerebellum_mean = Node(ImageStats(), name="DOmap_cerebellum_mean")
            DOmap_cerebellum_mean.inputs.op_string = "-M"
            DOmap.connect(DOmap_masked_cerebellum, "out_file", DOmap_cerebellum_mean, "in_file")

            DOmap_restore_gmMask = Node(ApplyMask(), name="DOmap_restore_gmMask")
            DOmap_restore_gmMask.inputs.out_file = "masked_image_GM.nii.gz"
            DOmap.connect(DOmap_restore2mni1, "out_file", DOmap_restore_gmMask, "in_file")
            DOmap.connect(DOmap_gm2mni1, "out_file", DOmap_restore_gmMask, "mask_file")

            DOmap_normalised_GM_mask = Node(BinaryMaths(), name="DOmap_normalised_GM_mask")
            DOmap_normalised_GM_mask.inputs.operation = "div"
            DOmap_normalised_GM_mask.inputs.out_file = "normalised_GM_mask.nii.gz"
            DOmap.connect(DOmap_restore_gmMask, "out_file", DOmap_normalised_GM_mask, "in_file")
            DOmap.connect(DOmap_cerebellum_mean, "out_stat", DOmap_normalised_GM_mask, "operand_value")

            DOmap_smoothed_image_extension = Node(DilateImage_mo(), name="DOmap_smoothed_image_extension")
            DOmap_smoothed_image_extension.inputs.args = "-fmean"
            DOmap_smoothed_image_extension.inputs.kernel_shape = "boxv"
            DOmap_smoothed_image_extension.inputs.kernel_size = 5
            DOmap_smoothed_image_extension.inputs.out_file = "smoothed_image_extension.nii.gz"
            DOmap.connect(DOmap_normalised_GM_mask, "out_file", DOmap_smoothed_image_extension, "in_file")

            DOmap_image_extension = Node(BinaryMaths(), name="DOmap_image_extension")
            DOmap_image_extension.inputs.operation = "sub"
            DOmap_image_extension.inputs.operand_file = SWANi_supplement.mean_extension
            DOmap_image_extension.inputs.out_file = "extension_image.nii.gz"
            DOmap.connect(DOmap_smoothed_image_extension, "out_file", DOmap_image_extension, "in_file")

            DOmap_image_extensionz = Node(BinaryMaths(), name="DOmap_image_extensionz")
            DOmap_image_extensionz.inputs.operation = "div"
            DOmap_image_extensionz.inputs.operand_file = SWANi_supplement.std_final_extension
            DOmap_image_extensionz.inputs.out_file = "extension_z.nii.gz"
            DOmap.connect(DOmap_image_extension, "out_file", DOmap_image_extensionz, "in_file")

            DOmap_no_cereb_extension_z = Node(ApplyMask(), name="no_cereb_extension_z")
            DOmap_no_cereb_extension_z.inputs.out_file = "no_cereb_extension_z.nii.gz"
            DOmap.connect(DOmap_image_extensionz, "out_file", DOmap_no_cereb_extension_z, "in_file")
            DOmap.connect(DOmap_outliers_mask, "out_file", DOmap_no_cereb_extension_z, "mask_file")

            DOmap_extensionz2ref = Node(ApplyWarp(), name="DOmap_extensionz2ref")
            DOmap_extensionz2ref.inputs.out_file = "r-extension_z.nii.gz"
            DOmap.connect(DOmap_no_cereb_extension_z, "out_file", DOmap_extensionz2ref, "in_file")
            self.connect(mni1, "ref2mni1_INVWARP.inverse_warp", DOmap, "DOmap_extensionz2ref.field_file")
            self.connect(t1, "ref_BET.out_file", DOmap, "DOmap_extensionz2ref.ref_file")
            DOmap.sink_result(self.base_dir, DOmap_extensionz2ref, 'out_file', 'scene')

            DOmap_junctionz2ref = Node(ApplyWarp(), name="DOmap_junctionz2ref")
            DOmap_junctionz2ref.inputs.out_file = "r-junction_z.nii.gz"
            DOmap.connect(DOmap_junctionz, "out_file", DOmap_junctionz2ref, "in_file")
            self.connect(mni1, "ref2mni1_INVWARP.inverse_warp", DOmap, "DOmap_junctionz2ref.field_file")
            self.connect(t1, "ref_BET.out_file", DOmap, "DOmap_junctionz2ref.ref_file")
            DOmap.sink_result(self.base_dir, DOmap_junctionz2ref, 'out_file', 'scene')

            DOmap_binaryFLAIR2ref = Node(ApplyWarp(), name="DOmap_binaryFLAIR2ref")
            DOmap_binaryFLAIR2ref.inputs.out_file = "r-binaryFLAIR.nii.gz"
            DOmap.connect(DOmap_binaryFLAIR, "out_file", DOmap_binaryFLAIR2ref, "in_file")
            self.connect(mni1, "ref2mni1_INVWARP.inverse_warp", DOmap, "DOmap_binaryFLAIR2ref.field_file")
            self.connect(t1, "ref_BET.out_file", DOmap, "DOmap_binaryFLAIR2ref.ref_file")
            DOmap.sink_result(self.base_dir, DOmap_binaryFLAIR2ref, 'out_file', 'scene')

        # ELABORAZIONE FLAIR 2D TRA
        if flair2D and check_input['op_mr_flair2d_tra']:
            flair2d_tra = Workflow_mo(name="flair2d_tra", base_dir="./")

            # conversione dicom->nifti
            flair2d_tra_conv = Node(Dcm2niix_mo(), name='flair2d_tra_conv')
            flair_dir = os.path.join(self.base_dir,
                                     SWANiGlobalConfig['DEFAULTFOLDERS']['default_op_mr_flair2d_tra_folder'])
            flair2d_tra_conv.inputs.source_dir = flair_dir
            flair2d_tra_conv.inputs.out_filename = "flair"

            # orientamento in convenzione radiologica
            flair2d_tra_reOrient = Node(Orient_mo(), name='flair2d_tra_reOrient')
            flair2d_tra.connect(flair2d_tra_conv, "converted_files", flair2d_tra_reOrient, "in_file")

            # rimozione scalpo
            flair2d_tra_BET = Node(BET(), name='flair2d_tra_BET')
            flair2d_tra_BET.inputs.frac = 0.5
            flair2d_tra_BET.inputs.robust = True
            flair2d_tra_BET.inputs.threshold = True
            flair2d_tra.connect(flair2d_tra_reOrient, "out_file", flair2d_tra_BET, "in_file")

            # trasformazione lineare nello spazio ref
            flair2d_tra2ref_FLIRT = Node(FLIRT(), name='flair2d_tra2ref_FLIRT')
            flair2d_tra2ref_FLIRT.inputs.out_file = "r-flair2d_tra_brain.nii.gz"
            flair2d_tra2ref_FLIRT.inputs.out_matrix_file = "flair2d_tra2ref.mat"
            flair2d_tra.connect(flair2d_tra_BET, "out_file", flair2d_tra2ref_FLIRT, "in_file")
            self.connect(t1, "ref_BET.out_file", flair2d_tra, "flair2d_tra2ref_FLIRT.reference")
            flair2d_tra.sink_result(self.base_dir, flair2d_tra2ref_FLIRT, 'out_file', 'scene')

        # ELABORAZIONE FLAIR 2D COR
        if flair2D and check_input['op_mr_flair2d_cor']:
            flair2d_cor = Workflow_mo(name="flair2d_cor", base_dir="./")

            # conversione dicom->nifti
            flair2d_cor_conv = Node(Dcm2niix_mo(), name='flair2d_cor_conv')
            flair_dir = os.path.join(self.base_dir,
                                     SWANiGlobalConfig['DEFAULTFOLDERS']['default_op_mr_flair2d_cor_folder'])
            flair2d_cor_conv.inputs.source_dir = flair_dir
            flair2d_cor_conv.inputs.out_filename = "flair"

            # orientamento in convenzione radiologica
            flair2d_cor_reOrient = Node(Orient_mo(), name='flair2d_cor_reOrient')
            flair2d_cor.connect(flair2d_cor_conv, "converted_files", flair2d_cor_reOrient, "in_file")

            # rimozione scalpo
            flair2d_cor_BET = Node(BET(), name='flair2d_cor_BET')
            flair2d_cor_BET.inputs.frac = 0.5
            flair2d_cor_BET.inputs.robust = True
            flair2d_cor_BET.inputs.threshold = True
            flair2d_cor.connect(flair2d_cor_reOrient, "out_file", flair2d_cor_BET, "in_file")

            # trasformazione lineare nello spazio ref
            flair2d_cor2ref_FLIRT = Node(FLIRT(), name='flair2d_cor2ref_FLIRT')
            flair2d_cor2ref_FLIRT.inputs.out_file = "r-flair2d_cor_brain.nii.gz"
            flair2d_cor2ref_FLIRT.inputs.out_matrix_file = "flair2d_cor2ref.mat"
            flair2d_cor.connect(flair2d_cor_BET, "out_file", flair2d_cor2ref_FLIRT, "in_file")
            self.connect(t1, "ref_BET.out_file", flair2d_cor, "flair2d_cor2ref_FLIRT.reference")
            flair2d_cor.sink_result(self.base_dir, flair2d_cor2ref_FLIRT, 'out_file', 'scene')

        # ELABORAZIONE FLAIR 2D SAG
        if flair2D and check_input['op_mr_flair2d_sag']:
            flair2d_sag = Workflow_mo(name="flair2d_sag", base_dir="./")

            # conversione dicom->nifti
            flair2d_sag_conv = Node(Dcm2niix_mo(), name='flair2d_sag_conv')
            flair_dir = os.path.join(self.base_dir,
                                     SWANiGlobalConfig['DEFAULTFOLDERS']['default_op_mr_flair2d_sag_folder'])
            flair2d_sag_conv.inputs.source_dir = flair_dir
            flair2d_sag_conv.inputs.out_filename = "flair"

            # orientamento in convenzione radiologica
            flair2d_sag_reOrient = Node(Orient_mo(), name='flair2d_sag_reOrient')
            flair2d_sag.connect(flair2d_sag_conv, "converted_files", flair2d_sag_reOrient, "in_file")

            # rimozione scalpo
            flair2d_sag_BET = Node(BET(), name='flair2d_sag_BET')
            flair2d_sag_BET.inputs.frac = 0.5
            flair2d_sag_BET.inputs.robust = True
            flair2d_sag_BET.inputs.threshold = True
            flair2d_sag.connect(flair2d_sag_reOrient, "out_file", flair2d_sag_BET, "in_file")

            # trasformazione lineare nello spazio ref
            flair2d_sag2ref_FLIRT = Node(FLIRT(), name='flair2d_sag2ref_FLIRT')
            flair2d_sag2ref_FLIRT.inputs.out_file = "r-flair2d_sag_brain.nii.gz"
            flair2d_sag2ref_FLIRT.inputs.out_matrix_file = "flair2d_sag2ref.mat"
            flair2d_sag.connect(flair2d_sag_BET, "out_file", flair2d_sag2ref_FLIRT, "in_file")
            self.connect(t1, "ref_BET.out_file", flair2d_sag, "flair2d_sag2ref_FLIRT.reference")
            flair2d_sag.sink_result(self.base_dir, flair2d_sag2ref_FLIRT, 'out_file', 'scene')

        # ELABORAZIONE MDC
        if check_input['mr_mdc']:
            mdc = Workflow_mo(name="mdc", base_dir="./")

            # conversione dicom->nifti
            mdc_conv = Node(Dcm2niix_mo(), name='mdc_conv')
            mdc_dir = os.path.join(self.base_dir, SWANiGlobalConfig['DEFAULTFOLDERS']['default_mr_mdc_folder'])
            mdc_conv.inputs.source_dir = mdc_dir
            mdc_conv.inputs.crop = True
            mdc_conv.inputs.out_filename = "mdc"

            # orientamento in convenzione radiologica
            mdc_reOrient = Node(Orient_mo(), name='mdc_reOrient')
            mdc.connect(mdc_conv, "converted_files", mdc_reOrient, "in_file")

            # rimozione scalpo
            mdc_BET = Node(BET(), name='mdc_BET')
            mdc_BET.inputs.frac = 0.3
            mdc_BET.inputs.robust = True
            mdc_BET.inputs.threshold = True
            mdc.connect(mdc_reOrient, "out_file", mdc_BET, "in_file")

            # trasformazione lineare nello spazio ref
            mdc2ref_FLIRT = Node(FLIRT(), name='mdc2ref_FLIRT')
            mdc2ref_FLIRT.inputs.out_file = "r-mdc_brain.nii.gz"
            mdc2ref_FLIRT.inputs.out_matrix_file = "mdc2ref.mat"
            mdc2ref_FLIRT.inputs.cost = "mutualinfo"
            mdc2ref_FLIRT.inputs.searchr_x = [-90, 90]
            mdc2ref_FLIRT.inputs.searchr_y = [-90, 90]
            mdc2ref_FLIRT.inputs.searchr_z = [-90, 90]
            mdc2ref_FLIRT.inputs.dof = 6
            mdc2ref_FLIRT.inputs.interp = "trilinear"
            mdc.connect(mdc_BET, "out_file", mdc2ref_FLIRT, "in_file")
            self.connect(t1, "ref_BET.out_file", mdc, "mdc2ref_FLIRT.reference")
            mdc.sink_result(self.base_dir, mdc2ref_FLIRT, 'out_file', 'scene')

        # ELABORAZIONE ASL
        if check_input['mr_asl']:

            asl = Workflow_mo(name="asl", base_dir="./")

            # conversione dicom->nifti
            asl_conv = Node(Dcm2niix_mo(), name='asl_conv')
            asl_conv.inputs.out_filename = "asl"
            asl_dir = os.path.join(self.base_dir, SWANiGlobalConfig['DEFAULTFOLDERS']['default_mr_asl_folder'])
            asl_conv.inputs.source_dir = asl_dir

            # orientamento in convenzione radiologica
            asl_reOrient = Node(Orient_mo(), name='asl_reOrient')
            asl.connect(asl_conv, "converted_files", asl_reOrient, "in_file")

            # smoothing gaussiano
            asl_SMOOTH = Node(IsotropicSmooth(), name='asl_SMOOTH')
            asl_SMOOTH.inputs.sigma = 2
            asl.connect(asl_reOrient, "out_file", asl_SMOOTH, "in_file")

            # calcolo matrice di trasformazione nello spazio ref
            asl2ref_FLIRT = Node(FLIRT(), name='asl2ref_FLIRT')
            asl2ref_FLIRT.inputs.cost = "mutualinfo"
            asl2ref_FLIRT.inputs.searchr_x = [-90, 90]
            asl2ref_FLIRT.inputs.searchr_y = [-90, 90]
            asl2ref_FLIRT.inputs.searchr_z = [-90, 90]
            asl2ref_FLIRT.inputs.dof = 6
            asl2ref_FLIRT.inputs.interp = "trilinear"
            asl.connect(asl_reOrient, "out_file", asl2ref_FLIRT, "in_file")
            self.connect(t1, "ref_BET.out_file", asl, "asl2ref_FLIRT.reference")

            # trasposizione del volume smooth nello spazio ref
            aslsmooth2ref_FLIRT = Node(FLIRT(), name='aslsmooth2ref_FLIRT')
            aslsmooth2ref_FLIRT.inputs.out_file = "r-asl.nii.gz"
            aslsmooth2ref_FLIRT.inputs.interp = "trilinear"
            asl.connect(asl_SMOOTH, "out_file", aslsmooth2ref_FLIRT, "in_file")
            self.connect(t1, "ref_BET.out_file", asl, "aslsmooth2ref_FLIRT.reference")
            asl.connect(asl2ref_FLIRT, "out_matrix_file", aslsmooth2ref_FLIRT, "in_matrix_file")

            # rimozione scalpo
            asl_mask = Node(ApplyMask(), name='asl_mask')
            asl_mask.inputs.out_file = 'r-asl.nii.gz'
            asl.connect(aslsmooth2ref_FLIRT, "out_file", asl_mask, "in_file")
            self.connect(t1, "ref_BET.mask_file", asl, "asl_mask.mask_file")
            asl.sink_result(self.base_dir, asl_mask, 'out_file', 'scene')

            if isfreesurfer:
                # PROIEZIONE DELLA asl SULLA SUPERFICIE PIALE DI FREESURFER
                asl_surf_lh = Node(SampleToSurface(), name='asl_surf_lh')
                asl_surf_lh.inputs.hemi = 'lh'
                asl_surf_lh.inputs.out_file = "asl_surf_lh.mgz"
                asl_surf_lh.inputs.cortex_mask = True
                asl_surf_lh.inputs.reg_header = True
                asl_surf_lh.inputs.sampling_method = "point"
                asl_surf_lh.inputs.sampling_range = 0.5
                asl_surf_lh.inputs.sampling_units = "frac"
                asl.connect(asl_mask, "out_file", asl_surf_lh, "source_file")
                self.connect(freesurfer, "reconAll.subjects_dir", asl, "asl_surf_lh.subjects_dir")
                self.connect(freesurfer, "reconAll.subject_id", asl, "asl_surf_lh.subject_id")
                asl.sink_result(self.base_dir, asl_surf_lh, 'out_file', 'scene')

                asl_surf_rh = Node(SampleToSurface(), name='asl_surf_rh')
                asl_surf_rh.inputs.hemi = 'rh'
                asl_surf_rh.inputs.out_file = "asl_surf_rh.mgz"
                asl_surf_rh.inputs.cortex_mask = True
                asl_surf_rh.inputs.reg_header = True
                asl_surf_rh.inputs.sampling_method = "point"
                asl_surf_rh.inputs.sampling_range = 0.5
                asl_surf_rh.inputs.sampling_units = "frac"
                asl.connect(asl_mask, "out_file", asl_surf_rh, "source_file")
                self.connect(freesurfer, "reconAll.subjects_dir", asl, "asl_surf_rh.subjects_dir")
                self.connect(freesurfer, "reconAll.subject_id", asl, "asl_surf_rh.subject_id")
                asl.sink_result(self.base_dir, asl_surf_rh, 'out_file', 'scene')

                # STATISTICA ZSCORE SULLA asl
                asl_zscore = Node(Zscore(), name="asl_zscore")
                asl.connect(aslsmooth2ref_FLIRT, "out_file", asl_zscore, "in_file")
                self.connect(freesurfer, "bgtROI.out_file", asl, "asl_zscore.ROI_file")

                asl_zscore_mask = Node(ApplyMask(), name="asl_zscore_mask")
                asl_zscore_mask.inputs.out_file = "r-asl_brain_z.nii.gz"
                asl.connect(asl_zscore, "out_file", asl_zscore_mask, "in_file")
                self.connect(t1, "ref_BET.mask_file", asl, "asl_zscore_mask.mask_file")
                asl.sink_result(self.base_dir, asl_zscore_mask, 'out_file', 'scene')

                # PROIEZIONE DELLA asl z-score SULLA SUPERFICIE PIALE DI FREESURFER
                aslZscore_surf_lh = Node(SampleToSurface(), name='aslZscore_surf_lh')
                aslZscore_surf_lh.inputs.hemi = 'lh'
                aslZscore_surf_lh.inputs.out_file = "aslZscore_surf_lh.mgz"
                aslZscore_surf_lh.inputs.cortex_mask = True
                aslZscore_surf_lh.inputs.reg_header = True
                aslZscore_surf_lh.inputs.sampling_method = "point"
                aslZscore_surf_lh.inputs.sampling_range = 0.5
                aslZscore_surf_lh.inputs.sampling_units = "frac"
                asl.connect(asl_zscore_mask, "out_file", aslZscore_surf_lh, "source_file")
                self.connect(freesurfer, "reconAll.subjects_dir", asl, "aslZscore_surf_lh.subjects_dir")
                self.connect(freesurfer, "reconAll.subject_id", asl, "aslZscore_surf_lh.subject_id")
                asl.sink_result(self.base_dir, aslZscore_surf_lh, 'out_file', 'scene')

                aslZscore_surf_rh = Node(SampleToSurface(), name='aslZscore_surf_rh')
                aslZscore_surf_rh.inputs.hemi = 'rh'
                aslZscore_surf_rh.inputs.out_file = "aslZscore_surf_rh.mgz"
                aslZscore_surf_rh.inputs.cortex_mask = True
                aslZscore_surf_rh.inputs.reg_header = True
                aslZscore_surf_rh.inputs.sampling_method = "point"
                aslZscore_surf_rh.inputs.sampling_range = 0.5
                aslZscore_surf_rh.inputs.sampling_units = "frac"
                asl.connect(asl_zscore_mask, "out_file", aslZscore_surf_rh, "source_file")
                self.connect(freesurfer, "reconAll.subjects_dir", asl, "aslZscore_surf_rh.subjects_dir")
                self.connect(freesurfer, "reconAll.subject_id", asl, "aslZscore_surf_rh.subject_id")
                asl.sink_result(self.base_dir, aslZscore_surf_rh, 'out_file', 'scene')

            if ai:
                # trasformazione non lineare delle immagini asl nell'atlante simmetrico
                asl2sym_APPLYWARP = Node(ApplyWarp(), name='asl2sym_APPLYWARP')
                asl2sym_APPLYWARP.inputs.ref_file = sym_template
                asl.connect(asl_mask, "out_file", asl2sym_APPLYWARP, "in_file")
                self.connect(sym, "ref2sym_FNIRT.fieldcoeff_file", asl, "asl2sym_APPLYWARP.field_file")

                # immagine ribaltata in RL della asl nello spazio dell'atlante simmetrico
                aslsym_SWAP = Node(SwapDimensions(), name='aslsym_SWAP')
                aslsym_SWAP.inputs.out_file = "asl_sym_swapped.nii.gz"
                aslsym_SWAP.inputs.new_dims = ("-x", "y", "z")
                asl.connect(asl2sym_APPLYWARP, "out_file", aslsym_SWAP, "in_file")

                # trasformazione non lineare da immagine ribaltata a immagine simmetrica
                asl_swapped_APPLYWARP = Node(ApplyWarp(), name='asl_swapped_APPLYWARP')
                asl_swapped_APPLYWARP.inputs.ref_file = sym_template
                asl.connect(aslsym_SWAP, "out_file", asl_swapped_APPLYWARP, "in_file")
                self.connect(sym, "swap2sym_FNIRT.fieldcoeff_file", asl, "asl_swapped_APPLYWARP.field_file")

                # calcolo asimmetry index
                asl_AI = Node(AIndex(), name="asl_AI")
                asl_AI.inputs.out_file = "aslAI.nii.gz"
                asl.connect(asl_swapped_APPLYWARP, "out_file", asl_AI, "swapped_file")
                asl.connect(aslsym_SWAP, "out_file", asl_AI, "in_file")

                # trasformazione non lineare da atlante simmetrico a ref
                asl_AI2ref = Node(ApplyWarp(), name="asl_AI2ref")
                asl_AI2ref.inputs.out_file = "r-asl_AI.nii.gz"
                asl.connect(asl_AI, "out_file", asl_AI2ref, "in_file")
                self.connect(sym, "ref2sym_INVWARP.inverse_warp", asl, "asl_AI2ref.field_file")
                self.connect(t1, "ref_BET.out_file", asl, "asl_AI2ref.ref_file")
                asl.sink_result(self.base_dir, asl_AI2ref, 'out_file', 'scene')

                if isfreesurfer:
                    # PROIEZIONE DELLA asl AI SULLA SUPERFICIE PIALE DI FREESURFER
                    aslAI_surf_lh = Node(SampleToSurface(), name='aslAI_surf_lh')
                    aslAI_surf_lh.inputs.hemi = 'lh'
                    aslAI_surf_lh.inputs.out_file = "aslAI_surf_lh.mgz"
                    aslAI_surf_lh.inputs.cortex_mask = True
                    aslAI_surf_lh.inputs.reg_header = True
                    aslAI_surf_lh.inputs.sampling_method = "point"
                    aslAI_surf_lh.inputs.sampling_range = 0.5
                    aslAI_surf_lh.inputs.sampling_units = "frac"
                    asl.connect(asl_AI2ref, "out_file", aslAI_surf_lh, "source_file")
                    self.connect(freesurfer, "reconAll.subjects_dir", asl, "aslAI_surf_lh.subjects_dir")
                    self.connect(freesurfer, "reconAll.subject_id", asl, "aslAI_surf_lh.subject_id")
                    asl.sink_result(self.base_dir, aslAI_surf_lh, 'out_file', 'scene')

                    aslAI_surf_rh = Node(SampleToSurface(), name='aslAI_surf_rh')
                    aslAI_surf_rh.inputs.hemi = 'rh'
                    aslAI_surf_rh.inputs.out_file = "aslAI_surf_rh.mgz"
                    aslAI_surf_rh.inputs.cortex_mask = True
                    aslAI_surf_rh.inputs.reg_header = True
                    aslAI_surf_rh.inputs.sampling_method = "point"
                    aslAI_surf_rh.inputs.sampling_range = 0.5
                    aslAI_surf_rh.inputs.sampling_units = "frac"
                    asl.connect(asl_AI2ref, "out_file", aslAI_surf_rh, "source_file")
                    self.connect(freesurfer, "reconAll.subjects_dir", asl, "aslAI_surf_rh.subjects_dir")
                    self.connect(freesurfer, "reconAll.subject_id", asl, "aslAI_surf_rh.subject_id")
                    asl.sink_result(self.base_dir, aslAI_surf_rh, 'out_file', 'scene')

        # ELABORAZIONE PET
        if check_input['pet_brain']:  # and check_input['ct_brain']:

            pet = Workflow_mo(name="pet", base_dir="./")

            # #conversione immagine TC dicom->nifti
            # pet_ct_conv = Node(Dcm2niix_mo(), name='pet_ct_conv')
            # pet_ct_dir = os.path.join(self.base_dir,SWANiGlobalConfig['DEFAULTFOLDERS']['default_ct_brain_folder'])
            # pet_ct_conv.inputs.source_dir=pet_ct_dir
            # pet_ct_conv.inputs.out_filename ="pet_ct"

            # #orientamento in convenzione radiologica della TC
            # pet_ct_reOrient=Node(Orient_mo(),name='pet_ct_reOrient')
            # pet.connect(pet_ct_conv, "converted_files", pet_ct_reOrient, "in_file")

            # #https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4446187/
            # #soglio la CT per valori 0 100 come primo passaggio per bet
            # pet_ct_shold= Node(ImageMaths(),name="pet_ct_shold")
            # pet_ct_shold.inputs.op_string="-thr 0 -uthr 100"
            # pet.connect(pet_ct_reOrient, "out_file", pet_ct_shold, "in_file")

            # pet_ct_bet=Node(BET(),name="pet_ct_bet")
            # pet_ct_bet.inputs.frac = 0.1
            # pet_ct_bet.inputs.robust = True
            # pet_ct_bet.inputs.threshold = True
            # pet.connect(pet_ct_shold, "out_file", pet_ct_bet, "in_file")

            # conversione immagine PET dicom->nifti
            pet_brain_conv = Node(Dcm2niix_mo(), name='pet_brain_conv')
            pet_brain_dir = os.path.join(self.base_dir, SWANiGlobalConfig['DEFAULTFOLDERS']['default_pet_brain_folder'])
            pet_brain_conv.inputs.source_dir = pet_brain_dir
            pet_brain_conv.inputs.out_filename = "pet_brain"

            # orientamento in convenzione radiologica della PET
            pet_brain_reOrient = Node(Orient_mo(), name='pet_brain_reOrient')
            pet.connect(pet_brain_conv, "converted_files", pet_brain_reOrient, "in_file")

            # #trasformazione lineare immagine TC su ref
            # pet_ct2ref_FLIRT = Node(FLIRT(), name='pet_ct2ref_FLIRT')
            # pet_ct2ref_FLIRT.inputs.out_file  = "r-pet_ct.nii.gz"
            # pet_ct2ref_FLIRT.inputs.out_matrix_file  = "ct2ref.mat"
            # pet_ct2ref_FLIRT.inputs.cost = "mutualinfo"
            # pet_ct2ref_FLIRT.inputs.searchr_x = [-90,90]
            # pet_ct2ref_FLIRT.inputs.searchr_y = [-90,90]
            # pet_ct2ref_FLIRT.inputs.searchr_z = [-90,90]
            # pet_ct2ref_FLIRT.inputs.dof = 6
            # pet_ct2ref_FLIRT.inputs.interp = "trilinear"
            # pet.connect(pet_ct_bet, "out_file", pet_ct2ref_FLIRT, "in_file")
            # self.connect(t1, "ref_BET.out_file", pet, "pet_ct2ref_FLIRT.reference")
            # pet.sink_result(self.base_dir,pet_ct2ref_FLIRT,'out_file','scene')

            # #trasformazione lineare immagine PET su TC
            # pet_brain2ct_FLIRT = Node(FLIRT(), name='pet_brain2ct_FLIRT')
            # pet_brain2ct_FLIRT.inputs.out_matrix_file  = "pet2ct.mat"
            # #pet_brain2ct_FLIRT.no_search=True
            # pet_brain2ct_FLIRT.inputs.cost = "mutualinfo"
            # pet_brain2ct_FLIRT.inputs.searchr_x = [-90,90]
            # pet_brain2ct_FLIRT.inputs.searchr_y = [-90,90]
            # pet_brain2ct_FLIRT.inputs.searchr_z = [-90,90]
            # pet_brain2ct_FLIRT.inputs.dof = 6
            # pet_brain2ct_FLIRT.inputs.interp = "trilinear"
            # pet.connect(pet_brain_reOrient, "out_file", pet_brain2ct_FLIRT, "in_file")
            # pet.connect(pet_ct_bet, "out_file", pet_brain2ct_FLIRT, "reference")
            # pet.sink_result(self.base_dir,pet_brain2ct_FLIRT,'out_file','scene')

            # #concatenazione delle due trasformazioni precedenti
            # pet_convert_XFM = Node(ConvertXFM(), name='pet_convert_XFM')
            # pet_convert_XFM.inputs.concat_xfm = True
            # pet_convert_XFM.inputs.out_file = "pet2ref.mat"
            # pet.connect(pet_ct2ref_FLIRT, "out_matrix_file", pet_convert_XFM, "in_file2")
            # pet.connect(pet_brain2ct_FLIRT, "out_matrix_file", pet_convert_XFM, "in_file")

            # trasformazione lineare immagine PET su ref
            # pet_brain2ref_FLIRT = Node(FLIRT(), name='pet_brain2ref_FLIRT')
            # pet_brain2ref_FLIRT.inputs.out_file  = "r-pet_brain.nii.gz"
            # pet_brain2ref_FLIRT.inputs.apply_xfm = True
            # pet_brain2ref_FLIRT.inputs.interp = "trilinear"
            # pet.connect(pet_brain_reOrient, "out_file", pet_brain2ref_FLIRT, "in_file")
            # pet.connect(pet_convert_XFM, "out_file", pet_brain2ref_FLIRT, "in_matrix_file")
            # self.connect(t1, "ref_reOrient.out_file", pet, "pet_brain2ref_FLIRT.reference")pet_ct2ref_FLIRT = Node(FLIRT(), name='pet_ct2ref_FLIRT')
            pet_brain2ref_FLIRT = Node(FLIRT(), name='pet_brain2ref_FLIRT')
            pet_brain2ref_FLIRT.inputs.out_file = "r-pet_brain.nii.gz"
            pet_brain2ref_FLIRT.inputs.out_matrix_file = "ct2ref.mat"
            pet_brain2ref_FLIRT.inputs.cost = "mutualinfo"
            pet_brain2ref_FLIRT.inputs.searchr_x = [-90, 90]
            pet_brain2ref_FLIRT.inputs.searchr_y = [-90, 90]
            pet_brain2ref_FLIRT.inputs.searchr_z = [-90, 90]
            pet_brain2ref_FLIRT.inputs.dof = 6
            pet_brain2ref_FLIRT.inputs.interp = "trilinear"
            pet.connect(pet_brain_reOrient, "out_file", pet_brain2ref_FLIRT, "in_file")
            self.connect(t1, "ref_reOrient.out_file", pet, "pet_brain2ref_FLIRT.reference")

            # smoothing gaussiano
            pet_brain_SMOOTH = Node(IsotropicSmooth(), name='pet_brain_SMOOTH')
            pet_brain_SMOOTH.inputs.sigma = 2
            pet.connect(pet_brain2ref_FLIRT, "out_file", pet_brain_SMOOTH, "in_file")
            pet.sink_result(self.base_dir, pet_brain_SMOOTH, 'out_file', 'scene')

            if isfreesurfer:
                # PROIEZIONE DELLA PET SULLA SUPERFICIE PIALE DI FREESURFER
                pet_surf_lh = Node(SampleToSurface(), name='pet_surf_lh')
                pet_surf_lh.inputs.hemi = 'lh'
                pet_surf_lh.inputs.out_file = "pet_surf_lh.mgz"
                pet_surf_lh.inputs.cortex_mask = True
                pet_surf_lh.inputs.reg_header = True
                pet_surf_lh.inputs.sampling_method = "point"
                pet_surf_lh.inputs.sampling_range = 0.5
                pet_surf_lh.inputs.sampling_units = "frac"
                pet.connect(pet_brain_SMOOTH, "out_file", pet_surf_lh, "source_file")
                self.connect(freesurfer, "reconAll.subjects_dir", pet, "pet_surf_lh.subjects_dir")
                self.connect(freesurfer, "reconAll.subject_id", pet, "pet_surf_lh.subject_id")
                pet.sink_result(self.base_dir, pet_surf_lh, 'out_file', 'scene')

                pet_surf_rh = Node(SampleToSurface(), name='pet_surf_rh')
                pet_surf_rh.inputs.hemi = 'rh'
                pet_surf_rh.inputs.out_file = "pet_surf_rh.mgz"
                pet_surf_rh.inputs.cortex_mask = True
                pet_surf_rh.inputs.reg_header = True
                pet_surf_rh.inputs.sampling_method = "point"
                pet_surf_rh.inputs.sampling_range = 0.5
                pet_surf_rh.inputs.sampling_units = "frac"
                pet.connect(pet_brain_SMOOTH, "out_file", pet_surf_rh, "source_file")
                self.connect(freesurfer, "reconAll.subjects_dir", pet, "pet_surf_rh.subjects_dir")
                self.connect(freesurfer, "reconAll.subject_id", pet, "pet_surf_rh.subject_id")
                pet.sink_result(self.base_dir, pet_surf_rh, 'out_file', 'scene')

                # STATISTICA Z-SCORE SULLA pet
                pet_zscore = Node(Zscore(), name="pet_zscore")
                pet.connect(pet_brain_SMOOTH, "out_file", pet_zscore, "in_file")
                self.connect(freesurfer, "bgtROI.out_file", pet, "pet_zscore.ROI_file")

                pet_zscore_mask = Node(ApplyMask(), name="pet_zscore_mask")
                pet_zscore_mask.inputs.out_file = "r-pet_brain_z.nii.gz"
                pet.connect(pet_zscore, "out_file", pet_zscore_mask, "in_file")
                self.connect(t1, "ref_BET.mask_file", pet, "pet_zscore_mask.mask_file")
                pet.sink_result(self.base_dir, pet_zscore_mask, 'out_file', 'scene')

                # PROIEZIONE DELLA PET z-score SULLA SUPERFICIE PIALE DI FREESURFER
                petZscore_surf_lh = Node(SampleToSurface(), name='petZscore_surf_lh')
                petZscore_surf_lh.inputs.hemi = 'lh'
                petZscore_surf_lh.inputs.out_file = "petZscore_surf_lh.mgz"
                petZscore_surf_lh.inputs.cortex_mask = True
                petZscore_surf_lh.inputs.reg_header = True
                petZscore_surf_lh.inputs.sampling_method = "point"
                petZscore_surf_lh.inputs.sampling_range = 0.5
                petZscore_surf_lh.inputs.sampling_units = "frac"
                pet.connect(pet_zscore_mask, "out_file", petZscore_surf_lh, "source_file")
                self.connect(freesurfer, "reconAll.subjects_dir", pet, "petZscore_surf_lh.subjects_dir")
                self.connect(freesurfer, "reconAll.subject_id", pet, "petZscore_surf_lh.subject_id")
                pet.sink_result(self.base_dir, petZscore_surf_lh, 'out_file', 'scene')

                petZscore_surf_rh = Node(SampleToSurface(), name='petZscore_surf_rh')
                petZscore_surf_rh.inputs.hemi = 'rh'
                petZscore_surf_rh.inputs.out_file = "petZscore_surf_rh.mgz"
                petZscore_surf_rh.inputs.cortex_mask = True
                petZscore_surf_rh.inputs.reg_header = True
                petZscore_surf_rh.inputs.sampling_method = "point"
                petZscore_surf_rh.inputs.sampling_range = 0.5
                petZscore_surf_rh.inputs.sampling_units = "frac"
                pet.connect(pet_zscore_mask, "out_file", petZscore_surf_rh, "source_file")
                self.connect(freesurfer, "reconAll.subjects_dir", pet, "petZscore_surf_rh.subjects_dir")
                self.connect(freesurfer, "reconAll.subject_id", pet, "petZscore_surf_rh.subject_id")
                pet.sink_result(self.base_dir, petZscore_surf_rh, 'out_file', 'scene')

            if ai:
                # trasformazione non lineare delle immagini PET nell'atlante simmetrico
                pet_brain_sm_APPLYWARP = Node(ApplyWarp(), name='pet_brain_sm_APPLYWARP')
                pet_brain_sm_APPLYWARP.inputs.ref_file = sym_template
                pet.connect(pet_brain_SMOOTH, "out_file", pet_brain_sm_APPLYWARP, "in_file")
                self.connect(sym, "ref2sym_FNIRT.fieldcoeff_file", pet, "pet_brain_sm_APPLYWARP.field_file")

                # immagine ribaltata in RL della PET nello spazio dell'atlante simmetrico
                petsym_SWAP = Node(SwapDimensions(), name='petsym_SWAP')
                petsym_SWAP.inputs.out_file = "pet_brain_sym_swapped.nii.gz"
                petsym_SWAP.inputs.new_dims = ("-x", "y", "z")
                pet.connect(pet_brain_sm_APPLYWARP, "out_file", petsym_SWAP, "in_file")

                # trasformazione non lineare da immagine ribaltata a immagine simmetrica
                pet_brain_swapped_APPLYWARP = Node(ApplyWarp(), name='pet_brain_swapped_APPLYWARP')
                pet_brain_swapped_APPLYWARP.inputs.ref_file = sym_template
                pet.connect(petsym_SWAP, "out_file", pet_brain_swapped_APPLYWARP, "in_file")
                self.connect(sym, "swap2sym_FNIRT.fieldcoeff_file", pet, "pet_brain_swapped_APPLYWARP.field_file")

                # calcolo asimmetry index
                pet_AI = Node(AIndex(), name="pet_AI")
                pet_AI.inputs.out_file = "petAI.nii.gz"
                pet.connect(pet_brain_sm_APPLYWARP, "out_file", pet_AI, "in_file")
                pet.connect(pet_brain_swapped_APPLYWARP, "out_file", pet_AI, "swapped_file")

                # trasformazione non lineare da atlante simmetrico a ref
                pet_AI2ref = Node(ApplyWarp(), name="pet_AI2ref")
                pet_AI2ref.inputs.out_file = "r-petAI.nii.gz"
                pet.connect(pet_AI, "out_file", pet_AI2ref, "in_file")
                self.connect(sym, "ref2sym_INVWARP.inverse_warp", pet, "pet_AI2ref.field_file")
                self.connect(t1, "ref_BET.out_file", pet, "pet_AI2ref.ref_file")

                # applico la maschera per eliminare il fondo
                pet_AI_mask = Node(ApplyMask(), name="pet_AI_mask")
                pet_AI_mask.inputs.out_file = "r-pet_brain_AI.nii.gz"
                pet.connect(pet_AI2ref, "out_file", pet_AI_mask, "in_file")
                self.connect(t1, "ref_BET.mask_file", pet, "pet_AI_mask.mask_file")
                pet.sink_result(self.base_dir, pet_AI_mask, 'out_file', 'scene')

                if isfreesurfer:
                    # PROIEZIONE DELLA PET AI SULLA SUPERFICIE PIALE DI FREESURFER
                    petAI_surf_lh = Node(SampleToSurface(), name='petAI_surf_lh')
                    petAI_surf_lh.inputs.hemi = 'lh'
                    petAI_surf_lh.inputs.out_file = "petAI_surf_lh.mgz"
                    petAI_surf_lh.inputs.cortex_mask = True
                    petAI_surf_lh.inputs.reg_header = True
                    petAI_surf_lh.inputs.sampling_method = "point"
                    petAI_surf_lh.inputs.sampling_range = 0.5
                    petAI_surf_lh.inputs.sampling_units = "frac"
                    pet.connect(pet_AI_mask, "out_file", petAI_surf_lh, "source_file")
                    self.connect(freesurfer, "reconAll.subjects_dir", pet, "petAI_surf_lh.subjects_dir")
                    self.connect(freesurfer, "reconAll.subject_id", pet, "petAI_surf_lh.subject_id")
                    pet.sink_result(self.base_dir, petAI_surf_lh, 'out_file', 'scene')

                    petAI_surf_rh = Node(SampleToSurface(), name='petAI_surf_rh')
                    petAI_surf_rh.inputs.hemi = 'rh'
                    petAI_surf_rh.inputs.out_file = "petAI_surf_rh.mgz"
                    petAI_surf_rh.inputs.cortex_mask = True
                    petAI_surf_rh.inputs.reg_header = True
                    petAI_surf_rh.inputs.sampling_method = "point"
                    petAI_surf_rh.inputs.sampling_range = 0.5
                    petAI_surf_rh.inputs.sampling_units = "frac"
                    pet.connect(pet_AI_mask, "out_file", petAI_surf_rh, "source_file")
                    self.connect(freesurfer, "reconAll.subjects_dir", pet, "petAI_surf_rh.subjects_dir")
                    self.connect(freesurfer, "reconAll.subject_id", pet, "petAI_surf_rh.subject_id")
                    pet.sink_result(self.base_dir, petAI_surf_rh, 'out_file', 'scene')

        # ELABORAZIONE VENOSA
        if check_input['mr_venosa']:
            venosa = Workflow_mo(name="venosa", base_dir="./")

            # conversione dicom->nifti
            venosa_conv = Node(Dcm2niix_mo(), name='venosa_conv')
            venosa_dir = os.path.join(self.base_dir, SWANiGlobalConfig['DEFAULTFOLDERS']['default_mr_venosa_folder'])
            venosa_conv.inputs.source_dir = venosa_dir
            venosa_conv.inputs.out_filename = "venosa"

            # orientamento in convenzione radiologica
            venosa_reOrient = Node(Orient_mo(), name='venosa_reOrient')
            venosa.connect(venosa_conv, "converted_files", venosa_reOrient, "in_file")

            # individuo la fase venosa dal modulo
            venosa_check = Node(VenosaCheck(), name='venosa_check')

            if check_input['mr_venosa2']:
                # se le fasi sono separate, converto anche la seconda
                # conversione dicom->nifti
                venosa2_conv = Node(Dcm2niix_mo(), name='venosa2_conv')
                venosa2_dir = os.path.join(self.base_dir,
                                           SWANiGlobalConfig['DEFAULTFOLDERS']['default_mr_venosa2_folder'])
                venosa2_conv.inputs.source_dir = venosa2_dir
                venosa2_conv.inputs.out_filename = "venosa2"

                # orientamento in convenzione radiologica
                venosa2_reOrient = Node(Orient_mo(), name='venosa2_reOrient')
                venosa.connect(venosa2_conv, "converted_files", venosa2_reOrient, "in_file")

                # unifico gli output dei reOrient da passare al check
                venosa_merge = Node(Merge(2), name="venosa_merge")
                venosa.connect(venosa_reOrient, "out_file", venosa_merge, "in1")
                venosa.connect(venosa2_reOrient, "out_file", venosa_merge, "in2")

                venosa.connect(venosa_merge, "out", venosa_check, "in_files")
            else:
                # altrimenti separo le due fasi della phase contrast
                venosa_split = Node(Split(), name='venosa_split')
                venosa_split.inputs.dimension = 't'
                venosa.connect(venosa_reOrient, "out_file", venosa_split, "in_file")

                venosa.connect(venosa_split, "out_files", venosa_check, "in_files")

            # segmento le strutture intracraniche nel modulo (migliore visualizzazione dell'osso)
            venosa_BET = Node(BET(), name='venosa_BET')
            venosa_BET.inputs.frac = 0.4
            venosa_BET.inputs.mask = True
            venosa_BET.inputs.threshold = True
            venosa_BET.inputs.surfaces = True
            venosa.connect(venosa_check, "out_file_modulo", venosa_BET, "in_file")

            # registrazione lineare modulo a ref
            venosa_modulo2ref_FLIRT = Node(FLIRT(), name='venosa_modulo2ref_FLIRT')
            venosa_modulo2ref_FLIRT.inputs.out_matrix_file = "venosa2ref.mat"
            venosa_modulo2ref_FLIRT.inputs.cost = "mutualinfo"
            venosa_modulo2ref_FLIRT.inputs.searchr_x = [-90, 90]
            venosa_modulo2ref_FLIRT.inputs.searchr_y = [-90, 90]
            venosa_modulo2ref_FLIRT.inputs.searchr_z = [-90, 90]
            venosa_modulo2ref_FLIRT.inputs.dof = 6
            venosa_modulo2ref_FLIRT.inputs.interp = "trilinear"
            venosa.connect(venosa_BET, "out_file", venosa_modulo2ref_FLIRT, "in_file")
            self.connect(t1, "ref_BET.out_file", venosa, "venosa_modulo2ref_FLIRT.reference")

            # applico la maschera delle strutture intracraniche alla fase venosa
            venosa_inskull_mask = Node(ApplyMask(), name='venosa_inskull_mask')
            venosa.connect(venosa_check, "out_file_venosa", venosa_inskull_mask, "in_file")
            venosa.connect(venosa_BET, "inskull_mask_file", venosa_inskull_mask, "mask_file")

            # trasformazione lineare fase venosa su ref
            venosa2ref_FLIRT = Node(FLIRT(), name='venosa2ref_FLIRT')
            venosa2ref_FLIRT.inputs.out_file = "r-venosa_inskull.nii.gz"
            venosa2ref_FLIRT.inputs.interp = "trilinear"
            venosa.connect(venosa_inskull_mask, "out_file", venosa2ref_FLIRT, "in_file")
            venosa.connect(venosa_modulo2ref_FLIRT, "out_matrix_file", venosa2ref_FLIRT, "in_matrix_file")
            self.connect(t1, "ref_BET.out_file", venosa, "venosa2ref_FLIRT.reference")

            # trovo il valore massimo della fase venosa
            venosa_range = Node(ImageStats(), name="venosa_range")
            venosa_range.inputs.op_string = "-R"
            venosa.connect(venosa2ref_FLIRT, "out_file", venosa_range, "in_file")

            # rescale della venosa in 0-100
            venosa_rescale = Node(ImageMaths(), name="venosa_rescale")
            venosa_rescale.inputs.out_file = "r-venosa_inskull.nii.gz"
            def rescale_string(range):
                op_string = "-mul 100 -div %f" % range[1]
                return op_string
            venosa.connect(venosa_range, ('out_stat', rescale_string), venosa_rescale, 'op_string')
            venosa.connect(venosa2ref_FLIRT, "out_file", venosa_rescale, "in_file")
            venosa.sink_result(self.base_dir, venosa_rescale, 'out_file', 'scene')

        # ELABORAZIONE DTI
        if check_input['mr_dti']:

            dti_preproc = Workflow_mo(name="dti_preproc", base_dir="./")

            # conversione dicom->nifti
            dti_conv = Node(Dcm2niix_mo(), name='dti_conv')
            dti_dir = os.path.join(self.base_dir, SWANiGlobalConfig['DEFAULTFOLDERS']['default_mr_dti_folder'])
            dti_conv.inputs.source_dir = dti_dir
            dti_conv.inputs.out_filename = "dti"

            # TODO ci serve riorientare la dti secondo i nostri piani standard?
            # dti_reOrient=Node(Orient_mo(),name='dti_reOrient')

            # estrazione immagine b0
            dti_nodif = Node(ExtractROI(), name='dti_nodif')
            dti_nodif.inputs.t_min = 0
            dti_nodif.inputs.t_size = 1
            dti_nodif.inputs.roi_file = 'nodif.nii.gz'
            dti_preproc.connect(dti_conv, "converted_files", dti_nodif, "in_file")

            # rimozione scalpo al b0
            nodif_BET = Node(BET(), name='nodif_BET')
            nodif_BET.inputs.frac = 0.3
            nodif_BET.inputs.robust = True
            nodif_BET.inputs.threshold = True
            nodif_BET.inputs.mask = True
            dti_preproc.connect(dti_nodif, "roi_file", nodif_BET, "in_file")

            # correzione artefatti da movimento e eddy current
            dti_eddy = Node(EddyCorrect(), name='dti_eddy')
            dti_eddy.inputs.ref_num = 0
            dti_eddy.inputs.out_file = "data.nii.gz"
            dti_preproc.connect(dti_conv, "converted_files", dti_eddy, "in_file")

            # calcolo delle metriche base dti
            dti_dtifit = Node(DTIFit(), name='dti_dtifit')
            dti_preproc.connect(dti_eddy, "eddy_corrected", dti_dtifit, "dwi")
            dti_preproc.connect(nodif_BET, "mask_file", dti_dtifit, "mask")
            dti_preproc.connect(dti_conv, "bvecs", dti_dtifit, "bvecs")
            dti_preproc.connect(dti_conv, "bvals", dti_dtifit, "bvals")

            # trasformazione lineare nodif nello spazio ref
            diff2ref_FLIRT = Node(FLIRT(), name='diff2ref_FLIRT')
            diff2ref_FLIRT.inputs.out_matrix_file = "diff2ref.mat"
            diff2ref_FLIRT.inputs.cost = "corratio"
            diff2ref_FLIRT.inputs.searchr_x = [-90, 90]
            diff2ref_FLIRT.inputs.searchr_y = [-90, 90]
            diff2ref_FLIRT.inputs.searchr_z = [-90, 90]
            diff2ref_FLIRT.inputs.dof = 6
            dti_preproc.connect(nodif_BET, "out_file", diff2ref_FLIRT, "in_file")
            self.connect(t1, "ref_BET.out_file", dti_preproc, "diff2ref_FLIRT.reference")

            # sposto FA nello spazio ref
            FA2ref_FLIRT = Node(FLIRT(), name='FA2ref_FLIRT')
            FA2ref_FLIRT.inputs.out_file = "r-FA.nii.gz"
            FA2ref_FLIRT.inputs.interp = "trilinear"
            dti_preproc.connect(dti_dtifit, "FA", FA2ref_FLIRT, "in_file")
            dti_preproc.connect(diff2ref_FLIRT, "out_matrix_file", FA2ref_FLIRT, "in_matrix_file")
            self.connect(t1, "ref_BET.out_file", dti_preproc, "FA2ref_FLIRT.reference")
            dti_preproc.sink_result(self.base_dir, FA2ref_FLIRT, 'out_file', 'scene')

            if tractography:
                # calcolo del modello di trattografia
                dti_bedpostx = Node(BEDPOSTX5_mo(), name='dti_bedpostx')
                dti_bedpostx.inputs.n_fibres = 2
                dti_bedpostx.inputs.rician = True
                # dti_bedpostx.inputs.num_threads=18
                dti_bedpostx.inputs.sample_every = 25
                dti_bedpostx.inputs.n_jumps = 1250
                dti_bedpostx.inputs.burn_in = 1000
                dti_preproc.connect(dti_eddy, "eddy_corrected", dti_bedpostx, "dwi")
                dti_preproc.connect(nodif_BET, "mask_file", dti_bedpostx, "mask")
                dti_preproc.connect(dti_conv, "bvecs", dti_bedpostx, "bvecs")
                dti_preproc.connect(dti_conv, "bvals", dti_bedpostx, "bvals")

                # calcolo di varie matrici di trasformazione derivate che serviranno per la trattografia
                ref2diff_convert = Node(ConvertXFM(), name='ref2diff_convert')
                ref2diff_convert.inputs.invert_xfm = True
                ref2diff_convert.inputs.out_file = 'ref2diff.mat'
                dti_preproc.connect(diff2ref_FLIRT, "out_matrix_file", ref2diff_convert, "in_file")

                diff2mni_convert = Node(ConvertXFM(), name='diff2mni_convert')
                diff2mni_convert.inputs.concat_xfm = True
                diff2mni_convert.inputs.out_file = 'diff2mni.mat'
                dti_preproc.connect(diff2ref_FLIRT, "out_matrix_file", diff2mni_convert, "in_file2")

                mni2diff_convert = Node(ConvertXFM(), name='mni2diff_convert')
                mni2diff_convert.inputs.invert_xfm = True
                mni2diff_convert.inputs.out_file = 'mni2diff.mat'
                dti_preproc.connect(diff2mni_convert, "out_file", mni2diff_convert, "in_file")
                self.connect(mni, "ref2mni_FLIRT.out_matrix_file", dti_preproc, "diff2mni_convert.in_file")

                diff2mni_convertwarp = Node(ConvertWarp(), name='diff2mni_convertwarp')
                diff2mni_convertwarp.inputs.reference = mni_path
                diff2mni_convertwarp.inputs.out_file = 'diff2mni_warp.nii.gz'
                dti_preproc.connect(diff2ref_FLIRT, "out_matrix_file", diff2mni_convertwarp, "premat")
                self.connect(mni, "ref2mni_FNIRT.fieldcoeff_file", dti_preproc, "diff2mni_convertwarp.warp1")

                mni2diff_convertwarp = Node(ConvertWarp(), name='mni2diff_convertwarp')
                mni2diff_convertwarp.inputs.out_file = 'mni2diff_warp.nii.gz'
                dti_preproc.connect(nodif_BET, "out_file", mni2diff_convertwarp, "reference")
                dti_preproc.connect(ref2diff_convert, "out_file", mni2diff_convertwarp, "postmat")
                self.connect(mni, "ref2mni_INVWARP.inverse_warp", dti_preproc, "mni2diff_convertwarp.warp1")

                tractWf_list = {}
                for tract in ptConfig['DEFAULTTRACTS'].keys():
                    if not ptConfig.getboolean('DEFAULTTRACTS', tract): continue
                    tractWf_list[tract] = create_probtrackx2_pipeline('tract_' + tract, tract, self.base_dir)
                    self.connect(dti_preproc, "dti_bedpostx.merged_fsamples", tractWf_list[tract], "inputnode.fsamples")
                    self.connect(dti_preproc, "nodif_BET.mask_file", tractWf_list[tract], "inputnode.mask")
                    self.connect(dti_preproc, "dti_bedpostx.merged_phsamples", tractWf_list[tract],
                                 "inputnode.phsamples")
                    self.connect(dti_preproc, "dti_bedpostx.merged_thsamples", tractWf_list[tract],
                                 "inputnode.thsamples")
                    self.connect(dti_preproc, "mni2diff_convertwarp.out_file", tractWf_list[tract], "inputnode.xfm")
                    self.connect(dti_preproc, "diff2mni_convertwarp.out_file", tractWf_list[tract], "inputnode.inv_xfm")
                    self.connect(t1, "ref_BET.out_file", tractWf_list[tract], "inputnode.ref")
                    self.connect(mni, "ref2mni_INVWARP.inverse_warp", tractWf_list[tract], "inputnode.mni2ref_warp")

        # CONTROLLO SE SONO STATE CARICATE SEQUENZE FMRI ED EVENTUALMENTE LE ANALIZZO SINGOLARMENTE
        for y in range(ptConfig.FMRI_NUM):

            if check_input['mr_fmri_%d' % y]:

                taskName = ptConfig['FMRI']["task_%d_name" % y]
                taskDuration = ptConfig['FMRI'].getint('task_%d_duration' % y)
                restDuration = ptConfig['FMRI'].getint('rest_%d_duration' % y)

                try:
                    TR = ptConfig['FMRI'].getfloat('task_%d_tr' % y)
                except:
                    TR = -1

                try:
                    slice_timing = ptConfig['FMRI'].getint('task_%d_st' % y)
                except:
                    slice_timing = 0

                try:
                    nvols = ptConfig['FMRI'].getint('task_%d_vols' % y)
                except:
                    nvols = -1

                fMRI_wf = create_fMRI_pipeline(y, self.base_dir)
                inputnode = fMRI_wf.get_node("inputnode")
                inputnode.inputs.TR = TR
                inputnode.inputs.slice_timing = slice_timing
                inputnode.inputs.nvols = nvols
                inputnode.inputs.taskName = taskName
                inputnode.inputs.taskDuration = taskDuration
                inputnode.inputs.restDuration = restDuration
                inputnode.inputs.fMRI_dir = os.path.join(self.base_dir, SWANiGlobalConfig['DEFAULTFOLDERS'][
                    'default_mr_fmri_%d_folder' % y])
                self.connect(t1, "ref_BET.out_file", fMRI_wf, "inputnode.ref_BET")
