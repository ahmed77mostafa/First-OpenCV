import cv2 as cv

image = cv.imread("C:/Users/ahmed.mostafa/PycharmProjects/OpenCV_Project/images/dead guy.jpg")
cv.imshow("dead guy",image)
img_RGB = cv.cvtColor(image,cv.COLOR_BGR2RGB)
cv.imshow("dead guy RGB",img_RGB)
img_gray = cv.cvtColor(image,cv.COLOR_RGB2GRAY)
cv.imshow("dead guy GRAY", img_gray)

cv.imwrite('C:/Users/ahmed.mostafa/PycharmProjects/OpenCV_Project/saved images/img_RGP.png',img_RGB)
cv.waitKey(0)
cv.destroyWindow("dead guy")