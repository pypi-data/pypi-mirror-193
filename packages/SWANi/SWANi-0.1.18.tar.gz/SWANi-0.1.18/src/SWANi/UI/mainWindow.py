from PySide6.QtWidgets import (QMainWindow, QMessageBox, QFileDialog, QInputDialog,
                               QLineEdit, QTabWidget, QGridLayout, QLabel, QSizePolicy,
                               QSpacerItem, QWidget, QTabBar, QDialog)
from SWANi.utils.check_dependency import (check_dcm2niix, check_fsl, check_freesurfer,
                                          check_graphviz, check_slicer)
from PySide6.QtGui import QAction, QIcon, QPixmap, QFont
from PySide6.QtCore import QCoreApplication
from PySide6.QtSvgWidgets import QSvgWidget
import os
import shutil
import sys
import pyshortcuts
from pyshortcuts.shortcut import shortcut as shcdef
from pyshortcuts.shortcut import Shortcut

from SWANi.UI.ptTAB import ptTAB
from SWANi.UI.preferencesWindow import preferencesWindow
import SWANi_supplement
from SWANi.utils.APPLABELS import APPLABELS
from SWANi import __version__
from SWANi import strings


class mainWindow(QMainWindow):
    ptDirPath = ""
    tabWidget = None

    def __init__(self, SWANiGlobalConfig):

        self.SWANiGlobalConfig = SWANiGlobalConfig

        super(mainWindow, self).__init__()
        self.setWindowIcon(QIcon(QPixmap(SWANi_supplement.appIcon_file)))

        self.okIcon_file = SWANi_supplement.okIcon_file
        self.errorIcon_file = SWANi_supplement.errorIcon_file
        self.warnIcon_file = SWANi_supplement.warnIcon_file
        self.loadingMovie_file = SWANi_supplement.loadingMovie_file
        self.voidsvg_file = SWANi_supplement.voidsvg_file

        self.okIcon = QPixmap(self.okIcon_file)
        self.errorIcon = QPixmap(self.errorIcon_file)
        self.warnIcon = QPixmap(self.warnIcon_file)

        while self.SWANiGlobalConfig.getPatientsFolder() == "" or not os.path.exists(self.SWANiGlobalConfig.getPatientsFolder()):
            msgBox = QMessageBox()
            msgBox.setText(strings.mainwindow_chose_working_dir)
            msgBox.exec()
            self.setPatientsFolder()

        os.chdir(self.SWANiGlobalConfig.getPatientsFolder())

        self.inizializeUI()

        # controllo che eventuali shortcut salvati esistano
        if self.SWANiGlobalConfig['MAIN']['shortcutPath'] != '':
            targets = self.SWANiGlobalConfig['MAIN']['shortcutPath'].split("|")
            newPath = ''
            change = False
            for fil in targets:
                if "SWANi" in fil and os.path.exists(fil):
                    if newPath != '':
                        newPath = newPath+"|"
                    newPath = newPath+fil
                else:
                    change = True
            if change:
                self.SWANiGlobalConfig['MAIN']['shortcutPath'] = newPath
                self.SWANiGlobalConfig.save()

    def openPtDir(self, folderPath):
        thistab = ptTAB(self.SWANiGlobalConfig, folderPath,
                        self, parent=self.mainTAB)
        self.ptTabsArray.append(thistab)

        self.mainTAB.addTab(thistab, os.path.basename(folderPath))
        self.mainTAB.setCurrentWidget(thistab)
        thistab.loadPt()

    def check_pt_limit(self):
        if self.SWANiGlobalConfig.getint('MAIN', 'maxPt') > 0 and len(self.ptTabsArray) >= self.SWANiGlobalConfig.getint('MAIN', 'maxPt'):
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText(strings.mainwindow_max_pt_error)
            msgBox.exec()
            return False
        return True


    def searchPtDir(self):
        if not self.check_pt_limit():
            return

        fileDialog = QFileDialog()
        fileDialog.setDirectory(self.SWANiGlobalConfig.getPatientsFolder())
        folderPath = fileDialog.getExistingDirectory(self, strings.mainwindow_select_pt_folder)
        if not os.path.exists(folderPath):
            return

        if not os.path.abspath(folderPath).startswith(os.path.abspath(self.SWANiGlobalConfig.getPatientsFolder())+os.sep):
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText(strings.mainwindow_ptfolder_outside_workingdir_error)
            msgBox.exec()
            return

        for pt in self.ptTabsArray:
            if pt.ptFolder == folderPath:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setText(strings.mainwindow_pt_already_loaded_error)
                msgBox.exec()
                return

        if not self.checkPtDir(folderPath):
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText(strings.mainwindow_invalid_folder_error)
            msgBox.exec()

            msgBox2 = QMessageBox()
            msgBox2.setInformativeText(strings.mainwindow_force_dir_update)
            msgBox2.setIcon(QMessageBox.Warning)
            msgBox2.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msgBox2.button(QMessageBox.Yes).setText("Yes")
            msgBox2.button(QMessageBox.No).setText("No")
            msgBox2.setDefaultButton(QMessageBox.No)
            ret = msgBox2.exec()
            if ret == QMessageBox.Yes:
                self.updatePtDir(folderPath)
            else:
                return
        self.openPtDir(folderPath)

    def getSuggestedPatientName(self):
        import re
        regex = re.compile(
            '^'+self.SWANiGlobalConfig["MAIN"]["patientsprefix"]+'\d+$')
        fileList = []
        for thisDir in os.listdir(self.SWANiGlobalConfig.getPatientsFolder()):
            if regex.match(thisDir):
                fileList.append(
                    int(thisDir.replace(self.SWANiGlobalConfig['MAIN']['patientsprefix'], "")))

        if len(fileList) == 0:
            return self.SWANiGlobalConfig['MAIN']['patientsprefix']+"1"
        return self.SWANiGlobalConfig['MAIN']['patientsprefix']+str(max(fileList)+1)

    def choseNewPtDir(self):
        if not self.check_pt_limit():
            return

        text, ok = QInputDialog.getText(self, strings.mainwindow_new_pt_title,
                                        strings.mainwindow_new_pt_name, QLineEdit.Normal, self.getSuggestedPatientName())

        if not ok:
            return

        ptName = str(text)

        if ptName == "":
            msgBox = QMessageBox()
            msgBox.setText(strings.mainwindow_new_pt_name_error+ptName)
            msgBox.exec()
            return

        if os.path.exists(os.path.join(self.SWANiGlobalConfig.getPatientsFolder(), ptName)):
            msgBox = QMessageBox()
            msgBox.setText(strings.mainwindow_pt_exists_error+ptName)
            msgBox.exec()
            return

        self.createNewPtDir(ptName)

    def setPatientsFolder(self):
        folderPath = QFileDialog.getExistingDirectory(self, strings.mainwindow_chose_working_dir_title)
        if not os.path.exists(folderPath):
            return
        self.SWANiGlobalConfig["MAIN"]["PatientsFolder"] = os.path.abspath(folderPath)
        self.SWANiGlobalConfig.save()
        os.chdir(folderPath)

    def createNewPtDir(self, ptName):
        baseFolder = os.path.abspath(os.path.join(
            self.SWANiGlobalConfig.getPatientsFolder(), ptName))

        for folder in self.SWANiGlobalConfig["DEFAULTFOLDERS"]:
            os.makedirs(os.path.join(
                baseFolder, self.SWANiGlobalConfig['DEFAULTFOLDERS'][folder]), exist_ok=True)

        msgBox = QMessageBox()
        msgBox.setText(strings.mainwindow_new_pt_created+baseFolder)
        msgBox.exec()

        self.openPtDir(baseFolder)

    def checkPtDir(self, dirPath):
        for folder in self.SWANiGlobalConfig["DEFAULTFOLDERS"]:
            if not os.path.exists(os.path.join(dirPath, self.SWANiGlobalConfig["DEFAULTFOLDERS"][folder])):
                return False
        return True

    def updatePtDir(self, dirPath):
        for folder in self.SWANiGlobalConfig["DEFAULTFOLDERS"]:
            if not os.path.exists(os.path.join(dirPath, self.SWANiGlobalConfig["DEFAULTFOLDERS"][folder])):
                os.makedirs(os.path.join(
                    dirPath, self.SWANiGlobalConfig['DEFAULTFOLDERS'][folder]), exist_ok=True)

    def editConfig(self):
        if self.check_running_wfs():
            msgBox = QMessageBox()
            msgBox.setText(strings.mainwindow_pref_disabled_error)
            msgBox.exec()
            return
        self.w = preferencesWindow(self.SWANiGlobalConfig, self)
        ret = self.w.exec()
        if ret == APPLABELS.EXIT_CODE_REBOOT:
            self.close()
            QCoreApplication.exit(APPLABELS.EXIT_CODE_REBOOT)
        if ret != 0:
            self.reset_wfs()

    def check_running_wfs(self):
        if not hasattr(self, "ptTabsArray"):
            return False
        for pt in self.ptTabsArray:
            if hasattr(pt, "wf_process") and pt.wf_process.is_alive():
                return True
        return False

    def reset_wfs(self):
        for pt in self.ptTabsArray:
            pt.reset_wf()

    def toggleShortcut(self):
        if self.SWANiGlobalConfig['MAIN']['shortcutPath'] == "":

            setattr(pyshortcuts.shortcut, "shortcut", my_shortcut)

            if pyshortcuts.platform.startswith('darwin'):
                setattr(pyshortcuts.darwin, "shortcut", my_shortcut)
                iconFile = SWANi_supplement.appIcns_file
            else:
                iconFile = SWANi_supplement.appIcon_file
                setattr(pyshortcuts.linux, "shortcut", my_shortcut)

            scut = pyshortcuts.make_shortcut(
                strings.APPNAME, name=strings.APPNAME, icon=iconFile, terminal=False, executable=sys.executable+" -m")
            targets = [os.path.join(f, scut.target)
                       for f in (scut.desktop_dir, scut.startmenu_dir)]
            self.SWANiGlobalConfig['MAIN']['shortcutPath'] = "|".join(targets)
            msgBox = QMessageBox()
            msgBox.setText(strings.mainwindow_shortcut_created)
            msgBox.exec()
        else:
            targets = self.SWANiGlobalConfig['MAIN']['shortcutPath'].split("|")
            for fil in targets:
                if "SWANi" in fil and os.path.exists(fil):
                    if os.path.isdir(fil):
                        shutil.rmtree(fil, ignore_errors=True)
                    else:
                        os.remove(fil)
            self.SWANiGlobalConfig['MAIN']['shortcutPath'] = ""
            msgBox = QMessageBox()
            msgBox.setText(strings.mainwindow_shortcut_removed)
            msgBox.exec()
        self.SWANiGlobalConfig.save()

    def about(self):
        aboutDialog = QDialog(parent=self)
        layout = QGridLayout()

        boldFont = QFont()
        boldFont.setBold(True)
        titleFont = QFont()
        titleFont.setBold(True)
        titleFont.setPointSize(titleFont.pointSize()*1.5)

        label_about1 = QLabel(strings.APPNAME)
        label_about1.setFont(titleFont)
        label_about2 = QLabel(strings.app_acronym)
        label_about3 = QLabel("Version: "+__version__)

        label_about4 = QLabel(strings.aboutwindow_python_libs)

        label_about_icon = QLabel()
        icon = QPixmap(SWANi_supplement.appIcon_file)

        label_about_icon.setPixmap(icon.scaled(60, 60))

        layout.addWidget(label_about1, 0, 1)
        layout.addWidget(label_about2, 1, 1)
        layout.addWidget(label_about3, 2, 1)
        layout.addWidget(label_about4, 3, 1)

        layout.addWidget(label_about_icon, 0, 0, 3, 1)

        aboutDialog.setLayout(layout)
        aboutDialog.exec()

    def inizializeUI(self):
        self.resize(800, 600)
        self.setWindowTitle(strings.APPNAME+" - "+strings.app_acronym)

        self.statusBar().showMessage('')

        button_action = QAction(QIcon.fromTheme(
            "document-open"), strings.menu_load_pt, self)
        button_action.setStatusTip(strings.menu_load_pt_tip)
        button_action.triggered.connect(self.searchPtDir)

        button_action2 = QAction(QIcon.fromTheme(
            "document-new"), strings.menu_new_pt, self)
        button_action2.setStatusTip(strings.menu_new_pt_tip)
        button_action2.triggered.connect(self.choseNewPtDir)

        button_action3 = QAction(QIcon.fromTheme(
            "application-exit"), strings.menu_exit, self)
        button_action3.triggered.connect(self.close)

        button_action4 = QAction(QIcon.fromTheme(
            "preferences-other"), strings.menu_pref, self)
        button_action4.setStatusTip("Edit "+strings.APPNAME+" precerences")
        button_action4.triggered.connect(self.editConfig)

        button_action5 = QAction("Shortcut", self)
        button_action5.setStatusTip(strings.menu_pref_tip)
        button_action5.triggered.connect(self.toggleShortcut)

        button_action6 = QAction(strings.menu_about, self)
        button_action6.triggered.connect(self.about)

        menu = self.menuBar()
        menu.setNativeMenuBar(False)
        file_menu = menu.addMenu(strings.menu_file_name)
        file_menu.addAction(button_action)
        file_menu.addAction(button_action2)
        file_menu.addAction(button_action3)
        tool_menu = menu.addMenu(strings.menu_tools_name)
        tool_menu.addAction(button_action4)
        tool_menu.addAction(button_action5)
        help_menu = menu.addMenu(strings.menu_help_name)
        help_menu.addAction(button_action6)

        self.mainTAB = QTabWidget(parent=self)
        self.mainTAB.setTabsClosable(True)
        self.mainTAB.tabCloseRequested.connect(self.closePt)
        self.setCentralWidget(self.mainTAB)
        self.homeTab = QWidget()

        self.mainTAB.addTab(self.homeTab, strings.mainwindow_home_tab_name)

        # rimozione tasto chiusura da tab home, a destra o sinistra in base allo stile
        self.mainTAB.tabBar().setTabButton(0, QTabBar.LeftSide, None)
        self.mainTAB.tabBar().setTabButton(0, QTabBar.RightSide, None)

        self.homeTabUI()

        self.ptTabsArray = []

        self.show()

    def closePt(self, index):
        if index == -1:
            return

        tabItem = self.mainTAB.widget(index)
        if hasattr(tabItem, "wf_process") and tabItem.wf_process.is_alive():
            msgBox = QMessageBox()
            msgBox.setText(strings.mainwindow_wf_executing_error_1)
            msgBox.exec()
            return

        tabItem.closeRoutine()
        self.ptTabsArray.remove(tabItem)
        self.mainTAB.removeTab(index)
        tabItem = None

    def closeEvent(self, event):
        # evito la chiusura se il wf è in esecuzione
        if not self.check_running_wfs():
            return super(mainWindow, self).closeEvent(event)
        else:
            msgBox = QMessageBox()
            msgBox.setText(strings.mainwindow_wf_executing_error_2)
            msgBox.exec()
            event.ignore()

    def homeTabUI(self):
        layout = QGridLayout()

        boldFont = QFont()
        boldFont.setBold(True)
        titleFont = QFont()
        titleFont.setBold(True)
        titleFont.setPointSize(titleFont.pointSize()*1.5)
        x = 0

        label_welcome1 = QLabel(strings.mainwindow_home_label1)
        label_welcome1.setFont(titleFont)
        label_welcome2 = QLabel(strings.mainwindow_home_label2)
        label_welcome2.setWordWrap(True)
        label_welcome3 = QLabel(strings.mainwindow_home_label3)
        label_welcome3.setWordWrap(True)
        label_welcome4 = QLabel(strings.mainwindow_home_label4)
        label_welcome4.setFont(boldFont)

        layout.addWidget(label_welcome1, x, 0, 1, 2)
        x += 1
        layout.addWidget(label_welcome2, x, 0, 1, 2)
        x += 1
        layout.addWidget(label_welcome3, x, 0, 1, 2)
        x += 1
        layout.addWidget(label_welcome4, x, 0, 1, 2)
        x += 1

        label_main_dep = QLabel(strings.mainwindow_home_label5)
        label_main_dep.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        label_main_dep.setFont(boldFont)
        layout.addWidget(label_main_dep, x, 0, 1, 2)
        x += 1

        msg, self.dcm2niix = check_dcm2niix()
        x = self.add_home_entry(layout, msg, self.dcm2niix, x)

        msg, self.fsl = check_fsl()
        x = self.add_home_entry(layout, msg, self.fsl, x)

        label_main_dep = QLabel(strings.mainwindow_home_label6)
        label_main_dep.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        label_main_dep.setFont(boldFont)
        layout.addWidget(label_main_dep, x, 0, 1, 2)
        x += 1

        msg, self.freesurfer = check_freesurfer()
        x = self.add_home_entry(layout, msg, self.freesurfer[0], x)

        if self.SWANiGlobalConfig['MAIN']['slicerPath'] == '' or not os.path.exists(self.SWANiGlobalConfig['MAIN']['slicerPath']):
            self.slicerlabel_icon = QSvgWidget()
            self.slicerlabel_icon.setFixedSize(25, 25)
            self.slicerlabel_icon.load(self.loadingMovie_file)
            layout.addWidget(self.slicerlabel_icon, x, 0)
            self.slicerlabel = QLabel(strings.mainwindow_dep_slicer_src)
            self.slicerlabel.setOpenExternalLinks(True)
            self.slicerlabel.setSizePolicy(
                QSizePolicy.Minimum, QSizePolicy.Minimum)
            layout.addWidget(self.slicerlabel, x, 1)
            x += 1

            self.SWANiGlobalConfig['MAIN']['slicerPath'] = ''
            slicerrun = check_slicer(x, parent=self)
            slicerrun.start()
            slicerrun.signal.slicer.connect(self.slicerrow)
        else:
            self.add_home_entry(layout, strings.mainwindow_dep_slicer_found, True, x)
        x += 1

        label_main_dep = QLabel(strings.mainwindow_home_label7)
        label_main_dep.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        label_main_dep.setFont(boldFont)
        layout.addWidget(label_main_dep, x, 0, 1, 2)
        x += 1

        msg, self.graphviz = check_graphviz()
        x = self.add_home_entry(layout, msg, self.graphviz, x)

        verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(verticalSpacer, x, 0, 1, 2)

        self.homeTab.setLayout(layout)

    def add_home_entry(self, gridlayout, msg, icon, x):
        label_icon = QLabel()
        label_icon.setFixedSize(25, 25)
        label_icon.setScaledContents(True)
        if icon:
            label_icon.setPixmap(self.okIcon)
        else:
            label_icon.setPixmap(self.errorIcon)
        gridlayout.addWidget(label_icon, x, 0)
        label = QLabel(msg)
        label.setOpenExternalLinks(True)
        label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        gridlayout.addWidget(label, x, 1)
        return (x+1)

    def slicerrow(self, cmd, msg, found, x):
        if found:
            self.SWANiGlobalConfig['MAIN']['slicerPath'] = cmd
            self.SWANiGlobalConfig.save()
            self.slicerlabel_icon.load(self.okIcon_file)
        else:
            self.slicerlabel_icon.load(self.errorIcon_file)
        self.slicerlabel.setText(msg)


orig_shortcut = shcdef


def my_shortcut(script, userfolders, name=None, description=None, folder=None, working_dir=None, icon=None):
    r = orig_shortcut(script, userfolders, name=name, description=description,
                      folder=folder, working_dir=working_dir, icon=icon)
    return Shortcut(strings.APPNAME, strings.APPNAME, r.icon, r.target,
                    working_dir, strings.APPNAME, strings.APPNAME, r.arguments,
                    r.desktop_dir, r.startmenu_dir)
