import configparser
import os
from SWANi.utils.APPLABELS import APPLABELS
from SWANi import strings

#todo valutare di spostare le key delle configurazioni in file costanti esterno
class SWANiConfig(configparser.ConfigParser):

    FMRI_NUM = 3

    INPUTLIST = [
        'mr_t13d',
        'mr_flair3d',
        'mr_mdc',
        'mr_venosa',
        'mr_venosa2',
        'mr_dti',
        'mr_asl',
        #todo da cancellare se confermiamo eliminazione elaborazione ct
        # 'ct_brain',
        'pet_brain',
        'op_mr_flair2d_tra',
        'op_mr_flair2d_cor',
        'op_mr_flair2d_sag',
    ]

    for x in range(FMRI_NUM):
        INPUTLIST.append('mr_fmri_%d' % x)

    TRACTS = {}
    TRACTS["af"] = ['Arcuate Fasciculus', 'true']
    TRACTS["cst"] = ['Corticospinal Tract', 'true']
    TRACTS["or"] = ['Optic Radiation', 'true']
    TRACTS["ar"] = ['Acoustic Radiation', 'false']
    TRACTS["fa"] = ['Frontal Aslant', 'false']
    TRACTS["fx"] = ['Fornix', 'false']
    TRACTS["ifo"] = ['Inferior Fronto-Occipital Fasciculus', 'false']
    TRACTS["ilf"] = ['Inferior Longitudinal Fasciculus', 'false']
    TRACTS["uf"] = ['Uncinate Fasciculus', 'false']

    DEFAULT_WF = {}
    DEFAULT_WF['0'] = {
        'wftype': '0',
        'freesurfer': 'true',
        'hippoAmygLabels': 'false',
        'domap': 'false',
        'ai': 'false',
        'tractography': 'true',
    }
    DEFAULT_WF['1'] = {
        'wftype': '1',
        'freesurfer': 'true',
        'hippoAmygLabels': 'true',
        'domap': 'true',
        'ai': 'true',
        'tractography': 'false',
    }

    def __init__(self, ptFolder=None, freesurfer=None):
        super(SWANiConfig, self).__init__()
        

        if ptFolder != None:
            # NEL CASO STIA GESTENDO LE IMPOSTAZIONI SPECIFICHE DI UN UTENTE COPIO ALCUNI VALORI DALLE IMPOSTAZIONI GLOBALI
            self.globalConfig = False
            self.configFile = os.path.join(os.path.join(ptFolder, ".config"))
            self.freesurfer=freesurfer
        else:
            # NEL CASO STIA GESTENDO LE IMPOSTAZIONI GLOBALI DELL'APP
            self.globalConfig = True
            self.configFile = os.path.abspath(os.path.join(
                os.path.expanduser("~"), "."+strings.APPNAME+"config"))

        self.createDefaultConfig()

        if os.path.exists(self.configFile):
            self.read(self.configFile)

        self.save()

    def reLoad(self):
        self.read(self.configFile)

    def createDefaultConfig(self):
        if self.globalConfig:
            self['MAIN'] = {
                'patientsfolder': '',
                'patientsprefix': 'pt_',
                'slicerPath': '',
                'shortcutPath': '',
                'lastPID': '-1',
                'maxPt': '1',
                'maxPtCPU': '-1',
                'slicerSceneExt': '0',
                'defaultWfType': '0',
                'fmritaskduration': '30',
            }

            self['OPTIONAL_SERIES'] = {'mr_flair2d': 'false'}

            self['DEFAULTFOLDERS'] = {}
            for this in self.INPUTLIST:
                self['DEFAULTFOLDERS']['default_' +
                                       this+'_folder'] = 'dicom/'+this+'/'

            self['DEFAULTNAMESERIES'] = {}
            for name in self.INPUTLIST:
                self['DEFAULTNAMESERIES']["Default_"+name+"_name"] = ""

            self['DEFAULTTRACTS'] = {}

            for index, key in enumerate(self.TRACTS):
                self['DEFAULTTRACTS'][key] = self.TRACTS[key][1]
        else:
            tmpConfig = SWANiConfig()
            self.setWfOption(tmpConfig['MAIN']['defaultWfType'])
            self['FMRI'] = {}

            for x in range(SWANiConfig.FMRI_NUM):
                self['FMRI']['task_%d_name' % x] = 'Task'
                self['FMRI']['task_%d_duration' % x] = tmpConfig['MAIN']['fmritaskduration']
                self['FMRI']['rest_%d_duration' % x] = tmpConfig['MAIN']['fmritaskduration']
                self['FMRI']['task_%d_tr' % x] = 'auto'
                self['FMRI']['task_%d_vols' % x] = 'auto'
                self['FMRI']['task_%d_st' % x] = '0'

            self['DEFAULTTRACTS'] = tmpConfig['DEFAULTTRACTS']

    def setWfOption(self, wf):
        if self.globalConfig:
            return
        wf = str(wf)
        self['WF_OPTION'] = SWANiConfig.DEFAULT_WF[wf]
        self.update_freesurfer_pref()

    def update_freesurfer_pref(self):
        if not self.is_freesurfer():
            self['WF_OPTION']['freesurfer'] = 'false'
        if not self.is_freesurfer_matlab():
            self['WF_OPTION']['hippoAmygLabels'] = 'false'
            
    def is_freesurfer(self):
        if self.globalConfig or self.freesurfer is None:
            return False
        return self.freesurfer[0]
    
    def is_freesurfer_matlab(self):
        if self.globalConfig or self.freesurfer is None:
            return False
        return self.freesurfer[0]

    def save(self):
        with open(self.configFile, "w") as openedFile:
            self.write(openedFile)

    def getPatientsFolder(self):
        return self["MAIN"]["PatientsFolder"]
