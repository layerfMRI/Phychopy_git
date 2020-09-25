# User Psychopy3 for this
from __future__ import division
from __future__ import print_function

from psychopy import visual, core, event

#win = visual.Window([1024,768])
# the screen refers to which monitor is used to show the movie
# is was win = visual.Window([1024,768],fullscr=False,allowGUI=False,monitor='testMonitor',screen=0)
win = visual.Window([1536,1152],fullscr=False,allowGUI=False,monitor='testMonitor',screen=0)
# use nosound.mkv if youy want it to run withiout errors
#it was mov = visual.MovieStim3(win, 'withsound.mp4', size=[1024,720],   
mov = visual.MovieStim3(win, 'withsound.mp4', size=[1536,1080],   
                       flipVert=False, flipHoriz=False, loop=False)
#print 'orig movie size=[%i,%i]' %(mov.format.width, mov.format.height)
#print 'duration=%.2fs' %(mov.duration)
print('orig movie size=%s' % mov.size)
print('duration=%.2fs' % mov.duration)
globalClock = core.Clock()


msg1 = visual.TextStim(win, text=u"Please do not move! ",height=100,units='pix',name='intro', color='black',wrapWidth=600,pos=(0,0))  # default position = centered
msg1.draw()
win.flip()

event.waitKeys(keyList=['return','t']);                                                                   # Wait for Scanner Trigger.


while mov.status != visual.FINISHED:
    mov.draw()
    win.flip()
    if event.getKeys(keyList=['escape','q']):
        win.close()
        core.quit()

core.quit()

"""Different systems have different sets of codecs.
avbin (which PsychoPy uses to load movies) seems not to load compressed audio on all systems.
To create a movie that will play on all systems I would recommend using the format:
    video: H.264 compressed,
    audio: Linear PCM
"""
