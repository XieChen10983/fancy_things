# coding=gbk
"""
�����������£�
1. ����ģ��
2. ͨ�������������������
3. ������ַ
4. ���������
5. �Ƴ������
"""

# 1. ����ģ��
from selenium import webdriver
import time  # ˯��5�����ٹر������

# 2. ͨ������������������󣬲�����Ҫָ������·��
driver_path = './chromedriver.exe'
browser = webdriver.Chrome(driver_path)

# 3. ������ַ
browser.get(url='https://www.baidu.com')

# 4. ���������
'''
find ϵ�к�����ר�����ڶ�λԪ��
find_element_by_XXX       Ѱ�ҷ��������ĵ�һ��Ԫ��
find_elements_by_XXX      Ѱ�ҷ�������������Ԫ�أ�������һ���б�

XXX
find_element(s)_by_class_name       : ͨ��class_nameѰ��Ԫ��
find_element(s)_by_id               : ͨ��idѰ��Ԫ��
find_element(s)_by_name             : ͨ������Ѱ��Ԫ��
find_element(s)_by_tag_name         : ͨ����ǩ������Ѱ��Ԫ��
find_element(s)_by_css_selector     : ͨ��css��ʽѰ��Ԫ��
find_element(s)_by_link_text        : ͨ���ı�����Ѱ��Ԫ��
find_element(s)_by_partial_link_text: ͨ���ı�����������Ѱ��Ԫ��
find_element(s)_by_xpath            : ͨ��xpathѰ��Ԫ��

��element.text��ȡԪ�ص�����
��element.send_keys()ΪԪ���������
��element.get_attribute(����������)��ȡԪ�ص�����
��element.click()���Ԫ��
'''
# 4.1 ����ؼ���
input_element = browser.find_element_by_id('kw')  # ͨ��������id����kw���ҵ������
input_element.send_keys('���пƼ���ѧ')
# 4.2 ����ٶ�һ��
button_element = browser.find_element_by_id('su')
button_element.click()
time.sleep(2.)
# 4.3 �ҵ���Ҫ�����Ӳ��Ҵ�
link_element = browser.find_element_by_class_name('t')
link_element = link_element.get_attribute('href')
print()
link_element.click()

# 5. �˳������
time.sleep(5.)
browser.quit()
