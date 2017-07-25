#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 01:03:52 2017

@author: spock
"""


def thermostat_higher():
    print ("T inc")

def thermostat_lower():
    print ("T dec")

def lights_on():
    print ("Lights ON")

def lights_off():
    print ("Lights OFF")
    a = 1/0
    print (a)

def iot_event_handler (intent):
    if intent == 'lights_on':
        try:
            lights_on()
            return True
        except:
            return False
    elif intent == "light_off":
        try:
            lights_off()
            return True
        except:
            return False
    elif intent == "thermostat_higher":
        try:
            thermostat_higher()
            return True
        except:
            return False
    elif intent == "thermostat_lower":
        try:
            thermostat_lower()
            return True
        except:
            return False
    else:
        return True
        
        