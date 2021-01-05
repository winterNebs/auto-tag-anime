import tag
import subprocess
import model
import sys
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


class addAnimeTags():
    def __init__(self):
        self.model = model.deepdanbooruModel()
        pass

    def navigateDir(self, path):
        if os.path.isdir(path):
            for root, dirs, files in os.walk(path):
                for filename in files:
                    print(self.addTagsToImage(
                        os.path.normpath(root + '/' + filename)))
        else:
            print(self.addTagsToImage(path))

    def addTagsToImage(self, path):

        # goals:
        # 1. figure out paths?
        # 2. figure out tagging
        # testing here
        # self.add_tags(path,["test"])
        exts = [".png", ".lep", ".jpg", ".jpeg", ".jfif"]
        filename, file_extension = os.path.splitext(path)
        if file_extension.lower() not in exts:
            return 'invalid file type'

        # if file_extension.lower() == ".lep":
        #     # convert to jpg temperarily
        #     subprocess.run(["./lepton-slow-best-ratio.exe", path])
        #     # eval then add tags
        #     # convert back

        status, tags = self.model.classify_image(path)
        if status == 'success':
            self.add_tags(path, tags)
            return 'added ' + str(len(tags)) + ' tags to ' + path
        else:
            return 'failed to add tags for ' + path

    def add_tags(self, file, tags):
        tag.win_addInfo(file, tags)


def parseArgs():
    if len(sys.argv) < 2:
        print("no path")
        sys.exit()

    if not os.path.exists(sys.argv[1]):
        print('path does not exist')
        sys.exit()


if __name__ == "__main__":
    parseArgs()
    addAnimeTags = addAnimeTags()
    addAnimeTags.navigateDir(sys.argv[1])
