import sys
import os
from iptcinfo3 import IPTCInfo
from PIL.PngImagePlugin import PngImageFile, PngInfo
from imgtag import ImgTag


def win_addInfo(F, TagList):
    filename, file_extension = os.path.splitext(F)

    jpg_exts = [".jpg", ".jpeg", ".jfif"]
    if file_extension.lower() == ".png":
        test = ImgTag(filename=F)

        test.set_tags(TagList)
        test.close()

    elif file_extension.lower() in jpg_exts:
        info = IPTCInfo(F)
        info['keywords'] = TagList
        info.save()
        os.remove(F + '~')

    else:
        print("INVALID FILE")
