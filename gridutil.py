"""
/***************************************************************************
 util - Utility functions and classes.
                                 A QGIS plugin
 Overlays a user-definable grid on the map.
                             -------------------
        begin                : 2012-05-30
        copyright            : (C) 2012 by John Donovan
        email                : mersey.viking@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import math

class QgsVector(object):
  """2D vector class with (almost) the same signature as the QGIS one."""
  def __init__(self, x=0.0, y=0.0):
    self.x = x
    self.y = y

  def __neg__(self):
    return QgsVector(-self.x, -self.y)

  def __mul__(self, scalar):
    return QgsVector(self.x * scalar, self.y * scalar)

  def __div__(self, scalar):
    return QgsVector(self.x, self.y) * (1.0 / scalar)

  def __add__(self, v):
    return QgsVector(self.x + v.x, self.y + v.y)

  # Vector dot product.
  def __and__(self, v):
    return self.x * v.x + self.y * v.y

  def length(self):
    return math.sqrt(self.x * self.x + self.y * self.y)

  def perpVector(self):
    return QgsVector(-self.y, self.x)

  def angle(self, v=None):
    if v is None:
      ang = math.atan2(self.y, self.x)
      return ang + 2.0 * math.pi if ang < 0.0 else ang
    else:
      return v.angle() - self.angle()

  def rotateBy(self, rot):
    ang = math.atan2(self.y, self.x) + rot
    length = self.length()
    return QgsVector(length * math.cos(ang), length * math.sin(ang))

  def normal(self):
    if self.length() == 0.0:
      raise

    return QgsVector(self.x, self.y) / self.length()

class Angle():
    cardinals = ('N', 'E', 'S', 'W')

    def __init__(self, degrees):
        round(degrees, 6)
        self.sign = '-' if degrees < 0.0 else ''
        decimal_degrees = math.fabs(degrees) % 360.0
        self.angle = -decimal_degrees if degrees < 0.0 else decimal_degrees
        self.degrees, self.fracDegrees = divmod(decimal_degrees, 1.0)
        self.minutes, self.fracMinutes = divmod(self.fracDegrees * 60.0, 1.0)
        self.seconds, self.fracSeconds = divmod(self.fracMinutes * 60.0, 1.0)

    def __format__(self, format_spec):
        s = ''
        b, m, e = format_spec.partition('%')

        while e != '':
            pad = False
            precision = 0
            s += b

            precPos = 0
            while e[precPos].isdigit():
                precPos += 1

            precString = e[:precPos]

            if precString != '':
                if precString[0] == '0':
                    pad = True

                precision = int(precString)

            spec = e[precPos]

            if spec == 'g':
                s += self.sign
            elif spec == 'D':
                if pad:
                    s += str(int(self.degrees)).zfill(3)
                else:
                    s += str(int(self.degrees))
            elif spec == 'd':
                s += '{0:f}'.format(self.fracDegrees).ljust(2 + precision, '0')[2:2 + precision]
            elif spec == 'M':
                if pad:
                    s += str(int(self.minutes)).zfill(2)
                else:
                    s += str(int(self.minutes))
            elif spec == 'm':
                s += '{0:f}'.format(self.fracMinutes).ljust(2 + precision, '0')[2:2 + precision]
            elif spec == 'S':
                if pad:
                    s += str(int(self.seconds)).zfill(2)
                else:
                    s += str(int(self.seconds))
            elif spec == 's':
                s += '{0:f}'.format(self.fracSeconds).ljust(2 + precision, '0')[2:2 + precision]
            elif spec == 'n':
                if self.sign == '':
                    s += Angle.cardinals[0]
                else:
                    s += Angle.cardinals[2]
            elif spec == 'e':
                if self.sign == '':
                    s += Angle.cardinals[1]
                else:
                    s += Angle.cardinals[3]
            else:
                raise ValueError("Invalid format specifier '%c'" % spec)

            b, m, e = e[precPos + 1:].partition('%')

        s += b
        return s

from qgis import core
from mgrs import MGRS
import re

class MgrsTool():
  ct = MGRS()
  epsg4326 = core.QgsCoordinateReferenceSystem("EPSG:4326")
  re_mgrs = re.compile('([0-9]{1,2})([A-Z]+)([0-9]*)')

  def toMgrs(self, pt):
#        canvas = iface.mapCanvas()
        canvas = qgis.utils.iface.mapCanvas()

#        canvasCrs = canvas.mapRenderer().destinationCrs()

        try:
             canvasCrs = canvas.mapSettings().destinationCrs()
        except:
             canvasCrs = canvas.mapRenderer().destinationCrs()

        transform = QgsCoordinateTransform(canvasCrs, self.epsg4326)
        pt4326 = transform.transform(pt.x(), pt.y())

        try:
            mgrsCoords = self.ct.toMGRS(pt4326.y(), pt4326.x())
        except:
            mgrsCoords = None

        return mgrsCoords

# MGRS 54SVG999574 / zone:'54', letters:'SVG', easting: '999', northing: '574'
# The function Break_MGRS_String breaks down an MGRS
# coordinate string into its component parts.
#   MGRS           : MGRS coordinate string          (input)
#   Zone           : UTM Zone                        (output)
#   Letters        : MGRS coordinate string letters  (output)
#   Easting        : Easting value                   (output)
#   Northing       : Northing value                  (output)
#   Precision      : Precision level of MGRS string  (output)

  def parseMGRS(self, mgrs):
        m = re_mgrs.match(mgrs)
        zone = m.group(0)
        letters = m.group(1)
        nums = m.group(2)
        precision = len(nums) / 2
        if precision>0:
            Easting = nums[0:precision]
            Northing = nums[precision+1,precision*2]
        else:
            Easting = ''
            Northing = ''

        return ( zone, letters, easting, nothing, precision )
