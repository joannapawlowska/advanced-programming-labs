import cv2
from numpy import shape

FRAME_COLOR = (255, 0, 0)
TEXT_COLOR = (255, 255, 255)


def frame_detected_people(image: {shape}, coordinates: list[list[int]], accuracies: list[float], min: float) -> int:
    count = 0

    for i, (x, y, w, h) in enumerate(coordinates):
        accuracy = accuracies[i]

        if accuracy > min:
            text = f'{accuracy:.4f}'
            box_size = calculate_text_box_size(x, y, text)
            cv2.rectangle(image, (x, y), (w, h), FRAME_COLOR, 2)
            cv2.rectangle(image, box_size[0], box_size[1], FRAME_COLOR, cv2.FILLED)
            cv2.putText(image, text, (x, y - 2), cv2.FONT_HERSHEY_SIMPLEX, 0.4, TEXT_COLOR, 1)

            count += 1

    return count


def calculate_text_box_size(x: int, y: int, text: str) -> [(int, int), (int, int)]:
    (width, height) = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, fontScale=1.0, thickness=1)[0]
    return [(x, y), (x + width - 65, y - height + 4)]


def print_result(image, count: int, time: float) -> None:
    print(f'Total number of people \'{count}\' detected in time \'{time:.4f}s\'')
    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
