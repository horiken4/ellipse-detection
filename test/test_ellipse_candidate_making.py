# coding: utf-8

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
    # image = cv2.imread('../images/rot-ellipse.png', 1)
    # image = cv2.imread('../images/rot-ellipse-2.png', 1)

    image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    seg_det = ed.SegmentDetector()
    segments = seg_det.detect(image_gray)

    ellipse_cand_maker = ed.EllipseCandidateMaker()
    #debug_image = image.copy()
    #ellipse_cands = ellipse_cand_maker.make(segments, debug_image)
    ellipse_cands = ellipse_cand_maker.make(segments)

    print 'num ellipse candidates =', len(ellipse_cands)

    for ellipse_cand in ellipse_cands:
        image_ellipse_cand = image.copy()
        ellipse_cand.draw(image_ellipse_cand)
        cv2.imshow('ellipse candidate', image_ellipse_cand)
        cv2.waitKey(0)


if __name__ == '__main__':
    main()
