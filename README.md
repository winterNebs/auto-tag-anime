# Auto Anime Tag

## Changes in this fork:

This fork rewrites tag handling and adds support for lepton files. Only compatible with linux unfortunately. (If you can get exempi to compile on windows then it may work but I gave up)

## Original description

Automatically adds booru style tags to an image or directory of images by using this neural net model: https://github.com/KichangKim/DeepDanbooru

## Instructions

**You will need**:
- lepton https://github.com/dropbox/lepton, follow instructions and build, then put in auto-anime-tag folder
- pre-trained model deepdanbooru-v3 from https://github.com/KichangKim/DeepDanbooru, grab the model from the 'releases' section, or train your own, put the files in `auto-anime-tag/deep`
- Exempi, install with your package manager
- Python 3.8 (3.9 will not work for now)

1. `git clone https://github.com/winterNebs/auto-tag-anime.git`
2. `cd auto-tag-anime`
3. `python3.8 -m pip install -r requirements.txt`

## How to use
`python3 auto-tag-anime.py "example.jpg"`

`python3 auto-tag-anime.py "/path/to/directory/"`


## Notes
* See a list of tags the model will predict in 'tags.txt' inside of the deepdanbooru-v3 folder
* checks for images in subdirectories 
