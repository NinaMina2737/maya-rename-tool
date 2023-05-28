#!/usr/bin/env python
# coding=utf-8

from __future__ import absolute_import, division, print_function, unicode_literals
import maya.cmds as cmds
import traceback


def rename_node(rename_text):
    try:
        # Open an undo chunk
        cmds.undoInfo(openChunk=True)
        # Execute the script
        selections = cmds.ls(selection=True)
        for selection in selections:
            cmds.rename(selection, rename_text)
    except Exception as e:
        # Print the error message
        cmds.warning("An error occurred: {}".format(str(e)))
        # Print the traceback
        cmds.warning(traceback.format_exc())
    finally:
        # Close the undo chunk
        cmds.undoInfo(closeChunk=True)

def replace_node_name(target_text, replace_text):
    try:
        # Open an undo chunk
        cmds.undoInfo(openChunk=True)
        # Execute the script
        selections = cmds.ls(selection=True)
        for selection in selections:
            new_name = selection.replace(target_text, replace_text)
            cmds.rename(selection, selection.replace(selection, new_name))
    except Exception as e:
        # Print the error message
        cmds.warning("An error occurred: {}".format(str(e)))
        # Print the traceback
        cmds.warning(traceback.format_exc())
    finally:
        # Close the undo chunk
        cmds.undoInfo(closeChunk=True)

def insert_node_name(target_text, insert_text, mode="before"):
    try:
        # Open an undo chunk
        cmds.undoInfo(openChunk=True)
        # Execute the script
        selections = cmds.ls(selection=True)
        for selection in selections:
            new_name = ""
            if mode == "before":
                new_name = selection.replace(target_text, insert_text + target_text)
            elif mode == "after":
                new_name = selection.replace(target_text, target_text + insert_text)
            cmds.rename(selection, new_name)
    except Exception as e:
        # Print the error message
        cmds.warning("An error occurred: {}".format(str(e)))
        # Print the traceback
        cmds.warning(traceback.format_exc())
    finally:
        # Close the undo chunk
        cmds.undoInfo(closeChunk=True)
