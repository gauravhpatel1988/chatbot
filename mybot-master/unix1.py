#! /usr/bin/python3
import subprocess 
import os
def getOS():
   command = "cat /etc/redhat-release"
   x = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
   return x 
def getHOST():
   command = "hostname"
   x = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
   return x
def getMEM():
   command = "free -g"
   x = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
   return x
def getCPU():
   command = "cat /proc/loadavg | awk '{print $1}'"
   x = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
   return x
def getUPT():
   command = "uptime"
   x = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
   return x
def getDISK():
   command = "df -h"
   x = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
   return x
print(getOS())
print(getHOST())
print(getMEM())
print(getCPU())
print(getUPT())
