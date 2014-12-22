#!/usr/bin/env python

import lldb

#def doLoadGenericSummaries(debugger, dictionary):
#  """Method to load my generic LLDB summaries in to the debugger"""
#
#  debugger.HandleCommand('type summary add --summary-string')
#
#def __lldb_init_module(debugger, dictionary):
#  """LLDB init method"""
#
#  doLoadGenericSummaries(debugger, dictionary)

##################################################
# Command example
##################################################
#
# debugger = SBDebugger
# user_input = Python string
# result = SBCommandReturnObject
#
#def MyCommand_Impl(debugger, user_input, result, unused):
#  """docstring for MyCommand_Impl"""
#  pass
#
# Add the command to the debugger
# co sc a foo -f foo
# command script add foo --python-function foo

##################################################
# How to get the thread from the Debugger object
##################################################
# thread = debugger.GetSelectedTarget().GetProcess().GetSelectedThread()
# thread.frames

##################################################
# Breakpoint example
##################################################
# frame = SBFrame
# location = SBBreakpointLocation
#
#def break_point_example(frame, location, unused):
#  """docstring for break_point_example"""
#  pass
#
# Add the breakpoint to the debugger
#
# br co a -s p -F foo 1
# breakpoint command add --script python --python-function foo 1

