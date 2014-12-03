              
          
    update-rc.d命令，是用来自动的升级System V类型初始化脚本，简单的讲就是，哪些东西是你想要系统在引导初始化的时候运行的，哪些是希望在关机或重启时停止的，可以用它来帮你设置。

    开机启动，首先把需要的服务copy到 /etc/init.d中

    然后:sudo update-rc.d -f (mysqld|nginx|php-fpm) defaults;

    取消开机启动用：

    sudo update-rc.d -f (mysqld|nginx|php-fpm) remove;
    
    
      
来自:http://www.i5good.com/20140623165.html