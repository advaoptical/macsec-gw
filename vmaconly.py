#! /usr/bin/env python
# coding=utf-8
##############################################
# Copyright (c) 2020
# ADVA Optical Networking
##############################################
__version__ = "0.0"

import os
import binascii
import commands
import time
import base64
import codecs
import hashlib 
import hmac 
import sys
import constants

from ctypes import *

host = "root@20.20.20.52"

if len(sys.argv[1:]):
	host = sys.argv[1]

path_near = constants.BASE_PATH+"alice/"
path_far = constants.BASE_PATH+"bob/"
if len(sys.argv[2:]):
	path_near = constants.BASE_PATH+"bob/"
	path_far = constants.BASE_PATH+"alice/"

hybridkey = ""
########################
if os.path.isfile('./qkdkey.txt'):
    dh_sharedkey = open("qkdkey.txt", "r").read()
    hybridkey += dh_sharedkey
    print("QKD key is added.")

if os.path.isfile('./dhkey.txt'):
    dh_sharedkey = open("dhkey.txt", "r").read()
    hybridkey += dh_sharedkey
    print("DH key is added.")

if os.path.isfile('./sharedKey.txt'):
    mce_sharedkey = open("sharedKey.txt", "r").read()
    hybridkey += mce_sharedkey
    print("MCE key is added.")

h = hmac.new("SAFE", hybridkey, hashlib.sha256)
#hmac.update(mce_sharedkey)
mac = h.hexdigest()
print("MAC = ")
print(mac)

# mac transmission 
f = open("mac.txt", "w+")
f.write(mac)
f.close()

# store mac in the local folder
cmd = "cp mac.txt " + path_near
print(cmd)
(err,output) = commands.getstatusoutput(cmd)
print(err)
print(output)

cmd = "scp mac.txt " + host + ":" + path_near
print(cmd)
(err,output) = commands.getstatusoutput(cmd)
print(err)
print(output)

cmd = "ssh " + host  + " stat " + path_far + "mac.txt" 
print(cmd)
err = 1
print("Waiting for the MAC from the remote side...")
while err != 0:
	(err,output) = commands.getstatusoutput(cmd)
#	print(err)

	if err == 0: 
		cmd = "scp " + host + ":" + path_far + "mac.txt " + "./mac_far.txt"
		(err,output) = commands.getstatusoutput(cmd)
		print(err)
	else:
		time.sleep(1)
#		print("bob/ct.txt does not exist.")


# remove  mac_far.txt 
cmd = "ssh " + host  + " rm " + path_far + "mac.txt" 
print(cmd)
(err,output) = commands.getstatusoutput(cmd)
print(err)

mac_far = open("mac_far.txt", "r").read()
if mac == mac_far:
	print("the final key is verified!")
else:
	print("ERROR: the final key is NOT verified!")

print("Done")


