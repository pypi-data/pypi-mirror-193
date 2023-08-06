import sys
import os
import psutil
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtGui import QIcon, QPixmap
import SWANi_supplement
from SWANi.UI.mainWindow import mainWindow
from SWANi.utils.SWANiConfig import SWANiConfig
from SWANi.utils.APPLABELS import APPLABELS
from SWANi import strings


def main():

    currentExitCode = APPLABELS.EXIT_CODE_REBOOT

    while currentExitCode == APPLABELS.EXIT_CODE_REBOOT:

        if not QApplication.instance():
            app = QApplication(sys.argv)
        else:
            app = QApplication.instance()

        app.setWindowIcon(QIcon(QPixmap(SWANi_supplement.appIcon_file)))
        app.setApplicationDisplayName(strings.APPNAME)

        SWANiGlobalConfig = SWANiConfig()

        # escludo che ci siano altre istanze di SWANi in esecuzione
        lastPID = SWANiGlobalConfig.getint('MAIN', 'lastPID')
        if lastPID != os.getpid():
            try:
                psutil.Process(lastPID)
                msgBox = QMessageBox()
                msgBox.setText("Another instance of " +
                               strings.APPNAME+" is already running!")
                msgBox.exec()
                break

            except (psutil.NoSuchProcess, ValueError):
                SWANiGlobalConfig['MAIN']['lastPID'] = str(os.getpid())
                SWANiGlobalConfig.save()

        # e' fondmentale che la mainwindow sia "salvata" in una var, altrimenti
        # viene rimossa appena creata e l'app crasha!
        widget = mainWindow(SWANiGlobalConfig)
        widget.setWindowIcon(QIcon(QPixmap(SWANi_supplement.appIcon_file)))
        currentExitCode = app.exec()

    sys.exit(currentExitCode)


if __name__ == "__main__":

    main()
