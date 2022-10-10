import cv2
import numpy as np
import time
from recognize import recognize_trace

def nothing(x):
    pass

# def showtext(dispay, text):
# 	c_time = time.time()
# 	while(time.time() - c_time < 3):
# 		cv2.putText(display, text, (100,100),
# 						cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1, cv2.LINE_AA)
# Choose your webcam: 0, 1, ...
cap = cv2.VideoCapture(1)
if not cap.isOpened():
	cap.open()

#cv2.namedWindow('Threshold Sliders')
#cv2.createTrackbar('R', 'Threshold Sliders', 0, 255, nothing)
#cv2.createTrackbar('B', 'Threshold Sliders', 0, 255, nothing)

status = 0 # Not recognizing, status = 1 => recognizing.
leave_times = 0 # The times that the finger leaves the pad.
leave_time = 0 # The time that the finger leaves the pad.
finger_pos = []   # A list to store the position of finger.
origin_end = [] # A list to store the origin and the end of every sections.
last_record = 0
extreme = [0, 0, 1000, 1000]

while(True):
	# Get one frame from the camera
	ret, frame = cap.read()
	frame = cv2.flip(frame, 0)
	cv2.imshow('frame', frame)

	# Split RGB channels
	b, g, r = cv2.split(frame)
	zeros = np.zeros(frame.shape[:2], dtype="uint8")

	# get the current value of the slider
	#r_thresh = cv2.getTrackbarPos('R', 'Threshold Sliders')
	#b_thresh = cv2.getTrackbarPos('B', 'Threshold Sliders')

	# Perform thresholding to each channel
	_, r_thresh_binary = cv2.threshold(r, 135, 255, cv2.THRESH_BINARY)
	_, b_thresh_binary_inv = cv2.threshold(b, 200, 255, cv2.THRESH_BINARY_INV)

	# Get the final result using bitwise operation
	result = cv2.bitwise_and(r_thresh_binary, b_thresh_binary_inv, mask = None)
#	result = cv2.blur(result, frame.shape[:2])

	# Find and draw contours
	contours, hierarchy = cv2.findContours(result, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	display = cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)
	cv2.drawContours(display, contours, -1, (0,0,255))	
	if len(contours) > 0:
		x_main = 0
		y_main = 0
		rad_main = 0
		for cnt in contours:
			(x,y), radius = cv2.minEnclosingCircle(cnt)
			if radius > rad_main:
				rad_main = radius
				x_main = x
				y_main = y
		if rad_main < 20:
			continue
		if leave_time > 0:
			leave_times += 1
		leave_time = 0
		if status == 0: # Start recognizing.
			status = 1
		# for cnt in contours:
		# 	area = cv2.contourArea(cnt)
		# 	(x,y), radius = cv2.minEnclosingCircle(cnt)
		# 	if radius > rad_main:
		# 		rad_main = radius
		# 		x_main = x
		# 		y_main = y
		# print(rad_main)
		x_main = int(x_main)
		y_main = int(y_main)
		rad_main = int(rad_main)

		text = '(' + str(x_main) + ',' + str(y_main) + ')'
		cv2.putText(display, text, (x_main, y_main),
					cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1, cv2.LINE_AA)
		cv2.circle(display, (x_main, y_main), rad_main, (0, 255, 0))
		if time.time() - last_record > 0.1:
			last_record = time.time()
			finger_pos.append((x_main, y_main))
			extreme[0] = max(x_main, extreme[0])
			extreme[1] = max(y_main, extreme[1])
			extreme[2] = min(x_main, extreme[2])
			extreme[3] = min(y_main, extreme[3])
	else:
		if status == 1:
			if leave_time == 0:
				leave_time = time.time()
				origin_end.append([finger_pos[0], finger_pos[-1]])
				print(origin_end)
				finger_pos = []
			if time.time() - leave_time > 0.7: # The writer has finished writing.
				number = recognize_trace(origin_end, extreme, leave_times)
				origin_end = []
				status = 0
				finger_pos = []
				leave_time = 0
				leave_times = 0
				text1 = "prediction :" + str(number)
				print(number)

	
	
	# Show the frame	
	#cv2.imshow("Red", cv2.merge([zeros, zeros, r_thresh_binary]))
	#cv2.imshow("Blue", cv2.merge([b_thresh_binary_inv, zeros, zeros]))
	cv2.imshow("display", display)
#	cv2.imshow('frame', result)

	# Press q to quit
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# Release the camera
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()