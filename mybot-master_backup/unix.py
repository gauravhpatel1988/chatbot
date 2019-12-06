#! /usr/bin/python3
import os

def getos():
    os.system("cat /etc/redhat-release ")

def getfilesystem():
    os.system("df -h")

def getcpuinfo():
    cpuinfo = os.system("cat /proc/cpuinfo | grep proc | wc -l")
      
print (getos())
print (getfilesystem())
print ('Total CPU',getcpuinfo())
