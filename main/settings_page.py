# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_settings(object):
    def setupUi(self, settings):
        settings.setObjectName("settings")
        settings.resize(1920, 1080)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        settings.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(settings)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(settings)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setStyleSheet("")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.to_program_config = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.to_program_config.sizePolicy().hasHeightForWidth())
        self.to_program_config.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.to_program_config.setFont(font)
        self.to_program_config.setObjectName("to_program_config")
        self.verticalLayout_3.addWidget(self.to_program_config)
        self.to_daily_config = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.to_daily_config.sizePolicy().hasHeightForWidth())
        self.to_daily_config.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(15)
        self.to_daily_config.setFont(font)
        self.to_daily_config.setObjectName("to_daily_config")
        self.verticalLayout_3.addWidget(self.to_daily_config)
        self.to_lessons = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.to_lessons.sizePolicy().hasHeightForWidth())
        self.to_lessons.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(22)
        self.to_lessons.setFont(font)
        self.to_lessons.setObjectName("to_lessons")
        self.verticalLayout_3.addWidget(self.to_lessons)
        self.to_time = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.to_time.sizePolicy().hasHeightForWidth())
        self.to_time.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.to_time.setFont(font)
        self.to_time.setObjectName("to_time")
        self.verticalLayout_3.addWidget(self.to_time)
        self.to_resetting = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.to_resetting.sizePolicy().hasHeightForWidth())
        self.to_resetting.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.to_resetting.setFont(font)
        self.to_resetting.setObjectName("to_resetting")
        self.verticalLayout_3.addWidget(self.to_resetting)
        self.gridLayout.addWidget(self.widget_3, 1, 0, 1, 1)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setStyleSheet("")
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(5)
        self.tabWidget.setFont(font)
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setObjectName("tabWidget")
        self.set_program_config = QtWidgets.QWidget()
        self.set_program_config.setObjectName("set_program_config")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.set_program_config)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.program_config_scrollarea = QtWidgets.QScrollArea(self.set_program_config)
        self.program_config_scrollarea.setWidgetResizable(True)
        self.program_config_scrollarea.setObjectName("program_config_scrollarea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 98, 44))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.program_config_show_area = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.program_config_show_area.setObjectName("program_config_show_area")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.program_config_show_area)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_7.addWidget(self.program_config_show_area)
        self.program_config_scrollarea.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_2.addWidget(self.program_config_scrollarea)
        self.tabWidget.addTab(self.set_program_config, "")
        self.set_daily_config = QtWidgets.QWidget()
        self.set_daily_config.setObjectName("set_daily_config")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.set_daily_config)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.daily_config_tab_widget = QtWidgets.QTabWidget(self.set_daily_config)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.daily_config_tab_widget.setFont(font)
        self.daily_config_tab_widget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.daily_config_tab_widget.setMovable(True)
        self.daily_config_tab_widget.setObjectName("daily_config_tab_widget")
        self.tab_lessons_edit = QtWidgets.QWidget()
        self.tab_lessons_edit.setObjectName("tab_lessons_edit")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_lessons_edit)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.widget_6 = QtWidgets.QWidget(self.tab_lessons_edit)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.add_dailyconfig_lessons = QtWidgets.QPushButton(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_dailyconfig_lessons.sizePolicy().hasHeightForWidth())
        self.add_dailyconfig_lessons.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(17)
        self.add_dailyconfig_lessons.setFont(font)
        self.add_dailyconfig_lessons.setObjectName("add_dailyconfig_lessons")
        self.horizontalLayout_4.addWidget(self.add_dailyconfig_lessons)
        self.sort_by_time = QtWidgets.QPushButton(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sort_by_time.sizePolicy().hasHeightForWidth())
        self.sort_by_time.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.sort_by_time.setFont(font)
        self.sort_by_time.setObjectName("sort_by_time")
        self.horizontalLayout_4.addWidget(self.sort_by_time)
        self.verticalLayout_8.addWidget(self.widget_6)
        self.daily_config_tableWidget = QtWidgets.QTableWidget(self.tab_lessons_edit)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.daily_config_tableWidget.setFont(font)
        self.daily_config_tableWidget.setObjectName("daily_config_tableWidget")
        self.daily_config_tableWidget.setColumnCount(4)
        self.daily_config_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.daily_config_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.daily_config_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.daily_config_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.daily_config_tableWidget.setHorizontalHeaderItem(3, item)
        self.daily_config_tableWidget.horizontalHeader().setStretchLastSection(False)
        self.verticalLayout_8.addWidget(self.daily_config_tableWidget)
        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 10)
        self.daily_config_tab_widget.addTab(self.tab_lessons_edit, "")
        self.horizontalLayout_3.addWidget(self.daily_config_tab_widget)
        self.tabWidget.addTab(self.set_daily_config, "")
        self.set_lessons = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(9)
        self.set_lessons.setFont(font)
        self.set_lessons.setObjectName("set_lessons")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.set_lessons)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.set_lessons_tabWidget = QtWidgets.QTabWidget(self.set_lessons)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.set_lessons_tabWidget.setFont(font)
        self.set_lessons_tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.set_lessons_tabWidget.setObjectName("set_lessons_tabWidget")
        self.lessons_monday = QtWidgets.QWidget()
        self.lessons_monday.setObjectName("lessons_monday")
        self.set_lessons_tabWidget.addTab(self.lessons_monday, "")
        self.lessons_tuesday = QtWidgets.QWidget()
        self.lessons_tuesday.setObjectName("lessons_tuesday")
        self.set_lessons_tabWidget.addTab(self.lessons_tuesday, "")
        self.lessons_wednesday = QtWidgets.QWidget()
        self.lessons_wednesday.setObjectName("lessons_wednesday")
        self.set_lessons_tabWidget.addTab(self.lessons_wednesday, "")
        self.lessons_thursday = QtWidgets.QWidget()
        self.lessons_thursday.setObjectName("lessons_thursday")
        self.set_lessons_tabWidget.addTab(self.lessons_thursday, "")
        self.lessons_friday = QtWidgets.QWidget()
        self.lessons_friday.setObjectName("lessons_friday")
        self.set_lessons_tabWidget.addTab(self.lessons_friday, "")
        self.lessons_saturday = QtWidgets.QWidget()
        self.lessons_saturday.setObjectName("lessons_saturday")
        self.set_lessons_tabWidget.addTab(self.lessons_saturday, "")
        self.lessons_sunday = QtWidgets.QWidget()
        self.lessons_sunday.setObjectName("lessons_sunday")
        self.set_lessons_tabWidget.addTab(self.lessons_sunday, "")
        self.lessons_special = QtWidgets.QWidget()
        self.lessons_special.setObjectName("lessons_special")
        self.set_lessons_tabWidget.addTab(self.lessons_special, "")
        self.lessons_with_homework = QtWidgets.QWidget()
        self.lessons_with_homework.setObjectName("lessons_with_homework")
        self.set_lessons_tabWidget.addTab(self.lessons_with_homework, "")
        self.horizontalLayout_5.addWidget(self.set_lessons_tabWidget)
        self.tabWidget.addTab(self.set_lessons, "")
        self.show_about = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.show_about.setFont(font)
        self.show_about.setObjectName("show_about")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.show_about)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtWidgets.QLabel(self.show_about)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.widget_5 = QtWidgets.QWidget(self.show_about)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(7)
        self.widget_5.setFont(font)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.now_version = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.now_version.setFont(font)
        self.now_version.setObjectName("now_version")
        self.verticalLayout_5.addWidget(self.now_version)
        self.label_3 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("a { color: #007aff; }")
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 1)
        self.verticalLayout_5.setStretch(2, 1)
        self.verticalLayout_6.addWidget(self.widget_5)
        self.verticalLayout_6.setStretch(0, 3)
        self.verticalLayout_6.setStretch(1, 8)
        self.tabWidget.addTab(self.show_about, "")
        self.set_time = QtWidgets.QWidget()
        self.set_time.setObjectName("set_time")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.set_time)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.set_time_tabWidget = QtWidgets.QTabWidget(self.set_time)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.set_time_tabWidget.setFont(font)
        self.set_time_tabWidget.setObjectName("set_time_tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.time_edit_tableWidget = QtWidgets.QTableWidget(self.tab)
        self.time_edit_tableWidget.setObjectName("time_edit_tableWidget")
        self.time_edit_tableWidget.setColumnCount(3)
        self.time_edit_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.time_edit_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.time_edit_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.time_edit_tableWidget.setHorizontalHeaderItem(2, item)
        self.horizontalLayout_7.addWidget(self.time_edit_tableWidget)
        self.widget_7 = QtWidgets.QWidget(self.tab)
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.time_edit_reorder = QtWidgets.QPushButton(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_edit_reorder.sizePolicy().hasHeightForWidth())
        self.time_edit_reorder.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.time_edit_reorder.setFont(font)
        self.time_edit_reorder.setObjectName("time_edit_reorder")
        self.verticalLayout_9.addWidget(self.time_edit_reorder)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem)
        self.verticalLayout_9.setStretch(0, 1)
        self.verticalLayout_9.setStretch(1, 3)
        self.horizontalLayout_7.addWidget(self.widget_7)
        self.horizontalLayout_7.setStretch(0, 7)
        self.set_time_tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.time_edit_tableWidget_special = QtWidgets.QTableWidget(self.tab_2)
        self.time_edit_tableWidget_special.setObjectName("time_edit_tableWidget_special")
        self.time_edit_tableWidget_special.setColumnCount(3)
        self.time_edit_tableWidget_special.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.time_edit_tableWidget_special.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.time_edit_tableWidget_special.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.time_edit_tableWidget_special.setHorizontalHeaderItem(2, item)
        self.horizontalLayout_8.addWidget(self.time_edit_tableWidget_special)
        self.widget_8 = QtWidgets.QWidget(self.tab_2)
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget_8)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.time_edit_reorder_special = QtWidgets.QPushButton(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_edit_reorder_special.sizePolicy().hasHeightForWidth())
        self.time_edit_reorder_special.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.time_edit_reorder_special.setFont(font)
        self.time_edit_reorder_special.setObjectName("time_edit_reorder_special")
        self.verticalLayout_10.addWidget(self.time_edit_reorder_special)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem1)
        self.verticalLayout_10.setStretch(0, 1)
        self.verticalLayout_10.setStretch(1, 3)
        self.horizontalLayout_8.addWidget(self.widget_8)
        self.horizontalLayout_8.setStretch(0, 7)
        self.set_time_tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout_6.addWidget(self.set_time_tabWidget)
        self.tabWidget.addTab(self.set_time, "")
        self.resetting = QtWidgets.QWidget()
        self.resetting.setObjectName("resetting")
        self.tabWidget.addTab(self.resetting, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.gridLayout.addWidget(self.widget_4, 1, 1, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.save_exit = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_exit.sizePolicy().hasHeightForWidth())
        self.save_exit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.save_exit.setFont(font)
        self.save_exit.setObjectName("save_exit")
        self.horizontalLayout.addWidget(self.save_exit)
        self.not_save_exit = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.not_save_exit.sizePolicy().hasHeightForWidth())
        self.not_save_exit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(17)
        self.not_save_exit.setFont(font)
        self.not_save_exit.setObjectName("not_save_exit")
        self.horizontalLayout.addWidget(self.not_save_exit)
        self.to_about = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.to_about.sizePolicy().hasHeightForWidth())
        self.to_about.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.to_about.setFont(font)
        self.to_about.setObjectName("to_about")
        self.horizontalLayout.addWidget(self.to_about)
        self.gridLayout.addWidget(self.widget_2, 0, 0, 1, 2)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 6)
        self.gridLayout.setRowStretch(0, 2)
        self.gridLayout.setRowStretch(1, 13)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(settings)
        self.tabWidget.setCurrentIndex(4)
        self.daily_config_tab_widget.setCurrentIndex(0)
        self.set_lessons_tabWidget.setCurrentIndex(0)
        self.set_time_tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(settings)

    def retranslateUi(self, settings):
        _translate = QtCore.QCoreApplication.translate
        settings.setWindowTitle(_translate("settings", "Form"))
        self.to_program_config.setText(_translate("settings", "程序基本设置"))
        self.to_daily_config.setText(_translate("settings", "今日配置文件更改"))
        self.to_lessons.setText(_translate("settings", "课表设置"))
        self.to_time.setText(_translate("settings", "课程时间设置"))
        self.to_resetting.setText(_translate("settings", "重置相关"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.set_program_config), _translate("settings", "Tab 1"))
        self.add_dailyconfig_lessons.setText(_translate("settings", "新建项于末尾"))
        self.sort_by_time.setText(_translate("settings", "按时间排序"))
        item = self.daily_config_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("settings", "名称"))
        item = self.daily_config_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("settings", "起始时间"))
        item = self.daily_config_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("settings", "终止时间"))
        item = self.daily_config_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("settings", "点击删除(不可撤销)"))
        self.daily_config_tab_widget.setTabText(self.daily_config_tab_widget.indexOf(self.tab_lessons_edit), _translate("settings", "课表"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.set_daily_config), _translate("settings", "页"))
        self.set_lessons_tabWidget.setTabText(self.set_lessons_tabWidget.indexOf(self.lessons_monday), _translate("settings", "周一"))
        self.set_lessons_tabWidget.setTabText(self.set_lessons_tabWidget.indexOf(self.lessons_tuesday), _translate("settings", "周二"))
        self.set_lessons_tabWidget.setTabText(self.set_lessons_tabWidget.indexOf(self.lessons_wednesday), _translate("settings", "周三"))
        self.set_lessons_tabWidget.setTabText(self.set_lessons_tabWidget.indexOf(self.lessons_thursday), _translate("settings", "周四"))
        self.set_lessons_tabWidget.setTabText(self.set_lessons_tabWidget.indexOf(self.lessons_friday), _translate("settings", "周五"))
        self.set_lessons_tabWidget.setTabText(self.set_lessons_tabWidget.indexOf(self.lessons_saturday), _translate("settings", "周六"))
        self.set_lessons_tabWidget.setTabText(self.set_lessons_tabWidget.indexOf(self.lessons_sunday), _translate("settings", "周日"))
        self.set_lessons_tabWidget.setTabText(self.set_lessons_tabWidget.indexOf(self.lessons_special), _translate("settings", "特殊"))
        self.set_lessons_tabWidget.setTabText(self.set_lessons_tabWidget.indexOf(self.lessons_with_homework), _translate("settings", "需生成作业"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.set_lessons), _translate("settings", "Tab 2"))
        self.label.setText(_translate("settings", "Simple Class Information Display"))
        self.now_version.setText(_translate("settings", "版本号:等待读取"))
        self.label_3.setText(_translate("settings", "项目链接: 在<a href=\"https://github.com/erduotong/Simple_Class_Information_Display/\"style=\"color: #007aff;\">Github</a>上查看/在<a href=\"https://gitee.com/erduotong/Simple_Class_Information_Display/\"style=\"color: #007aff;\">Gitee</a>上查看"))
        self.label_4.setText(_translate("settings", "制作:耳朵同"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.show_about), _translate("settings", "页"))
        item = self.time_edit_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("settings", "课程"))
        item = self.time_edit_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("settings", "开始时间"))
        item = self.time_edit_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("settings", "结束时间"))
        self.time_edit_reorder.setText(_translate("settings", "按时间重排序"))
        self.set_time_tabWidget.setTabText(self.set_time_tabWidget.indexOf(self.tab), _translate("settings", "常规课程(通用)"))
        item = self.time_edit_tableWidget_special.horizontalHeaderItem(0)
        item.setText(_translate("settings", "课程"))
        item = self.time_edit_tableWidget_special.horizontalHeaderItem(1)
        item.setText(_translate("settings", "开始时间"))
        item = self.time_edit_tableWidget_special.horizontalHeaderItem(2)
        item.setText(_translate("settings", "结束时间"))
        self.time_edit_reorder_special.setText(_translate("settings", "按时间重排序"))
        self.set_time_tabWidget.setTabText(self.set_time_tabWidget.indexOf(self.tab_2), _translate("settings", "特殊课程(对应单一课程)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.set_time), _translate("settings", "页"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.resetting), _translate("settings", "页"))
        self.save_exit.setText(_translate("settings", "保存并退出"))
        self.not_save_exit.setText(_translate("settings", "不保存并退出"))
        self.to_about.setText(_translate("settings", "关于"))
