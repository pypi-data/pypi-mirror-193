import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import h5py
import cv2 as cv
import random

from stimugenerator import visualization
from stimugenerator import dataIO

videoPath = "../data/mouse_footage/"
videoName = "20180713_13_1.h5"
movie = dataIO.read_movie_from_h5(videoPath+videoName)
lenMovie = len(movie)

# button section
bt_bottom_pos = 0.002
bt_width = 0.1
bt_height = 0.025

# (fast) for/back-ward stepsize
smallStep = 1
bigStep = 10
# declaration
global frameNr
global saveClip
global crop_x
global crop_y
# manuelly reset everytime the program crashes -> find out why it crashes/gets slower
reStartIndex = 0
frameNr = reStartIndex

plt.rcParams["figure.figsize"] = [7.50, 7.50]
plt.rcParams["figure.autolayout"] = True
plt.rcParams["xtick.labelsize"] = 8
plt.rcParams["ytick.labelsize"] = 8


fig = plt.figure(constrained_layout=True, figsize=(16, 8))
subfigs = fig.subfigures(1,2)

# the left panel
axLeft = subfigs[0].subplots()
axLeft.imshow(visualization.img_real2view(movie[frameNr][...,::-1]))
axLeft.set_title("Frame "+str(frameNr)+"/"+str(lenMovie),fontsize = 10)

axRight = subfigs[1].subplots(3,5)
axRight = axRight.flatten()
for each in axRight:
    each.axis("off")

fastBackwardAx = subfigs[0].add_axes([0.1, bt_bottom_pos, bt_width, bt_height])
fbw_bt = Button(fastBackwardAx, color = "red",label='-10')

backwardAx = subfigs[0].add_axes([0.25, bt_bottom_pos, bt_width, bt_height])
bw_bt = Button(backwardAx, color = "red",label='-1')

forwardAx = subfigs[0].add_axes([0.6, bt_bottom_pos, bt_width, bt_height])
fw_bt = Button(forwardAx, color = "green",label='+1')

fastForwardAx = subfigs[0].add_axes([0.75, bt_bottom_pos, bt_width, bt_height])
ffw_bt = Button(fastForwardAx, color = "green",label='+10')

def prevOne(val):
    global frameNr
    axLeft.clear()

    if frameNr>=smallStep:
        frameNr = frameNr-smallStep
    axLeft.imshow(visualization.img_real2view(movie[frameNr][...,::-1]))
    axLeft.set_title("Frame "+str(frameNr)+"/"+str(lenMovie),fontsize = 10)
    subfigs[0].canvas.draw_idle()

def nextOne(val):
    global frameNr
    axLeft.clear()

    frameNr = frameNr+smallStep

    axLeft.imshow(visualization.img_real2view(movie[frameNr][...,::-1]))
    axLeft.set_title("Frame "+str(frameNr)+"/"+str(lenMovie),fontsize = 10)
    subfigs[0].canvas.draw_idle()

def prevMore(val):
    global frameNr
    axLeft.clear()

    if frameNr>=bigStep:
        frameNr = frameNr-bigStep
    axLeft.imshow(visualization.img_real2view(movie[frameNr][...,::-1]))
    axLeft.set_title("Frame "+str(frameNr)+"/"+str(lenMovie),fontsize = 10)
    subfigs[0].canvas.draw_idle()

def nextMore(val):
    global frameNr
    axLeft.clear()

    frameNr = frameNr+bigStep

    axLeft.imshow(visualization.img_real2view(movie[frameNr][...,::-1]))
    axLeft.set_title("Frame "+str(frameNr)+"/"+str(lenMovie),fontsize = 10)
    subfigs[0].canvas.draw_idle()

fbw_bt.on_clicked(prevMore)
bw_bt.on_clicked(prevOne)

fw_bt.on_clicked(nextOne)
ffw_bt.on_clicked(nextMore)

# event handling on the left figures
# upon selection a crop on one frame
def onclick(event):
    global frameNr
    global saveClip
    global crop_x
    global crop_y
 
    click_x,click_y = round(event.xdata),round(event.ydata)
    if click_x+click_y<=2:
        print("not a valid crop")
    else:
        crop_x = click_x
        crop_y = click_y
        axLeft.clear()
        for each in axRight: 
            each.clear()
        print("x-coor: "+str(click_x)+", y-coor: "+str(click_y))

        # on the left panel 
        toDraw = np.copy(movie[frameNr])

        # on the right panel
        toPlot = np.copy(movie[frameNr:frameNr+50,click_y:click_y+18,click_x:click_x+16,:]) 
        
        # prepare the 50-frame clip to save
        saveClip = np.zeros((1,2,50,18,16))
        saveClip[0,0,:,:,:] = np.copy(toPlot[:,:,:,0]);saveClip[0,1,:,:,:] = np.copy(toPlot[:,:,:,1])
        # print(saveClip.shape)
        # print(toPlot.shape)# shape 50 18 16 3
        # print(toDraw.shape)

        # visualize the 18x16 crop
        cv.rectangle(toDraw,(click_x,click_y),(click_x+16,click_y+18),color = (255,255,255),thickness=1) # shows the starting position of the crop
        axLeft.imshow(visualization.img_real2view(toDraw[...,::-1]))
        axLeft.set_title("Frame "+str(frameNr)+"/"+str(lenMovie),fontsize = 10)

        # randomly select 5 frame 
        randomIdx = sorted(random.sample(range(0, 50), 5))
        for i in range(5):
            axRight[i].imshow(visualization.img_real2view(toPlot[randomIdx[i]][...,::-1]))
            axRight[i+5].imshow(saveClip[0,0,randomIdx[i],:,:]) # UV sanity check
            axRight[i+10].imshow(saveClip[0,1,randomIdx[i],:,:]) # Green sanity check
            axRight[i].set_title("frame: "+str(randomIdx[i]))
            axRight[i].axis("off")
        subfigs[1].canvas.draw_idle()

leftPanel_cid = subfigs[0].canvas.mpl_connect('button_press_event', onclick)

# save button
saveAx = subfigs[0].add_axes([0.4, bt_bottom_pos, bt_width, bt_height])
save_bt = Button(saveAx, color = "blue",label='save clip')

def saveClip(val):
    global frameNr
    global saveClip
    global crop_x
    global crop_y
    print("save a clip")
    saveFileName = videoName.split(".")[0]+"_"+str(frameNr)+"_"+str(crop_x)+"_"+str(crop_y)+'.npy'
    #print(saveFileName)
    if np.sum(saveClip)>0:
        np.save('../data/stimuli/sky/'+saveFileName,saveClip)

save_bt.on_clicked(saveClip)

plt.show()

