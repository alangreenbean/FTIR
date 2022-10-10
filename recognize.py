import cv2
import numpy as np
import math
import time

def recognize_trace(origin_end, extreme, stop_time):

    if stop_time > 0:
        if origin_end[1][1][0] < 145 and origin_end[1][1][1] > 119:
            return 4
        if origin_end[1][1][0] > 145 and origin_end[1][1][1] < 119:
            return 5
        if origin_end[1][1][0] > 145 and origin_end[1][1][1] > 119:
            return 7
    else:
        if origin_end[0][1][0] > 145 and origin_end[0][1][1] < 119:
            return 8
        if origin_end[0][1][0] > 145 and origin_end[0][1][1] > 119:
            if origin_end[0][0][0] > 145 and origin_end[0][0][1] > 119:
                return 9
            else:
                return 2
        if origin_end[0][1][0] < 145 and origin_end[0][1][1] < 119:
            return 0
        else:
            if origin_end[0][0][0] > 145 and origin_end[0][0][1] < 119:
                return 1
            if origin_end[0][1][1] > 200:
                    return 3
            else:
                    return 6
            
            
        # if origin_end[0][0][0] < 145 and origin_end[0][0][1] < 119:
        #     if origin_end[0][1][0] < 145 and origin_end[0][1][1] < 119:
        #         return 0
        #     if origin_end[0][1][0] > 145 and origin_end[0][1][1] > 119:
        #         return 2
        #     else:
        #         if origin_end[0][1][1] > 200:
        #             return 3
        #         else:
        #             return 6
        # else:
        #     if origin_end[0][1][0] < 145 and origin_end[0][1][1] > 119:
        #         return 1
        #     if origin_end[0][1][0] > 145 and origin_end[0][1][1] < 119:
        #         return 8
        #     if origin_end[0][1][0] > 145 and origin_end[0][1][1] > 119:
        #         return 9

    return -1
            


# 	x_max = extreme[0]
# 	y_max = extreme[1]
# 	x_min = extreme[2]
# 	y_min = extreme[3]
# 	if x_max == x_min:
# 		x_max += 0.000000001
# 	if y_max == y_min:
# 		y_max += 0.000000001
# #	print(stop_time)
# 	# print(origin_end)
# 	for session in range(stop_time + 1):
# 		for j in range(2):
# #			print(session)
# #			print(j)
# 			origin_end[session][j] = ((origin_end[session][j][0] - x_min) / (x_max - x_min), 2 * (origin_end[session][j][1] - y_min) / (y_max - y_min))
# 	print(origin_end)
# 	if stop_time > 0:
# 		# The number is 4, 5, or 7
# 		if origin_end[0][0][1] < 0.25 and origin_end[1][1][1] < 0.25:
# 			return 5
# 		elif origin_end[0][1][0] > 0.8:
# 			return 4
# 		else:
# 			return 7
# 	else:
# 		# The number is 0, 1, 2, 3, 6, 8, or 9
# 		if math.sqrt((origin_end[0][0][0] - origin_end[0][1][0])**2 + (origin_end[0][0][1] - origin_end[0][1][1])**2) < 0.3:
# 			# The number is 0 or 8
# 			if origin_end[0][1][0] > 0.75:
# 				return 8
# 			else:
# 				return 0
# 		else:
# 			# The number is 1, 2, 3, 6, or 9
# 			if origin_end[0][0][0] < 0.3 and origin_end[0][1][0] < 0.3:
# 				return 3
# 			elif origin_end[0][0][0] > 0.6 and origin_end[0][1][0] > 0.6:
# 				return 9
# 			else:
# 				# The number is 1, 2, or 6
# 				if origin_end[0][0][1] > 0.1:
# 			   		return 2
# 				if origin_end[0][1][1] > 1.9:
# 					return 1
# 				else:
# 					return 6
# 	return -1
		
#	size = len(finger_pos)
#	finger_pos = normalize(finger_pos)
#	vector = [finger_pos[idx] - finter_pos[(idx + 1) % size] for idx in range(size)]
	# Count the number of straight line.
	# We define that two vectors belong to a straight line
	#		if the angle between them is less than 10 degree.
#	straight_line = []
#	switching_angle = []
#	switch_dist = []
#	for idx in range(size - 1):
#		outer_product = vector[idx][0] * vector[idx + 1][1] - vector[idx][1] * vector[idx + 1][0]
#		if outer_product > 0:
#		 	switching_angle.append(1)
#		else:
#			switching_angle.append(0)
#		switch_dist.append(sqrt((finger_pos[0][0] - finger_pos[idx][0])**2 + (finger_pos[0][1] - finger_pos[idx][1])**2))
#		inner_product = vector[idx][0] * vector[idx + 1][0] + vector[idx][1] * vector[idx + 1][1]
#		length_product = sqrt(vector[idx][0] ** 2 + vector[idx][1] ** 2) + sqrt(vector[idx + 1][0] ** 2 + vector[idx + 1][1] ** 2)
#		angle = innter_product / length_product
#		if angle > 0.98:
#			straight_line.append(1)
#		else:
#			straight_line.append(0)
#	straight_line_n = 0
#	for i in range(len(straight_line) - 1):
#		if straight_line[i] == straight_line[i + 1]:
#			continue
#		straight_line_n += 1
#	switching_angle_n = 0
#	for i in range(len(switching_angle) - 1):
#		if switching_angle[i] == switching_angle[i + 1]:
#			continue
#		switching_angle_n += 1
#	switch_dist_n = 0

	
	# start classifying
#	if sqrt(vector[size - 2][0] ** 2 + vector[size - 2][1] ** 2) < 0.3:
		# The number is 0 or 8
#		if switching_angle_n > 0:
#			return 8
#		else:
#			return 0
#	else:
		# 1, 2, 3, 4, 5, 6, 7, 9 remaining
#		if finger_pos[0][1] < 1 and finger_pos[size - 1][1] < 1:
			# The number is 5 or 6
#			if stop_time > 0:
#				return 5
#			else:
#				return 6
#		else:
			# 1, 2, 3, 4, 6, 7, 9 remaining
#			if switching_angle_n == 0:
				# The number is 1, 4, or 6.
#				if switch_dist == 0:
#					return 1
#				elif switch_dist < 4:
#					return 6
#				else:
#					return 4
#			elif switching_angle_n == 1:
				# The number is 2, 7, or 9.
#				if finger_pos[0][0] > 0.5 and finger_pos[size - 1][0] > 0.5:
#					return 9
#				elif stop_time == 0:
#				 		return 2
#				else:
#					return 7	
#			else:
#				return 3	
#	return -1
	



if __name__ == "__main__":
	oe1 = [[(1,3), (-2,-2)]]
	ex1 = [2, 3, -2, -5]
	st1 = 0
	oe1 = [[(100,33), (102,31)]]
	ex1 = [103, 34, 98, 30]
	st1 = 0
	oe1 = [[(0, 0), (1.5, -2)], [(1,0), (1,-4)]]
	ex1 = [1.5, 0, -2, -4]
	st1 = 1
	print(recognize_trace(oe1, ex1, st1))	