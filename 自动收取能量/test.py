from appium import webdriver
import time
import winsound

duration1 = 100
freq = 440

desired_caps = dict()

desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9'
desired_caps['deviceName'] = '192.168.0.104'
desired_caps['noReset'] = True
desired_caps['appPackage'] = 'com.eg.android.AlipayGphone'
desired_caps['appActivity'] = 'AlipayLogin'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(10)


def get_screen_size():
    x = driver.get_window_size()['width']  # 获取屏幕宽度
    y = driver.get_window_size()['height']  # 获取屏幕高度
    return x, y


# 在首页找到【蚂蚁森林】的入口，点击进入
def get_home_view_by_text_then_click(Driver, tag):
    home_app_view_list = Driver.find_elements_by_id('com.alipay.android.phone.openplatform:id/home_app_view')
    home_len = len(home_app_view_list)
    for i in range(0, home_len):
        home_app_view_text = home_app_view_list[i].find_element_by_id(
            'com.alipay.android.phone.openplatform:id/app_text').text
        print(home_app_view_text)
    for i in range(0, home_len):
        home_app_view_text = home_app_view_list[i].find_element_by_id(
            'com.alipay.android.phone.openplatform:id/app_text').text
        if home_app_view_text == tag:
            print('-------------------------------------')
            print(str(tag) + '->' + str(i))
            print('点击【' + home_app_view_text + '】')
            home_app_view_list[i].click()
            break


# 通用的查找指定元素并点击的方法
def get_common_view_by_class_then_click(Driver, tag):
    common_app_view_list = Driver.find_elements_by_class_name('android.view.View')
    common_len = len(common_app_view_list)
    # for i in range(0,common_len):
    #     common_app_view_text = common_app_view_list[i].get_attribute('name')
    #     if common_app_view_text:
    #         print(common_app_view_text)
    for i in range(0, common_len):
        common_app_view_text = common_app_view_list[i].get_attribute('name')
        if common_app_view_text == tag:
            print('-------------------------------------')
            print(str(tag) + '->' + str(i))
            print('点击【' + common_app_view_text + '】')
            for _ in range(3):
                common_app_view_list[i].click()
            # print(dir(common_app_view_list[i]))
            time.sleep(3)
            break


# 实现一次按坐标进行的点击
def tap_alone(x, y, duration=900):
    length = get_screen_size()
    width = int(length[0])  # 获取屏幕宽度
    height = int(length[1])  # 获取屏幕高度
    tap_x1 = int((int(x) / width) * width)
    tap_y1 = int((int(y) / height) * height)
    print('点击坐标:[' + str(tap_x1) + ', ' + str(tap_y1) + ']')
    driver.tap([(tap_x1, tap_y1), (tap_x1, tap_y1)], duration)
    winsound.Beep(freq, duration1)


# 实现一次收取能量
def tap_get_energy():
    # 能量球可能出现的区域坐标
    start_x = 120
    start_y = 470
    end_x = 920
    end_y = 870

    print('开始收取自己的能量>>>')
    # 依次点击指定区域内的等距离坐标点
    for _ in range(3):  # 可能会有重合的能量球，多次重复操作保证收集所有的能量球
        for i in range(start_y, end_y, 80):
            for j in range(start_x, end_x, 80):
                print('[' + str(j) + ', ' + str(i) + ']', "\t", end="")
                tap_alone(j, i)  # 通过坐标实行一次点击，其中包含了duration
            print()


# 遍历获取好友列表
def get_friend_view_by_class_then_click(Driver):
    time.sleep(1)
    for i in range(0, 1):
        print(str(i))
        swipeUp(2000, 500, 3000)
        print("上滑")
        time.sleep(3)
        print("上滑")
    for i in range(0, 1):
        print(str(i))
        swipeDown(500, 2000, 3000)
        print("下滑")
        time.sleep(3)
        print("下滑")
    time.sleep(1)

    swipeUp(2000, 1805, 1000)
    print("准备点击")
    time.sleep(1.1)
    for i in range(200, 800, 80):
        for j in range(200, 800, 80):
            print('[' + str(j) + ', ' + str(i) + ']', "\t", end="")
            tap_alone(j, i)  # 通过坐标实行一次点击，其中包含了duration
        print()
    # tap_alone(540, 200, 500)
    # tap_alone(540, 200, 10000)
    time.sleep(5)

    # friend_view_square = Driver.find_element_by_id('J_rank_list')
    # friend_view_list = friend_view_square.find_elements_by_class_name('android.view.View')
    # Common_len = len(friend_view_list)
    # print(Common_len)
    # print('-------------------------------------')
    # count = 0
    # for i in range(0, Common_len):
    #     friend_view_view_text = friend_view_list[i].get_attribute('name')
    #     if friend_view_view_text:
    #         # print(friend_view_view_text)
    #         if count % 10 == 0 and count != 0:
    #             count = 0
    #             print('向上划一页')
    #             swipeUp(2000, 120)
    #             time.sleep(1)
    #         # if '获得了' in friend_view_view_text and count<10:
    #         if 'g' in friend_view_view_text:
    #             print('-------------------------------------')
    #             print('收取【' + friend_view_list[i - 2].get_attribute('name') + '】的能量>>>')
    #             friend_view_list[i].click()
    #             count += 1
    #             # print(count)
    #             time.sleep(1)
    #             tap_get_energy()
    #             Driver.press_keycode(4)
    #
    # # for i in range(0,common_len):
    # #     friend_view_view_text = friend_view_list[i].get_attribute('name')
    # #     if friend_view_view_text:
    # #         print('-------------------------------------')
    # #         print(str(friend_view_view_text) + '->' + str(i))
    # #         print('点击【' + friend_view_view_text + '】')
    # #         friend_view_list[i].click()


# 实现安坐标精准滑动：向上滑动
def swipeUp(y1, y2, duration=5000):
    length = get_screen_size()
    width = int(length[0])  # 获取屏幕宽度
    height = int(length[1])  # 获取屏幕高度
    x1 = int(width * 0.5)
    y1_start = int((int(y1) / height) * height)
    y2_end = int((int(y2) / height) * height)
    driver.swipe(x1, y1_start, x1, y2_end, duration)
    print('向上滑动【' + str(y1_start - y2_end) + '】')


# 实现安坐标精准滑动：向下滑动
def swipeDown(y1, y2, duration=5000):
    length = get_screen_size()
    width = int(length[0])  # 获取屏幕宽度
    height = int(length[1])  # 获取屏幕高度
    x1 = int(width * 0.5)
    y1_start = int((int(y1) / height) * height)
    y2_end = int((int(y2) / height) * height)
    driver.swipe(x1, y1_start, x1, y2_end, duration)
    print('向下滑动【' + str(y2_end - y1_start) + '】')


tap_alone(600, 500)
time.sleep(10)
for _ in range(100):
    tap_alone(540, 1800)
time.sleep(5)
swipeUp(2000, 200, 3000)
swipeUp(2000, 200, 3000)
# swipeUp(2000, 200, 3000)
tap_alone(540, 800)

# # 点击【蚂蚁森林】
# get_home_view_by_text_then_click(driver, '蚂蚁森林')  # 找到蚂蚁森林并进入
# time.sleep(5)
#
# # 收取自己的能量
# tap_get_energy()
# time.sleep(3)
#
# # 滑动屏幕，找到【好友排行榜】
# swipeUp(2000, 100)
# time.sleep(1)
# swipeUp(2000, 100)
# time.sleep(1)
# swipeUp(2000, 900)
# time.sleep(1)
# #
# # # 点击进入【好友排行榜】
# # # get_common_view_by_class_then_click(driver, '查看更多好友')
# tag = '查看更多好友'
# common_app_view_list = driver.find_elements_by_class_name('android.view.View')
# common_len = len(common_app_view_list)
#
# for i in range(0, common_len):
#     common_app_view_text = common_app_view_list[i].get_attribute('name')
#     # print(common_app_view_list[i].value_of_css_property("bounds"))
#
#     if common_app_view_text == tag:
#         # if i == 143:
#         print('-------------------------------------')
#         print(str(tag) + '->' + str(i))
#         print('点击【' + common_app_view_text + '】')
#         for _ in range(1):
#             common_app_view_list[i].click()
#             time.sleep(1)
#
# time.sleep(1)
#
# # 开始收取好友列表中好友的能量
# # common_app_view_list = driver.find_elements_by_class_name('android.view.View')
# # common_len = len(common_app_view_list)
# # for i in range(0, common_len):
# #     common_app_view_text = common_app_view_list[i].get_attribute('name')
#     # print(common_app_view_text, "  size:", common_app_view_list[i].size, "  location:", common_app_view_list[i].location)
#
# image = driver.get_screenshot_as_file("D:/1.png")
# print(image)
# # get_friend_view_by_class_then_click(driver)
#
# time.sleep(1)
# for i in range(0, 1):
#     print(str(i))
#     swipeUp(2000, 500, 3000)
#     print("上滑")
#     time.sleep(3)
#     print("上滑")
# for i in range(0, 1):
#     print(str(i))
#     swipeDown(500, 2000, 3000)
#     print("下滑")
#     time.sleep(3)
#     print("下滑")
# time.sleep(1)
#
# swipeUp(2000, 1805, 1000)
# print("准备点击")
# time.sleep(1.1)
# # for i in range(200, 800, 80):
# #     for j in range(200, 800, 80):
# #         print('[' + str(j) + ', ' + str(i) + ']', "\t", end="")
# #         tap_alone(j, i)  # 通过坐标实行一次点击，其中包含了duration
# #     print()
# for _ in range(4):
#     swipeUp(2000, 200, 3000)
#     print("上滑")
#     time.sleep(3)
#
# for _ in range(30):
#     tap_alone(540, 1023, 500)
#
time.sleep(5)
driver.quit()
