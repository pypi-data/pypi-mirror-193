from random import randint

__all__ = ["idx2color"]

COLORMAP = [
    (255, 0, 255),
    (0, 255, 0),
    (0, 128, 255),
    (255, 255, 0),
    (0, 255, 255),
    (255, 128, 255),
    (128, 255, 0),
    (255, 0, 128),
    (128, 255, 255),
    (255, 255, 255),
    (255, 255, 128),
    (255, 128, 0),
    (128, 0, 255),
    (0, 0, 255),
    (0, 255, 128),
    (255, 0, 0)
]


def idx2color(idx):
    if idx == -1:
        return tuple(randint(0, 255) for _ in range(3))
    else:
        return COLORMAP[idx % len(COLORMAP)]
