#----------------------------------------------------------------------
# This file was generated by C:\Python24\Scripts\img2py
#
from wx import ImageFromStream, BitmapFromImage
import cStringIO, zlib


def getDosData():
    return zlib.decompress(
'x\xda\x01\x84\x01{\xfe\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\
\x00\x00\x00\x10\x08\x02\x00\x00\x00\x90\x91h6\x00\x00\x00\x03sBIT\x08\x08\
\x08\xdb\xe1O\xe0\x00\x00\x01<IDAT(\x91\x8d\x8f1K\x03A\x10\x85\xdf\xecN\x82\
\x85Q\x13"i\x12H\xab\x90\xc2\xc2\x14Z\x8aplg\xe1_\xf27\xf8\x03\xec\xec,\x8e \
X\xd9i\x91R\x83\x10\xd0*\x08\x8a\x9a(\x98\xbb\x9d\xb1\xb8\xb8\t\xf1\x12|\xc5\
\xf2\xd8\xfdf\xde[:8\xf9\x00\x00\xc0{\x9d\x18\xb5X,\xf6\x1e")A\xa7\xa8&y$\
\x11Y\x10\xb8\x7f\x7fU)\x97\x0c1\xa0\xd3\xd7_[`\xab\x00\x19p2\x1c\xbc\x0c\
\xd7k;\xfc]o\r6\xab\x10\xffw\xa7*\x0e\xb7K\xa31m\x14}\xfb\xe1\xfc\xecM\x1e{\
\x97\xdc\xd2\x9b\xd7\xee\xad\xb1\xc5\xdc\xc6\xfd;(\xf0\x0c<\xe9\xd7\xfb\xa8&\
\x89\xe1\xb4w\xdd\xbd8]\xf2\xcb\xa0\xea\xd6\xd1Js\xcfx%\x00Q\x14\x89\x88\x88\
DQ\x14\x08\x11\x99k\x08\x85\x914\x05\x10\xc7\xb1s\xce9\x17\xc7\xf1,:;\x9f\
\x89\x83\xebt:\x00\x8c1\xe1\xcc\xe63\x1fd\x0csX\x96\x15\x0b\t\xd9\x8a\xb9\
\x90\t\x1d\xca8\xe7BBn\x08\x87>s\xd1\x8b\xee\rS\x0e\x97+C\xa4P\x1e\x16\x1a\
\xcd\xddck\x0b\xcbi\x82$\xc5z"\x9e?\xcbm6uM\tV\x97\x0c(\x885Y\xad4y\xad\xb1\
\x8f\x06\x00\x18\x19\xff\xa7\xd8\x0f\xe9v\x8bL\x17_k\xac\x00\x00\x00\x00IEND\
\xaeB`\x821\x01\x9eY' )

def getDosBitmap():
    return BitmapFromImage(getDosImage())

def getDosImage():
    stream = cStringIO.StringIO(getDosData())
    return ImageFromStream(stream)
