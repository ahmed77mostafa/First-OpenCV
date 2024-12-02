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
# Loading the image

half = cv2.resize(image, (0, 0), fx = 0.1, fy = 0.1)
bigger = cv2.resize(image, (1050, 1610))

stretch_near = cv2.resize(image, (780, 540),
               interpolation = cv2.INTER_LINEAR)


Titles =["Original", "Half", "Bigger", "Interpolation Nearest"]
images =[image, half, bigger, stretch_near]
count = 4

for i in range(count):
    plt.subplot(2, 2, i + 1)
    plt.title(Titles[i])
    plt.imshow(images[i])

plt.show()