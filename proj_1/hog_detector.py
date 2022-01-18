import argparse
import time

import cv2
import imutils
import numpy
from imutils.object_detection import non_max_suppression

import printer

descriptor = cv2.HOGDescriptor()
descriptor.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


def hog_detector() -> None:
    args = vars(parse_args())
    image = resize_image(args['path'])
    detect_people(image, args['non_max_suppression'])


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog='hog_detector')
    parser.add_argument('--path', default=None, help='path to image file', required=True)
    parser.add_argument('--non-max-suppression', default=0, type=int, help='whether to apply non max suppression')
    return parser.parse_args()


def resize_image(image_path: str):
    image = cv2.imread(image_path)
    return imutils.resize(image, width=min(800, image.shape[1]))


def detect_people(image, non_max_suppression: int) -> None:
    start = time.time()

    coordinates, accuracies = descriptor.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale=1.03)
    coordinates = numpy.array([[x, y, x + w, y + h] for (x, y, w, h) in coordinates])
    if non_max_suppression:
        coordinates = apply_non_max_suppression(coordinates)

    end = time.time()

    count = printer.frame_detected_people(image, coordinates, accuracies, 0.7)
    printer.print_result(image, count, end - start)


def apply_non_max_suppression(coordinates) -> list:
    return non_max_suppression(coordinates, probs=None, overlapThresh=0.6)


if __name__ == "__main__":
    hog_detector()
