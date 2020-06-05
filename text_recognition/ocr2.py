# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/6/4 16:42
filename(文件名): ocr2.py
function description(功能描述):
...
    APP_ID = "20227038"
    API_KEY = "tuQ3GPXA7Qt9uHKtahZgoUwn"
    SECRET_KEY = "hoGMLSu2cNt5ttfVl2hGnMCKQtoSMO5N"
"""
from PIL import ImageGrab
import shutil
from aip import AipOcr
import keyboard
import os
import time
import cv2 as cv

APP_ID = "20227038"
API_KEY = "tuQ3GPXA7Qt9uHKtahZgoUwn"
SECRET_KEY = "hoGMLSu2cNt5ttfVl2hGnMCKQtoSMO5N"
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
Count = 1
From_initial = True


def able_to_read(path):
    """
    给定一张图像的路径，判断该图像是否可读。
    :param path:
    :return:
    """
    if os.path.isfile(path):
        paths = [path]
    else:
        paths = [os.path.join(path, file) for file in os.listdir(path)]
    for path in paths:
        with open(path, 'rb') as File:
            Img = File.read()
        try:
            result = client.basicAccurate(Img)
            if len(result) == 0:
                return 1
            else:
                return 2
        except:
            return 0


def Solve():
    global Count
    Name = ''
    # dir_name = str(Count)
    # if not os.path.exists(dir_name):
    #     os.makedirs(dir_name)
    # Name = dir_name + "/1.png"
    # Image = ImageGrab.grabclipboard()  # 获取截图的图片
    # Image.save(Name)
    try:
        print("im trying...")
        dir_name = str(Count)
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        if From_initial:
            Name = dir_name + "/1.png"
            Image = ImageGrab.grabclipboard()  # 获取截图的图片
            Image.save(Name)
            time.sleep(0.2)
        file_names = os.listdir(str(Count))
        files = [os.path.join(dir_name, file_name) for file_name in file_names]
        print(files)
        Results = []
        for file in files:
            with open(file, 'rb') as File:
                Img = File.read()
            Result = client.basicAccurate(Img)
            Num = Result["words_result_num"]
            if not Num == 0:
                Results.append(Result)
        if len(Results) == 0:
            print("Has no Strings.")
        else:
            for Result in Results:
                for x in Result["words_result"]:
                    print(x["words"])

        Count += 1
        print("Count = ", Count)
    except:
        print("split...")
        print(Name)
        image = cv.imread(Name)
        gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
        _, binary = cv.threshold(gray, 128, 256, cv.THRESH_OTSU | cv.THRESH_BINARY_INV)
        height, width = binary.shape[:2]
        split_height = height // 2
        while sum(binary[split_height, :]) > 20:
            split_height -= 1
        image_1 = image[:split_height, :, :]
        image_2 = image[split_height:, :, :]
        name_components = Name.split('.')
        name_1 = name_components[0] + "_1." + name_components[1]
        name_2 = name_components[0] + "_2." + name_components[1]
        cv.imwrite(name_1, image_1)
        cv.imwrite(name_2, image_2)
        os.remove(Name)


def Clear():
    global Count
    try:
        for x in range(1, 999):
            Name = str(x) + "/.png"
            os.remove(Name)
    except:
        print("Done")
    Count = 1


def split_image(file_):
    image = cv.imread(file_)
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    _, binary = cv.threshold(gray, 128, 256, cv.THRESH_OTSU)

    height, width = binary.shape[:2]
    # print(binary.sum())
    # print(height*width/2)
    if binary.sum()/256 > height*width/2:
        binary = 255 - binary
    split_height = height // 2
    while sum(binary[split_height, :]) > 200:
        split_height += 1
    image_1 = image[:split_height, :, :]
    image_2 = image[split_height:, :, :]
    name_components = file_.split('.')
    name_1 = name_components[0] + "_1." + name_components[1]
    name_2 = name_components[0] + "_2." + name_components[1]
    cv.imwrite(name_1, image_1)
    cv.imwrite(name_2, image_2)
    return name_1, name_2


def solve():
    global Count
    image_dir = str(Count)
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)
    else:
        shutil.rmtree(image_dir)
        os.mkdir(image_dir)
    Name = image_dir + "/1.png"
    Image = ImageGrab.grabclipboard()  # 获取截图的图片
    Image.save(Name)
    time.sleep(0.2)
    need_to_solve = [os.path.join(image_dir, file) for file in os.listdir(image_dir)]
    need_to_solve.sort()
    print(need_to_solve)
    while not able_to_read(need_to_solve[0]):
        # print("分割前", need_to_solve)
        for file in need_to_solve:
            _, _ = split_image(file)
            # need_to_solve.remove(file)
            # need_to_solve.append(file1)
            # need_to_solve.append(file2)
            # print(need_to_solve)
            # print(file)
            os.remove(file)
        need_to_solve = [os.path.join(image_dir, file) for file in os.listdir(image_dir)]
        need_to_solve.sort()
        # print("分割后", need_to_solve)
    # print(need_to_solve)
    Results = []
    for file in need_to_solve:
        with open(file, 'rb') as File:
            Img = File.read()
        Result = client.basicAccurate(Img)
        print(Result)
        time.sleep(1)
        Num = Result["words_result_num"]
        if not Num == 0:
            Results.append(Result)
    if len(Results) == 0:
        print("Has no Strings.")
    else:
        for Result in Results:
            for x in Result["words_result"]:
                print(x["words"])

    Count += 1
    # print("Count = ", Count)


def main():
    # file = "B:/project/fancy_things/text_recognition/1"
    # print(able_to_read(file))
    # solve()
    keyboard.add_hotkey('f7', solve)
    keyboard.add_hotkey('f9', Clear)
    keyboard.wait("esc")


if __name__ == "__main__":
    main()
