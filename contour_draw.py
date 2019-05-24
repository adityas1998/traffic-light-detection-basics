import sys
import cv2
import numpy as np
import circles
# import matplotlib.pyplot as plt
def colour_detect(argv):
	if (len(sys.argv) < 1):
		print ('Not enough parameters')
		print ('Usage:\nmatch_template_demo.py <image_name> <template_name> [<mask_name>]')
		return -1
	image=cv2.imread(sys.argv[1])
	imgr=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
	lower_green = np.array([50,100,100])
	upper_green = np.array([90,255,255])
	lower_red = np.array([160,100,100])
	upper_red = np.array([180,255,255])
	lower_yellow = np.array([20,100,100])
	upper_yellow = np.array([30,255,255])

	# blurred=cv2.pyrMeanShiftFiltering(imgr,31,91)
	maskg = cv2.inRange(imgr, lower_green, upper_green)
	maskr =cv2.inRange(imgr, lower_red, upper_red)
	masky =cv2.inRange(imgr, lower_yellow, upper_yellow)
	# res=0
	ch=int(input("Enter choice no.:\n 1. Green \n 2. Red \n 3. Yellow \n"))
	if ch==1:
		res = cv2.bitwise_and(imgr,imgr,mask= maskg)
	elif ch==2:
		res = cv2.bitwise_and(imgr,imgr,mask= maskr)
	elif ch==3:
		res = cv2.bitwise_and(imgr,imgr,mask= masky)
	# res = cv2.bitwise_and(imgr,imgr,mask= maskg)
	x=cv2.split(res)
	ret,thresh1 = cv2.threshold(x[2],127,255,cv2.THRESH_TOZERO)
	# im2=cv2.imwrite("thresh.jpg",thresh1)
	# im3=cv2.imread("thresh.jpg")
	circles.circles(thresh1)
	# gray=cv2.cvtColor(blurred,cv2.COLOR_BGR2GRAY)
	# ret,thresh=cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	# _,contours,_=cv2.findContours(thresh1,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
	# # print(len(contours))
	# print("No. of contours:",len(contours))
	# cv2.drawContours(image,contours,-1,	(255,140,0),6)
	# cv2.namedWindow("Display",cv2.WINDOW_NORMAL)
	# # cv2.imshow("Display",image)
	# cv2.imshow("Display",thresh1)
	# cv2.namedWindow("HSV",cv2.WINDOW_NORMAL)
	# cv2.imshow("HSV",imgr)
	# cv2.namedWindow("image",cv2.WINDOW_NORMAL)
	# cv2.imshow("image",image)
	# cv2.waitKey()
if __name__=="__main__":
	colour_detect(sys.argv[1:])
