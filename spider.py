#coding=utf-8
#---------------------------------------  
#   程序：网络爬虫  
#   版本：0.1  
#   作者：kenvinwei  
#   日期：2014-12-01  
#   语言：Python 3.4.1  
#   操作：爬虫快速抓取内容   
#--------------------------------------- 
import string  
import urllib.request
import re
#----------- 处理页面上的各种标签 -----------  
class HTML_Tool:  
    # 用非 贪婪模式 匹配 \t 或者 \n 或者 空格 或者 超链接 或者 图片  
    BgnCharToNoneRex = re.compile("(\t|\n| |<a.*?>|<img.*?>)")  
      
    # 用非 贪婪模式 匹配 任意<>标签  
    EndCharToNoneRex = re.compile("<.*?>")  
  
    # 用非 贪婪模式 匹配 任意<p>标签  
    BgnPartRex = re.compile("<p.*?>")  
    CharToNewLineRex = re.compile("(<br/>|</p>|<tr>|<div>|</div>)")  
    CharToNextTabRex = re.compile("<td>")  
  
    # 将一些html的符号实体转变为原始符号  
    replaceTab = [("<","<"),(">",">"),("&gt;",">"),("&lt;","<"),("&amp","&"),("&nbsp;",""),("&","&"),("\\\"","\""),(" "," "),("-->","")]  
      
    def Replace_Char(self,x):  
        x = self.BgnCharToNoneRex.sub(" ",x)  
        x = self.BgnPartRex.sub("\n    ",x)  
        x = self.CharToNewLineRex.sub("\n",x)  
        x = self.CharToNextTabRex.sub("\t",x)  
        x = self.EndCharToNoneRex.sub("",x)  
  
        for t in self.replaceTab:    
            x = x.replace(t[0],t[1])    
        return x
class I5good_Spider: 
    def __init__(self,url):  
        self.myUrl = url
        self.urllist = []
        self.datas = []  
        self.myTool = HTML_Tool()
        print('爬虫开始了.....')
    # 初始化加载页面并将其转码储存  
    def getcontent(self):  
        # 读取页面的原始信息并将其从gbk转码  
        myPage = urllib.request.urlopen(self.myUrl).read().decode('utf-8', 'ignore')
        # 计算楼主发布内容一共有多少页  
        endPage = self.page_counter(myPage)    
        # 获取最终的数据  
        self.save_data(self.myUrl,endPage) 
        #用来计算一共有多少页  
    def page_counter(self,myPage):   
        myMatch = re.search(r'个 1/(\d+?) 页', myPage, re.S)
        if myMatch:    
            endPage = int(myMatch.group(1))  
            print(u'爬虫报告：发现楼主共有%d页的原创内容' % endPage)  
        else:  
            endPage = 0  
            print(u'爬虫报告：无法计算楼主发布内容有多少页！')  
        return endPage  
    #抓取标题 
    def find_title(self,myPage):   
        myMatch = re.search(r'<h4>(.*?)<\/h4>', myPage, re.S)
        title = u'暂无标题'  
        if myMatch:  
            title  = myMatch.group(1)  
        else:  
            print(u'爬虫报告：无法加载文章标题！')  
        # 文件名不能包含以下字符： \ / ： * ? " < > |  
        title = title.replace('\\','').replace('/','').replace(':','').replace('*','').replace('?','').replace('"','').replace('>','').replace('<','').replace('|','')  
        return title  
  
  
    # 用来存储楼主发布的内容  
    def save_data(self,url,endPage):  
        # 加载页面数据到数组中  
        self.get_data(url,endPage)  
        # 打开本地文件
        for item in self.urllist:
            info = urllib.request.urlopen(item).read().decode("utf-8", 'ignore')
            # 获取该帖的标题  
            title = self.find_title(info)  
            print(u'文章名称：' + title)
            content = re.search(r'class="arinfo">(.*?)<div\sclass=\'arbefore\'', info, re.S)
            data = content.group(1)
            data = self.myTool.Replace_Char(data.replace("\n",""))
            #data = data.replace("&nbsp;","")
            data += '\r\n'+"来自:"+item
            f = open("./linux/"+title+'.md','w+')  
            f.writelines(data)  
            f.close()  
        print(u'爬虫报告：文件已下载到本地并打包成txt文件')   
  
    # 获取页面源码并将其存储到数组中  
    def get_data(self,url,endPage):  
        url = url + '/Article/type/type/5/p/'  
        for i in range(1,endPage+1):  
            print(u'爬虫报告：爬虫%d号正在加载中...' % i)
            myPage = urllib.request.urlopen(url + str(i)).read().decode('utf-8', 'ignore')  
            # 将myPage中的html代码处理并存储到datas里面  
            #self.deal_data(myPage.decode('utf-8'))
            myMatch = re.search(r'class="new_article_list">(.*?)<div\sstyle="float:right;"', myPage, re.S)
            if myMatch:
                myItems = re.findall(r'www.i5good.com\/(\d+?).html"',myMatch.group(1),re.S)
                if myItems:
                   for item in myItems:
                       self.urllist.append("http://www.i5good.com/"+item+".html")
  
    # 将内容从页面代码中抠出来  
    def deal_data(self,myPage):  
        myItems = re.findall('class="content.*?>(.*?)<div\sstyle="float:right;"',myPage,re.S)
        for item in myItems:
            data = self.myTool.Replace_Char(item.replace("\n",""))  
            self.datas.append(data+'\n')  
myurl = 'http://www.i5good.com/t5.html' 
#调用  
mySpider = I5good_Spider(myurl)  
mySpider.getcontent()  
