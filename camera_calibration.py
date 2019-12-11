import numpy as np
import cv2
import glob
import sys

blocksize = 25 #mm
pxmm = 1.12*0.001# px size in mm

# 캘리브리션 이미지의 가로 - 1, 세로 - 1 값을 적습니다.
cbrow = 8
cbcol = 6

if len(sys.argv) == 2: #if the user has provided enough arguments
    #extract the arguments
    imagefolder = sys.argv[1]
    print("folder name" + imagefolder)
else:
    print ("Please use as following: calibrate.py imagefolder [lsd_cal_output_folder/name]")
    sys.exit

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
print ("preparing opject points")

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((cbrow * cbcol, 3), np.float32)
objp[:,:2] = np.mgrid[0:cbcol, 0:cbrow].T.reshape(-1,2)
objp = objp * blocksize #resize to m

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.
print ("retrieving images")

# 찍은 사진의 확장자에 맞게 바꿔주어야 합니다.
#imgnames = imagefolder + '/*.JPG'
imgnames = imagefolder + '*.jpg'

images = glob.glob(imgnames)
print (str(len(images))+" images retrieved as: "+ imgnames)

if len(images)<1:
    print ("There are no images in this directory:" + imgnames)
    sys.exit

# Create a Window
cv2.startWindowThread()
cv2.namedWindow('img',cv2.WINDOW_NORMAL)
cv2.resizeWindow('img', 800, 450)
i = 0

for fname in images:
    i += 1
    print ("starting processing image number: "+ str(i))
    #read image and convert to grayscale image
    img = cv2.imread(fname)
#    img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, (cbcol, cbrow), None)
    # If found, add object points, image points (after refining them)

    if ret == True:
        print("Corners are found\n")
        objpoints.append(objp)
        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        imgpoints.append(corners2)
        # Draw and display the corners
        img = cv2.drawChessboardCorners(img, (cbcol, cbrow), corners2,ret)
        cv2.imshow('img',img)
        cv2.waitKey(500)

print ("done processing the images")
cv2.destroyAllWindows()

print()
print ("starting calibrations")
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)

print ("finished calibrations\n\n")
print ("The camera matrix in px is: ")
print (mtx)
print ()

# print "The camera matrix in mm is: "
# mtxmm = mtx * pxmm
# print mtxmm
print ("The disortion coefficients are: ")
print (dist)

# print "The rotation vector is: "
# print rvecs
# print "The translation vector is: "
# print tvecs36
