import cv2
import time
import cv2.aruco as A
import numpy as np

# import calibrate function from this file and call it with your camera's
# video file name (string) as a parameter to get the correct paramters for your camera
# example: retval, mtx, dist, rvecs, tvecs = calibrate("video.mp4")
def calibrate(video_filename):
    dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
    board = cv2.aruco.CharucoBoard_create(8, 5, 0.1, 0.065, dictionary=dictionary)

    # Change to video from your own camera for calibration
    cap = cv2.VideoCapture(video_filename)
    ret, frame = cap.read()
    
    allCorners = []
    allIds = []
    decimator = 0
    while ret:
        # print(i)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        res = cv2.aruco.detectMarkers(gray,dictionary)

        if len(res[0])>0:
            res2 = cv2.aruco.interpolateCornersCharuco(res[0],res[1],gray,board)
            if res2[1] is not None and res2[2] is not None and len(res2[1])>3 and decimator%3==0:
                allCorners.append(res2[1])
                allIds.append(res2[2])

            cv2.aruco.drawDetectedMarkers(gray,res[0],res[1])

        # cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        decimator+=1
        
        ret,frame = cap.read()

    imsize = gray.shape

    #Calibration fails for lots of reasons. Release the video if we do
    try:
        # cameraMatrix, distCoeffs, rvecs, tvecs = cv2.aruco.calibrateCameraCharuco(allCorners,allIds,board,imsize,None,None)
        cal = cv2.aruco.calibrateCameraCharuco(allCorners, allIds, board, imsize, None, None)
        print("retval:")
        print(cal[0])
        print("cameraMatrix:")
        print(cal[1])
        print("distCoeffs: ")
        print(cal[2])
        # print("rvecs: ")
        # print(cal[3])
        # print("tvecs: ")
        # print(cal[4])

        return cal[0], cal[1], cal[2], cal[3], cal[4]
    except:
        cap.release()

    cap.release()
    cv2.destroyAllWindows()
    # print(allIds)
    # print(allCorners)
    # print(len(allIds))
    # print(len(allCorners))
