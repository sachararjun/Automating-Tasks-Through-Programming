#!/usr/bin/env python 
from network import *
import shutil
import psutil 
def check_disk_usage(disk):
      """ Verifies that there's enough free space on disk """
      du= shutil.disk_usage(disk)
      free =du.free/du.total * 100
      return free > 30
def check_cpu_usage():
      """ Verifies that there's enough unused cpu """
      usage = psutil.cpu.percent(1)
      return usage < 73
    
# If there is not enough disk , or not enough CPU , Print an error

if not check_disk_usage('/') or not check_cpu_usage():
      print("ERROR")
      
elif check_localhost() and check_connectivity():
      print("Everything is OKAY")
      
else :
      print("Network checks failed") 
      
           
