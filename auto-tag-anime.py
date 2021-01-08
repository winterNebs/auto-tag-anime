import tag
import subprocess
import model
import sys
import os
import argparse
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


class addAnimeTags():
    def __init__(self, skip=False):
        self.model = model.deepdanbooruModel()
        self.skip=skip

    def navigateDir(self, path):
        if os.path.isdir(path):
            for root, dirs, files in os.walk(path):
                for filename in files:
                    print(self.addTagsToImage(
                        os.path.normpath(root + '/' + filename)))
        else:
            print(self.addTagsToImage(path))

    def addTagsToImage(self, path):

        exts = [".png", ".lep", ".jpg", ".jpeg", ".jfif"]
        filename, file_extension = os.path.splitext(path)
        if file_extension.lower() not in exts:
            return 'invalid file type'

        new_path = path
        if file_extension.lower() == ".lep":
            # convert to jpg temperarily
            new_path = filename + ".jpg"
            completed = subprocess.run(["./lepton-slow-best-ratio", path, "-o", new_path])

            if completed.returncode != 0:
                return 'failed to add tags for ' + path

        # skip if has tag
        if self.skip and tag.check_tag(new_path):
            if file_extension.lower() == ".lep":
                # remove jpg
                os.remove(new_path)
            return "has tag at " + path

        status, tags = self.model.classify_image(new_path)
        if status == 'success':
            self.add_tags(new_path, tags)
            if file_extension.lower() == ".lep":
                # convert jpg back to lep
                completed = subprocess.run(["./lepton-slow-best-ratio", new_path, "-o", path])
                # remove jpg
                os.remove(new_path)

            return 'added ' + str(len(tags)) + ' tags to ' + path
        else:
            return 'failed to add tags for ' + path

    def add_tags(self, file, tags):
        tag.win_addInfo(file, tags)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automatically tag images")
    parser.add_argument("path", metavar="P", type=str, help="Path to directory or image")
    parser.add_argument("--skip", dest="skip", action="store_true",help="Skip already tagged images")
    args=parser.parse_args();
    addAnimeTags = addAnimeTags(args.skip)
    addAnimeTags.navigateDir(args.path)
