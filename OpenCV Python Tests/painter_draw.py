import numpy as np
import cv2
import cv2.aruco as aruco
import time

from senlib import SEN as sen


def draw_pointer(frame, rvec, tvec, aruco_marker_corners, mtx, dist):
	# Set line_type to (0) for a regular line and (1) for a triangle type pointer.
	line_type = 0
	if line_type == 0:
		end_of_pointer = np.float32([[1, 0, 0]])
		end_point_in_img, _ = cv2.projectPoints(end_of_pointer, rvec, tvec, mtx, dist)
		mid_point = np.mean(aruco_marker_corners[0], axis=0)
		frame = cv2.line(frame, tuple(mid_point), tuple(end_point_in_img[0][0]), (255, 0, 0), 2)
	elif line_type == 1:
		ends_of_pointer = np.float32([[0, -0.00001, 0], [0, 0.00001, 0], [1, 0, 0]])
		img_ends_of_pointer, _ = cv2.projectPoints(ends_of_pointer, rvec, tvec, mtx, dist)
		img_ends_of_pointer = np.int32(img_ends_of_pointer).reshape(-1, 2)
		frame = cv2.drawContours(frame, [img_ends_of_pointer], -1, (255, 0, 0), -1)

	return frame


def point_of_intersection_wrt_camera(ray_origin, point_on_ray_path, point_on_plane, plane_normal, epsilon=1e-6):
	'''
	Finds the point where a given ray intersects a plane. All points should be in the same camera frame.
	:param ray_origin:
	:param point_on_ray_path:
	:param point_on_plane:
	:param plane_normal:
	:param epsilon:
	:return: The location where the ray intersects the plane.
	'''

	u = point_on_ray_path - ray_origin
	dot = np.dot(plane_normal.T, u)

	if abs(dot) > epsilon:
		w = ray_origin - point_on_plane
		fac = -np.dot(plane_normal.T, w) / dot
		u *= fac
		return ray_origin + u
	else:
		return None


vidcap = cv2.VideoCapture('http://143.215.50.155:8081')
ret, frame = vidcap.read()

# camera parameters determined through calibration for iPhone 7 Plus - change to your camera calibration parameters
mtx = np.matrix([[1.83546363e+03, 0.00000000e+00, 9.23925379e+02], [0.00000000e+00, 1.84001029e+03, 5.32820726e+02],
				 [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])
dist = np.matrix([[9.54776078e-02, -1.03980826e-01, 2.73126290e-04, -5.51001160e-03, -3.16378824e-01]])

start_time = time.time()
aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
parameters = aruco.DetectorParameters_create()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

points_to_draw_wrt_id0 = []
while ret:
	# frame resize and graying before performing the rest of the stuff.
	# frame = cv2.resize(frame, (480, 270))
	frame_start_time = time.time()

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

	# fetch all the markers in the scene.
	id_positions = {0: None, 2: None, 16: None, 18: None, 15: None}
	if ids is not None:
		for id, rvec, tvec, aruco_corners in zip(ids, rvecs, tvecs, all_aruco_corners):
			# frame = aruco.drawAxis(frame, mtx, dist, rvec, tvec, 0.03)
			aruco.drawDetectedMarkers(frame, [aruco_corners], id)

			if id == 0 or id == 2 or id == 16 or id == 18 or id == 15:
				# aruco.drawAxis(frame, mtx, dist, rvec, tvec, 0.03)
				id_positions[id[0]] = sen.SE3(np.matrix(tvec[0]).T, np.matrix(cv2.Rodrigues(rvec)[0]))

			if id == 15:
				aruco.drawAxis(frame, mtx, dist, rvec, tvec, 0.03)
			# if id == 0 or id == 2 or id == 16:
			# 	aruco.drawAxis(frame, mtx, dist, rvec, tvec, 0.03)

	# draw the appropriate lines in the scene
	if id_positions[0] is not None and id_positions[15] is not None:
		r0 = id_positions[15].translation()
		r1 = id_positions[15] * np.matrix('0;0.01;0;1')

		rvec = id_positions[15].rotation()
		tvec = id_positions[15].translation()

		end_point_in_img_1, _ = cv2.projectPoints(np.float32(r0.T), np.eye(3), np.zeros((3, 1)), mtx, dist)

		p0 = id_positions[0].translation()
		pn = id_positions[0] * np.matrix('0;0;1;0')

		point_to_plot_wrt_camera = point_of_intersection_wrt_camera(r0, r1[:3, 0], p0, pn[:3, 0])

		if point_to_plot_wrt_camera is not None:
			end_point_in_img_2, _ = cv2.projectPoints(np.float32(point_to_plot_wrt_camera.T), np.eye(3), np.zeros((3, 1)), mtx, dist)

			if abs(end_point_in_img_2[0][0][0]) < 2000 and abs(end_point_in_img_2[0][0][1]) < 2000:
				frame = cv2.line(frame, tuple(end_point_in_img_1[0][0]), tuple(end_point_in_img_2[0][0]), (255, 0, 0), 2)
				point_wrt_to_id0 = sen.inv(id_positions[0]) * point_to_plot_wrt_camera
				points_to_draw_wrt_id0.append(point_wrt_to_id0)

	if len(points_to_draw_wrt_id0) > 100:
		points_to_draw_wrt_id0 = points_to_draw_wrt_id0[1:]

	if id_positions[0] is not None:
		for point in points_to_draw_wrt_id0:
			point_wrt_to_camera = id_positions[0] * point
			point_wrt_to_camera_2 = id_positions[0] * sen.SE3(point, sen.EulerXYZtoR(0, 0, 0)) * np.matrix('0.001; 0.001; 0')
			points_to_plot = np.float32(np.vstack((point_wrt_to_camera.T, point_wrt_to_camera_2.T)))
			img_plane_point, _ = cv2.projectPoints(points_to_plot, np.eye(3), np.zeros((1, 3)), mtx, dist)

			frame = cv2.line(frame, tuple(img_plane_point[0][0]), tuple(img_plane_point[1][0]), (255, 0, 0), 10)

	cv2.imshow('frame', frame)

	# print('time/loop:', time.time()-frame_start_time)
	# get next frame
	vid_read = time.time()
	ret, frame = vidcap.read()
	# print('time/loop2:', time.time()-vid_read)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

		# UNCOMMENT for FPS
		# print(1/(time.time() - frame_start_time), "fps")

# When everything done, release the capture
print("Total Time: " + str(time.time() - start_time))
vidcap.release()
cv2.destroyAllWindows()
