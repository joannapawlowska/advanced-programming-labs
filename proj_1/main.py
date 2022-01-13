import argparse
import time

import cv2
import numpy
import imutils
from imutils.object_detection import non_max_suppression


def detect(args):
    image = cv2.imread(args['path'])
    frame = imutils.resize(image, width=min(800, image.shape[1]))

    start = time.time()

    coordinates, weights = descriptor.detectMultiScale(frame, winStride=(4, 4), padding=(8, 8), scale=1.03)
    if args['non_max_suppression']:
        coordinates = apply_non_max_suppression(coordinates)

    end = time.time()

    count = 0
    for i, (x, y, w, h) in enumerate(coordinates):
        if weights[i] > 0.7:
            cv2.rectangle(frame, (x, y), (w, h), (255, 0, 0), 2)
            count += 1

    print(f'Total number of people \'{count}\' detected in time \'{(end - start):.4f}s\'')
    return frame


def apply_non_max_suppression(coordinates):
    coordinates = numpy.array([[x, y, x + w, y + h] for (x, y, w, h) in coordinates])
    return non_max_suppression(coordinates, probs=None, overlapThresh=0.6)


def print_result(image):
    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', default=None, help='path to image file', required=True)
    parser.add_argument('--non-max-suppression', default=0, type=int, help='whether to apply non max suppression')
    return parser.parse_args()


if __name__ == "__main__":
    descriptor = cv2.HOGDescriptor()
    descriptor.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    args = vars(parse_arguments())
    print_result(detect(args))
