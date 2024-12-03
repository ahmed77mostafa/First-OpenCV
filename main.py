import cv2
import  numpy
import matplotlib.pyplot as plt

arr = numpy.array([1,2,3,4,5])
arr2 = numpy.array( [[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(arr)
print(type(arr))
print(numpy.__version__)
print(arr2)

image = cv2.imread("D:\Wallpaper\dead guy.jpg")
cv2.imshow("dead guy",image)
cv2.waitKey(0)
cv2.destroyAllWindows()