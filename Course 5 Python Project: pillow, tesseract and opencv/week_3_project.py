# # The Project #
# 1. This is a project with minimal scaffolding. Expect to use the the discussion forums
# to gain insights! It’s not cheating to ask others for opinions or perspectives!
# 2. Be inquisitive, try out new things.
# 3. Use the previous modules for insights into how to complete the functions! You'll have
# to combine Pillow, OpenCV, and Pytesseract
# 4. There are hints provided in Coursera, feel free to explore the hints if needed. Each
# hint provide progressively more details on how to solve the issue. This project is intended
# to be comprehensive and difficult if you do it without the hints.
# ### The Assignment ###
# Take a [ZIP file](https://en.wikipedia.org/wiki/Zip_(file_format)) of images and process
# them, using a [library built into python](https://docs.python.org/3/library/zipfile.html)
# that you need to learn how to use. A ZIP file takes several different files and compresses
# them, thus saving space, into one single file. The files in the ZIP file we provide are
# newspaper images (like you saw in week 3). Your task is to write python code which allows
# one to search through the images looking for the occurrences of keywords and faces. E.g. if
# you search for "pizza" it will return a contact sheet of all of the faces which were
# located on the newspaper page which mentions "pizza". This will test your ability to learn
# a new ([library](https://docs.python.org/3/library/zipfile.html)), your ability to use
# OpenCV to detect faces, your ability to use tesseract to do optical character recognition,
# and your ability to use PIL to composite images together into contact sheets.
# Each page of the newspapers is saved as a single PNG image in a file
# called [images.zip](./readonly/images.zip). These newspapers are in english, and contain
# a variety of stories, advertisements and images. Note: This file is fairly large (~200 MB)
# and may take some time to work with, I would encourage you to use
# [small_img.zip](./readonly/small_img.zip) for testing.
# Here's an example of the output expected. Using the [small_img.zip](./readonly/small_img.zip)
# file, if I search for the string "Christopher" I should see the following image:
# ![Christopher Search](./readonly/small_project.png)
# If I were to use the [images.zip](./readonly/images.zip) file and search for "Mark" I should
# see the following image (note that there are times when there are no faces on a page,
# but a word is found!):
# ![Mark Search](./readonly/large_project.png)
# Note: That big file can take some time to process - for me it took nearly ten minutes!
# Use the small one for testing.
import zipfile
import os
from PIL import Image
import tesserocr

# or import pytesseract
import cv2 as cv
import numpy as np


def main():
    # loading the face detection classifier
    face_cascade = cv.CascadeClassifier(
        "./readonly/haarcascade_frontalface_default.xml"
    )
    # for testing use small_img.zip
    LOCAL_ZIP = "./readonly/images.zip"
    with zipfile.ZipFile(LOCAL_ZIP, "r") as zip_ref:
        # for testing use zip_ref.extractall("small_img")
        zip_ref.extractall("images")
    # append to list that contains the images names
    # for testing use pages_list=os.listdir('small_img')
    pages_list = os.listdir("images")
    sheet_list = []
    for page_name in pages_list:
        img_and_desc_list = []
        # for testing use img = Image.open('small_img/'+page_name)
        img = Image.open("images/" + page_name)
        # if using pytesseract module instead of tesserocr
        # image_string = pytesseract.image_to_string(img)
        # tesseract is kind of a weird module. see https://stackoverflow.com/questions/50655738/how-do-i-resolve-a-tesseractnotfounderror if you get any errors
        # you can use pytesseract as directed by the course but it is slow due to long I/O
        api = tesserocr.PyTessBaseAPI()
        api.SetImage(img)
        text_ = api.GetUTF8Text()
        desc = text_.replace("\n", "")
        img_and_desc_list.append(page_name)
        img_and_desc_list.append(desc)
        sheet_list.append(img_and_desc_list)

    def search(text: str, folder: str) -> any:
        """searches for text in folder and displays relevant face"""
        for element in sheet_list:
            if text in element[1]:
                print(f"Result found in file {element[0]}")
            else:
                print(f"Result not found in file {element[0]}")
            try:
                img2 = Image.open(str(folder + element[0]))
                array_of_images = np.array(img2)
                # use img2 instead of face_cascade.detectMultiScale(array_of_images,1.35,4)
                faces_func = face_cascade.detectMultiScale(array_of_images, 1.35, 4)
                faces = faces_func.tolist()
                # storing the bounding boxes of all faces detected in each image iteration
                faces_in_each = []
                for x_coordinate, y_coordinate, width, height in faces:
                    cropped_images = img2.crop(
                        (
                            x_coordinate,
                            y_coordinate,
                            x_coordinate + width,
                            y_coordinate + height,
                        )
                    )
                    faces_in_each.append(cropped_images)
                sheet_length = len(faces_in_each) / 5
                sheet_length_limit = np.ceil(sheet_length)
                sheet_size = (550, 110 * int(sheet_length_limit))
                contact_sheet = Image.new(img2.mode, sheet_size)
                x_coordinate2 = 0
                y_coordinate2 = 0
                for face in faces_in_each:
                    face.thumbnail((110, 110))
                    contact_sheet.paste(face, (x_coordinate2, y_coordinate2))
                    if x_coordinate2 + 110 == contact_sheet.width:
                        x_coordinate2 = 0
                        y_coordinate2 = y_coordinate2 + 110
                    else:
                        x_coordinate2 = x_coordinate2 + 110
                return contact_sheet.show()
            except:
                return "no faces detected"

    search(text="Mark", folder="images/")


if __name__ == "__main__":
    main()
