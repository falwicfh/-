from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time,requests,os
from lxml import etree
from selenium.webdriver import ActionChains



root = 'E://绝对领域//'
headers ={
          'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

url = 'https://www.jdlingyu.mobi'
# 启动谷歌
driver = webdriver.Chrome(r'E:\chrome\chromedriver.exe')
driver.get(url)
time.sleep(5)



def getUrl():
    #爬取的网站

    #html = driver.page_source
    #获取想要的大页面
    page = driver.find_elements_by_xpath('//div[@class="pos-r cart-list"]')
    #遍历出图片页面
    for li in page:
        #pname = li.find_element_by_xpath('.//div[2]/h2/a').text
        #获取图片url
        pagelist = li.find_element_by_xpath('.//div[2]/h2/a').get_attribute('href')

        #获取图片地纸
        #转换成xpath可以读的文件
        html = requests.get(pagelist).text
        s = etree.HTML(html)
        pic = s.xpath('//*[@id="content-innerText"]/p/img/@src')
        #图片名字
        picname = s.xpath('//*[@id="post-single"]/h1/text()')
        #确认路径是否在，不在生一个，如果不加这句，会出现没有路役的时候，别问我为什么知道
        if not os.path.exists(root):
            os.mkdir(root)
        #在其下再生一个文件夹，存放该主题图片
        root_new = "E://绝对领域//{}//".format(picname)
        #继续确认
        if not os.path.exists(root_new):
            os.mkdir(root_new)
        #遍历出图片
        for i in pic:
            path = root_new + i.split('/')[-1]
            if not os.path.exists(path):
                r = requests.get(i,headers=headers)
                r.raise_for_status()    #错误提醒函数
                with open(path, 'wb') as f:
                    f.write(r.content)
                    print('动图已保存')
            else:
                print('动图已存在')

    getnetxpage()

#//*[@id="main"]/div[3]/div/div[4]/button[2]
def getnetxpage():
    button = driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div[4]/button[2]')
    ActionChains(driver).move_to_element(button).click(button).perform()
    time.sleep(5)
    getUrl()
    #程序停止机关，想爬到第几页，由于主要测试的是上面的主程序，停止程序随便写了个
    if 12 == driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div[1]/button[5]').text:
     driver.quit()


if  '__main__':
    getUrl()