#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2026.1.1),
    on April 27, 2026, at 14:12
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (
    NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, STOPPING, FINISHED, PRESSED, 
    RELEASED, FOREVER, priority
)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Run 'Before Experiment' code from code
import random
total_time= 30
# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2026.1.1'
expName = 'numbers_control'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'Language': ["arabic_path","hindi_path","mandarin_path"],
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'expVersion|hid': expVersion,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1440, 900]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # replace default participant ID
    if prefs.piloting['replaceParticipantID']:
        expInfo['participant'] = 'pilot'

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version=expVersion,
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\micha\\OneDrive - Georgia Southern University\\4_RESEARCH\\ABA\\numbers\\numerals\\numbers_control_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    # store pilot mode in data file
    thisExp.addData('piloting', PILOTING, priority=priority.LOW)
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    if PILOTING:
        # show a visual indicator if we're in piloting mode
        if prefs.piloting['showPilotingIndicator']:
            win.showPilotingIndicator()
        # always show the mouse in piloting mode
        if prefs.piloting['forceMouseVisible']:
            win.mouseVisible = True
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], currentRoutine=None):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    currentRoutine : psychopy.data.Routine
        Current Routine we are in at time of pausing, if any. This object tells PsychoPy what Components to pause/play/dispatch.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # dispatch messages on response components
        if currentRoutine is not None:
            for comp in currentRoutine.getDispatchComponents():
                comp.device.dispatchMessages()
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # update experiment info
    expInfo['date'] = data.getDateStr()
    expInfo['expName'] = expName
    expInfo['expVersion'] = expVersion
    expInfo['psychopyVersion'] = psychopyVersion
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "trial" ---
    # Run 'Begin Experiment' code from code
    digits = [0,1,2,3,4,5,6,7,8,9]
    correct_digits = []
    total_time = 30
    correct = 0
    incorrect = 0
    print('In begin experiment section of trial routine')
    mouse = event.Mouse(win=win)
    x, y = [None, None]
    mouse.mouseClock = core.Clock()
    image = visual.ImageStim(
        win=win,
        name='image', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.2), draggable=False, size=(0.3, 0.3),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    button_0 = visual.ButtonStim(win, 
        text='', font='Arvo',
        pos=(-.5, -.1),
        letterHeight=0.05,
        size=(0.09, 0.09), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='bottom-center',
        name='button_0',
        depth=-4
    )
    button_0.buttonClock = core.Clock()
    button_1 = visual.ButtonStim(win, 
        text='', font='Arvo',
        pos=(-.25, -.1),
        letterHeight=0.05,
        size=(0.09, 0.09), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='bottom-center',
        name='button_1',
        depth=-5
    )
    button_1.buttonClock = core.Clock()
    button_2 = visual.ButtonStim(win, 
        text='', font='Arvo',
        pos=(0, -.1),
        letterHeight=0.05,
        size=(0.09, 0.09), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='bottom-center',
        name='button_2',
        depth=-6
    )
    button_2.buttonClock = core.Clock()
    button_3 = visual.ButtonStim(win, 
        text='', font='Arvo',
        pos=(.25, -.1),
        letterHeight=0.05,
        size=(0.09, 0.09), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='bottom-center',
        name='button_3',
        depth=-7
    )
    button_3.buttonClock = core.Clock()
    button_4 = visual.ButtonStim(win, 
        text='', font='Arvo',
        pos=(.5, -.1),
        letterHeight=0.05,
        size=(0.09, 0.09), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='bottom-center',
        name='button_4',
        depth=-8
    )
    button_4.buttonClock = core.Clock()
    button_5 = visual.ButtonStim(win, 
        text='', font='Arvo',
        pos=(-.5, -.3),
        letterHeight=0.05,
        size=(0.09, 0.09), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='bottom-center',
        name='button_5',
        depth=-9
    )
    button_5.buttonClock = core.Clock()
    button_6 = visual.ButtonStim(win, 
        text='', font='Arvo',
        pos=(-.25, -.3),
        letterHeight=0.05,
        size=(0.09, 0.09), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='bottom-center',
        name='button_6',
        depth=-10
    )
    button_6.buttonClock = core.Clock()
    button_7 = visual.ButtonStim(win, 
        text='', font='Arvo',
        pos=(0, -.3),
        letterHeight=0.05,
        size=(0.09, 0.09), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='bottom-center',
        name='button_7',
        depth=-11
    )
    button_7.buttonClock = core.Clock()
    button_8 = visual.ButtonStim(win, 
        text='', font='Arvo',
        pos=(.25, -.3),
        letterHeight=0.05,
        size=(0.09, 0.09), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='bottom-center',
        name='button_8',
        depth=-12
    )
    button_8.buttonClock = core.Clock()
    button_9 = visual.ButtonStim(win, 
        text='', font='Arvo',
        pos=(.5, -.3),
        letterHeight=0.05,
        size=(0.09, 0.09), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='bottom-center',
        name='button_9',
        depth=-13
    )
    button_9.buttonClock = core.Clock()
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    if eyetracker is not None:
        eyetracker.enableEventReporting()
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler2(
        name='trials',
        nReps=300.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('digit_paths_black.csv'), 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial in trials:
        trials.status = STARTED
        if hasattr(thisTrial, 'status'):
            thisTrial.status = STARTED
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # set up handler to look after randomisation of conditions etc
        inner_loop = data.TrialHandler2(
            name='inner_loop',
            nReps=1.0, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
            isTrials=False, 
        )
        thisExp.addLoop(inner_loop)  # add the loop to the experiment
        thisInner_loop = inner_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisInner_loop.rgb)
        if thisInner_loop != None:
            for paramName in thisInner_loop:
                globals()[paramName] = thisInner_loop[paramName]
        
        for thisInner_loop in inner_loop:
            inner_loop.status = STARTED
            if hasattr(thisInner_loop, 'status'):
                thisInner_loop.status = STARTED
            currentLoop = inner_loop
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # abbreviate parameter names if possible (e.g. rgb = thisInner_loop.rgb)
            if thisInner_loop != None:
                for paramName in thisInner_loop:
                    globals()[paramName] = thisInner_loop[paramName]
            
            # --- Prepare to start Routine "trial" ---
            # create an object to store info about Routine trial
            trial = data.Routine(
                name='trial',
                components=[mouse, image, button_0, button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9],
            )
            trial.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from code
            random.shuffle(digits)
            response = None
            point_subtracted = False
            responded = False
            started_routine_at = globalClock.getTime()
            routineTimer.reset()
            # setup some python lists for storing info about the mouse
            mouse.x = []
            mouse.y = []
            mouse.leftButton = []
            mouse.midButton = []
            mouse.rightButton = []
            mouse.time = []
            gotValidClick = False  # until a click is received
            image.setImage(trials.thisTrial[expInfo['Language']]
            )
            button_0.setText(digits[0])
            # reset button_0 to account for continued clicks & clear times on/off
            button_0.reset()
            button_1.setText(digits[1])
            # reset button_1 to account for continued clicks & clear times on/off
            button_1.reset()
            button_2.setText(digits[2])
            # reset button_2 to account for continued clicks & clear times on/off
            button_2.reset()
            button_3.setText(digits[3])
            # reset button_3 to account for continued clicks & clear times on/off
            button_3.reset()
            button_4.setText(digits[4])
            # reset button_4 to account for continued clicks & clear times on/off
            button_4.reset()
            button_5.setText(digits[5])
            # reset button_5 to account for continued clicks & clear times on/off
            button_5.reset()
            button_6.setText(digits[6])
            # reset button_6 to account for continued clicks & clear times on/off
            button_6.reset()
            button_7.setText(digits[7])
            # reset button_7 to account for continued clicks & clear times on/off
            button_7.reset()
            button_8.setText(digits[8])
            # reset button_8 to account for continued clicks & clear times on/off
            button_8.reset()
            button_9.setText(digits[9])
            # reset button_9 to account for continued clicks & clear times on/off
            button_9.reset()
            # store start times for trial
            trial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            trial.tStart = globalClock.getTime(format='float')
            trial.status = STARTED
            thisExp.addData('trial.started', trial.tStart)
            trial.maxDuration = None
            # keep track of which components have finished
            trialComponents = trial.components
            for thisComponent in trial.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "trial" ---
            thisExp.currentRoutine = trial
            trial.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 5.0:
                # if trial has changed, end Routine now
                if hasattr(thisInner_loop, 'status') and thisInner_loop.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from debug_text_trial
                timer_lines = []
                timer_lines.append(f"Global: {globalClock.getTime():.2f}s")
                
                try:
                    timer_lines.append(f"Routine: {routineTimer.getTime():.2f}s")
                except:
                    timer_lines.append("Routine: N/A")
                
                #try:
                #    timer_lines.append(f"Inner: {innerClock.getTime():.2f}s")
                #except:
                #    timer_lines.append("Inner: N/A")
                #
                #try:
                #    timer_lines.append(f"Trial: {trialClock.getTime():.2f}s")
                #except:
                #    timer_lines.append("Trial: N/A")
                
                #try:
                #    timer_lines.append(f"Inner remaining: {inner_loop.nRemaining}")
                #except:
                #    timer_lines.append("Inner remaining: N/A")
                
                # Add the digit being shown this trial
                try:
                    timer_lines.append(f"Digit: {digit}")
                except:
                    timer_lines.append("Digit: N/A")
                
                timer_display = "\n".join(timer_lines)
                # Run 'Each Frame' code from code
                # -----------------------------
                # SCORING + ROUTINE END LOGIC
                # -----------------------------
                
                if globalClock.getTime() > total_time:
                    print(f"Timeout in TRIAL routine at {globalClock.getTime():.2f}")
                    inner_loop.finished = True      # end the inner loop
                    continueRoutine = False         # end THIS routine immediately
                
                # *mouse* updates
                
                # if mouse is starting this frame...
                if mouse.status == NOT_STARTED and t >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse.frameNStart = frameN  # exact frame index
                    mouse.tStart = t  # local t and not account for scr refresh
                    mouse.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    mouse.status = STARTED
                    mouse.mouseClock.reset()
                    prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
                if mouse.status == STARTED:  # only update if started and not finished!
                    buttons = mouse.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            pass
                            x, y = mouse.getPos()
                            mouse.x.append(float(x))
                            mouse.y.append(float(y))
                            buttons = mouse.getPressed()
                            mouse.leftButton.append(buttons[0])
                            mouse.midButton.append(buttons[1])
                            mouse.rightButton.append(buttons[2])
                            mouse.time.append(mouse.mouseClock.getTime())
                
                # *image* updates
                
                # if image is starting this frame...
                if image.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image.frameNStart = frameN  # exact frame index
                    image.tStart = t  # local t and not account for scr refresh
                    image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    image.status = STARTED
                    image.setAutoDraw(True)
                
                # if image is active this frame...
                if image.status == STARTED:
                    # update params
                    pass
                # *button_0* updates
                
                # if button_0 is starting this frame...
                if button_0.status == NOT_STARTED and t >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    button_0.frameNStart = frameN  # exact frame index
                    button_0.tStart = t  # local t and not account for scr refresh
                    button_0.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(button_0, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    button_0.status = STARTED
                    win.callOnFlip(button_0.buttonClock.reset)
                    button_0.setAutoDraw(True)
                
                # if button_0 is active this frame...
                if button_0.status == STARTED:
                    # update params
                    pass
                    # check whether button_0 has been pressed
                    if button_0.isClicked:
                        if not button_0.wasClicked:
                            # if this is a new click, store time of first click and clicked until
                            button_0.timesOn.append(routineTimer.getTime())
                            button_0.timesOff.append(routineTimer.getTime())
                        elif len(button_0.timesOff):
                            # if click is continuing from last frame, update time of clicked until
                            button_0.timesOff[-1] = routineTimer.getTime()
                        if not button_0.wasClicked:
                            # end routine when button_0 is clicked
                            continueRoutine = False
                        if not button_0.wasClicked:
                            # run callback code when button_0 is clicked
                            response = digits[0]
                            print(response)
                            if response == digit:
                             correct += 1
                             print('incremented correct')
                             print(correct)
                            
                            else:
                             incorrect += 1
                             print('incremented incorrect')
                             print(incorrect)  
                # take note of whether button_0 was clicked, so that next frame we know if clicks are new
                button_0.wasClicked = button_0.isClicked and button_0.status == STARTED
                # *button_1* updates
                
                # if button_1 is starting this frame...
                if button_1.status == NOT_STARTED and t >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    button_1.frameNStart = frameN  # exact frame index
                    button_1.tStart = t  # local t and not account for scr refresh
                    button_1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(button_1, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    button_1.status = STARTED
                    win.callOnFlip(button_1.buttonClock.reset)
                    button_1.setAutoDraw(True)
                
                # if button_1 is active this frame...
                if button_1.status == STARTED:
                    # update params
                    pass
                    # check whether button_1 has been pressed
                    if button_1.isClicked:
                        if not button_1.wasClicked:
                            # if this is a new click, store time of first click and clicked until
                            button_1.timesOn.append(routineTimer.getTime())
                            button_1.timesOff.append(routineTimer.getTime())
                        elif len(button_1.timesOff):
                            # if click is continuing from last frame, update time of clicked until
                            button_1.timesOff[-1] = routineTimer.getTime()
                        if not button_1.wasClicked:
                            # end routine when button_1 is clicked
                            continueRoutine = False
                        if not button_1.wasClicked:
                            # run callback code when button_1 is clicked
                            response = digits[1]
                            print(response)
                            if response == digit:
                             correct += 1
                             print('incremented correct')
                             print(correct)
                            
                            else:
                             incorrect += 1
                             print('incremented incorrect')
                             print(incorrect)  
                # take note of whether button_1 was clicked, so that next frame we know if clicks are new
                button_1.wasClicked = button_1.isClicked and button_1.status == STARTED
                # *button_2* updates
                
                # if button_2 is starting this frame...
                if button_2.status == NOT_STARTED and t >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    button_2.frameNStart = frameN  # exact frame index
                    button_2.tStart = t  # local t and not account for scr refresh
                    button_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(button_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    button_2.status = STARTED
                    win.callOnFlip(button_2.buttonClock.reset)
                    button_2.setAutoDraw(True)
                
                # if button_2 is active this frame...
                if button_2.status == STARTED:
                    # update params
                    pass
                    # check whether button_2 has been pressed
                    if button_2.isClicked:
                        if not button_2.wasClicked:
                            # if this is a new click, store time of first click and clicked until
                            button_2.timesOn.append(routineTimer.getTime())
                            button_2.timesOff.append(routineTimer.getTime())
                        elif len(button_2.timesOff):
                            # if click is continuing from last frame, update time of clicked until
                            button_2.timesOff[-1] = routineTimer.getTime()
                        if not button_2.wasClicked:
                            # end routine when button_2 is clicked
                            continueRoutine = False
                        if not button_2.wasClicked:
                            # run callback code when button_2 is clicked
                            response = digits[2]
                            print(response)
                            if response == digit:
                             correct += 1
                             print('incremented correct')
                             print(correct)
                            
                            else:
                             incorrect += 1
                             print('incremented incorrect')
                             print(incorrect)  
                # take note of whether button_2 was clicked, so that next frame we know if clicks are new
                button_2.wasClicked = button_2.isClicked and button_2.status == STARTED
                # *button_3* updates
                
                # if button_3 is starting this frame...
                if button_3.status == NOT_STARTED and t >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    button_3.frameNStart = frameN  # exact frame index
                    button_3.tStart = t  # local t and not account for scr refresh
                    button_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(button_3, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    button_3.status = STARTED
                    win.callOnFlip(button_3.buttonClock.reset)
                    button_3.setAutoDraw(True)
                
                # if button_3 is active this frame...
                if button_3.status == STARTED:
                    # update params
                    pass
                    # check whether button_3 has been pressed
                    if button_3.isClicked:
                        if not button_3.wasClicked:
                            # if this is a new click, store time of first click and clicked until
                            button_3.timesOn.append(routineTimer.getTime())
                            button_3.timesOff.append(routineTimer.getTime())
                        elif len(button_3.timesOff):
                            # if click is continuing from last frame, update time of clicked until
                            button_3.timesOff[-1] = routineTimer.getTime()
                        if not button_3.wasClicked:
                            # end routine when button_3 is clicked
                            continueRoutine = False
                        if not button_3.wasClicked:
                            # run callback code when button_3 is clicked
                            response = digits[3]
                            print(response)
                            if response == digit:
                             correct += 1
                             print('incremented correct')
                             print(correct)
                            
                            else:
                             incorrect += 1
                             print('incremented incorrect')
                             print(incorrect)  
                # take note of whether button_3 was clicked, so that next frame we know if clicks are new
                button_3.wasClicked = button_3.isClicked and button_3.status == STARTED
                # *button_4* updates
                
                # if button_4 is starting this frame...
                if button_4.status == NOT_STARTED and t >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    button_4.frameNStart = frameN  # exact frame index
                    button_4.tStart = t  # local t and not account for scr refresh
                    button_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(button_4, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    button_4.status = STARTED
                    win.callOnFlip(button_4.buttonClock.reset)
                    button_4.setAutoDraw(True)
                
                # if button_4 is active this frame...
                if button_4.status == STARTED:
                    # update params
                    pass
                    # check whether button_4 has been pressed
                    if button_4.isClicked:
                        if not button_4.wasClicked:
                            # if this is a new click, store time of first click and clicked until
                            button_4.timesOn.append(routineTimer.getTime())
                            button_4.timesOff.append(routineTimer.getTime())
                        elif len(button_4.timesOff):
                            # if click is continuing from last frame, update time of clicked until
                            button_4.timesOff[-1] = routineTimer.getTime()
                        if not button_4.wasClicked:
                            # end routine when button_4 is clicked
                            continueRoutine = False
                        if not button_4.wasClicked:
                            # run callback code when button_4 is clicked
                            response = digits[4]
                            print(response)
                            if response == digit:
                             correct += 1
                             print('incremented correct')
                             print(correct)
                            
                            else:
                             incorrect += 1
                             print('incremented incorrect')
                             print(incorrect)  
                # take note of whether button_4 was clicked, so that next frame we know if clicks are new
                button_4.wasClicked = button_4.isClicked and button_4.status == STARTED
                # *button_5* updates
                
                # if button_5 is starting this frame...
                if button_5.status == NOT_STARTED and t >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    button_5.frameNStart = frameN  # exact frame index
                    button_5.tStart = t  # local t and not account for scr refresh
                    button_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(button_5, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    button_5.status = STARTED
                    win.callOnFlip(button_5.buttonClock.reset)
                    button_5.setAutoDraw(True)
                
                # if button_5 is active this frame...
                if button_5.status == STARTED:
                    # update params
                    pass
                    # check whether button_5 has been pressed
                    if button_5.isClicked:
                        if not button_5.wasClicked:
                            # if this is a new click, store time of first click and clicked until
                            button_5.timesOn.append(routineTimer.getTime())
                            button_5.timesOff.append(routineTimer.getTime())
                        elif len(button_5.timesOff):
                            # if click is continuing from last frame, update time of clicked until
                            button_5.timesOff[-1] = routineTimer.getTime()
                        if not button_5.wasClicked:
                            # end routine when button_5 is clicked
                            continueRoutine = False
                        if not button_5.wasClicked:
                            # run callback code when button_5 is clicked
                            response = digits[5]
                            print(response)
                            if response == digit:
                             correct += 1
                             print('incremented correct')
                             print(correct)
                            
                            else:
                             incorrect += 1
                             print('incremented incorrect')
                             print(incorrect)  
                # take note of whether button_5 was clicked, so that next frame we know if clicks are new
                button_5.wasClicked = button_5.isClicked and button_5.status == STARTED
                # *button_6* updates
                
                # if button_6 is starting this frame...
                if button_6.status == NOT_STARTED and t >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    button_6.frameNStart = frameN  # exact frame index
                    button_6.tStart = t  # local t and not account for scr refresh
                    button_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(button_6, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    button_6.status = STARTED
                    win.callOnFlip(button_6.buttonClock.reset)
                    button_6.setAutoDraw(True)
                
                # if button_6 is active this frame...
                if button_6.status == STARTED:
                    # update params
                    pass
                    # check whether button_6 has been pressed
                    if button_6.isClicked:
                        if not button_6.wasClicked:
                            # if this is a new click, store time of first click and clicked until
                            button_6.timesOn.append(routineTimer.getTime())
                            button_6.timesOff.append(routineTimer.getTime())
                        elif len(button_6.timesOff):
                            # if click is continuing from last frame, update time of clicked until
                            button_6.timesOff[-1] = routineTimer.getTime()
                        if not button_6.wasClicked:
                            # end routine when button_6 is clicked
                            continueRoutine = False
                        if not button_6.wasClicked:
                            # run callback code when button_6 is clicked
                            response = digits[6]
                            print(response)
                            if response == digit:
                             correct += 1
                             print('incremented correct')
                             print(correct)
                            
                            else:
                             incorrect += 1
                             print('incremented incorrect')
                             print(incorrect)  
                # take note of whether button_6 was clicked, so that next frame we know if clicks are new
                button_6.wasClicked = button_6.isClicked and button_6.status == STARTED
                # *button_7* updates
                
                # if button_7 is starting this frame...
                if button_7.status == NOT_STARTED and t >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    button_7.frameNStart = frameN  # exact frame index
                    button_7.tStart = t  # local t and not account for scr refresh
                    button_7.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(button_7, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    button_7.status = STARTED
                    win.callOnFlip(button_7.buttonClock.reset)
                    button_7.setAutoDraw(True)
                
                # if button_7 is active this frame...
                if button_7.status == STARTED:
                    # update params
                    pass
                    # check whether button_7 has been pressed
                    if button_7.isClicked:
                        if not button_7.wasClicked:
                            # if this is a new click, store time of first click and clicked until
                            button_7.timesOn.append(routineTimer.getTime())
                            button_7.timesOff.append(routineTimer.getTime())
                        elif len(button_7.timesOff):
                            # if click is continuing from last frame, update time of clicked until
                            button_7.timesOff[-1] = routineTimer.getTime()
                        if not button_7.wasClicked:
                            # end routine when button_7 is clicked
                            continueRoutine = False
                        if not button_7.wasClicked:
                            # run callback code when button_7 is clicked
                            response = digits[7]
                            print(response)
                            if response == digit:
                             correct += 1
                             print('incremented correct')
                             print(correct)
                            
                            else:
                             incorrect += 1
                             print('incremented incorrect')
                             print(incorrect)  
                # take note of whether button_7 was clicked, so that next frame we know if clicks are new
                button_7.wasClicked = button_7.isClicked and button_7.status == STARTED
                # *button_8* updates
                
                # if button_8 is starting this frame...
                if button_8.status == NOT_STARTED and t >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    button_8.frameNStart = frameN  # exact frame index
                    button_8.tStart = t  # local t and not account for scr refresh
                    button_8.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(button_8, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    button_8.status = STARTED
                    win.callOnFlip(button_8.buttonClock.reset)
                    button_8.setAutoDraw(True)
                
                # if button_8 is active this frame...
                if button_8.status == STARTED:
                    # update params
                    pass
                    # check whether button_8 has been pressed
                    if button_8.isClicked:
                        if not button_8.wasClicked:
                            # if this is a new click, store time of first click and clicked until
                            button_8.timesOn.append(routineTimer.getTime())
                            button_8.timesOff.append(routineTimer.getTime())
                        elif len(button_8.timesOff):
                            # if click is continuing from last frame, update time of clicked until
                            button_8.timesOff[-1] = routineTimer.getTime()
                        if not button_8.wasClicked:
                            # end routine when button_8 is clicked
                            continueRoutine = False
                        if not button_8.wasClicked:
                            # run callback code when button_8 is clicked
                            response = digits[8]
                            print(response)
                            if response == digit:
                             correct += 1
                             print('incremented correct')
                             print(correct)
                            
                            else:
                             incorrect += 1
                             print('incremented incorrect')
                             print(incorrect)  
                # take note of whether button_8 was clicked, so that next frame we know if clicks are new
                button_8.wasClicked = button_8.isClicked and button_8.status == STARTED
                # *button_9* updates
                
                # if button_9 is starting this frame...
                if button_9.status == NOT_STARTED and t >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    button_9.frameNStart = frameN  # exact frame index
                    button_9.tStart = t  # local t and not account for scr refresh
                    button_9.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(button_9, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    button_9.status = STARTED
                    win.callOnFlip(button_9.buttonClock.reset)
                    button_9.setAutoDraw(True)
                
                # if button_9 is active this frame...
                if button_9.status == STARTED:
                    # update params
                    pass
                    # check whether button_9 has been pressed
                    if button_9.isClicked:
                        if not button_9.wasClicked:
                            # if this is a new click, store time of first click and clicked until
                            button_9.timesOn.append(routineTimer.getTime())
                            button_9.timesOff.append(routineTimer.getTime())
                        elif len(button_9.timesOff):
                            # if click is continuing from last frame, update time of clicked until
                            button_9.timesOff[-1] = routineTimer.getTime()
                        if not button_9.wasClicked:
                            # end routine when button_9 is clicked
                            continueRoutine = False
                        if not button_9.wasClicked:
                            # run callback code when button_9 is clicked
                            response = digits[9]
                            print(response)
                            if response == digit:
                             correct += 1
                             print('incremented correct')
                             print(correct)
                            
                            else:
                             incorrect += 1
                             print('incremented incorrect')
                             print(incorrect)  
                # take note of whether button_9 was clicked, so that next frame we know if clicks are new
                button_9.wasClicked = button_9.isClicked and button_9.status == STARTED
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=trial,
                    )
                    # skip the frame we paused on
                    continue
                
                # has a Component requested the Routine to end?
                if not continueRoutine:
                    trial.forceEnded = routineForceEnded = True
                # has the Routine been forcibly ended?
                if trial.forceEnded or routineForceEnded:
                    break
                # has every Component finished?
                continueRoutine = False
                for thisComponent in trial.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "trial" ---
            for thisComponent in trial.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for trial
            trial.tStop = globalClock.getTime(format='float')
            trial.tStopRefresh = tThisFlipGlobal
            thisExp.addData('trial.stopped', trial.tStop)
            # Run 'End Routine' code from code
            ended_routine_at = globalClock.getTime()
            
            if ended_routine_at - min_time_for_incorrect > started_routine_at:
                if response == None:
                    incorrect += 1
            #if globalClock.getTime() < total_time:
            #    print("Not enough time — repeating this trial")
            #    trials.thisTrialN -= 1
            #
            # store data for inner_loop (TrialHandler)
            inner_loop.addData('mouse.x', mouse.x)
            inner_loop.addData('mouse.y', mouse.y)
            inner_loop.addData('mouse.leftButton', mouse.leftButton)
            inner_loop.addData('mouse.midButton', mouse.midButton)
            inner_loop.addData('mouse.rightButton', mouse.rightButton)
            inner_loop.addData('mouse.time', mouse.time)
            inner_loop.addData('button_0.numClicks', button_0.numClicks)
            if button_0.numClicks:
               inner_loop.addData('button_0.timesOn', button_0.timesOn)
               inner_loop.addData('button_0.timesOff', button_0.timesOff)
            else:
               inner_loop.addData('button_0.timesOn', "")
               inner_loop.addData('button_0.timesOff', "")
            inner_loop.addData('button_1.numClicks', button_1.numClicks)
            if button_1.numClicks:
               inner_loop.addData('button_1.timesOn', button_1.timesOn)
               inner_loop.addData('button_1.timesOff', button_1.timesOff)
            else:
               inner_loop.addData('button_1.timesOn', "")
               inner_loop.addData('button_1.timesOff', "")
            inner_loop.addData('button_2.numClicks', button_2.numClicks)
            if button_2.numClicks:
               inner_loop.addData('button_2.timesOn', button_2.timesOn)
               inner_loop.addData('button_2.timesOff', button_2.timesOff)
            else:
               inner_loop.addData('button_2.timesOn', "")
               inner_loop.addData('button_2.timesOff', "")
            inner_loop.addData('button_3.numClicks', button_3.numClicks)
            if button_3.numClicks:
               inner_loop.addData('button_3.timesOn', button_3.timesOn)
               inner_loop.addData('button_3.timesOff', button_3.timesOff)
            else:
               inner_loop.addData('button_3.timesOn', "")
               inner_loop.addData('button_3.timesOff', "")
            inner_loop.addData('button_4.numClicks', button_4.numClicks)
            if button_4.numClicks:
               inner_loop.addData('button_4.timesOn', button_4.timesOn)
               inner_loop.addData('button_4.timesOff', button_4.timesOff)
            else:
               inner_loop.addData('button_4.timesOn', "")
               inner_loop.addData('button_4.timesOff', "")
            inner_loop.addData('button_5.numClicks', button_5.numClicks)
            if button_5.numClicks:
               inner_loop.addData('button_5.timesOn', button_5.timesOn)
               inner_loop.addData('button_5.timesOff', button_5.timesOff)
            else:
               inner_loop.addData('button_5.timesOn', "")
               inner_loop.addData('button_5.timesOff', "")
            inner_loop.addData('button_6.numClicks', button_6.numClicks)
            if button_6.numClicks:
               inner_loop.addData('button_6.timesOn', button_6.timesOn)
               inner_loop.addData('button_6.timesOff', button_6.timesOff)
            else:
               inner_loop.addData('button_6.timesOn', "")
               inner_loop.addData('button_6.timesOff', "")
            inner_loop.addData('button_7.numClicks', button_7.numClicks)
            if button_7.numClicks:
               inner_loop.addData('button_7.timesOn', button_7.timesOn)
               inner_loop.addData('button_7.timesOff', button_7.timesOff)
            else:
               inner_loop.addData('button_7.timesOn', "")
               inner_loop.addData('button_7.timesOff', "")
            inner_loop.addData('button_8.numClicks', button_8.numClicks)
            if button_8.numClicks:
               inner_loop.addData('button_8.timesOn', button_8.timesOn)
               inner_loop.addData('button_8.timesOff', button_8.timesOff)
            else:
               inner_loop.addData('button_8.timesOn', "")
               inner_loop.addData('button_8.timesOff', "")
            inner_loop.addData('button_9.numClicks', button_9.numClicks)
            if button_9.numClicks:
               inner_loop.addData('button_9.timesOn', button_9.timesOn)
               inner_loop.addData('button_9.timesOff', button_9.timesOff)
            else:
               inner_loop.addData('button_9.timesOn', "")
               inner_loop.addData('button_9.timesOff', "")
            # Run 'End Routine' code from code_2
            thisExp.addData("Number_correct", correct)
            thisExp.addData("Number_incorrect", incorrect)
            
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if trial.maxDurationReached:
                routineTimer.addTime(-trial.maxDuration)
            elif trial.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-5.000000)
            # mark thisInner_loop as finished
            if hasattr(thisInner_loop, 'status'):
                thisInner_loop.status = FINISHED
            # if awaiting a pause, pause now
            if inner_loop.status == PAUSED:
                thisExp.status = PAUSED
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[globalClock], 
                )
                # once done pausing, restore running status
                inner_loop.status = STARTED
        # completed 1.0 repeats of 'inner_loop'
        inner_loop.status = FINISHED
        
        # mark thisTrial as finished
        if hasattr(thisTrial, 'status'):
            thisTrial.status = FINISHED
        # if awaiting a pause, pause now
        if trials.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            trials.status = STARTED
        thisExp.nextEntry()
        
    # completed 300.0 repeats of 'trials'
    trials.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    # stop any playback components
    if thisExp.currentRoutine is not None:
        for comp in thisExp.currentRoutine.getPlaybackComponents():
            comp.stop()
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # run any 'at exit' functions
    for fcn in runAtExit:
        fcn()
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
