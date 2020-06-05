# coding=gbk
"""
author(����): Channing Xie(л�)
time(ʱ��): 2020/6/4 16:09
filename(�ļ���): ocr.py
function description(��������):
...
    APP_ID = "20227038"
    API_KEY = "tuQ3GPXA7Qt9uHKtahZgoUwn"
    SECRET_KEY = "hoGMLSu2cNt5ttfVl2hGnMCKQtoSMO5N"
"""
from PIL import ImageGrab
from aip import AipOcr
import keyboard, os, time, cv2

""" ��� APPID AK SK """
APP_ID = "20227038"
API_KEY = "tuQ3GPXA7Qt9uHKtahZgoUwn"
SECRET_KEY = "hoGMLSu2cNt5ttfVl2hGnMCKQtoSMO5N"
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
"""����"""
global Count
Count = 1


def Solve():
    global Count  # ���ǰ�˳��������ȫ�ֱ���
    try:
        Image = ImageGrab.grabclipboard()  # ��ȡ��ͼͼƬ
        Name = str(Count) + r'.jpg'

        Image.save(Name)  # ����ͼƬ
        time.sleep(1)  # ˯���ȴ�
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
            print("Your Image Has Not Strings")  # ���ͼƬ����û����Ŷ
        else:
            for x in Result['words_result']:
                print(x['words'])
    except:
        print("No Image")  # ���ڴ�û��ͼƬŶ


def Clear():  # try a try
    global Count
    try:
        for x in range(1, 999):  # Ŀ��������Ӧ�������999����
            Name = str(x) + r'.jpg'
            os.remove(Name)
    except:
        print("Done")
    Count = 1  # �����ˣ������Ǳ��˻��ý�ס�ã�������ٱ�Ϊ1


def able_to_read(path):
    """
    ����һ��ͼ���·�����жϸ�ͼ���Ƿ�ɶ���
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
#     ����һ��ͼ���·�����жϸ�ͼ���Ƿ�ɶ���
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
#             print("û����")
#             return 1
#         else:
#             print("����")
#             return 2
#         # print(result)
#         # print(path)
#     except:
#         print("������")
#         return 0


def main():
    file = "B:/project/fancy_things/text_recognition/1/1_1_1.png"
    print(able_to_read(file))
    keyboard.add_hotkey('f7', Solve)  # f7����ͼƬ
    keyboard.add_hotkey('f9', Clear)  # f9ɾ��ͼƬ
    keyboard.wait('esc')  # ���˳�����������


if __name__ == '__main__':
    main()
