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

def generateHash(saveToFile, hashPath, photoPath, hashType):
  captureFile = None

  if(photoPath):
    _captureFrame(photoPath)
    captureFile = _fileToBytes(open(photoPath, 'rb'))
  elif(photoPath is None):
    raise ValueError("Error: argument 'photoPath' cannot be empty")

  hashDict = {
    "sha1":hashlib.sha1(captureFile).hexdigest(),
    "sha256":hashlib.sha256(captureFile).hexdigest(),
    "sha512":hashlib.sha512(captureFile).hexdigest(),
    "blake2b":hashlib.blake2b(captureFile).hexdigest(),
    "blake2s":hashlib.blake2s(captureFile).hexdigest(),
    "md5":hashlib.md5(captureFile).hexdigest(),
    "sha3_256":hashlib.sha3_256(captureFile).hexdigest(),
    "sha3_512":hashlib.sha3_512(captureFile).hexdigest()
  }

  if(saveToFile == "true"):
    if(hashPath is None):
      raise ValueError("Error: argument 'hashPath' cannot be empty if argument 'saveToFile' is defined as 'true'")
    else:
      with open(hashPath, 'w') as f:
        if(hashType is None):
          print("Hash type not defined. Saved checksum file to '{}' using 'sha256'".format(hashPath))
          return f.write(hashlib.sha256(_fileToBytes(open(photoPath, 'rb'))).hexdigest())
        else:
          print("Saved checksum file to '{}' using '{}'".format(hashPath, hashType))
          return f.write(hashDict.get(hashType, "Invalid hash type defined"))
  elif(saveToFile == "false"):
    return hashDict.get(hashType, "Invalid hash type defined")
  else:
    raise ValueError("Error: argument 'saveToFile' is either not defined or is an incorrect value")