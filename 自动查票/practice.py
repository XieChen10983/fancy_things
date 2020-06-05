# coding=gbk
"""
具体流程如下：
1. 导入模块
2. 通过驱动创建浏览器对象
3. 输入网址
4. 操作浏览器
5. 推出浏览器
"""

# 1. 导入模块
from selenium import webdriver
import time  # 睡眠5秒钟再关闭浏览器

# 2. 通过驱动创建浏览器对象，参数需要指定驱动路径
driver_path = './chromedriver.exe'
browser = webdriver.Chrome(driver_path)

# 3. 输入网址
browser.get(url='https://www.baidu.com')

# 4. 操作浏览器
'''
find 系列函数，专门用于定位元素
find_element_by_XXX       寻找符合条件的第一个元素
find_elements_by_XXX      寻找符合条件的所有元素（返回是一个列表）

XXX
find_element(s)_by_class_name       : 通过class_name寻找元素
find_element(s)_by_id               : 通过id寻找元素
find_element(s)_by_name             : 通过名称寻找元素
find_element(s)_by_tag_name         : 通过标签的名称寻找元素
find_element(s)_by_css_selector     : 通过css样式寻找元素
find_element(s)_by_link_text        : 通过文本内容寻找元素
find_element(s)_by_partial_link_text: 通过文本部分内容来寻找元素
find_element(s)_by_xpath            : 通过xpath寻找元素

用element.text获取元素的内容
用element.send_keys()为元素添加内容
用element.get_attribute(‘属性名’)获取元素的属性
用element.click()点击元素
'''
# 4.1 输入关键字
input_element = browser.find_element_by_id('kw')  # 通过输入框的id：‘kw’找到输入框
input_element.send_keys('华中科技大学')
# 4.2 点击百度一下
button_element = browser.find_element_by_id('su')
button_element.click()
time.sleep(2.)
# 4.3 找到需要的连接并且打开
link_element = browser.find_element_by_class_name('t')
link_element = link_element.get_attribute('href')
print()
link_element.click()

# 5. 退出浏览器
time.sleep(5.)
browser.quit()
