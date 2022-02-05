import cv2
import matplotlib.pyplot

# reading image
img = cv2.imread('./img/img-1.png')

# representing image in numbers
print(type(img))
print(img.shape)

# printing image
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# displaying image with matplotlib
matplotlib.pyplot.imshow(img)
matplotlib.pyplot.show()
