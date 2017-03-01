import numpy as np
import cv2
import cv2.aruco as aruco
import time


# TODO: Need to make the cube jiggle less. Maybe use multiple corners to generate a cube instead of just one.

def draw_pose(frame, rvec, tvec, aruco_marker_corners, mtx, dist):
    """ Draws the pose at the center of the specified Aruco marker.

    Args:
        frame: give the image to draw the pose on the center of the Aruco marker.
        rvec: the rotation vector from the camera to the Aruco marker center.
        tvec: the translation vector from the camera to the Aruco marker center.
        aruco_marker_corners: the corners of the respective aruco marker in list representation obtained from aruco.detectMarkers
        mtx: the intrinsic camera properties.
        dist: the distortion coefficients for the camera.

    Returns:
        frame: the frame with the pose drawn on the marker
    """

    points_wrt_aruco_center = np.float32([[0.03, 0, 0], [0, 0.03, 0], [0, 0, -0.03]])
    imgpts, jac = cv2.projectPoints(points_wrt_aruco_center, rvec, tvec, mtx, dist)

    mid_point = np.mean(aruco_marker_corners[0], axis=0)
    frame = cv2.line(frame, tuple(mid_point), tuple(imgpts[0][0]), (255, 0, 0), 5)
    frame = cv2.line(frame, tuple(mid_point), tuple(imgpts[1][0]), (0, 255, 0), 5)
    frame = cv2.line(frame, tuple(mid_point), tuple(imgpts[2][0]), (0, 0, 255), 5)

    return frame


def draw_cube(frame, rvec, tvec, aruco_marker_corners, mtx, dist):
    """ Draws a cube spawning at the center of the specified Aruco marker.

    Args:
        frame: give the image to draw the pose on the center of the Aruco marker.
        rvec: the rotation vector from the camera to the Aruco marker center.
        tvec: the translation vector from the camera to the Aruco marker center.
        aruco_marker_corners: the corners of the respective aruco marker in list representation obtained from aruco.detectMarkers.
        mtx: the intrinsic camera properties.
        dist: the distortion coefficients for the camera.

    Returns:
        frame: the frame with the cube drawn on the marker.
    """

    points_wrt_aruco_center = np.matrix('0,0,0; 0,0,0.1; 0,0.1,0.1; 0,0.1,0;'
                                        '0,0,0; 0,0,0.1; 0.1,0,0.1; 0.1,0,0;'
                                        '0,0,0; 0,0.1,0; 0.1,0.1,0; 0.1,0,0;'
                                        '0,0,0.1; 0,0.1,0.1; 0.1,0.1,0.1; 0.1,0,0.1;'
                                        '0,0.1,0.1; 0,0.1,0; 0.1,0.1,0; 0.1,0.1,0.1;'
                                        '0.1,0,0.1; 0.1,0,0; 0.1,0.1,0; 0.1,0.1,0.1', dtype=np.float32)
    imgpts, jac = cv2.projectPoints(points_wrt_aruco_center, rvec, tvec, mtx, dist)

    imgpts = np.int32(imgpts).reshape(-1, 2)
    color = 0
    for point_ind in range(0, np.shape(imgpts)[0], 4):
        frame = cv2.drawContours(frame, [imgpts[point_ind:point_ind+4]], -1, (255, color, color), -1)
        color += 30

    return frame

vidcap = cv2.VideoCapture('IMG_0227.m4v')
ret, frame = vidcap.read()

# camera parameters determined through calibration for iPhone 7 Plus - change to your camera calibration parameters
mtx = np.matrix([[3.63073713e+03, 0.00000000e+00, 8.22942919e+02], [0.00000000e+00, 3.77169215e+03, 5.88888908e+02],
                 [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])
dist = np.matrix([[6.79408999e-02, 1.74574431e+01, 1.04400486e-02, -8.23621330e-02, -2.57734449e+02]])

start_time = time.time()
aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
parameters = aruco.DetectorParameters_create()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

while ret:
    frame_start_time = time.time()

    # frame resize and graying before performing the rest of the stuff.
    frame = cv2.resize(frame, (1280, 720))
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # lists of marker corners, ids, and rejected markers (squares)
    all_aruco_corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

    # extract rotational/transitional vectors for markers in current frame, this localizes to the middle of the marker.
    rvecs, tvecs = aruco.estimatePoseSingleMarkers(all_aruco_corners, 0.05, mtx, dist)

    # CODE FOR GETTING THE TRANSLATION AND ROTATION TO EACH CORNER
    # objp = np.zeros((19, 3), np.float32)
    # objp[:, :2] = np.mgrid[0:5, 0:4].T.reshape(-1, 2)[:-1, :]
    #
    # rvecs, tvecs, inliers = cv2.solvePnP(objp, corners, mtx, dist)

    if ids is not None:
        for id, rvec, tvec, aruco_corners in zip(ids, rvecs, tvecs, all_aruco_corners):
            if id == 10:
                # frame = aruco.drawAxis(frame, mtx, dist, rvec, tvec, 0.03)
                frame = draw_pose(frame, rvec, tvec, aruco_corners, mtx, dist)
                # aruco.drawDetectedMarkers(frame, [corner])
            elif id == 11:
                frame = draw_cube(frame, rvec, tvec, aruco_corners, mtx, dist)

    cv2.imshow('frame', frame)

    # get next frame
    ret, frame = vidcap.read()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # UNCOMMENT for FPS
    # print(1/(time.time() - frame_start_time), "fps")

# When everything done, release the capture
print("Total Time: " + str(time.time() - start_time))
vidcap.release()
cv2.destroyAllWindows()
