#!/usr/bin/env python
# -*- cimport numpy as np
import sys
import argparse
import numpy as np
try:
	import cv2
except ImportError:
	# Workaround Ubuntu import errors
	sys.path.append('/usr/lib/python2.7/dist-packages')
	sys.path.append('/usr/local/lib/python2.7/site-packages')
	import cv2
from pprint import pprint

def startcamera(cameraindex):
	return cv2.VideoCapture(cameraindex)

def showvideogray(camerahandler):
	while(True):
		# Capture frame-by-frame
		ret, frame = camerahandler.read()

		# Our operations on the frame come here
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		# Display the resulting frame
		cv2.imshow('frame',gray)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

def cameraclose(camerahandler):
	# When everything done, release the capture
	cap.release()
	cv2.destroyAllWindows()


if __name__ == '__main__':
	ap = argparse.ArgumentParser()
	ap.add_argument("--camera", help="Number of the camera. Use 0 if only have one", type=int, required=True)
	args = vars(ap.parse_args())
	camfd = startcamera(args['camera'])
	showvideogray(camfd)
	cameraclose(camfd)

