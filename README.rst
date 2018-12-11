.. -*- mode: rst -*-

.. image:: https://github.com/layerfMRI/Psychopy/blob/master/readme/icon.png
    :target: https://github.com/layerfMRI/Psychopy/blob/master/readme/icon.png
    :alt: Renzos simple Psychopy programs
    
These Programs are mostly optimices for application on a Mac laptop with an external projector. 


Setup 
======

Psychopy installation::

http://www.psychopy.org/installation.html
https://sourceforge.net/projects/psychpy/files/latest/download?source=files

Customizing Phsychopy::

Include Path of GeneralTools in Phsychopy→Perferences→General→paths:
    [u'absolutePathToGeneralToolsFolder']

The main File is: The file to run with Psychopy it “TappingWithTrTiming_Movie_d3.pyc”
The prompt text is given in: subfolder

Comment on frame rate (tapping frequency and flickering frequency)::
The frame rates of the different tapping frequencies. Are given on line 50. 
Note, he speed maxes out at arronf 0.3 Hz. I.h. any value above 30 will appear slower.

Fix for lost window::
Sometimes in mac the wondow is of screen:
t getit back on screen, 
1.) select the program in the task bar.
2.) in the top bar go to Window → zoom.

.. image:: https://github.com/layerfMRI/Psychopy/blob/master/readme/window_isgone.png
    :target: https://github.com/layerfMRI/Psychopy/blob/master/readme/window_isgone.png
    :alt: screenshot of zoomed window


