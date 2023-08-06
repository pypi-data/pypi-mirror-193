"""MainWindow of Beamline console.

Based on P22 EC by sebastian.piec@desy.de and yury.matveev@desy.de
"""

import logging
import os
import sys

import psutil

from PyQt5 import QtWidgets, QtCore

from beamline_console.constants import APP_NAME, LOG_FORMATTER

from beamline_console.snapshot.snapshotwidget import SnapshotWidget
from beamline_console.devicecontrol.beamlinewidget import BeamlineWidget
from beamline_console.beamlinehal import BeamlineHAL
from beamline_console.logger.loggingwidget import LoggingWidget
from beamline_console.logger.guilogger import GuiLogger
from beamline_console.utils.aboutdialog import AboutDialog
from beamline_console.utils.errordialog import ErrormsgLogger
from beamline_console.utils.settings import Settings
from beamline_console.utils.input_dialog import InputDialog

from beamline_console.gui.MainWindow_ui import Ui_MainWindow

logger = logging.getLogger(APP_NAME)

# ----------------------------------------------------------------------
class ExperimentalControl(QtWidgets.QMainWindow):
    """
    """
    windowClosed = QtCore.pyqtSignal()

    # ----------------------------------------------------------------------
    def __init__(self, options):
        """
        """
        super().__init__()

        self._childWindows = []
        self._dockList = []

        self._options = options

        # avoid running multiple instances of the app
        # self._lockFileName = "{}.lock".format(str(options.beamlineID).lower())
        # assertUniqueInstance(self._lockFileName, self)

        # process main settings
        main_folder = os.path.join(os.path.expanduser('~'), '.beamline_console')

        self.settings = Settings(os.path.join(main_folder, "main.cfg"))

        errh = ErrormsgLogger()
        errh.setFormatter(LOG_FORMATTER)
        logger.addHandler(errh)

        self._gui_logger = GuiLogger()
        self._gui_logger.setFormatter(LOG_FORMATTER)
        logger.addHandler(self._gui_logger)

        self.beamline_hal = BeamlineHAL(self, options.user)

        # GUI
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        menu_bar = self.menuBar()

        self.action_user = QtWidgets.QAction('Enable superuser', self)
        self.action_user.triggered.connect(self.switch_user)
        menu_bar.addAction(self.action_user)

        self.menu_view = QtWidgets.QMenu('View')
        menu_bar.addMenu(self.menu_view)

        action_about = QtWidgets.QAction('About', self)
        action_about.triggered.connect(self._show_about)
        menu_bar.addAction(action_about)

        action_quit = QtWidgets.QAction('Quit', self)
        action_quit.triggered.connect(self.exit_program)
        menu_bar.addAction(action_quit)

        self.setCentralWidget(None)

        self.setDockOptions(QtWidgets.QMainWindow.AnimatedDocks |
                            QtWidgets.QMainWindow.AllowNestedDocks |
                            QtWidgets.QMainWindow.AllowTabbedDocks)

        self._beamline_widget, self._beamline_dock = \
            self._add_dock(BeamlineWidget, "Beamline Control", QtCore.Qt.LeftDockWidgetArea, self)

        self._snapshot_widget, self._snapshot_dock = \
            self._add_dock(SnapshotWidget, "Beamline Snapshots", QtCore.Qt.LeftDockWidgetArea, self)

        self._logging_widget, self._logging_dock = \
            self._add_dock(LoggingWidget, "Logs", QtCore.Qt.RightDockWidgetArea, self)

        # Cross-connection signals

        self._gui_logger.emit_record.connect(self._logging_widget.get_record)

        self._beamline_widget.save_snapshot.connect(self._snapshot_widget.save_snapshot)
        self._beamline_widget.device_selected.connect(self._snapshot_widget.device_selected)

        self._snapshot_widget.motors_moved.connect(self._beamline_widget.sync_control_widget)

        dev_list = list(self.beamline_hal.device_map.keys())
        if len(dev_list) == 1:
            self._snapshot_widget.device_selected(dev_list)

        self._load_ui_settings()

        self._refresh_status_timer = QtCore.QTimer(self)
        self._refresh_status_timer.timeout.connect(self._refresh_status_bar)
        self._refresh_status_timer.start(1000)

        self._init_status_bar()

        logger.info("Beamline console successfully initialized")

    # ----------------------------------------------------------------------
    def _add_dock(self, WidgetClass, label, location, *args, **kwargs):
        """
        """
        widget = WidgetClass(*args, **kwargs)
    
        dock = QtWidgets.QDockWidget(label)
        dock.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        dock.setFocusPolicy(QtCore.Qt.StrongFocus)
        dock._currentWindow = '0'
        dock.setObjectName("{}Dock".format("".join(label.split())))
        dock.setWidget(widget)

        self.addDockWidget(location, dock)
        self._dockList.append(dock)
        self.menu_view.addAction(dock.toggleViewAction())

        return widget, dock

    # ----------------------------------------------------------------------
    def _stop_beamline(self):
        """
        """
        self.beamline_hal.stop_all()
        self.beamline_hal.safe_close()
     
    # ----------------------------------------------------------------------  
    def _save_ui_settings(self):
        """Save GUI state using QT settings mechanism.
        """
        settings = QtCore.QSettings(APP_NAME)
  
        self._beamline_widget.save_ui_settings(settings)
        self._snapshot_widget.save_ui_settings(settings)
        self._logging_widget.save_ui_settings(settings)

        settings.setValue("mainWindow/state", self.saveState())
        settings.setValue("mainWindow/geometry", self.saveGeometry())

    # ----------------------------------------------------------------------
    def _load_ui_settings(self):
        """Load GUI state using QT settings system.
        """
        settings = QtCore.QSettings(APP_NAME)

        try:
            self.restoreGeometry(settings.value("mainWindow/geometry"))
            self.restoreState(settings.value("mainWindow/state"))
        except:
            pass

        self._beamline_widget.load_ui_settings(settings)
        self._snapshot_widget.load_ui_settings(settings)
        self._logging_widget.load_ui_settings(settings)

    # ----------------------------------------------------------------------
    def _init_status_bar(self):

        # move progressbar TODO
        self.pb_movement = QtWidgets.QProgressBar()
        self.pb_movement.setMaximumSize(2000, 25)

        # display info on the status bar
        lb_process_id = QtWidgets.QLabel(f"pid {os.getpid()} |")
        lb_process_id.setStyleSheet("QLabel {color: #000066;}")
    
        # resources usage info
        process = psutil.Process(os.getpid())
        mem = float(process.memory_info().rss) / (1024. * 1024.)
        cpu = process.cpu_percent()

        self._lb_resources_status = QtWidgets.QLabel(f"| {mem:.2f}MB | CPU {cpu} %")

        self.statusBar().addPermanentWidget(QtWidgets.QLabel("Movement status: "))
        self.statusBar().addPermanentWidget(self.pb_movement)
        self.statusBar().addPermanentWidget(lb_process_id)
        self.statusBar().addPermanentWidget(self._lb_resources_status)

    # ----------------------------------------------------------------------
    def switch_user(self):
        """
        """
        try:
            if self.beamline_hal.access_level != 'superuser':
                if InputDialog(mode="pin", super_user_password=int(self.settings.option("general", "superuser_pin")),
                               max_attempts=int(self.settings.option("general", "max_attempts"))).exec():
                    self.beamline_hal.access_level_changed('superuser')
                    self._beamline_widget.access_level_changed('superuser')
                    self._snapshot_widget.access_level_changed('superuser')
                    self.action_user.setText('Disable superuser')
            else:
                self.beamline_hal.access_level_changed('user')
                self._beamline_widget.access_level_changed('superuser')
                self._snapshot_widget.access_level_changed('superuser')
                self.action_user.setText('Enable superuser')

        except Exception as err:
            logger.error(f"Authorization Failed: {repr(err)}", exc_info=sys.exc_info())

    # ----------------------------------------------------------------------
    def _refresh_status_bar(self):
        """
        """
        process = psutil.Process(os.getpid())
        mem = float(process.memory_info().rss) / (1024. * 1024.)
        cpu = psutil.cpu_percent()      # of the whole system?

        self._lb_resources_status.setText(f" {mem:.2f}MB | CPU {cpu} %")

        self.pb_movement.setValue(self.beamline_hal.progress())

    # ----------------------------------------------------------------------
    def _show_about(self):
        """
        """
        AboutDialog(self).show()
    
    # ---------------------------------------------------------------------- 
    def closeEvent(self, event):
        """Process "close event" (e.g. emitted when window's cross is clicked).
        """
        if self._clean_exit():
            event.accept()  
        else:  
            event.ignore()  

    # ----------------------------------------------------------------------
    def exit_program(self):
        """Called when Quit action is triggered.
        """
        if self._clean_exit():
            QtWidgets.qApp.quit()

    # ----------------------------------------------------------------------
    def _clean_exit(self):
        """
        """ 
        if self._really_quit():
            self._refresh_status_timer.stop()
            self._stop_beamline()
            # unlockAppInstance(self._lockFileName)
            self._save_ui_settings()
            QtWidgets.qApp.clipboard().clear()
            return True

        return False

    # ----------------------------------------------------------------------  
    @staticmethod
    def _really_quit():
        """Make sure that the user wants to quit this program.
        """
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("Quit")
        msg_box.setText(f"Do you want to exit beamline console?")
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        return msg_box.exec_() == QtWidgets.QMessageBox.Yes
