import cv2
import matplotlib.pyplot as plt
from ex_1 import read_from_image, read_from_image_with_invert, read_from_image_with_bilateral_filter

path_img_1 = './img/img-1.png'
path_img_2 = './img/img-2.png'
path_img_3 = './img/img-3.png'
path_img_4 = './img/img-4.png'
path_img_5 = './img/img-5.png'

print('### image 1 ###')
plt.imshow(cv2.imread(path_img_1))
plt.show()
print(read_from_image(path_img_1))

print('### image 2 ###')
plt.imshow(cv2.imread(path_img_2))
plt.show()
print(read_from_image(path_img_2))

print('### image 3 ###')
plt.imshow(cv2.imread(path_img_3))
plt.show()
print(read_from_image_with_invert(path_img_3))

print('### image 4 ###')
plt.imshow(cv2.imread(path_img_4))
plt.show()
print(read_from_image(path_img_4))

print('### image 5 ###')
plt.imshow(cv2.imread(path_img_5))
plt.show()
print(read_from_image_with_bilateral_filter(path_img_5))
