import numpy as np
import cv2
import cv2.aruco as aruco
import time
# import calibrate_camera_online
import sys
# from PIL import Image, ImageDraw
# import turtle

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
aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
parameters = aruco.DetectorParameters_create()
counter = 0
path_list = []
reference_id = 16
pointer_id = 4
while ret:
    # uncomment line below if you want to see time to process each frame
    # frame_start_time = time.time()
    
    # frame set up before passing in to detect method
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # lists of marker corners, ids, and rejected markers (squares)
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    
    # store aruco marker data for current frame
    id_list = []
    if ids != None:
        for id in ids:
            id_list.append(id[0])

    # extract rotational and transitional vectors for markers in current frame
    rvecs_curr, tvecs_curr = aruco.estimatePoseSingleMarkers(corners, 0.05, mtx, dist)
    # if len(corners) != 0:
    #     print(corners)
    #     print(corners[0])
    #     print(corners[0][0])
    #     print(corners[0][0][0])

    if ids != None:
        for rvec, tvec in zip(rvecs_curr, tvecs_curr):
            # Draw 3D axes
            aruco.drawAxis(frame, mtx, dist, rvec, tvec, 0.05)
            # print(rvec, tvec)
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

    # Draws dots in path created by marker with id = pointer_id
    # and draws with respect to marker with id = reference_id
    # default reference_id = 16
    # default pointer_id = 4
    # can be changec out of while loop
    if reference_id in id_list:
        reference_index = id_list.index(reference_id)
        reference_x = corners[reference_index][0][0][0]
        reference_y = corners[reference_index][0][0][1]
        print(reference_x, reference_y)
        if pointer_id in id_list:
            pointer_index = id_list.index(pointer_id)
            pointer_x = corners[pointer_index][0][0][0]
            pointer_y = corners[pointer_index][0][0][1]
            path_list.append((reference_x - pointer_x, reference_y - pointer_y))
        if len(path_list) > 0:
            for coord in path_list:
                draw_x = reference_x - coord[0]
                draw_y = reference_y - coord[1]
                draw_coord = (draw_x, draw_y)
                print(draw_coord)
                cv2.circle(frame, draw_coord, 3, (0, 255, 0), 3, 8, 0)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
    # capture next frame
    ret, frame = cap.read()
    
# When everything done, release the capture
print("Total Time: " + str(time.time() - start_time))
cap.release()
cv2.destroyAllWindows()
