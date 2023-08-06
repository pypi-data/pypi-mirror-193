# Imports
try:
  import rsa
  import os
  import binascii
  import time
  import random
  import datetime
  from colorama import Fore, Style
except:
  print("Error: Missing required modules. Please install the following modules: rsa, datetime, time, colorama and random")
  os.system("pip install -r requirements.txt")

try:
  from randomhex import createDigest
  from filterfile import filterFile
  from clearconsole import CC
  from extractlist import extractList
  from extracttable import extractTable
except:
  print("Error: Missing required program files, ensure that the following files are present: randomhex.py, clearconsole.py, filterfile.py, extractlist.py and extracttable.py")


# Global Variables
class Files():
  modulePath = str("C:/Users/" + os.getlogin() + "/AppData/Local/Programs/Python/Libs")
  programDir = str(modulePath + "/data-extraction")
  programDir2 = str(modulePath + "/data-extraction/modules")
  programDir3 = str(modulePath + "/data-extraction/standalone")
  filterFile = str(modulePath + "/data-extraction/modules/filterfile.py")
  extractList = str(modulePath + "/data-extraction/modules/extractlist.py")
  extractTable = str(modulePath + "/data-extraction/modules/extracttable.py")
  randomHex = str(modulePath + "/data-extraction/modules/randomhex.py")
  
class errorMessages():
  error = str("ERROR: An unknown error has occured.")
  fileUnreadable = str("ERROR: The file given cannot be read.")
  fileEmpty = str("ERROR: The given file is empty and contains no data.")
  insufficientPerm = str("ERROR: The file cannot be accessed due to insufficient permissions.")
  fileExists = str("ERROR: The file does not exist/the path can't be found.")
  fileOpen = str("ERROR: The file cannot be opened due to it being in use by another process.")   

user = str(os.getlogin())
sleep = time.sleep(3)
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n\n"
  
  
def checks():
  # File checks
  if os.path.exists(Files.programDir) is False:
    os.makedirs(Files.programDir)
  if os.path.exists(Files.programDir2) is False:
    os.makedirs(Files.programDir2)
  if os.path.exists(Files.programDir3) is False:
    os.makedirs(Files.programDir3)
  if os.path.exists(Files.modulePath) is False:
    os.mkdir(Files.modulePath)
  else:
    pass
  
  # Check file status
  try:
   testFilter = open(Files.filterFile, "r")
   testList = open(Files.extractList, "r")
   testTable = open(Files.extractTable, "r")
   testhex = open(Files.randomHex, "r")
  except IOError:
    print(errorMessages.fileOpen)
    raise RuntimeError

