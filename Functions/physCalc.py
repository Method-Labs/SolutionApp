 #Import all required libraries and modules (this list will grow with time)
import sys
import cv2
import numpy
import matplotlib
import Tkinter
import time
import math

#define vars
d = 0
v = 0
t = 0
a = 0
vf = 0
vi = 0
distanceUnit = 0
timeUnit = 0
#define functions
def setDistanceUnit():
    global distanceUnit
    distanceUnit = raw_input('Pick your unit of distance: ')
    if distanceUnit == ('m'):
        print('Distance unit set to meters.')
        distanceUnit = ('meters')
    elif distanceUnit == ('km'):
        print('Distance unit set to kilometers.')
        distanceUnit = ('kilometers')
    elif distanceUnit == ('mi'):
        print('Distance unit set to miles.')
        distanceUnit = ('miles')
    elif distanceUnit == ('ft'):
        print('Distance unit set to feet.')
        distanceUnit = ('feet')
    elif distanceUnit == ('in'):
        print('Distance unit set to inches.')
        distanceUnit = ('inches')

def setTimeUnit():
    global timeUnit
    timeUnit = raw_input('Pick your unit of time: ')
    if timeUnit == ('m') or timeUnit == ('min'):
        print('Time unit set to minutes.')
        timeUnit = ('minutes')
    elif timeUnit == ('s'):
        print('Time unit set to seconds.')
        timeUnit = ('seconds')
    elif timeUnit == ('h') or timeUnit == ("hrs") or timeUnit == ('hr'):
        print('Time unit set to hours.')
        timeUnit = ('hours')

def setVelocityUnit():
    velocityUnit = raw_input('Pick your unit of velocity: ')
    if velocityUnit == ('m/s'):
        print('Velocity unit set to meters per second.')
    elif velocityUnit == ('km/h'):
        print('Velocity unit set to kilometers per hour')
    elif velocityUnit == ('mi/h'):
        print('Velocity unit set to miles per hour')
    elif velocityUnit == ('ft/s'):
        print('Velocity unit set to feet per second')

def velocity():
    global d
    global t
    setDistanceUnit()
    setTimeUnit()
    d = input('Distance in {}: '.format(distanceUnit))
    t = input('Time in {}: '.format(timeUnit))
    setVelocityUnit()


distCoversionFactors = {'mtokm': 0.001, 'mtomi': 0.000621371}

    
def distConvert():


def timeConvert():


