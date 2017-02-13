import numpy as np
import cv2
import cv2.aruco as aruco
import time
import calibrate_camera_online

print(cv2.__version__)
# change 'samplearucovideo.mp4' to any video
vidcap = cv2.VideoCapture('samplearucovideo.mp4')
ret, frame = vidcap.read()

# camera parameters determined through calibration for OnePlus 3T - change to your camera calibration parameters
mtx = np.matrix([[  3.63073713e+03,   0.00000000e+00,   8.22942919e+02], [  0.00000000e+00,   3.77169215e+03,   5.88888908e+02], [  0.00000000e+00,   0.00000000e+00,   1.00000000e+00]])
dist = np.matrix([[  6.79408999e-02,   1.74574431e+01,   1.04400486e-02,  -8.23621330e-02, -2.57734449e+02]])

start_time = time.time()

# lists to store corners, ids, and rejectedImgPoints for each frame
corners_list= []
ids_list = []
rejectedImgPoints_list = []

while ret:
    # uncomment line below if you want to see time to process each frame
    # frame_start_time = time.time()
    
    # frame set up before passing in to detect method
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
    parameters = aruco.DetectorParameters_create()

    # lists of marker corners, ids, and rejected markers (squares)
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    
    # store aruco marker data for current frame
    corners_list.append(corners)
    ids_list.append(ids)
    rejectedImgPoints_list.append(rejectedImgPoints)

    # extract rotational and transitional vectors for markers in current frame
    rvecs_curr, tvecs_curr = aruco.estimatePoseSingleMarkers(corners, 0.05, mtx, dist)

    if ids != None:
        for rvec, tvec in zip(rvecs_curr, tvecs_curr):
            # Draw 3D axes
            aruco.drawAxis(frame, mtx, dist, rvec, tvec, 0.05)
            
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
    # cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
    # capture next frame
    ret, frame = vidcap.read()
    
# When everything done, release the capture
print("Total Time: " + str(time.time() - start_time))
vidcap.release()
cv2.destroyAllWindows()
