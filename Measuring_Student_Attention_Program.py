# Program Name: BCI_NeuroHAND_Gather_Data
# Program Date: 12/15/2018   
# Program Author: Fawzan Hussain (Grade 10)
# Revision History: Base Program
#
# Program v.1.0 -> 12/15/2018
#
# 
#
#
# DO NOT DELETE THIS INFORMATION!
# This is the Initialization Block
# Here we import Python libraries needed for the program and initialize the variables

import os

from NeuroPy import NeuroPy #importing modules
from datetime import datetime
import csv
import sys
import random
import string
#import keyboard
import time
import datetime

#Operating System: Mac OS Sierra
#Laptop Model: MacBook Air (13-inch, 2017)
#Processor: 1.8 GHz Intel Core i5
#Memory: 8 GB 1600 MHz DDR3 


# MAIN PROGRAM
global str_filename
global str_glob_name
global str_datetime
now2 = datetime.datetime.now()
# Clear Screen 
intClearScreen = 0
while intClearScreen <80:
      print("\n")
      intClearScreen = intClearScreen + 1
time.sleep(2) # a 2 second rest
print('*' * 120)
print (now2.strftime("%Y-%m-%d %H:%M:%S"))
str_datetime = now2.strftime("%Y-%m-%d %H:%M:%S")
print("Welcome to Health Tutor ver 3.11 Release Date: 12-31-2017")
print("\n")
print("This is a Python program to record brain waves and health metrics using Neurosky and HealthPi.")
print("\n")
print("Brain metrics measured are - Attention, Meditation.....")
print("Health metrics measured are - Temperature ....")
print("These metrics are recorded in a Comma-separated file in the following folder: ")
print("Please press Cntl-D key to stop the program.")
print('*' * 120)
str_glob_name = raw_input("Please enter the test subject's First Name:   ")
str_filename = str_glob_name+"-"+str_datetime+".txt"
print("The data will be saved in the data file - ",str_filename)
print("\n")

object1=NeuroPy("/dev/tty.MindWave")

myFile = open(str_filename, "w")
ColumnTitleRow = ("Attention,Meditation\n")
myFile.write(ColumnTitleRow)



def attention_callback(attention_value): 
    "this function will be called everytime NeuroPy has a new value for attention"
    global prog_attention_value
    global prog_datetime_value
    now1 = datetime.datetime.now()
    mm = str(now1.month)
    dd = str(now1.day)
    yyyy = str(now1.year)
    hh = str(now1.hour)
    mi = str(now1.minute)
    ss = str(now1.second)
    prog_datetime_value = mm + "/" + dd + "/" + yyyy + " " + hh + ":" +mi + ":" +ss
    #print "Value of attention is",attention_value #stating the value of attention
    prog_attention_value = str(attention_value)
    return None

def meditation_callback(meditation_value): 
    "this function will be called everytime NeuroPy has a new value for meditation"
    global prog_meditation_value
    #print "Value of meditation is",meditation_value
    prog_meditation_value = str(meditation_value)
    print prog_datetime_value + "," + prog_attention_value + "," + prog_meditation_value
    return None


def delta_callback(delta_value): 
    "this function will be called everytime NeuroPy has a new value for meditation"
    global prog_delta_value
    prog_delta_value = str(delta_value)
    print "Value of delta is",(prog_delta_value)
    return None

###other variables:__ attention,meditation,rawValue,delta,theta,lowAlpha,highAlpha,lowBeta,highBeta,lowGamma,midGamma, poorSignal and blinkStrength 

def theta_callback(theta_value): 
    "this function will be called everytime NeuroPy has a new value for meditation"
    global prog_theta_value
    prog_theta_value = str(theta_value)
    print "Value of theta is",(prog_theta_value)
    return None

def lowAlpha_callback(lowAlpha_value): 
    "this function will be called everytime NeuroPy has a new value for meditation"
    global prog_lowAlpha_value
    prog_lowAlpha_value = str(lowAlpha_value)
    print "Value of lowAlpha is",(prog_lowAlpha_value)
    return None

def highAlpha_callback(highAlpha_value): 
    "this function will be called everytime NeuroPy has a new value for meditation"
    global prog_highAlpha_value
    prog_highAlpha_value = str(highAlpha_value)
    print "Value of highAlpha is",(prog_highAlpha_value)
    return None

def lowBeta_callback(lowBeta_value): 
    "this function will be called everytime NeuroPy has a new value for meditation"
    global prog_lowBeta_value
    prog_lowBeta_value = str(lowBeta_value)
    print "Value of lowBeta is",(prog_lowBeta_value)
    return None

def highBeta_callback(highBeta_value): 
    "this function will be called everytime NeuroPy has a new value for meditation"
    global prog_highBeta_value
    prog_highBeta_value = str(highBeta_value)
    print "Value of highBeta is",(prog_highBeta_value)
    return None

def lowGamma_callback(lowGamma_value): 
    "this function will be called everytime NeuroPy has a new value for meditation"
    global prog_lowGamma_value
    prog_lowGamma_value = str(lowGamma_value)
    print "Value of lowGamma is",(prog_lowGamma_value)
    return None

def midGamma_callback(midGamma_value): 
    "this function will be called everytime NeuroPy has a new value for meditation"
    global prog_midGamma_value
    prog_midGamma_value = str(midGamma_value)
    print "Value of midGamma is",(prog_midGamma_value)
    return None

##def poorSignal_callback(poorSignal_value): 
##    "this function will be called everytime NeuroPy has a new value for meditation"
##    global prog_poorSignal_value
##    prog_poorSignal_value = str(poorSignal_value)
##    print "Value of poorSignal is",(prog_poorSignal_value)
##    return None
## not needed

##def blinkStrength_callback(blinkStrength_value): 
##    "this function will be called everytime NeuroPy has a new value for meditation"
##    global prog_blinkStrength_value
##    prog_blinkStrength_value = str(blinkStrength_value)
##    print "Value of blinkStrength is",(prog_blinkStrength_value)
##    return None
##not available as per website





#set call back:
object1.setCallBack("attention",attention_callback)
object1.setCallBack("meditation",meditation_callback)
object1.setCallBack("delta",delta_callback)
object1.setCallBack("theta",theta_callback)
object1.setCallBack("lowAlpha",lowAlpha_callback)
object1.setCallBack("highAlpha",highAlpha_callback)
object1.setCallBack("lowBeta",lowBeta_callback)
object1.setCallBack("highBeta",highBeta_callback)
object1.setCallBack("lowGamma",lowGamma_callback)
object1.setCallBack("midGamma",midGamma_callback)
##object1.setCallBack("poorSignal",poorSignal_callback)
##object1.setCallBack("blinkStrength",blinkStrength_callback)

    



#call start method 
object1.start()


##
##while True:
##    if(object1.attention>70): #another way of accessing data provided by headset (1st being call backs)
##        print("exit")
##        myFile.close()
##        object1.stop() #if meditation level reaches above 70, stop fetching data from the headset
##        sys.exit()
##
##    if (object1.attention < 70):
##        ##myFile.write(str(attention_value),str(meditation_value))
##        print("Continue")
##        RowData = ("Attention,Meditation\n")
##        myFile.write(RowData)
