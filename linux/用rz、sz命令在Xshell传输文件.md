              
          
    Xshell很好用,然后有时候想在windows和linux之间上传或下载某个文件。有个很简单的方法就是rz,sz命令。首先你的Linux需要安装rz、sz(如果没有安装，请执行以下命令,安装完的请跳过。其它版本linux请自行安装相应软件)yum install lrzsz -y安装完毕即可使用rz，sz是便是Linux/Unix同Windows进行ZModem文件传输的命令行工具。windows端需要支持ZModem的telnet/ssh客户端(xshell支持,好像putty不支持)，SecureCRT就可以用SecureCRT登陆到Unix/Linux主机（telnet或ssh均可）运行命令rz，即是接收文件，xshell就会弹出文件选择对话框，选好文件之后关闭对话框，文件就会上传到linux里的当前目录。运行命令sz file 就是发文件到windows上（保存的目录是可以配置） 比ftp命令方便多了，而且服务器不用再开FTP服务了。更简便的方法是直接拖动文件到Xshell里面，就可以完成上传。
    
    
      
来自:http://www.i5good.com/20140928168.html