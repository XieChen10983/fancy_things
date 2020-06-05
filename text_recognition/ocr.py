# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/6/4 16:09
filename(文件名): ocr.py
function description(功能描述):
...
    APP_ID = "20227038"
    API_KEY = "tuQ3GPXA7Qt9uHKtahZgoUwn"
    SECRET_KEY = "hoGMLSu2cNt5ttfVl2hGnMCKQtoSMO5N"
"""
from PIL import ImageGrab
from aip import AipOcr
import keyboard, os, time, cv2

""" 你的 APPID AK SK """
APP_ID = "20227038"
API_KEY = "tuQ3GPXA7Qt9uHKtahZgoUwn"
SECRET_KEY = "hoGMLSu2cNt5ttfVl2hGnMCKQtoSMO5N"
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
"""结束"""
global Count
Count = 1


def Solve():
    global Count  # 这是按顺序命名的全局变量
    try:
        Image = ImageGrab.grabclipboard()  # 获取截图图片
        Name = str(Count) + r'.jpg'

        Image.save(Name)  # 保存图片
        time.sleep(1)  # 睡觉等待
        Count = Count + 1
        with open(Name, 'rb') as File:
            Img = File.read()

        # print("-------hi-----")
        print(type(Img))
        Result = client.basicAccurate(Img)
        # Result = client.basicGeneral(Img)
        # print("-------hello-----")
        Num = Result['words_result_num']
        if Num == 0:
            print("Your Image Has Not Strings")  # 你的图片里面没有字哦
        else:
            for x in Result['words_result']:
                print(x['words'])
    except:
        print("No Image")  # 你内存没有图片哦


def Clear():  # try a try
    global Count
    try:
        for x in range(1, 999):  # 目测正常人应该最多用999个吧
            Name = str(x) + r'.jpg'
            os.remove(Name)
    except:
        print("Done")
    Count = 1  # 我香了，别忘记别人还得接住用，把序号再变为1


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
        print(path)
        cv2.imshow("hi", cv2.imread(path))
        cv2.waitKey()
        cv2.destroyAllWindows()
        with open(path, 'rb') as File:
            Img = File.read()
        try:
            print("haiahia")
            result = client.basicAccurate(Img)
            print(result)
            if len(result) == 0:
                return 1
            else:
                return 2
            # print(path)
            # continue
        except:
            print(path)
            return 0
    # return True


# def able_to_read(path):
#     """
#     给定一张图像的路径，判断该图像是否可读。
#     :param path:
#     :return:
#     """
#     print(path)
#     cv2.imshow("hi", cv2.imread(path))
#     cv2.waitKey()
#     cv2.destroyAllWindows()
#     with open(path, 'rb') as File:
#         Img = File.read()
#     try:
#         print("haiahia")
#         result = client.basicAccurate(Img)
#         # Result = client.basicAccurate(Img)
#         Num = result["words_result_num"]
#         if len(Num) == 0:
#             print("没内容")
#             return 1
#         else:
#             print("成了")
#             return 2
#         # print(result)
#         # print(path)
#     except:
#         print("读不了")
#         return 0


def main():
    file = "B:/project/fancy_things/text_recognition/1/1_1_1.png"
    print(able_to_read(file))
    keyboard.add_hotkey('f7', Solve)  # f7处理图片
    keyboard.add_hotkey('f9', Clear)  # f9删除图片
    keyboard.wait('esc')  # 按退出键结束程序


if __name__ == '__main__':
    main()
