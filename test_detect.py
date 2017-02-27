import numpy as np
import cv2
import cv2.aruco as aruco
import time
import calibrate_camera_online
import sys
from PIL import Image, ImageDraw
import turtle

print(cv2.__version__)
# # change 'samplearucovideo.mp4' to any video
# vidcap = cv2.VideoCapture('fingersleeve_test2.mp4')
# ret, frame = vidcap.read()


# livestream setup
host = "128.61.114.241:8080"
if len(sys.argv)>1:
    host = sys.argv[1]

hoststr = 'http://' + host + '/video'
cap = cv2.VideoCapture(hoststr)
ret, frame = cap.read()

# camera parameters determined through calibration for OnePlus 3T - change to your camera calibration parameters
mtx = np.matrix([[  3.63073713e+03,   0.00000000e+00,   8.22942919e+02], [  0.00000000e+00,   3.77169215e+03,   5.88888908e+02], [  0.00000000e+00,   0.00000000e+00,   1.00000000e+00]])
dist = np.matrix([[  6.79408999e-02,   1.74574431e+01,   1.04400486e-02,  -8.23621330e-02, -2.57734449e+02]])

start_time = time.time()

# lists to store corners, ids, and rejectedImgPoints for each frame
corners_list= []
ids_list = []
rejectedImgPoints_list = []
aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
parameters = aruco.DetectorParameters_create()

while ret:
    # uncomment line below if you want to see time to process each frame
    # frame_start_time = time.time()
    
    # frame set up before passing in to detect method
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # lists of marker corners, ids, and rejected markers (squares)
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    
    # store aruco marker data for current frame
    corners_list.append(corners)
    ids_list.append(ids)
    rejectedImgPoints_list.append(rejectedImgPoints)

    # extract rotational and transitional vectors for markers in current frame
    rvecs_curr, tvecs_curr = aruco.estimatePoseSingleMarkers(corners, 0.05, mtx, dist)
    print corner

    if ids != None:
        for rvec, tvec in zip(rvecs_curr, tvecs_curr):
            # Draw 3D axes
            aruco.drawAxis(frame, mtx, dist, rvec, tvec, 0.05)
            print(rvec, tvec)
            # uncommment below to print rotational matrix and rotational/transitional vectors for each marker in the current frame
            # rmat = cv2.Rodrigues(rvec)
            # print("rmat:")
            # print(rmat)
            # print("translation:")
            # print(tvec)
            # print("rotation:")
            # print(rvec)

        # Draw A square around the markers
        aruco.drawDetectedMarkers(frame, corners) 

    # Uncomment to display the frame with axes and square around marker
    y_center = int(gray.shape[0]/2)
    x_center = int(gray.shape[1]/2)
    # print(x_center, y_center)
    cv2.circle(frame, (x_center, y_center), 100, (0, 255, 0), 2, 8, 0)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
    # capture next frame
    ret, frame = cap.read()
    
# When everything done, release the capture
print("Total Time: " + str(time.time() - start_time))
cap.release()
cv2.destroyAllWindows()