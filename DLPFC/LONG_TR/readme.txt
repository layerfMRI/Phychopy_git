Version fom Dec. 5th 2017
go it from Emily 
Dave wrote most of first version?!?
All of the new changes are from Emily, I think

Instructions to me are below

///it uses 12345 as input parameters

(“LetterOrderTask_d5.py”) is for the DLPFC task

The files BasicPromptTools.py and LetterOrderPrompts_5button.txt need to be in a subfolder called “Prompts” (of the directory you run the .py script from).
 
There are two parameter files: one to do the 6 min functional localizer of 10 s ON, 10 s OFF (“LetterOrder_6mLOC.pickle”) and one to do the full experimental run (“LetterOrder_20trialRUN.pickle”).
 
The script will give you the option to load one of these existing parameter files at the start of each run. The only thing you should need to modify prior to running are lines 29 and 33:
 
Line 29:
True if doing localizer, False otherwise
 
Line 33:
alphaVsRemem = True # this means the script will do 10 REMEM trials and 10 ALPHA trials, with all being GO (output) trials
alphaVsRemem = False # this means the script will do 10 go (output) trials and 10 no-go (no output) trials, with all being ALPHA trials
 
For the 20 trial RUN, each trial is 32s long as we discussed, and there is an 8-sec warm up at the beginning and 8-sec cool down at the end, so the total run length is 656 s, or 10m56s.
 

A couple of reminders, just so you have this in one place:
 
- Plug in 5-button stick
- Make sure silver box is set to ‘12345’ (not ‘BGYRT’)
- The side button (where the subject’s thumb is) corresponds to position 1, index finger = 2, middle finger = 3, ring finger = 4 and pinkie = 5 (logged as a ‘6’ since the TTL pulse is 5)
- General instructions: “You will see a sequence of five letters, such as ‘BDCEA’. Then the sequence will disappear from the screen, and you will get a cue that says either REMEMBER or ALPHABETIZE. If the cue is REMEMBER, your task is just to remember the letters in the order you saw them. If the cue is ALPHABETIZE, your task is to rearrange the letters into alphabetical order in your head (so, in this case, ‘ABCDE’). After about 10 seconds you will get a prompt asking you to give the position of one of the letters you saw. So for example, ‘D?’ In this example, in an ALPHABETIZE trial, D would be in the fourth position, so you would respond by pressing button 4. If it had been a REMEMBER trial, D was in the second position, so you would respond by pressing button 2.”
 
Now that we’ve split the contrasts into separate runs, it probably makes sense to give more run-specific instructions depending on whether you are doing the ALPHA vs REMEM contrast or the GO vs NOGO contrast.
 
For the localizer, you can say:
“We’re going to do six minutes’ worth of trials that will be all ALPHABETIZE and will require you to make a response on every trial.”
 
For the ALPHA vs REMEM contrast, you can say:
“We’re going to do 11 minutes’ worth of trials, some will be REMEMBER and others will be ALPHABETIZE, so make sure you pay attention to the cue given right after the letter string. You will need to make a response on all of these.”
 
For the GO vs NOGO:
“We’re going to do 11 minutes’ worth of trials. All of these will be ALPHABETIZE, but you will only need to make a response on some of them. If you see an asterisk-question mark, that means you don’t have to make a response, and you can forget the sequence and move on to the next trial.”