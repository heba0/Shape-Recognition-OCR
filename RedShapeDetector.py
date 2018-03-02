import cv2
 
class ShapeDetectorRed:
	def __init__(self):
		pass
 
	def detect(self, c):
		# initialize the shape name and approximate the contour
		shape = "unidentified"
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.04 * peri, True)
		# if the shape is a triangle, it will have 3 vertices
		if len(approx) == 3:
			shape = "Red triangle- PLANE A"
 
		# if the shape has 4 vertices, it is either a square or
		# a rectangle
		elif len(approx) == 4:
			# compute the bounding box of the contour and use the
			# bounding box to compute the aspect ratio
			(x, y, w, h) = cv2.boundingRect(approx)
			ar = w / float(h)
 
			# a square will have an aspect ratio that is approximately
			# equal to one, otherwise, the shape is a rectangle
			#shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"
			shape = "Red Rectangle - PLANE D"
 
		# if the shape is a pentagon, it will have 5 vertices
		elif len(approx) == 5: #pentagon
			shape = "Red Rectangle - PLANE D"
 
		# otherwise, we assume the shape is a circle
		else:
			shape = "Red Circle"
 
		# return the name of the shape
		#print shape
		return shape

