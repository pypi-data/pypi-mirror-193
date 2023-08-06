import os

from PySide6.QtCore import Qt
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import (QDialog, QLabel, QGridLayout, QLineEdit, QVBoxLayout,
                               QGroupBox, QPushButton, QFileDialog, QMessageBox, QCheckBox,
                               QComboBox, QStyle, QHBoxLayout, QSizePolicy)

from SWANi import strings
from SWANi.utils.APPLABELS import APPLABELS


class preferencesWindow(QDialog):

    def __init__(self, myConfig, parent=None):
        super(preferencesWindow, self).__init__(parent)

        self.myConfig = myConfig
        self.restart = False

        if self.myConfig.globalConfig:
            title = strings.pref_window_title_global
        else:
            title = os.path.basename(os.path.dirname(
                self.myConfig.configFile)) + strings.pref_window_title_user

        self.setWindowTitle(title)

        pixmapi = getattr(QStyle, "SP_DirOpenIcon")
        iconOpenDir = self.style().standardIcon(pixmapi)

        self.inputs = {}

        layout = QHBoxLayout()
        sn_pane = QGroupBox()
        sn_pane.setObjectName("sn_pane")
        sn_layout = QVBoxLayout()
        sn_pane.setLayout(sn_layout)
        sn_pane.setFlat(True)
        sn_pane.setStyleSheet("QGroupBox#sn_pane {border:none;}")
        layout.addWidget(sn_pane)

        if self.myConfig.globalConfig:

            groupBox1 = QGroupBox(strings.pref_window_global_box_title)
            grid1 = QGridLayout()
            groupBox1.setLayout(grid1)
            x = 0

            grid1.addWidget(QLabel(strings.pref_window_global_box_mwd), x, 0)
            self.inputs['MAIN.patientsfolder'] = QLineEdit()
            self.inputs['MAIN.patientsfolder'].setReadOnly(True)
            self.inputs['MAIN.patientsfolder'].setText(
                self.myConfig['MAIN']['patientsfolder'])
            grid1.addWidget(self.inputs['MAIN.patientsfolder'], x, 1)
            patientsfolderButton = QPushButton()
            patientsfolderButton.setIcon(iconOpenDir)
            patientsfolderButton.clicked.connect(
                lambda checked=None, edit=self.inputs['MAIN.patientsfolder'],
                       message=strings.mainwindow_chose_working_dir_title: self.choseDir(edit, message))
            grid1.addWidget(patientsfolderButton, x, 2)

            x += 1

            grid1.addWidget(QLabel(strings.pref_window_global_box_slicer), x, 0)
            self.inputs['MAIN.slicerPath'] = QLineEdit()
            self.inputs['MAIN.slicerPath'].setReadOnly(True)
            self.inputs['MAIN.slicerPath'].setText(
                self.myConfig['MAIN']['slicerPath'])
            grid1.addWidget(self.inputs['MAIN.slicerPath'], x, 1)
            slicerfolderButton = QPushButton()
            slicerfolderButton.setIcon(iconOpenDir)
            slicerfolderButton.clicked.connect(
                lambda checked=None, edit=self.inputs['MAIN.slicerPath'],
                       message=strings.pref_window_select_slicer: self.choseFile(edit, message))
            grid1.addWidget(slicerfolderButton, x, 2)
            x += 1

            grid1.addWidget(QLabel(strings.pref_window_global_box_default_wf), x, 0)
            self.inputs['MAIN.defaultWfType'] = QComboBox(self)
            for index, label in enumerate(APPLABELS.WFTYPES):
                self.inputs['MAIN.defaultWfType'].insertItem(index, label)
            self.inputs['MAIN.defaultWfType'].setCurrentIndex(
                self.myConfig.getint('MAIN', 'defaultWfType'))

            grid1.addWidget(self.inputs['MAIN.defaultWfType'], x, 1)
            x += 1

            grid1.addWidget(QLabel(strings.pref_window_global_box_default_task), x, 0)
            self.inputs['MAIN.fmritaskduration'] = QLineEdit()
            self.inputs['MAIN.fmritaskduration'].setText(
                self.myConfig['MAIN']['fmritaskduration'])
            self.inputs['MAIN.fmritaskduration'].setValidator(
                QIntValidator(1, 500))
            grid1.addWidget(self.inputs['MAIN.fmritaskduration'], x, 1)
            x += 1

            grid1.addWidget(QLabel(strings.pref_window_global_box_pt_limit), x, 0)
            self.inputs['MAIN.maxPt'] = QLineEdit()
            self.inputs['MAIN.maxPt'].setText(self.myConfig['MAIN']['maxPt'])
            self.inputs['MAIN.maxPt'].setValidator(QIntValidator(1, 4))
            grid1.addWidget(self.inputs['MAIN.maxPt'], x, 1)
            x += 1

            grid1.addWidget(QLabel(strings.pref_window_global_box_cpu_limit), x, 0)
            self.inputs['MAIN.maxPtCPU'] = QLineEdit()
            self.inputs['MAIN.maxPtCPU'].setText(
                self.myConfig['MAIN']['maxPtCPU'])
            self.inputs['MAIN.maxPtCPU'].setValidator(QIntValidator(-1, 40))
            grid1.addWidget(self.inputs['MAIN.maxPtCPU'], x, 1)
            x += 1

            grid1.addWidget(QLabel(strings.pref_window_global_box_default_ext), x, 0)
            self.inputs['MAIN.slicerSceneExt'] = QComboBox(self)
            for index, label in enumerate(APPLABELS.SLICEREXTS):
                self.inputs['MAIN.slicerSceneExt'].insertItem(index, label)

            self.inputs['MAIN.slicerSceneExt'].setCurrentIndex(
                self.myConfig.getint('MAIN', 'slicerSceneExt'))

            grid1.addWidget(self.inputs['MAIN.slicerSceneExt'], x, 1)
            x += 1

            grid1.addWidget(QLabel("2D Flair"), x, 0)
            self.inputs['OPTIONAL_SERIES.mr_flair2d'] = QCheckBox()
            self.setCheckBox(self.inputs['OPTIONAL_SERIES.mr_flair2d'], self.myConfig.getboolean(
                'OPTIONAL_SERIES', 'mr_flair2d'))
            self.inputs['OPTIONAL_SERIES.mr_flair2d'].stateChanged.connect(
                self.setRestart)
            grid1.addWidget(self.inputs['OPTIONAL_SERIES.mr_flair2d'], x, 1)
            x += 1

            sn_layout.addWidget(groupBox1)

        else:
            groupBox2 = QGroupBox(strings.pref_window_wf_box_title)
            grid2 = QGridLayout()
            groupBox2.setLayout(grid2)

            self.myConfig.update_freesurfer_pref()

            x = 0

            self.inputs['WF_OPTION.freesurfer'] = QCheckBox()
            self.setCheckBox(self.inputs['WF_OPTION.freesurfer'], self.myConfig.getboolean(
                'WF_OPTION', 'freesurfer'))
            grid2.addWidget(self.inputs['WF_OPTION.freesurfer'], x, 0)
            label = QLabel(strings.pref_window_wf_box_reconall)
            label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
            grid2.addWidget(label, x, 1)
            if not self.myConfig.is_freesurfer():
                self.inputs['WF_OPTION.freesurfer'].setEnabled(False)
                self.inputs['WF_OPTION.freesurfer'].setToolTip(strings.pref_window_wf_box_reconall_disabled_tip)
                label.setToolTip(strings.pref_window_wf_box_reconall_disabled_tip)
                label.setStyleSheet("color: gray")
            x += 1

            self.inputs['WF_OPTION.hippoAmygLabels'] = QCheckBox()
            self.setCheckBox(self.inputs['WF_OPTION.hippoAmygLabels'], self.myConfig.getboolean(
                'WF_OPTION', 'hippoAmygLabels'))
            grid2.addWidget(self.inputs['WF_OPTION.hippoAmygLabels'], x, 0)
            label = QLabel(strings.pref_window_wf_box_hippo)
            grid2.addWidget(label, x, 1)
            if not self.myConfig.is_freesurfer():
                self.inputs['WF_OPTION.hippoAmygLabels'].setEnabled(False)
                self.inputs['WF_OPTION.hippoAmygLabels'].setToolTip(strings.pref_window_wf_box_hippo_disabled_tip)
                label.setToolTip(strings.pref_window_wf_box_hippo_disabled_tip)
                label.setStyleSheet("color: gray")
            x += 1

            self.inputs['WF_OPTION.ai'] = QCheckBox()
            self.setCheckBox(
                self.inputs['WF_OPTION.ai'], self.myConfig.getboolean('WF_OPTION', 'ai'))
            grid2.addWidget(self.inputs['WF_OPTION.ai'], x, 0)
            grid2.addWidget(QLabel(strings.pref_window_wf_box_ai), x, 1)
            x += 1

            self.inputs['WF_OPTION.domap'] = QCheckBox()
            self.setCheckBox(
                self.inputs['WF_OPTION.domap'], self.myConfig.getboolean('WF_OPTION', 'domap'))
            grid2.addWidget(self.inputs['WF_OPTION.domap'], x, 0)
            grid2.addWidget(QLabel(strings.pref_window_wf_box_domap), x, 1)
            x += 1

            self.inputs['WF_OPTION.tractography'] = QCheckBox()
            self.setCheckBox(self.inputs['WF_OPTION.tractography'], self.myConfig.getboolean(
                'WF_OPTION', 'tractography'))
            grid2.addWidget(self.inputs['WF_OPTION.tractography'], x, 0)
            grid2.addWidget(QLabel(strings.pref_window_wf_box_tractography), x, 1)
            x += 1

            sn_layout.addWidget(groupBox2)

            dx_pane = QGroupBox()
            dx_pane.setObjectName("dx_pane")
            dx_pane.setFlat(True)
            dx_pane.setStyleSheet("QGroupBox#dx_pane {border:none;}")
            dx_layout = QVBoxLayout()
            layout.addWidget(dx_pane)
            dx_pane.setLayout(dx_layout)

            for y in range(myConfig.FMRI_NUM):

                groupBoxfunc = QGroupBox("fMRI - %d" % y)
                gridfunc = QGridLayout()
                groupBoxfunc.setLayout(gridfunc)
                x = 0

                optName = 'task_%d_name' % y
                gridfunc.addWidget(QLabel(strings.pref_window_fmri_box_task_name), x, 0)
                self.inputs['FMRI.' + optName] = QLineEdit()
                self.inputs['FMRI.' +
                            optName].setText(self.myConfig['FMRI'][optName])
                gridfunc.addWidget(self.inputs['FMRI.' + optName], x, 1)

                optName = 'task_%d_duration' % y
                gridfunc.addWidget(QLabel(strings.pref_window_fmri_box_task_duration), x, 2)
                self.inputs['FMRI.' + optName] = QLineEdit()
                self.inputs['FMRI.' +
                            optName].setText(self.myConfig['FMRI'][optName])
                self.inputs['FMRI.' +
                            optName].setValidator(QIntValidator(1, 500))
                gridfunc.addWidget(self.inputs['FMRI.' + optName], x, 3)
                x += 1

                optName = 'rest_%d_duration' % y
                gridfunc.addWidget(QLabel(strings.pref_window_fmri_box_rest_duration), x, 0)
                self.inputs['FMRI.' + optName] = QLineEdit()
                self.inputs['FMRI.' +
                            optName].setText(self.myConfig['FMRI'][optName])
                self.inputs['FMRI.' +
                            optName].setValidator(QIntValidator(1, 500))
                gridfunc.addWidget(self.inputs['FMRI.' + optName], x, 1)

                optName = 'task_%d_tr' % y
                gridfunc.addWidget(QLabel(strings.pref_window_fmri_box_tr), x, 2)
                self.inputs['FMRI.' + optName] = QLineEdit()
                self.inputs['FMRI.' +
                            optName].setText(self.myConfig['FMRI'][optName])
                gridfunc.addWidget(self.inputs['FMRI.' + optName], x, 3)
                x += 1

                optName = 'task_%d_vols' % y
                gridfunc.addWidget(QLabel(strings.pref_window_fmri_box_vols), x, 0)
                self.inputs['FMRI.' + optName] = QLineEdit()
                self.inputs['FMRI.' +
                            optName].setText(self.myConfig['FMRI'][optName])
                gridfunc.addWidget(self.inputs['FMRI.' + optName], x, 1)

                optName = 'task_%d_st' % y
                gridfunc.addWidget(QLabel(strings.pref_window_fmri_box_st), x, 2)
                self.inputs['FMRI.' + optName] = QComboBox(self)
                for index, label in enumerate(APPLABELS.SLICE_TIMING):
                    self.inputs['FMRI.' + optName].insertItem(index, label)

                self.inputs['FMRI.' + optName].setCurrentIndex(
                    self.myConfig.getint('FMRI', optName))

                gridfunc.addWidget(self.inputs['FMRI.' + optName], x, 3)
                x += 2

                dx_layout.addWidget(groupBoxfunc)

        groupBox3 = QGroupBox(strings.pref_window_tract_box_title)
        grid3 = QGridLayout()
        groupBox3.setLayout(grid3)
        x = 0

        for index, key in enumerate(self.myConfig.TRACTS):
            self.inputs['DEFAULTTRACTS.' + key] = QCheckBox()
            self.setCheckBox(
                self.inputs['DEFAULTTRACTS.' + key], self.myConfig.getboolean('DEFAULTTRACTS', key))
            grid3.addWidget(self.inputs['DEFAULTTRACTS.' + key], x, 0)
            label = QLabel(self.myConfig.TRACTS[key][0] + " reconstruction")
            label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
            grid3.addWidget(label, x, 1)
            x += 1

        sn_layout.addWidget(groupBox3)

        self.saveButton = QPushButton(strings.pref_window_save_button)
        self.saveButton.clicked.connect(self.savePreferences)
        sn_layout.addWidget(self.saveButton)

        discardButton = QPushButton("Discard changes")
        discardButton.clicked.connect(self.close)
        sn_layout.addWidget(discardButton)

        self.setLayout(layout)

    def choseDir(self, edit, message):
        folderPath = QFileDialog.getExistingDirectory(self, message)
        if not os.path.exists(folderPath):
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText(strings.pref_window_dir_error)
            msgBox.exec()
            return
        edit.setText(folderPath)
        self.setRestart()

    def choseFile(self, edit, message):
        filePath, filter = QFileDialog.getOpenFileName(self, message)
        if not os.path.exists(filePath):
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText(strings.pref_window_file_error)
            msgBox.exec()
            return
        edit.setText(filePath)
        self.setRestart()

    def setCheckBox(self, checkBox, bool):
        if bool:
            checkBox.setCheckState(Qt.Checked)
        else:
            checkBox.setCheckState(Qt.Unchecked)

    def setRestart(self):
        self.restart = True
        self.saveButton.setText(strings.pref_window_save_restart_button)

    def savePreferences(self):
        for index, key in enumerate(self.inputs):
            splitted = key.split(".")
            value = None
            if type(self.inputs[key]) is QLineEdit:
                value = self.inputs[key].text()
            elif type(self.inputs[key]) is QComboBox:
                value = str(self.inputs[key].currentIndex())
            elif type(self.inputs[key]) is QCheckBox:
                if self.inputs[key].checkState() == Qt.Checked:
                    value = 'true'
                else:
                    value = "false"

            if value != None:
                self.myConfig[splitted[0]][splitted[1]] = value

        self.myConfig.save()

        if self.restart:
            retcode = APPLABELS.EXIT_CODE_REBOOT
        else:
            retcode = 1

        self.done(retcode)
