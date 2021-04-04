import time
import cv2
import multitimer

PATH = "cryptocam_capture.png"
INTERVAL = 5

# --- PRIVATE FUNCTIONS --- #

camCapture = cv2.VideoCapture(0)
def _captureFrame():
  rev, frame = camCapture.read()
  cv2.imwrite(PATH, frame)

def _camCrypto():
  _captureFrame()
  return true

# --- PUBLIC FUNCTIONS --- #

print("Generating values...")
timer = multitimer.MultiTimer(interval=INTERVAL, function=_camCrypto)
timer.start()
print(_camCrypto())

def stopGeneration():
  timer.stop()
  camCapture.release()
  cv2.destroyAllWindows()
  print("Stopped generation")