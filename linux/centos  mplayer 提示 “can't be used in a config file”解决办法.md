              
          
    前几天安装了一个mplayer，还挺好用，音质也蛮不错，安装完成后就会在你安装的目录下生成，几个可执行文件：gmplayer、mplayer，运行gmplayer直接跑图形界面，如果不跑图形界面就可以直接运行mplayer

    但是我在用mplayerdirname.mp3的时候报如下错误：

    “Theflip-hebrewoptioncan&#39;tbeusedinaconfigfile”

    解决方法：

    打开mplayer的配置文件：

    /etc/mplayer/mplayer.conf

    然后找到：

    flip-hebrew=no

    注释掉此句，修改成：

    #flip-hebrew=no

    然后运行成功，写如下简单脚本：

    #! /bin/shcd /usr/local/soft/bin                                         ./mplayer /home/wei/音乐/*.mp3
    然后就可以不用打开界面播放音乐喽

    后台运行可以这样写：

    #! /bin/shcd /usr/local/soft/bin./mplayer /home/wei/音乐/*.mp3 > /dev/null 2>1&;
    图形界面运行：

    #! /bin/shcd /usr/local/soft/bin./gmplayer
    

    不妨玩玩哦！！！

    
    
    
      
来自:http://www.i5good.com/2012021973.html