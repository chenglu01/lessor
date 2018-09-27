# -*-coding:utf-8 -*-

import re
import urllib
import urllib2
import os


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def mkdir(path):
    path = path.strip()
    isExists = os.path.exists(path)
    if not isExists:
        print u'新建了名字叫做',path,u'的文件夹'
        os.makedirs(path)
        return True
    else:
        print u'名为',path,u'的文件夹已经创建成功'
        return False

def saveImages(imglist,name):
    number = 1
    for imageURL in imglist:
        splitPath = imageURL.split('.')
        fTail = splitPath.pop()
        if len(fTail) > 3:
            fTail = 'jpg'
        fileName = name + "/" + str(number) + "." + fTail
        # 对于每张图片地址，进行保存
        try:
            u = urllib2.urlopen(imageURL)
            data = u.read()
            f = open(fileName,'wb+')
            f.write(data)
            print u'正在保存的一张图片为',fileName
            f.close()
        except urllib2.URLError as e:
            print (e.reason)
        number += 1

def getAllImg(html):
    #利用正则表达式把源代码中的图片地址过滤出来
    # reg = r'src="(https://.+?\.jpg)"'
    # reg = r'data-actualsrc="(https?://pic.+?\.jpg|png|jpeg)"'
    reg = r'data-actualsrc="(.*?)">'
    imgre = re.compile(reg, re.S)
    imglist = imgre.findall(html) #表示在整个网页中过滤出所有图片的地址，放在imglist中
    return imglist

if __name__ == '__main__':
    html = getHtml("https://www.zhihu.com/question/37787176")
    path = './images'
    imglist = getAllImg(html) #获取图片的地址列表
    saveImages(imglist,path) # 保存图片
