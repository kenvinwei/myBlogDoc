              
          
    首次在centos6.2下使用zendstudio，遇到几个问题：第一个就是安装问题，下载的是bin二进制包，在命令行下面安装提示一个x11display变量没有设置，然后就退出安装了。我一气之下就直接用鼠标操作，一个双击就完成了安装，真的气人！第二个问题就是乱码问题：运行zend，天阿！菜单全都是乱码！在手选项设置了一下字体，选择为utf—8，然后这里的问题就解决了！还有第三个问题：还是乱码问题阿：打开文件，里面的注释文件，又是一堆乱码！很明显的字体问题！这个字体没有！在网上找到了这个解决方法：1.创建文件夹fallbackmkdirzend安装目录/ZendStudio-5.5.0/jre/lib/fonts/fallback2.复制字体simsun.ttc（WINDOWS系统的Fonts目录下面有这个字体）到fallback后名字为simsun.ttfcpsimsun.ttczend安装目录/ZendStudio-5.5.0/jre/lib/fonts/fallback/simsun.ttf从新启动ZEND，乱码问题解决了。我按照这个方法操作，搞掂了。
    
    
      
来自:http://www.i5good.com/2012031478.html