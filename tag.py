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
        try:
            info = IPTCInfo(F)
            info['keywords'] = TagList
            info.save()
            os.remove(F + '~')
        except:
            print("IPTC ERROR")
            return

    else:
        print("INVALID FILE")


def check_tag(F):
    filename, file_extension = os.path.splitext(F)

    jpg_exts = [".jpg", ".jpeg", ".jfif"]
    if file_extension.lower() == ".png":
        test = ImgTag(filename=F)
        result = (len(test.get_tags()) > 0)
        test.close()
        return result

    elif file_extension.lower() in jpg_exts:
        try:
            info = IPTCInfo(F)
            return len(info['keywords'])
        except:
            return False

    else:
        return False
