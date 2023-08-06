import os
import sys
import subprocess
from shutil import which
from nipype.interfaces import dcm2nii, fsl, freesurfer
from PySide6.QtCore import QThread, Signal, QObject
from SWANi import strings


def is_tool(name):
    """Check whether `name` is on PATH and marked as executable."""
    return which(name) is not None


def check_dcm2niix():
    version = dcm2nii.Info.version()
    if version is None:
        return strings.check_dep_dcm2niix_error, False
    return (strings.check_dep_dcm2niix_found % str(version)), True


def check_fsl():
    version = fsl.base.Info.version()
    if version is None:
        return strings.check_dep_fsl_error, False
    return (strings.check_dep_fsl_found % str(version)), True


def check_freesurfer():
    if freesurfer.base.Info.version() is None:
        return strings.check_dep_fs_error1, [False, False]

    version = freesurfer.base.Info.looseversion()
    if not "FREESURFER_HOME" in os.environ:
        return (strings.check_dep_fs_error2 % str(version)), [False, False]
    file = os.path.join(os.environ["FREESURFER_HOME"], "license.txt")
    if os.path.exists(file):
        mrc = os.system("checkMCR.sh")
        if mrc == 0:
            return (strings.check_dep_fs_found % str(version)), [True, True]
        # TODO: facciamo un parse dell'output del comando per dare all'utente il comando di installazione? o forse è meglio non basarsi sul formato attuale dell'output e linkare direttamente la pagina ufficiale?
        return (strings.check_dep_fs_error3 % str(version)), [True, False]

    return (strings.check_dep_fs_error4 % str(version)), [False, False]


def check_graphviz():
    if which("dot") is None:
        return strings.check_dep_graph_error, False
    return (strings.check_dep_graph_found), True


# def check_python_lib(libname):
#     return libname in sys.modules


class slicer_Signaler(QObject):
    slicer = Signal(str, str, bool, int)


class check_slicer(QThread):
    def __init__(self, x, parent=None):
        super(check_slicer, self).__init__(parent)
        self.signal = slicer_Signaler()
        self.x = x

    def run(self):
        import platform
        if platform.system() == "Darwin":
            findcmd = "find /Applications -type f -wholename *app/Contents/bin/PythonSlicer -print 2>/dev/null"
            relpath = "../MacOS/Slicer"
        elif platform.system() == "Linux":
            findcmd = "find / -executable -type f -wholename *bin/PythonSlicer -print -quit 2>/dev/null"
            relpath = "../Slicer"
        output = subprocess.run(findcmd, shell=True,
                                stdout=subprocess.PIPE).stdout.decode('utf-8')
        split = output.split("\n")
        cmd = ''
        found = False
        for entry in split:
            if entry == '':
                continue
            cmd = os.path.abspath(os.path.join(
                os.path.dirname(entry), relpath))
            break
        if cmd == '' or not os.path.exists(cmd):
            msg = strings.check_dep_slicer_error1
        else:
            cmd2 = cmd+" --no-splash --no-main-window --python-script " + \
                os.path.join(os.path.dirname(__file__), "modulecheck.py")
            output2 = subprocess.run(
                cmd2, shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
            if 'MODULE FOUND' in output2:
                found = True
                msg = strings.check_dep_slicer_found
            else:
                msg = strings.check_dep_slicer_error2

        self.signal.slicer.emit(cmd, msg, found, self.x)

    def terminate(self):
        return
