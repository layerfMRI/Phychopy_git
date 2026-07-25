
#!t/usr/bin/envt pythonwn
from psychopy import sound, core, visual, event, gui, logging, prefs, data
import time
import datetime
import os
import numpy
import string
import pandas as pd

_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session 
psychopyVersion = '2022.2.5'
expName = 'hippo_am-ma'
expInfo = {
    'participant': '001',
    'run': '1',
}

# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel ttq
expInfo['date'] = data.getDateStr()
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etcyyyyyyy
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
log = logging.LogFile(filename+'.log', level=logging.EXP)

win = visual.Window(
    size=[1512, 982], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False

# Default Definitions
outputPrefix = 'output'
numTrials = 30 # number of trials of stimulation+rest block repeats (max 44 per run!)
bufferDur = 0 # duration of additional fixation after scan starts, before first task block [TR]
taskDur = 6 # task block duration [TR]
#respDur = 2 # response block duration [TR]
restDur = 6 # rest block duration [TR]
# run duration: (bufferDur+restDur+num_trials*(taskDur+restDur))*TR/60.
# with current settings and 3s TR -> 10.35min

runFile = 'run%d.csv'%(int(expInfo['run'])) # run options 1,2,3,4
df_run = pd.read_csv(runFile)
block_type_list = list(df_run.block_type)
block_stim_list = []
resp_stim_list = []
for i in range(0,numTrials,1):
     block_stim_list.append(visual.TextStim(win,text=df_run['vis_stim'].iloc[i],height=50,units='pix',name='task_trial%d'%(i+1),color='black',wrapWidth=600,pos=(0,0)));
     if df_run['block_type'].iloc[i] == 'am':
         str = 'vague or vivid?'
     else:
         str = 'easy or difficult?'
     resp_stim_list.append(visual.TextStim(win,text=str,height=50,units='pix',name='resp_trial%d'%(i+1),color='black',wrapWidth=600,pos=(0,0)));

fix0 = visual.TextStim(win=win, name='fix0',
    text='+',
    font='Open Sans',
    units='cm', pos=(0, 0), height=1.5, wrapWidth=None, ori=0.0, 
    color=[0.6549, 0.6549, 0.6549], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
 
fix1 = visual.TextStim(win=win, name='fix1',
    text='+',
    font='Open Sans',
    units='cm', pos=(0, 0), height=1.5, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

clock=core.Clock();
logging.setDefaultClock(clock)                                                               #use this for timing of log messages, although these shouldn't be used for experimental events
logging.console.setLevel(logging.DATA)                                            #set the console to receive nearly all messges
# Logger=logging.LogFile(LogFileName,logging.DATA,'w');

fix0.draw();
win.flip();
event.waitKeys(keyList=['t'])
# clock.reset();
Exp_Start_Time=clock.getTime();                                                           # Record Scanning State Time


# BEGIN EXPERIMENT
#=====================

# initial buffer
numbtrigger=0
while numbtrigger<bufferDur:
    win.logOnFlip(level=logging.EXP, msg='buffer')
    for keys in event.getKeys(timeStamped=True):            #handle key presses each frame
        if keys[0] in ['escape','q']:
            win.close()
            core.quit()
    fix0.draw();
    win.flip();
    event.waitKeys(keyList=['t'])
    numbtrigger=numbtrigger+1

# rest block
numbtrigger=0
while numbtrigger<restDur:
    win.logOnFlip(level=logging.EXP, msg='rest')
    for keys in event.getKeys(timeStamped=True):            #handle key presses each frame
        if keys[0] in ['escape','q']:
            win.close()
            core.quit()
    fix1.draw();
    win.flip();
    event.waitKeys(keyList=['t'])
    numbtrigger=numbtrigger+1

for i in range(numTrials):
    # task block
    numbtrigger=0
    while numbtrigger<taskDur:
        win.logOnFlip(level=logging.EXP, msg='task %s'%(block_type_list[i]))
        for keys in event.getKeys(timeStamped=True):            #handle key presses each frame
            if keys[0] in ['escape','q']:
                win.close()
                core.quit()
        block_stim_list[i].draw();
        win.flip();
        event.waitKeys(keyList=['t'])
        numbtrigger=numbtrigger+1

    # resp block
    #numbtrigger=0
    #while numbtrigger<respDur:
    #    win.logOnFlip(level=logging.EXP, msg='resp %s'%(block_type_list[i]))
    #    for keys in event.getKeys(timeStamped=True):            #handle key presses each frame
    #        if keys[0] in ['escape','q']:
    #            win.close()
    #            core.quit()
    #    resp_stim_list[i].draw();
    #    win.flip();
    #    event.waitKeys(keyList=['t'])
    #    numbtrigger=numbtrigger+1

    # rest block
    numbtrigger=0
    while numbtrigger<restDur:
        win.logOnFlip(level=logging.EXP, msg='rest')
        for keys in event.getKeys(timeStamped=True):            #handle key presses each frame
            if keys[0] in ['escape','q']:
                win.close()
                core.quit()
        fix1.draw();
        win.flip();
        event.waitKeys(keyList=['t'])
        numbtrigger=numbtrigger+1
    
win.flip()
win.close()
core.quit()
