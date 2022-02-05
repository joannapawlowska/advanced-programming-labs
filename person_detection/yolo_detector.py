import argparse
import time

import cv2
import numpy
from numpy import shape

import printer

person_class_id = 0
net = cv2.dnn.readNet('data/yolov3.weights', 'data/yolov3.cfg')
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]


def yolo_detector() -> None:
    args = vars(parse_args())
    image = resize_image(args['path'])
    detect_people(image, args['gpu'])


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog='yolo_detector')
    parser.add_argument('--path', default=None, help='path to image file', required=True)
    parser.add_argument('--gpu', default=0, type=int, help='whether to use GPU support')
    return parser.parse_args()


def resize_image(image_path: str) -> {shape}:
    image = cv2.imread(image_path)
    size = min(800, image.shape[1])
    return cv2.resize(image, (size, size))


def detect_people(image: {shape}, gpu: int) -> None:
    if gpu:
        net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
        net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

    height, width = image.shape[:2]

    start = time.time()

    blob = cv2.dnn.blobFromImage(image, 1 / 255, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    output = net.forward(output_layers)

    end = time.time()

    coordinates, accuracies = extract_detection_results(output, width, height)
    count = printer.frame_detected_people(image, coordinates, accuracies, 0.9)
    printer.print_result(image, count, end - start)


def extract_detection_results(output, width: int, height: int) -> (list[int], list[float]):
    coordinates = []
    accuracies = []

    for out in output:
        for detection in out:

            scores = detection[5:]
            class_id = numpy.argmax(scores)

            if class_id == person_class_id:
                box = detection[0:4] * numpy.array([width, height, width, height])
                (center_x, center_y, w, h) = box.astype('int')
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                coordinates.append([x, y, int(w) + x, int(h) + y])
                accuracies.append(scores[class_id])

    box = cv2.dnn.NMSBoxes(coordinates, accuracies, 0.6, 0.7).flatten()
    return [coordinates[i] for i in box], [accuracies[i] for i in box]


if __name__ == "__main__":
    yolo_detector()
