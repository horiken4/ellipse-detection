#  coding: utf-8

import sys
sys.path.append('..')

import cv2

import ellipse_detection as ed


def main():
    image = cv2.imread('../images/493.jpg', 1)
    # image = cv2.imread('../images/sP1010080.jpg', 1)
    # image = cv2.imread('../images/20091031193703238.jpg', 1)
    # image = cv2.imread('../images/KM-612.jpg', 1)
    # image = cv2.imread('../images/49days-301.jpg', 1)
    # image = cv2.imread('../images/ellipse.png', 1)
    # image = cv2.imread('../images/83I83Z838D82P89F196DA81B.JPG', 1)
    # image = cv2.imread('../images/20120827-003.jpg', 1)
    # image = cv2.imread('../images/ellipse2.png', 1)
    # mage = cv2.imread('../images/rot-ellipse.png', 1)
    # image = cv2.imread('../images/rot-ellipse-2.png', 1)

    image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    ellipse_detector = ed.EllipseDetector()
    ellipses = ellipse_detector.detect(image_gray)

    for ellipse in ellipses:
        image_ellipse = image.copy()
        ellipse.draw(image_ellipse)
        cv2.imshow('ellipse', image_ellipse)
        cv2.waitKey(0)


if __name__ == '__main__':
    main()
