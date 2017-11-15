#!/usr/bin/python
# -*- coding:utf8 -*-

from selenium import webdriver
import os

driver1 = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')
driver1.get("http://www.csdn.net")

data = driver1.title

driver1.save_screenshot('csdn.png')

print data

print os.getcwd()