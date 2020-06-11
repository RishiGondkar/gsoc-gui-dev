#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#    Copyright (C) 2020 by YOUR NAME HERE
#
#    This file is part of RoboComp
#
#    RoboComp is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    RoboComp is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with RoboComp.  If not, see <http://www.gnu.org/licenses/>.
#
from genericworker import *
from datetime import date, datetime
from google_calender import CalenderApi
from PySide2.QtCore import QDateTime
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import json
import sys
import math

try:
    from ui_activity_form import *
except:
    print("Can't import ui_activity_form UI file")

try:
    from ui_dailyActivity import *
except ImportError:
    print("Can't import ui_dailyActivity UI file")

try:
    from ui_viewLaser import *
except ImportError:
    print("Can't import ui_viewLaser UI file")

try:
    from ui_cameraViewer import *
except ImportError:
    print("Can't import ui_cameraViewer UI file")

# If RoboComp was compiled with Python bindings you can use InnerModel in Python
# sys.path.append('/opt/robocomp/lib')
# import librobocomp_qmat
# import librobocomp_osgviewer
# import librobocomp_innermodel


class OpenActivityForm(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.parent = parent
        self.ui = Ui_activityForm()
        self.ui.setupUi(self)
        self.setModal(True)
        self.ui.pushButton.clicked.connect(self.button_ok)
        self.ui.pushButton_2.clicked.connect(self.button_cancel)
        self.ui.comboBox_4.currentIndexChanged.connect(self.type_check)
        self.ui.comboBox_5.activated.connect(self.location_check)
        self.ui.textEdit_3.setText("Activity " + str(self.parent.ui.comboBox_3.count() + 1))
        self.ui.comboBox_6.addItems({"Stretcher", "Robot"})

    # save the data when ok button is pressed
    def button_ok(self):
        print("ok button")
        self.parent.ui.comboBox_3.addItem(self.ui.textEdit_3.toPlainText())
        start = str(self.parent.ui.dateEdit.date().toPython()) + "T" + str(self.ui.timeEdit.time().toPython()) + "Z"
        end = str(self.parent.ui.dateEdit.date().toPython()) + "T" + str(self.ui.timeEdit_2.time().toPython()) + "Z"
        description_data = {"Type": self.ui.comboBox_4.currentText(),
                            "IndividualName": self.ui.textEdit.toPlainText(),
                            "TherapistName": self.ui.textEdit_2.toPlainText(),
                            "Location": self.ui.comboBox_5.currentText(),
                            "Element": self.ui.comboBox_6.currentText(),
                            "Notification": self.ui.checkBox.isChecked(),
                            }
        body_content = {"summary": self.ui.textEdit_3.toPlainText(),
                        "description": json.dumps(description_data),
                        "start": {"dateTime": start},
                        "end": {"dateTime": end},
                        }
        print(body_content)
        self.parent.calendarApiObj.createEvent(bodyContent=body_content)
        self.hide()

    # exit the form and discard all the data
    def button_cancel(self):
        self.hide()
        start = str(self.parent.ui.dateEdit.date().toPython()) + "T" + str(self.ui.timeEdit.time().toPython()) + "Z"
        end = str(self.parent.ui.dateEdit.date().toPython()) + "T" + str(self.ui.timeEdit_2.time().toPython()) + "Z"
        body = {"summary": self.ui.textEdit_3.toPlainText(),
                "description": {"Type": self.ui.comboBox_4.currentText(),
                                "IndividualName": self.ui.textEdit.toPlainText(),
                                "TherapistName": self.ui.textEdit_2.toPlainText(),
                                "Location": self.ui.comboBox_5.currentText(),
                                "Element": self.ui.comboBox_6.currentText(),
                                "Notification": self.ui.checkBox.isChecked(),
                                },
                "start": {"dateTime": start},
                "end": {"dateTime": end},
                }
        print(body)

    # check the type of the activity
    def type_check(self, index):
        if self.ui.comboBox_4.itemText(index) == "Individual":
            self.ui.label_9.show()
            self.ui.textEdit.show()
        else:
            self.ui.label_9.hide()
            self.ui.textEdit.hide()

    # check the location
    def location_check(self, index):
        if self.ui.comboBox_5.itemText(index) == "Physical therapy room":
            self.ui.comboBox_6.clear()
            self.ui.comboBox_6.addItems({"Stretcher", "Robot"})
        else:
            self.ui.comboBox_6.clear()
            self.ui.comboBox_6.addItems({"Table", "Robot", "TV"})


class DailyActivity(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.parent = parent
        self.ui = Ui_DailyActivity()
        self.ui.setupUi(self)
        self.setModal(True)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

    def closeEvent(self, arg__1):
        self.parent.ui.label.setText(" ")


class ViewLaser(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        self.parentObj = parent
        self.ui = Ui_LaserViewer()
        self.ui.setupUi(self)
        self.ui.doubleSpinBox.valueChanged.connect(self.repaint)
        self.ui.horizontalSlider.valueChanged.connect(self.updatePeriod)
        self.count = 0

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.updateValues)
        self.Period = 200
        self.laser_data, laser_dumy = [],[]
        self.timer.start(200)
        self.ui.horizontalSlider.setValue(5)

    def updatePeriod(self):
        period = int(self.ui.label_3.text())
        self.timer.setInterval(1000//period)

    def updateValues(self):
        self.update()

    def paintEvent(self, event=None):
        try:
            self.laser_data, laser_angle = self.parentObj.laser_proxy.getLaserAndBStateData()
        except:
            print("No laser is connected")
            print("exiting")
            self.close()

        xOff = self.width() / 2.
        yOff = self.height() / 2.
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)

        for point in self.laser_data:
            newCoor = self.measure2coord(point)
            painter.drawRect(newCoor[0] - 1, newCoor[1] - 1, 2, 2)

        for wm in range(10):
            w = 1000. * (1. + wm) * self.ui.doubleSpinBox.value()
            painter.drawEllipse(QRectF(0.5 * self.width() - w / 2., 0.5 * self.height() - w / 2., w, w))
        for wm in range(5):
            w = 200. * (1. + wm) * self.ui.doubleSpinBox.value()
            painter.drawEllipse(QRectF(0.5 * self.width() - w / 2., 0.5 * self.height() - w / 2., w, w))

        painter.end()
        painter = None

    def measure2coord(self, measure):
        const_mul = self.ui.doubleSpinBox.value()
        x = math.cos(measure.angle - 0.5 * math.pi) * measure.dist * const_mul + (0.5 * self.width())
        y = math.sin(measure.angle - 0.5 * math.pi) * measure.dist * const_mul + (0.5 * self.height())
        return x, y


class CameraViewer(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        self.parent = parent
        self.ui = Ui_CamViewer()
        self.ui.setupUi(self)

        # timer init
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.repaint)
        self.timer.start(30)

        # variable init
        self.color, self.depth, self.headState, self.baseState = None,None,None,None

    def paintEvent(self, event=None):
        try:
            self.color, self.depth, self.headState, self.baseState = self.parent.rgbd_proxy.getData()
            if (len(self.color) == 3 * 640 * 480):
                color_image_width = 640
                color_image_height = 480
            elif (len(self.color) == 3 * 320 * 240):
                color_image_width = 320
                color_image_height = 240
            else:
                print('Undetermined Color image size in getRGB: we shall not paint! %d' % (len(self.color)))
                return

            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing, True)

            if color_image_width != 0 and color_image_height != 0:
                image = QImage(self.color, color_image_width, color_image_height, QImage.Format_RGB888)
                painter.drawImage(QPointF(self.ui.frame.x(), self.ui.frame.y()), image)
            painter.end()
            painter = None
        except:
            print("No Camera is connected")
            print("exiting")
            self.close()

class SpecificWorker(GenericWorker):
    def __init__(self, proxy_map):
        super(SpecificWorker, self).__init__(proxy_map)
        # calling the calendar api object
        self.calendarApiObj = CalenderApi()

        self.timer.timeout.connect(self.compute)
        self.Period = 2000
        self.timer.start(self.Period)
        self.ui.pushButton_10.clicked.connect(self.newActivity)
        self.ui.pushButton_14.clicked.connect(self.viewAgenda)

        # setting the date to today
        self.ui.dateEdit.setDateTime(QDateTime.currentDateTimeUtc())

        # init functions for robot navigation and control part #
        self.ui.pushButton_8.clicked.connect(self.gotoPoint)
        self.ui.pushButton_9.clicked.connect(self.keyboardControl)
        self.ui.pushButton_4.clicked.connect(self.stopRobotB)
        self.ui.pushButton_5.clicked.connect(self.resetRobotB)

        # init control buttons
        self.ui.left_button.clicked.connect(self.moveLeft)
        self.ui.right_button.clicked.connect(self.moveRight)
        self.ui.up_button.clicked.connect(self.moveForward)
        self.ui.down_button.clicked.connect(self.moveBackward)
        self.ui.stop_button.clicked.connect(self.stopRobotB)
        self.ui.cc_button.clicked.connect(self.rotCounterClockwise)
        self.ui.c_button.clicked.connect(self.rotClockwise)

        # limits
        self.translationSpeedLimit = 2000
        self.rotationSpeedLimit = 2

        # robot velocities variables
        self.velX = 0
        self.velZ = 0
        self.velRot = 0

        # Agm related initialization
        # self.WorldModel = AGMModel()

        # view Laser method
        self.ui.viewLaser_button.clicked.connect(self.viewLaserB)
        self.laser_data, laser_dummy = [], []
        # view Camera method
        self.ui.view_camera_button.clicked.connect(self.viewCameraB)

    def __del__(self):
        print('SpecificWorker destructor')

    def setParams(self, params):
        # try:
        #	self.innermodel = InnerModel(params["InnerModelPath"])
        # except:
        #	traceback.print_exc()
        #	print("Error reading config params")
        return True

    @QtCore.Slot()
    def compute(self):
        # w = World()
        # w = self.agmexecutive_proxy.getModel()
        # print('SpecificWorker.compute...')
        # computeCODE
        # try:
        #     self.laser_data, laser_dummy = self.laser_proxy.getLaserAndBStateData()
        #     self.viewLaser.update()
        # except Ice.Exception as e:
        #     print(e)

        # The API of python-innermodel is not exactly the same as the C++ version
        # self.innermodel.updateTransformValues('head_rot_tilt_pose', 0, 0, 0, 1.3, 0, 0)
        # z = librobocomp_qmat.QVec(3,0)
        # r = self.innermodel.transform('rgbd', z, 'laser')
        # r.printvector('d')
        # print(r[0], r[1], r[2])

        return True

    #
    # SUBSCRIPTION to edgeUpdated method from AGMExecutiveTopic interface
    #
    def AGMExecutiveTopic_edgeUpdated(self, modification):
        #
        # subscribesToCODE
        #
        pass

    #
    # SUBSCRIPTION to edgesUpdated method from AGMExecutiveTopic interface
    #
    def AGMExecutiveTopic_edgesUpdated(self, modifications):
        #
        # subscribesToCODE
        #
        pass

    #
    # SUBSCRIPTION to selfEdgeAdded method from AGMExecutiveTopic interface
    #
    def AGMExecutiveTopic_selfEdgeAdded(self, nodeid, edgeType, attributes):
        #
        # subscribesToCODE
        #
        pass

    #
    # SUBSCRIPTION to selfEdgeDeleted method from AGMExecutiveTopic interface
    #
    def AGMExecutiveTopic_selfEdgeDeleted(self, nodeid, edgeType):
        #
        # subscribesToCODE
        #
        pass

    #
    # SUBSCRIPTION to structuralChange method from AGMExecutiveTopic interface
    #
    def AGMExecutiveTopic_structuralChange(self, w):
        #
        # subscribesToCODE
        #
        pass

    #
    # SUBSCRIPTION to symbolUpdated method from AGMExecutiveTopic interface
    #
    def AGMExecutiveTopic_symbolUpdated(self, modification):
        #
        # subscribesToCODE
        #
        pass

    #
    # SUBSCRIPTION to symbolsUpdated method from AGMExecutiveTopic interface
    #
    def AGMExecutiveTopic_symbolsUpdated(self, modifications):
        #
        # subscribesToCODE
        #
        pass

    # =============== Methods for Component Implements ==================
    # ===================================================================

    #
    # activateAgent
    #
    def AGMCommonBehavior_activateAgent(self, prs):
        ret = bool()
        #
        # implementCODE
        #
        return ret

    #
    # deactivateAgent
    #
    def AGMCommonBehavior_deactivateAgent(self):
        ret = bool()
        #
        # implementCODE
        #
        return ret

    #
    # getAgentParameters
    #
    def AGMCommonBehavior_getAgentParameters(self):
        ret = ParameterMap()
        #
        # implementCODE
        #
        return ret

    #
    # getAgentState
    #
    def AGMCommonBehavior_getAgentState(self):
        ret = StateStruct()
        #
        # implementCODE
        #
        return ret

    #
    # killAgent
    #
    def AGMCommonBehavior_killAgent(self):
        #
        # implementCODE
        #
        pass

    #
    # reloadConfigAgent
    #
    def AGMCommonBehavior_reloadConfigAgent(self):
        ret = bool()
        #
        # implementCODE
        #
        return ret

    #
    # setAgentParameters
    #
    def AGMCommonBehavior_setAgentParameters(self, prs):
        ret = bool()
        #
        # implementCODE
        #
        return ret

    #
    # uptimeAgent
    #
    def AGMCommonBehavior_uptimeAgent(self):
        ret = int()
        #
        # implementCODE
        #
        return ret

    # ===================================================================
    # ===================================================================

    # ======functions for ui=============
    def newActivity(self):
        print("button Clicked2")
        self.activityForm = OpenActivityForm(self)
        self.activityForm.show()

    def viewAgenda(self):
        print("view Agenda clicked")
        self.ui.label.show()
        self.ui.label.setText("Loading...")
        self.dailyActivity = DailyActivity(self)
        self.dailyActivity.ui.tableWidget.clearContents()
        self.dailyActivity.ui.tableWidget.setRowCount(1)
        self.fetchEvents()
        self.dailyActivity.show()

    def fetchEvents(self):
        self.ui.comboBox_3.clear()
        date_req = self.ui.dateEdit.date().toPython()
        eventList = self.calendarApiObj.getEvents(date_req)
        for event in eventList:
            try:
                type_string, IndividualName_string, TherapistName_string, Location_string, Element_string, Notification_string = '', '', '', '', '', ''
                # print(event)
                summary_string = str(event.get('summary', 'NoTitle'))
                # show only time not the date part of the string
                start_time = event.get('start', {})
                end_time = event.get('end', {})

                description_data = json.loads(event.get('description', '{}'))
                try:
                    type_string = description_data.get('Type', "Not Specified")
                    IndividualName_string = description_data.get('IndividualName', "Not Specified")
                    TherapistName_string = description_data.get('TherapistName', "Not Specified")
                    Location_string = description_data.get('Location', "Not Specified")
                    Element_string = description_data.get('Element', "Not Specified")
                    Notification_string = description_data.get('Notification', "Not Specified")
                    if Notification_string:
                        Notification_string = "True"
                    elif not Notification_string:
                        Notification_string = "False"
                except:
                    print("Unable to parse description")

                # if time is not specified meant the event is for full day
                start_string = start_time.get("dateTime", "           Full Day")[11:]
                end_string = end_time.get("dateTime", "           Full Day")[11:]

                # print(jsonObj["Type"], jsonObj["Type"], jsonObj["Type"])
                self.ui.comboBox_3.addItem(summary_string)
                rowNumber = self.dailyActivity.ui.tableWidget.rowCount()
                self.dailyActivity.ui.tableWidget.setItem(rowNumber - 1, 0, QTableWidgetItem(summary_string))
                self.dailyActivity.ui.tableWidget.setItem(rowNumber - 1, 1, QTableWidgetItem(start_string))
                self.dailyActivity.ui.tableWidget.setItem(rowNumber - 1, 2, QTableWidgetItem(end_string))
                self.dailyActivity.ui.tableWidget.setItem(rowNumber - 1, 3, QTableWidgetItem(type_string))
                self.dailyActivity.ui.tableWidget.setItem(rowNumber - 1, 4, QTableWidgetItem(IndividualName_string))
                self.dailyActivity.ui.tableWidget.setItem(rowNumber - 1, 5, QTableWidgetItem(TherapistName_string))
                self.dailyActivity.ui.tableWidget.setItem(rowNumber - 1, 6, QTableWidgetItem(Location_string))
                self.dailyActivity.ui.tableWidget.setItem(rowNumber - 1, 7, QTableWidgetItem(Element_string))
                self.dailyActivity.ui.tableWidget.setItem(rowNumber - 1, 8, QTableWidgetItem(Notification_string))
                self.dailyActivity.ui.tableWidget.setRowCount(rowNumber + 1)

            except:
                print("unable to parse the event")
                print("Unexpected error:", sys.exc_info()[0])

    def gotoPoint(self):
        robotPose = Pose3D()
        robotPose.x = float(self.ui.lineEdit.text())
        robotPose.y = 0
        robotPose.z = float(self.ui.lineEdit_2.text())
        robotPose.rx = 0
        robotPose.ry = float(self.ui.lineEdit_3.text())
        robotPose.rz = 0
        self.innermodelmanager_proxy.setPoseFromParent("robot", robotPose)
        print("goto")
        # print(float(self.ui.lineEdit.text())+2)

    def keyboardControl(self):
        if self.ui.pushButton_9.text() == 'Keyboard Control Off':
            self.ui.pushButton_9.setStyleSheet(u"background-color: rgb(41, 239, 41);")
            self.ui.pushButton_9.setText('Keyboard Control On')
            print("Keyboard Control On")
        else:
            self.ui.pushButton_9.setStyleSheet(u"background-color: rgb(239, 41, 41);")
            self.ui.pushButton_9.setText('Keyboard Control Off')
            print("Keyboard Control Off")

    # function for robot movement
    def moveForward(self):
        if self.velZ > self.translationSpeedLimit:
            self.velZ = self.velZ
        else:
            self.velZ += 20
        try:
            self.omnirobot_proxy.setSpeedBase(self.velX, self.velZ, self.velRot)
        except:
            print("no robot found")

    def moveBackward(self):
        if self.velZ < -1 * self.translationSpeedLimit:
            self.velZ = self.velZ
        else:
            self.velZ -= 20
        try:
            self.omnirobot_proxy.setSpeedBase(self.velX, self.velZ, self.velRot)
        except:
            print("no robot found")

    def moveLeft(self):
        if self.velX < -1 * self.translationSpeedLimit:
            self.velX = self.velX
        else:
            self.velX -= 20
        try:
            self.omnirobot_proxy.setSpeedBase(self.velX, self.velZ, self.velRot)
        except:
            print("no robot found")

    def moveRight(self):
        if self.velX > self.translationSpeedLimit:
            self.velX = self.velX
        else:
            self.velX += 20
        try:
            self.omnirobot_proxy.setSpeedBase(self.velX, self.velZ, self.velRot)
        except:
            print("no robot found")

    def rotCounterClockwise(self):
        if self.velRot < -1 * self.rotationSpeedLimit:
            self.velRot = self.velRot
        else:
            self.velRot -= 0.1
        try:
            self.omnirobot_proxy.setSpeedBase(self.velX, self.velZ, self.velRot)
        except:
            print("no robot found")

    def rotClockwise(self):
        if self.velRot > self.rotationSpeedLimit:
            self.velRot = self.velRot
        else:
            self.velRot += 0.1
        try:
            self.omnirobot_proxy.setSpeedBase(self.velX, self.velZ, self.velRot)
        except:
            print("no robot found")

    def stopRobot(self):
        self.velX = 0
        self.velZ = 0
        self.velRot = 0
        try:
            self.omnirobot_proxy.setSpeedBase(self.velX, self.velZ, self.velRot)
        except:
            print("no robot found")

    # overriding keyPressEvent from QWidget
    def keyPressEvent(self, event):
        if self.ui.pushButton_9.text() == 'Keyboard Control On':
            if event.key() == QtCore.Qt.Key_W:
                self.moveForward()
                print("w button")
            elif event.key() == QtCore.Qt.Key_S:
                self.moveBackward()
                print("s button")
            elif event.key() == QtCore.Qt.Key_A:
                self.moveLeft()
                print("a button")
            elif event.key() == QtCore.Qt.Key_D:
                self.moveRight()
                print("d button")
            elif event.key() == QtCore.Qt.Key_F:
                self.rotCounterClockwise()
                print("left button")
            elif event.key() == QtCore.Qt.Key_G:
                self.rotClockwise()
                print("right button")
            elif event.key() == QtCore.Qt.Key_Backspace:
                self.stopRobot()
                print("stop button")

    # method to stop the robot
    def stopRobotB(self):
        print("stop button")
        self.velX = 0
        self.velZ = 0
        self.velRot = 0
        try:
            self.omnirobot_proxy.setSpeedBase(self.velX, self.velZ, self.velRot)
        except:
            print("no robot found")

    # method to reset the position of the robot
    def resetRobotB(self):
        print("reset button")
        robotPose = Pose3D()
        robotPose.x = 0
        robotPose.y = 0
        robotPose.z = 0
        robotPose.rx = 0
        robotPose.ry = 0
        robotPose.rz = 0
        self.innermodelmanager_proxy.setPoseFromParent("robot", robotPose)

    def viewCameraB(self):
        self.viewCamera = CameraViewer(parent=self)
        self.viewCamera.show()

    def viewLaserB(self):
        self.viewLaser = ViewLaser(parent=self)
        self.viewLaser.show()
        # print(self.laser_data)