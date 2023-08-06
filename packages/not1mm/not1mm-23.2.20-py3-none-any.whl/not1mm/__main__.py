#!/usr/bin/env python3
"""
NOT1MM Logger
"""
# pylint: disable=unused-import, c-extension-no-member

import logging
import os
import pkgutil
import re
import sqlite3
import sys
from datetime import datetime
from json import dumps, loads
from pathlib import Path
from shutil import copyfile
from xmlrpc.client import Error, ServerProxy

import psutil
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import QDir, Qt  # pylint: disable=no-name-in-module
from PyQt5.QtGui import QFontDatabase  # pylint: disable=no-name-in-module

try:
    from not1mm.lib.cat_interface import CAT
    from not1mm.lib.cwinterface import CW
    from not1mm.lib.ham_utility import *
    from not1mm.lib.lookup import QRZlookup
    from not1mm.lib.version import __version__

    # from not1mm.lib.settings import Settings
except ModuleNotFoundError:
    from lib.cat_interface import CAT
    from lib.cwinterface import CW
    from lib.ham_utility import *
    from lib.lookup import QRZlookup
    from lib.version import __version__

    # from lib.settings import Settings


loader = pkgutil.get_loader("not1mm")
WORKING_PATH = os.path.dirname(loader.get_filename())


if "XDG_DATA_HOME" in os.environ:
    DATA_PATH = os.environ.get("XDG_DATA_HOME")
else:
    DATA_PATH = str(Path.home() / ".local" / "share")
DATA_PATH += "/not1mm"
try:
    os.mkdir(DATA_PATH)
except FileExistsError:
    ...

if "XDG_CONFIG_HOME" in os.environ:
    CONFIG_PATH = os.environ.get("XDG_CONFIG_HOME")
else:
    CONFIG_PATH = str(Path.home() / ".config")
CONFIG_PATH += "/not1mm"
try:
    os.mkdir(CONFIG_PATH)
except FileExistsError:
    ...


class MainWindow(QtWidgets.QMainWindow):
    """
    The main window
    """

    pref_ref = {
        "useqrz": False,
        "lookupusername": "username",
        "lookuppassword": "password",
        "gridsquare": "AA11aa",
        "run_state": True,
        "dark_mode": False,
        "command_buttons": True,
        "cw_macros": True,
        "bands_modes": True,
    }
    pref = None
    current_op = ""
    current_mode = ""
    current_band = ""
    look_up = None
    run_state = False
    fkeys = {}

    def __init__(self, *args, **kwargs):
        logger.info("MainWindow: __init__")
        super().__init__(*args, **kwargs)
        data_path = WORKING_PATH + "/data/main.ui"
        uic.loadUi(data_path, self)
        self.readpreferences()
        self.next_field = self.other
        self.field4.hide()
        self.actionCW_Macros.triggered.connect(self.cw_macros_stateChanged)
        self.actionCommand_Buttons.triggered.connect(self.command_buttons_stateChange)
        self.actionMode_and_Bands.triggered.connect(self.show_band_mode_stateChange)
        self.actionDark_Mode.triggered.connect(self.dark_mode_stateChange)
        self.radioButton_run.clicked.connect(self.run_sp_buttons_clicked)
        self.radioButton_sp.clicked.connect(self.run_sp_buttons_clicked)
        self.score.setText("0")
        self.callsign.textEdited.connect(self.callsign_changed)
        self.sent.setText("59")
        self.receive.setText("59")
        icon_path = WORKING_PATH + "/data/"
        self.greendot = QtGui.QPixmap(icon_path + "greendot.png")
        self.reddot = QtGui.QPixmap(icon_path + "reddot.png")
        self.leftdot.setPixmap(self.greendot)
        self.rightdot.setPixmap(self.reddot)
        self.read_cw_macros()
        self.rig_control = CAT("rigctld", "localhost", 4532)
        self.F1.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.F1.customContextMenuRequested.connect(self.edit_F1)
        self.F1.clicked.connect(self.sendf1)
        self.F2.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.F2.customContextMenuRequested.connect(self.edit_F2)
        self.F2.clicked.connect(self.sendf2)
        self.F3.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.F3.customContextMenuRequested.connect(self.edit_F3)
        self.F3.clicked.connect(self.sendf3)
        self.F4.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.F4.customContextMenuRequested.connect(self.edit_F4)
        self.F4.clicked.connect(self.sendf4)
        self.F5.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.F5.customContextMenuRequested.connect(self.edit_F5)
        self.F5.clicked.connect(self.sendf5)
        self.F6.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.F6.customContextMenuRequested.connect(self.edit_F6)
        self.F6.clicked.connect(self.sendf6)
        self.F7.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.F7.customContextMenuRequested.connect(self.edit_F7)
        self.F7.clicked.connect(self.sendf7)
        self.F8.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.F8.customContextMenuRequested.connect(self.edit_F8)
        self.F8.clicked.connect(self.sendf8)
        self.F9.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.F9.customContextMenuRequested.connect(self.edit_F9)
        self.F9.clicked.connect(self.sendf9)
        self.F10.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.F10.customContextMenuRequested.connect(self.edit_F10)
        self.F10.clicked.connect(self.sendf10)
        self.F11.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.F11.customContextMenuRequested.connect(self.edit_F11)
        self.F11.clicked.connect(self.sendf11)
        self.F12.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.F12.customContextMenuRequested.connect(self.edit_F12)
        self.F12.clicked.connect(self.sendf12)

    def edit_F1(self):
        logger.debug("F1 Right Clicked.")

    def edit_F2(self):
        logger.debug("F2 Right Clicked.")

    def edit_F3(self):
        logger.debug("F3 Right Clicked.")

    def edit_F4(self):
        logger.debug("F4 Right Clicked.")

    def edit_F5(self):
        logger.debug("F5 Right Clicked.")

    def edit_F6(self):
        logger.debug("F6 Right Clicked.")

    def edit_F7(self):
        logger.debug("F7 Right Clicked.")

    def edit_F8(self):
        logger.debug("F8 Right Clicked.")

    def edit_F9(self):
        logger.debug("F9 Right Clicked.")

    def edit_F10(self):
        logger.debug("F10 Right Clicked.")

    def edit_F11(self):
        logger.debug("F11 Right Clicked.")

    def edit_F12(self):
        logger.debug("F12 Right Clicked.")

    def sendf1(self):
        logger.debug("F1 Clicked")

    def sendf2(self):
        logger.debug("F2 Clicked")

    def sendf3(self):
        logger.debug("F3 Clicked")

    def sendf4(self):
        logger.debug("F4 Clicked")

    def sendf5(self):
        logger.debug("F5 Clicked")

    def sendf6(self):
        logger.debug("F6 Clicked")

    def sendf7(self):
        logger.debug("F7 Clicked")

    def sendf8(self):
        logger.debug("F8 Clicked")

    def sendf9(self):
        logger.debug("F9 Clicked")

    def sendf10(self):
        logger.debug("F10 Clicked")

    def sendf11(self):
        logger.debug("F11 Clicked")

    def sendf12(self):
        logger.debug("F12 Clicked")

    def run_sp_buttons_clicked(self):
        self.pref["run_state"] = self.radioButton_run.isChecked()
        self.write_preference()
        self.read_cw_macros()

    def write_preference(self):
        """
        Write preferences to json file.
        """
        try:
            with open(
                CONFIG_PATH + "/not1mm.json", "wt", encoding="utf-8"
            ) as file_descriptor:
                file_descriptor.write(dumps(self.pref, indent=4))
                logger.info("writing: %s", self.preference)
        except IOError as exception:
            ...
            logger.critical("writepreferences: %s", exception)

    def readpreferences(self):
        """
        Restore preferences if they exist, otherwise create some sane defaults.
        """
        try:
            if os.path.exists(CONFIG_PATH + "/not1mm.json"):
                with open(
                    CONFIG_PATH + "/not1mm.json", "rt", encoding="utf-8"
                ) as file_descriptor:
                    self.pref = loads(file_descriptor.read())
                    logger.info("%s", self.pref)
            else:
                logger.info("No preference file. Writing preference.")
                with open(
                    CONFIG_PATH + "/not1mm.json", "wt", encoding="utf-8"
                ) as file_descriptor:
                    self.pref = self.pref_ref.copy()
                    file_descriptor.write(dumps(self.pref, indent=4))
                    logger.info("%s", self.pref)
        except IOError as exception:
            ...
            logger.critical("Error: %s", exception)
        if self.pref.get("useqrz"):
            self.look_up = QRZlookup(
                self.pref.get("lookupusername"),
                self.pref.get("lookuppassword"),
            )
        if self.pref.get("run_state"):
            self.radioButton_run.setChecked(True)
        else:
            self.radioButton_sp.setChecked(True)

        if self.pref.get("dark_mode"):
            self.actionDark_Mode.setChecked(True)
        else:
            self.actionDark_Mode.setChecked(False)

        if self.pref.get("command_buttons"):
            self.actionCommand_Buttons.setChecked(True)
        else:
            self.actionCommand_Buttons.setChecked(False)

        if self.pref.get("cw_macros"):
            self.actionCW_Macros.setChecked(True)
        else:
            self.actionCW_Macros.setChecked(False)

        if self.pref.get("bands_modes"):
            self.actionMode_and_Bands.setChecked(True)
        else:
            self.actionMode_and_Bands.setChecked(False)

        self.dark_mode()
        self.show_command_buttons()
        self.show_CW_macros()
        self.show_band_mode()

    def dark_mode_stateChange(self):
        self.pref["dark_mode"] = self.actionDark_Mode.isChecked()
        self.write_preference()
        self.dark_mode()

    def dark_mode(self):
        if self.pref.get("dark_mode"):
            with open(WORKING_PATH + "/data/Combinear.qss") as stylefile:
                qss = stylefile.read()
                self.setStyleSheet(qss)
        else:
            self.setStyleSheet("")

    def cw_macros_stateChanged(self):
        self.pref["cw_macros"] = self.actionCW_Macros.isChecked()
        self.write_preference()
        self.show_CW_macros()

    def show_CW_macros(self):
        if self.pref.get("cw_macros"):
            self.Button_Row1.show()
            self.Button_Row2.show()
        else:
            self.Button_Row1.hide()
            self.Button_Row2.hide()

    def command_buttons_stateChange(self):
        self.pref["command_buttons"] = self.actionCommand_Buttons.isChecked()
        self.write_preference()
        self.show_command_buttons()

    def show_command_buttons(self):
        if self.pref.get("command_buttons"):
            self.Command_Buttons.show()
        else:
            self.Command_Buttons.hide()

    def show_band_mode_stateChange(self):
        self.pref["bands_modes"] = self.actionMode_and_Bands.isChecked()
        self.write_preference()
        self.show_band_mode()

    def show_band_mode(self):
        if self.actionMode_and_Bands.isChecked():
            self.Band_Mode_Frame.show()
        else:
            self.Band_Mode_Frame.hide()

    def callsign_changed(self):
        text = self.callsign.text()
        text = text.upper()
        stripped_text = text.strip()
        self.callsign.setText(stripped_text)

        if text[-1:] == " ":
            if stripped_text == "CW":
                self.setmode("CW")
                self.callsign.setText("")
                return
            if stripped_text == "SSB":
                self.setmode("SSB")
                self.callsign.setText("")
                return
            if stripped_text == "OPON":
                self.get_opon()
                self.callsign.setText("")
                return
            self.check_callsign(text)
            self.next_field.setFocus()

    def check_callsign(self, callsign):
        if hasattr(self.look_up, "session"):
            if self.look_up.session:
                response = self.look_up.lookup(callsign)
                logger.debug(f"The Response: {response}\n")
                if response:
                    theirgrid = response.get("grid")
                    theircountry = response.get("country")
                    if self.pref.get("gridsquare"):
                        heading = bearing(self.pref.get("gridsquare"), theirgrid)
                        kilometers = distance(self.pref.get("gridsquare"), theirgrid)
                        self.heading_distance.setText(
                            f"heading {heading}° / distance {kilometers}km"
                        )
                    self.dx_entity.setText(f"{theircountry}")
                else:
                    self.heading_distance.setText("Lookup failed.")
            ...

    def setmode(self, mode: str) -> None:
        if mode == "CW":
            self.mode.setText("CW")
            self.sent.setText("599")
            self.receive.setText("599")
            return
        if mode == "SSB":
            self.mode.setText("SSB")
            self.sent.setText("59")
            self.receive.setText("59")

    def get_opon(self):
        self.opon_dialog = OpOn()
        self.opon_dialog.accepted.connect(self.new_op)
        self.opon_dialog.open()

    def new_op(self):
        if self.opon_dialog.NewOperator.text():
            self.current_op = self.opon_dialog.NewOperator.text()

        self.opon_dialog.close()
        logger.debug(f"New Op: {self.current_op}")

    def poll_radio(self):
        if self.rig_control.online:
            vfo = self.rig_control.get_vfo()
            mode = self.rig_control.get_mode()
            logger.debug(f"VFO: {vfo}  MODE: {mode}")

    def read_cw_macros(self) -> None:
        """
        Reads in the CW macros, firsts it checks to see if the file exists. If it does not,
        and this has been packaged with pyinstaller it will copy the default file from the
        temp directory this is running from... In theory.
        """

        if not Path(DATA_PATH + "/cwmacros.txt").exists():
            logger.debug("read_cw_macros: copying default macro file.")
            copyfile(WORKING_PATH + "/data/cwmacros.txt", DATA_PATH + "/cwmacros.txt")
        with open(
            DATA_PATH + "/cwmacros.txt", "r", encoding="utf-8"
        ) as file_descriptor:
            for line in file_descriptor:
                try:
                    mode, fkey, buttonname, cwtext = line.split("|")
                    if mode.strip().upper() == "R" and self.pref.get("run_state"):
                        self.fkeys[fkey.strip()] = (buttonname.strip(), cwtext.strip())
                    if mode.strip().upper() != "R" and not self.pref.get("run_state"):
                        self.fkeys[fkey.strip()] = (buttonname.strip(), cwtext.strip())
                except ValueError as err:
                    ...
                    logger.info("read_cw_macros: %s", err)
        keys = self.fkeys.keys()
        if "F1" in keys:
            self.F1.setText(f"F1: {self.fkeys['F1'][0]}")
            self.F1.setToolTip(self.fkeys["F1"][1])
        if "F2" in keys:
            self.F2.setText(f"F2: {self.fkeys['F2'][0]}")
            self.F2.setToolTip(self.fkeys["F2"][1])
        if "F3" in keys:
            self.F3.setText(f"F3: {self.fkeys['F3'][0]}")
            self.F3.setToolTip(self.fkeys["F3"][1])
        if "F4" in keys:
            self.F4.setText(f"F4: {self.fkeys['F4'][0]}")
            self.F4.setToolTip(self.fkeys["F4"][1])
        if "F5" in keys:
            self.F5.setText(f"F5: {self.fkeys['F5'][0]}")
            self.F5.setToolTip(self.fkeys["F5"][1])
        if "F6" in keys:
            self.F6.setText(f"F6: {self.fkeys['F6'][0]}")
            self.F6.setToolTip(self.fkeys["F6"][1])
        if "F7" in keys:
            self.F7.setText(f"F7: {self.fkeys['F7'][0]}")
            self.F7.setToolTip(self.fkeys["F7"][1])
        if "F8" in keys:
            self.F8.setText(f"F8: {self.fkeys['F8'][0]}")
            self.F8.setToolTip(self.fkeys["F8"][1])
        if "F9" in keys:
            self.F9.setText(f"F9: {self.fkeys['F9'][0]}")
            self.F9.setToolTip(self.fkeys["F9"][1])
        if "F10" in keys:
            self.F10.setText(f"F10: {self.fkeys['F10'][0]}")
            self.F10.setToolTip(self.fkeys["F10"][1])
        if "F11" in keys:
            self.F11.setText(f"F11: {self.fkeys['F11'][0]}")
            self.F11.setToolTip(self.fkeys["F11"][1])
        if "F12" in keys:
            self.F12.setText(f"F12: {self.fkeys['F12'][0]}")
            self.F12.setToolTip(self.fkeys["F12"][1])


class OpOn(QtWidgets.QDialog):
    """Change the current operator"""

    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi(WORKING_PATH + "/data/opon.ui", self)
        self.buttonBox.clicked.connect(self.store)

    def store(self):
        """dialog magic"""
        ...
        # self.accept()


def load_fonts_from_dir(directory: str) -> set:
    """
    Well it loads fonts from a directory...
    """
    font_families = set()
    for _fi in QDir(directory).entryInfoList(["*.ttf", "*.woff", "*.woff2"]):
        _id = QFontDatabase.addApplicationFont(_fi.absoluteFilePath())
        font_families |= set(QFontDatabase.applicationFontFamilies(_id))
    return font_families


def install_icons():
    os.system(
        "xdg-icon-resource install --size 32 --context apps --mode user "
        f"{WORKING_PATH}/data/k6gte.not1mm-32.png k6gte-not1mm"
    )
    os.system(
        "xdg-icon-resource install --size 64 --context apps --mode user "
        f"{WORKING_PATH}/data/k6gte.not1mm-64.png k6gte-not1mm"
    )
    os.system(
        "xdg-icon-resource install --size 128 --context apps --mode user "
        f"{WORKING_PATH}/data/k6gte.not1mm-128.png k6gte-not1mm"
    )
    os.system(f"xdg-desktop-menu install {WORKING_PATH}/data/k6gte-not1mm.desktop")


def run():
    """
    Main Entry
    """

    install_icons()
    timer.start(1000)

    sys.exit(app.exec())


logger = logging.getLogger("__name__")
handler = logging.StreamHandler()
formatter = logging.Formatter(
    datefmt="%H:%M:%S",
    fmt="[%(asctime)s] %(levelname)s %(module)s - %(funcName)s Line %(lineno)d:\n%(message)s",
)
handler.setFormatter(formatter)
logger.addHandler(handler)

if Path("./debug").exists():
    # if True:
    logger.setLevel(logging.DEBUG)
    logger.debug("debugging on")
else:
    logger.setLevel(logging.WARNING)
    logger.warning("debugging off")

app = QtWidgets.QApplication(sys.argv)
app.setStyle("Fusion")
font_path = WORKING_PATH + "/data"
families = load_fonts_from_dir(os.fspath(font_path))
logger.info(families)
window = MainWindow()
window.setGeometry(-1, -1, 600, 200)
window.setWindowTitle(f"Not1MM v{__version__}")
window.show()
timer = QtCore.QTimer()
timer.timeout.connect(window.poll_radio)


if __name__ == "__main__":
    run()
