#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 16:25:29 2023

@author: arnab
"""
#conditons.py Input and Conditions program
temp = input("Please enter the current temperature: ")
if int(temp) > 90:
    print("Wear shorts")
elif int(temp) > 70:
    print ("Short sleeves are fine")
elif int(temp) > 50:
    print("Wear a jacket")
elif int(temp) > 32:
    print("Wear a heavy coat")
else:
    print("Stay inside")
    