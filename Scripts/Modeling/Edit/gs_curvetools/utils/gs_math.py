"""

License:
This collection of code named GS CurveTools is a property of George Sladkovsky (Yehor Sladkovskyi)
and can not be copied or distributed without his written permission.

GS CurveTools v1.3.1 Studio
Copyright 2023, George Sladkovsky (Yehor Sladkovskyi)
All Rights Reserved

Autodesk Maya is a property of Autodesk, Inc.

Social Media and Contact Links:

Discord Server:       https://discord.gg/f4DH6HQ
Online Store:         https://sladkovsky3d.artstation.com/store
Online Documentation: https://gs-curvetools.readthedocs.io/
Twitch Channel:       https://www.twitch.tv/videonomad
YouTube Channel:      https://www.youtube.com/c/GeorgeSladkovsky
ArtStation Portfolio: https://www.artstation.com/sladkovsky3d
Contact Email:        george.sladkovsky@gmail.com

"""

from PySide2 import QtGui


def lerp(x, y0, y1, x0=0, x1=1):
    """ Returns the value between y0 and y1 based on x in range of x0 and x1

    https://en.wikipedia.org/wiki/Linear_interpolation"""
    return float((y0 * (x1 - x) + y1 * (x - x0)) / (x1 - x0))


def quad(y1, y2, y3, fPoint, x1=0, x2=0.5, x3=1):
    """ Takes three points (y1, y2, y3) and returns a point on computed curve with fPoint """
    A = (x2 * (y1 - y3) + x3 * (y2 - y1)) / ((x1 - x2) * (x1 - x3) * (x2 - x3))
    B = (y2 - y1) / (x2 - x1) - A * (x1 + x2)
    C = y1
    return (A * (fPoint**2)) + (B * fPoint) + C


def dot(v1, v2):
    """ Dot product of two QVector2D """
    return QtGui.QVector2D.dotProduct(v1, v2)


def projectPoint(A, B, P):
    """ Project a point P onto a line made of two points A and B """
    A = QtGui.QVector2D(A)
    B = QtGui.QVector2D(B)
    P = QtGui.QVector2D(P)
    AP = A - P
    AB = A - B
    return (A - dot(AP, AB) / dot(AB, AB) * AB).toPointF()


def angleDiff(a1, a2):
    """ Find an absolute angle difference within 360 degrees"""
    a1 = a1 % 360
    a2 = a2 % 360
    return abs(a1) - abs(a2)
