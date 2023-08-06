import cv2
import numpy as np
from jcopvision.utils import denormalize_image, idx2color

__all__ = ["draw_single_circle"]


def draw_single_circle(frame, center, radius, color=-1, thickness=1):
    '''
    Draw a circle


    === Input ===
    frame: array
        image / frame to be drawn

    center: (int, int) or (float, float)
        location to draw the circle.

    color: int or (int, int, int)
        The color of the circle
        If int, it would be map to default colormap using jcopvision.utils.idx2color. Use -1 for random color.
        If (int, int, int), color in BGR format

    thickness: int
        The circle and text thickness


    === Return ===
    frame: array
        annotated image / frame
    '''
    frame = frame.copy()
    frame = denormalize_image(frame)

    if isinstance(color, int):
        color = idx2color(color)

    center = tuple(np.array(center).astype(int))
    cv2.circle(frame, center, radius, color, thickness)
    return frame
