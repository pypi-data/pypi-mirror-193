# Imports
try:
  import rsa
  import os
  import binascii
  import time
  import random
  import datetime
  from sys import platform
  from colorama import Fore, Style
except:
  print("Error: Missing required modules. Please install the following modules: rsa, datetime, time, colorama and random")
  

# Global Variables
class Files():
  modulePath = str("C:/Users/" + os.getlogin() + "/AppData/Local/Programs/Python/Libs")
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
keyValue = random.randint(90, 300)
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n\n"


# Functions
def CC():
  if platform == "linux" or platform == "linux2":
    os.system("clear")
  else:
    os.system("cls")
    

def extractList(file):
  with open(file, "r") as f:
    data = f.read()
    splitData = data.split('\n')
    f.close()
  
  print(splitData)
  return splitData


def extractTable(file):
  returnIteam = []
  with open(file, "r") as f:
    for line in f:
      data = f.read()
      extractedList = data.split('  ')
      extractData = ' '.join(extractedList)
      reformedData = str(extractData).split('\n')
      returnIteam.append(reformedData)

    print(returnIteam)
    return returnIteam
  

def filterFile(file, blklistword):
  with open(file, "r+") as f:
    for line in f:
      fline = line.split(' ')
      for word in fline:
        if word is blklistword:
          newline = line.replace(word, "")
          f.seek(word)
          f.write(newline)
        else:
          print("Word not found in file.")

        return fline
      
      
def createDigest():
  publicKey, privateKey = rsa.newkeys(keyValue)
  encMessage = rsa.encrypt(str(random.randint(1,10)).encode(), publicKey)
  hexMessage = binascii.hexlify(encMessage)
  bar = str(hexMessage).replace("'", '')
  foo = str(bar).replace('b', '')

  return foo

