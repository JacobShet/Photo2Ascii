from PIL import Image
import argparse
import math
import os

# region argParser
argParser = argparse.ArgumentParser()
argParser.add_argument("imageName")
argParser.add_argument("-o", "--output", help="sets the output directory", default=".")
sizingGroup = argParser.add_mutually_exclusive_group()
sizingGroup.add_argument("-x", "--width", type=int, help="sets the width", default=120)
sizingGroup.add_argument("-y", "--height", type=int, help="sets the height")
args = argParser.parse_args()
# endregion argParser


# region image
def resize_img(img: Image.ImageFile.ImageFile):
    width = args.width
    height = args.height
    if height != None:
        aspectRatio = height / img.height
        width = math.floor(img.width * aspectRatio)
    else:
        aspectRatio = width / img.width
        height = math.floor(img.height * aspectRatio)
    return img.resize((width, height))


try:
    imageNameWithExt = os.path.basename(args.imageName)
    # file,ext = os.path.splitext(imageNameWithExt)
    with Image.open(args.imageName) as img:
        outputFile = os.path.join(args.output, imageNameWithExt)
        img = resize_img(img)
        print("Image successfully loaded! " + str(img.width) + " " + str(img.height))
        print(outputFile)
        img.save(outputFile)
except FileNotFoundError:
    print("Error: Image not found")
except Exception as e:
    print(f"An error occured: {e}")


# endregion image
