# HapticSmartGlasses-ECE-Senior-Design-2

# To calibrate camera, create and run a file similar to the following with "video.mp4" changed to name of video you want to use for calibration.

from calibrate_camera_online import calibrate

retval, mtx, dist, rvecs, tvecs = calibrate("video.mp4")
