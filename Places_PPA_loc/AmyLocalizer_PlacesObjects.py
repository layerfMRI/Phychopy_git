""" Susan Wardle Feb 2020
# Places faces vs objects localizer
# written for PsychoPy 3.0.6 with Python-3
#task: 1 back

#code is *based on*
# Face-Scene 2020 on-off localizer
#made it so easy to change stim types!

NIH 3TB ######
BOLDscreen at end of scanning table
@ viewing distance 2.5m, 120 pix = 1 deg
BOLDscreen 15.9 x 9.0 deg visible area
#screenW=1920
#screenH=1080
#view distance = 2.5m
#active screen area: 698.4mm x 392.9mm 

NIH 7T ######
VPIXX projector (use VGA  with new laptop)
1920 x 1080 (so this code also works as for 3TB!)

TIMING:
320sec
160 TRs if TR=2s

whitebox version:: background is gray, but stimuli are on white background
show a white box inbetween stimuli so only stimuli change
this is because too bright to have whole screen as white in the scanner

june 1 2021-- added hide cursor

july 23 2021 -- added keypress buffer

february 2024 -- adapted to show Places vs Objects to localize PPA, scenes images
mainly from Meissner et al https://doi.org/10.1016/j.neuroimage.2019.02.025

""" 

# ===============================
# SETUP libraries

#psychopy
from psychopy import visual, core, event, logging, data, gui  # import some libraries from PsychoPy
from math import atan2, degrees

import numpy as np # nb can shorten name 
import numpy.matlib as npmat
import matplotlib.pyplot as plt
import random
import time

import os
import sys

import json #convert dict to str

import glob
# ===============================
# SETUP inital params

# ==== ~~ for testing ~~ ==== 
testMode=0 #if 1, can overwrite exisiting datafile (for TESTING), otherwise cannot (i.e. when collecting real data)
# ==== ~~ for testing ~~ ==== 
screenNum=1 #if multiple displays... nb: psychopy on a Mac cannot specify display screen, so have to MIRROR screens @ scanner

# ~~~~~~~~~~~~~~~~~~~~~t~~~~~~~~~~
# ===============================
# DEFINE which 2 categories of localizer stimuli to use
# (for easy changing / create new localizers)

exptname='AmyLocFacesObjects'

stim1='places'
stim2='objects'

#directory name (in 'stimuli' folder within this directory, or specify impath below)
stim1dir='100places'
stim2dir='100objects'

#directory that the above stimuli directories are in:
thisDir=os.getcwd()

print(thisDir)

imDir=thisDir+'/stimuli/'

#show this inbetween boxed stim so less flashing
whitebox=thisDir+'/stimuli/whitebox.tif'

ORIGstimsize=670 #in pixels, used for checking scaling by visual deg doesn't exceed original size of stim

# ===============================
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#3TBsetup: trigger and keys (same for 7T)
validKeys = ['r','g','b','y']
trigger = 't' #scanner trigger
tic = time.time()


# GUI

thisDir=os.getcwd()

gui = gui.Dlg(title=exptname)

gui.addField("Subject ID:", 'P00')
gui.addField("Run number:", 1)
gui.addField("Stim1 or Stim2 first (1 or 2):", 1)
gui.show()

subID= gui.data[0]
runNum = int(gui.data[1])
stimfirst = int(gui.data[2]) #1=stim1 first, 2= stim2 first
 
#check gui responses
if len(subID)==0:
    sys.exit('ERROR. Invalid subject ID entered')
else:
    print('CHECK: subject ID OK')

if isinstance(runNum,int):
    print('CHECK: run Number OK')
else:
	sys.exit('ERROR. Invalid runNumber entered (must be integer)')

if stimfirst == 1 or stimfirst == 2:
    print('CHECK: stimfirst number is OK (i.e. a 1 or a 2)')
else:
	sys.exit('ERROR. stimfirst number invalid (must be 1 or 2)')


# ===============================tttttttttttttttttttttttt

#localizer params
pixperdeg=120 #for 3TB BOLDscreen
stimSize=5*pixperdeg #5 deg
fixDuration=0 #16 seconds, both at start and end of run
numOnOffBlocks=5 #9 #complete on-off scene-face blocks
numBlocks=numOnOffBlocks*2 #scene or face blocks
stimDuration=1.0 #seconds each stim is shown
isi=0.5 #blank screen inbetween stim
numBlockStim=20 #how many stim in each category per block (scenes / faces)
blockDuration=30
numTaskTrials=numBlocks*2 #2 1-back trials per block

if stimSize>ORIGstimsize:
	sys.exit('ERROR. stimuli are requested at larger than actual size')

if stimfirst==1: #stim1 first
	blockList=npmat.repmat([1, 2],1, numOnOffBlocks)
elif stimfirst==2: #stim2 first
	blockList=npmat.repmat([2, 1],1, numOnOffBlocks)


# ===============================
# READ IN STIMULI

print(' #### LOADING STIMULI ...')

#nb listdir does not ignore any files starting with '.' and '..'
#s1List = os.listdir(imDir+stim1dir+'/')
#s2List = os.listdir(imDir+stim2dir+'/')

#this version to only read images
s1List = [f for f in os.listdir(imDir+stim1dir+'/') if (f.endswith(".jpg") or f.endswith(".tif"))]
s2List = [f for f in os.listdir(imDir+stim2dir+'/') if (f.endswith(".jpg") or f.endswith(".tif"))]
#shuffle the stimuli so always a different order
random.shuffle(s1List)
random.shuffle(s2List)

# ===============================
# WORK OUT 1-BACK TASK (and image order for each block)

stim1blocks=[]
imcnt=0
for b in range(numOnOffBlocks):
	stim1ims=[]
	for r in range(numBlockStim-2):
		stim1ims.append(s1List[imcnt])
		imcnt=imcnt+1 #image counter
#insert duplicate items from repeats list
	r1=random.randint(0,8)
	r2=random.randint(9,17)
	print(r1)
	print(r2)
	#insert first repeat
	stim1ims.insert(r1,stim1ims[r1])
	stim1ims.insert(r2+1,stim1ims[r2+1])
	stim1blocks.append(stim1ims)
print(stim1blocks)
#flatten the list using crazy python notation...
stim1imlist = [val for sublist in stim1blocks for val in sublist]
print(stim1imlist)

stim2blocks=[]
imcnt=0
for b in range(numOnOffBlocks):
	stim2ims=[]
	for r in range(numBlockStim-2):
		stim2ims.append(s2List[imcnt])
		imcnt=imcnt+1 #image counter
#insert duplicate items from repeats list
	r1=random.randint(0,8)
	r2=random.randint(9,17)
	print(r1)
	print(r2)
	#insert first repeat
	stim2ims.insert(r1,stim2ims[r1])
	stim2ims.insert(r2+1,stim2ims[r2+1])
	stim2blocks.append(stim2ims)
#flatten the list using crazy python notation...
stim2imlist = [val for sublist in stim2blocks for val in sublist]
print(stim2imlist)


# ===============================
# WINDOW 

#create a window 
#win = visual.Window(monitor="susanLab", units="pix", fullscr=True, allowGUI=False, screen=screenNum)
win = visual.Window(monitor="NIH3TB", size=(1920,1080), units="pix", fullscr=True, allowGUI=False, screen=screenNum,color=(0, 0, 0))
#win.mouseVisible=False
#check refresh rate
#refresh_rate=win.getActualFrameRate(nIdentical=10, nMaxFrames=100, nWarmUpFrames=10, threshold=1)
#print refresh_rate
#sys.exit('check')

#opened a full screen, can query window size
winW= win.size[0]
winH= win.size[1]

#crossCol=[0, 1, 1] #cyan
crossCol=[-1, -1, -1] #black
crossContrast=1 #0.7
fixdetectcol=[1, 1, 1] #cross turns white for detection task
crossLength=24 #pixels? or 0.5 deg
crossPenWidth=7

# fixation cross
fix = visual.ShapeStim(win, 
    vertices=((0, -crossLength), (0, crossLength), (0,0), (-crossLength,0), (crossLength, 0)),
    lineWidth=crossPenWidth,
    closeShape=False,
    lineColor=crossCol,
    contrast=crossContrast, units='pix'
)

# SETUP text messages
screentext=visual.TextStim(win, text='Hello World', font='', pos=(0.0, 0.0), depth=0, rgb=None, color=(1.0, 1.0, 1.0), \
colorSpace='rgb', opacity=1.0, contrast=1.0, units='norm', ori=0.0, height=0.07, antialias=True, bold=False, italic=False, \
alignHoriz='center', alignVert='center', fontFiles=(), wrapWidth=None, flipHoriz=False, flipVert=False, name=None, autoLog=None) \


#initalize (interpolate=True is important for resizing images)
stim=visual.ImageStim(win,image=None, size=(stimSize,stimSize), mask=None, pos=(0,0),units='pix',interpolate=True)

wbox=visual.ImageStim(win,image=whitebox, size=(stimSize,stimSize), mask=None, pos=(0,0),units='pix',interpolate=True)

# ===============================
# instructions screen
#this version shows instructions and will ignore all 't's so can keep scanner cable plugged in

print('press spacebar to continue')

screentext.text='Please fixate on the cross\n\nWhenever you see the same image twice in a row, press a key\n\n\n\n(experimenter: press spacebar)'
screentext.draw()
win.flip()

#wait for space so scanner doesn't trigger early!
event.waitKeys(keyList=['space']) 
#clear key buffer
event.clearEvents(eventType=None)

# start screen
screentext.text='Waiting for scanner (t)...'
screentext.draw()
win.flip()

#hide cursor
win.mouseVisible = False

# ===============================
# create DATA DIR, TEXT FILE for saving data

#thisDir=os.getcwd()
dataDir='./data/'

# see if data dir already exists, if not, make it
if not os.path.exists(dataDir):
    os.makedirs(dataDir)

expInfo = {'observer':subID, 'expName':exptname, 'runNum':runNum,'stim1':stim1,'stim2':stim2, 'whichstim_first':stimfirst, 'winW':float(winW), 'winH':float(winH)}
expInfo['dateStr'] = data.getDateStr()  # add the current time

# make a text file to save data
fileName = dataDir + exptname + '_' + expInfo['observer'] + '_run' + str(expInfo['runNum']) + '.tsv'

# check data file doesnt exist, quit if it does
data_path_exists = os.path.exists(fileName)
if data_path_exists:
	if testMode== 1:
		print('******* WARNNING. data file exists but is being overwritten because testMode==1! Did you mean to do this?')
	else:
		sys.exit("ERROR. Filename " + fileName + " already exists!")
else:
    print('data file OK')

dataFile = open(fileName, 'a')  # a simple text file, tab delim

#write whole dict to file?
dataFile.write('ExpInfo\n')
dataFile.write(json.dumps(expInfo))
dataFile.write('\n\n')
dataFile.write('\nstim1:\t')
dataFile.write(stim1)
dataFile.write('\nstim2:\t')
dataFile.write(stim2)
dataFile.write('\nstimSize:\t')
dataFile.write(str(stimSize)) 
dataFile.write('\nfixDuration:\t')
dataFile.write(str(fixDuration))
dataFile.write('\nstimDuration:\t')
dataFile.write(str(stimDuration)) 
dataFile.write('\nisi:\t')
dataFile.write(str(isi))
dataFile.write('\nblockDuration:\t')
dataFile.write(str(blockDuration)) 
dataFile.write('\nnumBlockStim:\t')
dataFile.write(str(numBlockStim))
dataFile.write('\nnumBlocks:\t')
dataFile.write(str(numBlocks))
dataFile.write('\nnumTaskTrials:\t')
dataFile.write(str(numTaskTrials))
dataFile.write('\n\n')
dataFile.write('\nblockNum\tstim1(1)/stim2(2)\tblockStart\tblockEnd\tkey1\tkey1time\tkey2\tkey2time\tnumCorrect(/2)\n')
dataFile.close()

    
# ===============================
# SCANNER trigger starts GLOBAL clock

while 1:
    pressed=event.getKeys(keyList=trigger, modifiers=False, timeStamped=False) #nb add the globalclock to timestamp
    if pressed:
        Gclock = core.MonotonicClock() # Unlike the Clock this cannot be reset to arbitrary times. 
        win.flip() #clear screen
        break

# ===============================
# TRIAL LOOP


# #use the intial fix time to wait until the start of a TR before starting the code! (e.g. for TR=2sec, will work if fixDuration is multiple of 2)
while Gclock.getTime() < fixDuration: #use global clock to start exactly on TR
    fix.draw()
    win.flip()


#Sclock = core.Clock() #stimulus clock

#initialize params
s1cnt=0
s2cnt=0
tally=0
laststim=[]
ncorrect=0
data=[]
imlist=[]
keylist=[]
Sclock = core.Clock() #stimulus clock
for t in range(numBlocks):

	key=[0, 0] #rest responses
	keytime=[0, 0]
	tally=0
	bStart=Gclock.getTime() 

	for im in range(numBlockStim):

		flag=0 #for recording each image onset
		waitresp=0 #only record first keypress made to each image (prevents multiples)
		Sclock.reset() #set clock to 0
		#IMAGE
		while Sclock.getTime() < stimDuration: #use local stimulus clock to control stim presentation time
		#while Gclock.getTime() < fixDuration+(t*blockDuration)+(stimDuration*(im))+(isi*(im))+stimDuration: #use local stimulus clock to control stim presentation time
			if flag==0:
				if blockList[0,t]==1:
					stim.image=imDir+stim1dir+'/'+stim1imlist[s1cnt]
					s1cnt=s1cnt+1 # image counter
				elif blockList[0,t]==2:
					stim.image=imDir+stim2dir+'/'+stim2imlist[s2cnt]
					s2cnt=s2cnt+1 # image counter
				stim.draw()
				Sclock.reset() #set clock to 0 again.. find that missing 50ms!
				win.flip()
				imstart=Gclock.getTime()
				flag=1
				
			pressed=event.getKeys(keyList=validKeys, modifiers=False, timeStamped=Gclock) #nb add the globalclock to timestamp
			for thisKey in pressed:
				keylist.append([thisKey[0],thisKey[1]])
				if stim.image == laststim: #if this stim is repeated
					if waitresp == 0:
						key[tally]=thisKey[0]
						keytime[tally]=thisKey[1]
						tally=tally+1
						waitresp = 1
				event.clearEvents(eventType=None) #clear any pressed keys
		wbox.draw()
		win.flip() #clear screen
		imlist.append([stim.image,imstart,Gclock.getTime()])
		#ISI INBETWEEN IMAGES
		while Gclock.getTime() < fixDuration+(t*blockDuration)+(stimDuration*(im+1))+(isi*(im+1)): #use global clock to prevent timing slip, recover time in blank
			#fix.draw()
			wbox.draw()
			win.flip()
			#check for 1-back response
			pressed=event.getKeys(keyList=validKeys, modifiers=False, timeStamped=Gclock) #nb add the globalclock to timestamp
			for thisKey in pressed:
				keylist.append([thisKey[0],thisKey[1]])
				if stim.image == laststim: #if this stim is repeated
					if waitresp == 0:
						key[tally]=thisKey[0]
						keytime[tally]=thisKey[1]
						tally=tally+1
						waitresp = 1
				event.clearEvents(eventType=None) #clear any pressed keys

		#inbetween stim and isi
		laststim=stim.image #store this image as the last stimulus for 1-back task response coding
		#print(laststim)

	bEnd=Gclock.getTime()
	ncorrect=ncorrect+tally
	data.append([t, blockList[0,t], bStart, bEnd, key[0], keytime[0], key[1], keytime[1], tally])
    


#save data at end of run
dataFile = open(fileName, 'a') #need to reopen file to write again
np.savetxt(
dataFile,
data,
fmt='%s',
delimiter="\t")
print('data saved')
dataFile.close()


#end fixation time
while Gclock.getTime() < fixDuration+(t*blockDuration)+blockDuration+fixDuration: #use global clock to start exactly on TR
	fix.draw()
	win.flip()
endFixEnd=Gclock.getTime()

#save task
percorrect=(ncorrect/numTaskTrials*1.0)*100

dataFile = open(fileName, 'a') #need to reopen file to write again
dataFile.write('\n\nEND FIXATION TIME (END OF EXPERIMENT):\t')
dataFile.write(str(endFixEnd)) 
dataFile.write('\n\nTASK tally correct:\t')
dataFile.write(str(ncorrect)) 
dataFile.write('\n\nTASK percent correct:\t')
dataFile.write(str(percorrect)) 
dataFile.write('\n\nTOTAL NUMBER OF KEYPRESSES (36 trials):\t')
dataFile.write(str(len(keylist))) 

dataFile.write('\n\nALL images: order and onset timestamps:\n')
np.savetxt(
dataFile,
imlist,
fmt='%s',
delimiter="\t")
print('data saved')

dataFile.write('\n\nSTIM1 image order:\n')
np.savetxt(
dataFile,
stim1imlist,
fmt='%s',
delimiter="\t")
print('data saved')

dataFile.write('\n\nSTIM2 image order:\n')
np.savetxt(
dataFile,
stim2imlist,
fmt='%s',
delimiter="\t")
print('data saved')

dataFile.write('\n\nALL keypresses:\n')
np.savetxt(
dataFile,
keylist,
fmt='%s',
delimiter="\t")
print('data saved')

print('TOTAL NUMBER OF KEYPRESSES (36 trials):')
print(len(keylist))

dataFile.close()


# end screen
screentext.text='Percent correct: %0.2f %%\nThis run is finished! :)\nPress a key to exit' %(percorrect)
screentext.color=(1,1,1)
screentext.draw()
win.flip()
event.waitKeys() #wait for keypress


#clean up
win.close()
core.quit()
