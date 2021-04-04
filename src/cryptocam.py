import cv2
import hashlib

# --- PRIVATE FUNCTIONS --- #

camCapture = cv2.VideoCapture(0)

def _captureFrame(path):
  rev, frame = camCapture.read()
  cv2.imwrite(path, frame)
  print("Saved photo capture to '{}'".format(path))

def _fileToBytes(file):
  with file:
    return file.read()

# --- PUBLIC FUNCTIONS --- #

def generateHash(saveToFile, hashPath, photoPath):
  if(photoPath):
    _captureFrame(photoPath)
  elif(photoPath is None):
    raise ValueError("Error: argument 'photoPath' cannot be empty")
  if(saveToFile == "true"):
    if(hashPath is None):
      raise ValueError("Error: argument 'hashPath' cannot be empty if argument 'saveToFile' is defined as 'true'")
    else:
      with open(hashPath, 'w') as f:
        print("Saved checksum file to '{}'".format(hashPath))
        return f.write(hashlib.sha256(_fileToBytes(open(photoPath, 'rb'))).hexdigest())
  elif(saveToFile == "false"):
    return hashlib.sha256(_fileToBytes(open(photoPath, 'rb'))).hexdigest()
  else:
    raise ValueError("Error: argument 'saveToFile' is either not defined or is an incorrect value")