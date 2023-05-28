#!/usr/bin/env python
# coding=utf-8

from __future__ import absolute_import, division, print_function, unicode_literals
from maya import cmds
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin
from PySide2 import QtCore, QtWidgets
import traceback

import maya_rename_tool as mrt
reload(mrt)

WINDOW_TITLE = "renameTool"

class RenameToolUI(MayaQWidgetBaseMixin, QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(RenameToolUI, self).__init__(*args, **kwargs)

        self.setWindowTitle(WINDOW_TITLE)

        self.create_widget()
        self.create_layout()
        return

    def create_widget(self):
        self.target_label = QtWidgets.QLabel("Target:")
        self.input_label = QtWidgets.QLabel("Input:")

        self.target_line_edit = QtWidgets.QLineEdit()
        self.target_line_edit.setPlaceholderText("Target")
        self.input_line_edit = QtWidgets.QLineEdit()
        self.input_line_edit.setPlaceholderText("Input")

        self.rename_button = QtWidgets.QPushButton("Rename")
        self.rename_button.clicked.connect(self.rename)
        self.replace_button = QtWidgets.QPushButton("Replace")
        self.replace_button.clicked.connect(self.replace)

        self.insert_before_button = QtWidgets.QPushButton("Insert (Before the target)")
        self.insert_before_button.clicked.connect(self.insert_before)
        self.insert_after_button = QtWidgets.QPushButton("Insert (After the target)")
        self.insert_after_button.clicked.connect(self.insert_after)
        return

    def create_layout(self):
        self.main_layout = QtWidgets.QVBoxLayout(self)

        self.target_horizontal_layout = QtWidgets.QHBoxLayout()
        self.target_horizontal_layout.addWidget(self.target_label)
        self.target_horizontal_layout.addWidget(self.target_line_edit)

        self.main_layout.addLayout(self.target_horizontal_layout)

        self.input_horizontal_layout = QtWidgets.QHBoxLayout()
        self.input_horizontal_layout.addWidget(self.input_label)
        self.input_horizontal_layout.addWidget(self.input_line_edit)

        self.main_layout.addLayout(self.input_horizontal_layout)

        self.main_layout.addWidget(self.rename_button)
        self.main_layout.addWidget(self.replace_button)
        self.main_layout.addWidget(self.insert_before_button)
        self.main_layout.addWidget(self.insert_after_button)
        return

    def rename(self):
        input_text = self.input_line_edit.text()
        mrt.rename_node(input_text)
        return

    def replace(self):
        target_text = self.target_line_edit.text()
        input_text = self.input_line_edit.text()
        mrt.replace_node_name(target_text, input_text)
        return

    def insert_before(self):
        target_text = self.target_line_edit.text()
        input_text = self.input_line_edit.text()
        mrt.insert_node_name(target_text=target_text, insert_text=input_text, mode="before")
        return

    def insert_after(self):
        target_text = self.target_line_edit.text()
        input_text = self.input_line_edit.text()
        mrt.insert_node_name(target_text=target_text, insert_text=input_text, mode="after")
        return

def execute():
    """
    Executes the UI.

    Raises:
        Exception: An error occurred.
    """
    try:
        # Check if the window already exists
        if cmds.window(WINDOW_TITLE, exists=True):
            cmds.deleteUI(WINDOW_TITLE)
        # Create the window
        window = RenameToolUI()
        window.show()
    except Exception as e:
        # Print the error message
        cmds.warning("An error occurred: {}".format(str(e)))
        # Print the traceback
        cmds.warning(traceback.format_exc())

if __name__ == "__main__":
    execute()
