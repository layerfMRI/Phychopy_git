#!t/usr/bin/envt pythonwn
from psychopy import sound, core, visual, event, gui, logging, prefs
#Renzo setup for first ecperimenteeeenbegqr
import time
import datetime
import os
import numpy
import string

import AppKit

print('Using %s (with %s) for sounds' % (sound.audioLib, sound.audioDriver))

def screenRes(myScreen):
    screens = AppKit.NSScreen.screens() # get list of screen objects
    screenRes = (int(screens[myScreen].frame().size.width), int(screens[myScreen].frame().size.height))
    #screenRes = [800,600]
    #print "screenRes = [%d,%d]"%screenRes 
    return screenRes

# Default Definitions
screen_to_show = 0 # Choose monitor [0 = Laptop | 1 = Second Monitor]
triggerKey     = 't'
exitKey        = 'q'
useEyeTracker  = True
doCalibration  = True
autoScreenSize = True
outputPrefix   = 'output'
numTrials=48                                              #Number of trials of stimulation+rest blocks
bufferDur=0                                              #Duration of additional fixation period immediately after scan starts and following last rest block [TRs]
visStimDur=12                                           #Duration of flickering checkerboard blocks
restDur=12

defaultScreenRes = [800,600]
# Ask user
myFields  = {'Monitor':['External','Laptop'],'Auto Screen Size Detection':['Yes','No'],'Log Prefix':outputPrefix,'Trigger':triggerKey,'Numer of trials':numTrials,'initial rest [TR]':bufferDur,'rest dur [TR]':restDur,'activity dur [TR]':visStimDur}
configDlg = gui.DlgFromDict(dictionary=myFields, title='Run Configuration',order=['Monitor','Auto Screen Size Detection','Log Prefix','Trigger'])
if (configDlg.OK==False):
    print ('User Cancelled')
    core.quit()
# Import visual here to avoid silly issue with GUI not selecting drop list options properly
from psychopy import visual
from psychopy.visual import DotStim

# Read values from the user GUI
if myFields.get('Monitor')=='Laptop':
    screen_to_show=0
else:
    screen_to_show=0

screenSize=[0,0]
if myFields.get('Auto Screen Size Detection')=='No':
    autoScreenSize = False
    screenSize     = defaultScreenRes
else:
    autoScreenSize = True
    screenSize = screenRes(screen_to_show)

outputPrefix = myFields.get('Log Prefix')
triggerKey   = myFields.get('Trigger')


numTrials= myFields.get('Numer of trials')
bufferDur= myFields.get('initial rest [TR]')
restDur=myFields.get('rest dur [TR]')
visStimDur=   myFields.get('activity dur [TR]')


# Print Selection
print ("Selected Monitor: %i" % (screen_to_show))
print ("Auto Screen Size Detection (True/False): %s" % (str(autoScreenSize)))
print ("Screen Size: (%i,%i)" % (screenSize[0],screenSize[1]))

# Create Log File
LogFileName='./ResponseLogs/'+outputPrefix+'_ResponseLog.txt';
Logger=logging.LogFile(LogFileName,34,'w');

params = {'portName': '/dev/tty.usbserial', 'portBaud': 115200, 'screenColor': (0,0,0), 'textColor': (255,255,255), 'screenSize':screenRes, 'screen_to_show':screen_to_show}
print (params)


# CREATE SCREEN
# ================
win=visual.Window([screenSize[0],screenSize[0]],fullscr=False,allowGUI=False,monitor='testMonitor',screen=screen_to_show,units='pix');

# STIMULI PARAMETERS
#=========================
stimA = visual.RadialStim(win,tex="sqrXsqr", ori=0, color=1, mask="none",units='deg',pos=(0,0),texRes=256,angularRes=200,
           size=[100,100], visibleWedge=[0, 360], radialCycles=35, angularCycles=12,name='stimA')
stimAInt=visual.RadialStim(win,tex="sqrXsqr", ori=0, color=1, mask="none",units='deg',pos=(0,0),texRes=256,angularRes=200,
           size=[20,20], visibleWedge=[0, 360], radialCycles=10, angularCycles=12,name='stimAInt')
stimACent=visual.RadialStim(win,tex="sqrXsqr", ori=0, color=1, mask="none",units='deg',pos=(0,0),texRes=256,angularRes=200,
           size=[8,8], visibleWedge=[0, 360], radialCycles=6, angularCycles=12,name='stimAInt')
stimB = visual.RadialStim(win,tex="sqrXsqr", ori=0, color=-1, mask="none",units='deg',pos=(0,0),texRes=256,angularRes=200,
           size=[100,100], visibleWedge=[0, 360], radialCycles=35, angularCycles=12,name='stimB')
stimBInt=visual.RadialStim(win,tex="sqrXsqr", ori=0, color=-1, mask="none",units='deg',pos=(0,0),texRes=256,angularRes=200,
           size=[20,20], visibleWedge=[0, 360], radialCycles=10, angularCycles=12,name='stimAInt')
stimBCent=visual.RadialStim(win,tex="sqrXsqr", ori=0, color=-1, mask="none",units='deg',pos=(0,0),texRes=256,angularRes=200,
           size=[8,8], visibleWedge=[0, 360], radialCycles=6, angularCycles=12,name='stimAInt')

flashRate = 0.125                                               #Frequency of flicker in seconds (i.e. 8 Hz = 0.125 s)

xhr = visual.ShapeStim(win,lineColor='#000000',lineWidth=3.0,vertices=((-30,0),(30,0),(0,0),(0,30),(0,-30)),units='pix',closeShape=False,name='rest');

# ===========                INSTRUCTIONS                    ==============
# ==============================================================

Instr_Rest_T='experiment will start shortly';
Instr_Rest_GRAPPA= 'do\'t move for a moment';
Instr_Rest_GRAPPA1= 'GRAPPA ref line acq';
Instr_Rest_WAIT= 'initial buffer'; # for initial rest
Instr_RELAX='RELAXING';
Instr_FLEX='listen to the sound';
Instr_EXTE='right pinky finger tapping';


#Instr_RELAX='left INDEX FINGER';
#Instr_TAP='left MIDDLE FINGER';
#Instr_TAP1='left RING FINGER';
#Instr_TAP2='left LITTLE FINGER';
Instr_DONE='Finished \nThank you';


Instr_Rest_S=visual.TextStim(win,text=Instr_Rest_T,height=50,units='pix',name='intro', color='black',wrapWidth=600,pos=(0,0));
Instr_Rest_GRAPPA=visual.TextStim(win,text=Instr_Rest_GRAPPA,height=50,units='pix',name='intro', color='black',wrapWidth=600,pos=(0,0));
Instr_Rest_GRAPPA1=visual.TextStim(win,text=Instr_Rest_GRAPPA1,height=10,units='pix',name='intro', color='black',wrapWidth=600,pos=(0,-100));
Instr_Rest_WAIT=visual.TextStim(win,text=Instr_Rest_WAIT,height=10,units='pix',name='intro', color='black',wrapWidth=600,pos=(0,-100));
Instr_FLEX=visual.TextStim(win,text=Instr_FLEX,height=100,units='pix',name='intro', color='black',wrapWidth=600,pos=(0,0));
Instr_EXTE=visual.TextStim(win,text=Instr_EXTE,height=100,units='pix',name='intro', color='black',wrapWidth=600,pos=(0,0));
Instr_RELAX=visual.TextStim(win,text=Instr_RELAX,height=100,units='pix',name='intro', color='black',wrapWidth=600,pos=(0,0));
Instr_DONE=visual.TextStim(win,text=Instr_DONE,height=100,units='pix',name='intro', color='black',wrapWidth=600,pos=(0,0));



Instr_Rest_Window=visual.Rect(win,width=300,height=200,pos=(0,-90),lineColor='black',lineWidth=3);
Instr_Rest_Crosshair=visual.ShapeStim(win,lineColor='#000000',lineWidth=3.0,vertices=((-30,-90),(30,-90),(0,-90),(0,-60),(0,-120)),units='pix',closeShape=False);

# SETTING GENERAL CLOCK AND LOGGING
# =========================================
clock=core.Clock();
logging.setDefaultClock(clock)                                                               #use this for timing of log messages, although these shouldn't be used for experimental events
logging.console.setLevel(logging.DATA)                                            #set the console to receive nearly all messges
Logger=logging.LogFile(LogFileName,logging.DATA,'w');
win.setRecordFrameIntervals(True);                                                  #capture frame intervals
win.saveFrameIntervals(fileName=LogFileName, clear=False);          #write frame intervals to LogFileName

# (0) PRINT FIRST SET OF INSTRUCTIONS AND WAIT FOR TRIGGER
# ==================================================================
win.logOnFlip('INITIAL INSTRUCTIONS',logging.DATA);

Instr_Rest_S.draw();win.flip();                                                                 # Plot Instructions.
event.waitKeys(keyList=['return','t']);                                                                   # Wait for Scanner Trigger.

Instr_Rest_GRAPPA.draw();Instr_Rest_GRAPPA1.draw();win.flip();  

event.waitKeys(keyList=['t']);
clock.reset();
Exp_Start_Time=clock.getTime();                                                           # Record Scanning State Time


# prepare sound stuff
#if prefs.general['audioLib'][0] == 'pyo':
    #if pyo is the first lib in the list of preferred libs then we could use small buffer
    #pygame sound is very bad with a small buffer though
#t   sound.init(48000,buffer=128)
#print ('Using %s(with %s) for sounds' %(sound.audioLib, sound.audioDriver))

#highA = sound.Sound('A',octave=3, sampleRate=44100, secs=2, bits=8)
#highA.setVolume(0.8)
#tick = sound.Sound(800,secs=0.1,sampleRate=44100, bits=8)#sample rate ignored because already set
#tock = sound.Sound('600',secs=0.1, sampleRate=44100)
gerauesch = sound.Sound('/Users/administrator/Git/Phychopy_git/Tapping_withTR_sound/file-2_2p25.wav')




# BEGIN EXPERIMENT
#=====================
numbtrigger=0

while numbtrigger<bufferDur:
    for keys in event.getKeys(timeStamped=True):            #handle key presses each frame
        if keys[0]in ['escape','q']:
            win.close()
            core.quit()
    Instr_RELAX.draw();Instr_Rest_WAIT.draw();win.flip();
    event.waitKeys(keyList=['t'])
    numbtrigger=numbtrigger+1


#xhr.setAutoDraw(True);                                                                          #Draw the crosshair every time the screen flips
#xhr.draw();
#win.flip();
#win.logOnFlip('[Starting Buffer] starts FRAME TIME = {0}'.format(win.lastFrameT),logging.DATA);
#count=0

numbtrigger=0
numbtrials=0


while numbtrials<numTrials:
    numbtrials=numbtrials+1
    numbtrigger=0
    while numbtrigger<restDur:
        for keys in event.getKeys(timeStamped=True):            #handle key presses each frame
            if keys[0]in ['escape','q']:
                win.close()
                core.quit()
        Instr_RELAX.draw();win.flip();
        event.waitKeys(keyList=['t'])
        numbtrigger=numbtrigger+1
    numbtrigger=0
    while numbtrigger<restDur:
        for keys in event.getKeys(timeStamped=True):            #handle key presses each frame
            if keys[0]in ['escape','q']:
                win.close()
                core.quit()
        Instr_FLEX.draw();win.flip();
        
        gerauesch.stop()
        gerauesch.play()
        core.wait(0.1)
        
        event.waitKeys(keyList=['t'])
        numbtrigger=numbtrigger+1



#for i in range(numTrials):
#    elapsedTime=elapsedTime+visStimDur;
#    win.flip();
#    win.logOnFlip('[Stim Block {0}] starts FRAME TIME = {1}'.format(i,(win.lastFrameT)),logging.DATA);

#    while clock.getTime()<elapsedTime:                                #Block of flickering checkerboard
#        t=clock.getTime()
#        if (t%flashRate) < (flashRate/2.0):
#            displayStim1 = stimA
#            displayStim2 = stimAInt
#            displayStim3 = stimACent
#        else:
#            displayStim1 = stimB
#            displayStim2 = stimBInt
#            displayStim3 = stimBCent
#        displayStim1.draw()
#        displayStim2.draw()
#        displayStim3.draw()
#        win.flip()
        
#        for keys in event.getKeys(timeStamped=True):            #handle key presses each frame
#            if keys[0]in ['escape','q']:
#                win.close()
#                core.quit()
    


win.flip()
win.close()
core.quit()
