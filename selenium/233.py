import time
import xlwt
import csv
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome()
driver.get("https://www.iqiyi.com/v_19rsm3gomk.html")
time.sleep(10)
js="var q=document.documentElement.scrollTop=100000"
driver.execute_script(js)
time.sleep(10)
WebDriverWait(driver, 20).until(lambda x: x.find_element_by_id("comment").is_displayed())
#html = driver.page_source
#driver.switch_to.frame("qy-comment-page")
comment = driver.find_elements_by_xpath('//div[@class="section-bd"]')
#//*[@id="comment"]/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[2]/div[1]/div[1]/a
result_list = []
for comment_dict in comment:
    result = {}
    result['usename'] = comment_dict.find_element_by_xpath('.//div[@class="comment-title"]/div/a').get_attribute('title')
    result['span'] = comment_dict.find_element_by_xpath('.//div[@class="comment-subject"]/span').get_attribute('data-comment-content')
    result_list.append(result)

with open('comment.csv','w',encoding='GBK') as f:
    writer = csv.DictWriter(f, fieldnames=['usename', 'span'])
    writer.writeheader()
    writer.writerows(result_list)
'''
workbook = xlwt.Workbook(encoding = 'ascii')
worksheet = workbook.add_sheet('My Worksheet')
worksheet.write(result_list)
workbook.save('Excel_Workbook.xls')
'''
driver.quit()