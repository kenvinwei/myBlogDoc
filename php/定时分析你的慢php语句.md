              
          
      php开发中，怎么确定慢的执行语句呢？php-fpm就可以满足你的需求，php-fpm.conf中有一个request_slowlog_timeout选项，这个选项能让你跟踪执行缓慢的脚本并把他们连同调用栈一起记录再日志文件中。例如如下设置：　　<value name=&quot;request_slowlog_timeout&quot;>5s</value>　　<value name=&quot;slowlog&quot;>logs/slow.log</value>　　正如你再例子中看到的，脚本运行了 5 秒以上，并很可能是由于 mysql 响应慢造成的（top backtrace），也可能是循环造成的，也可能.....

      开启这个选项很容易，不到2分钟就可以，其实我们还可以进一步做一下处理，我的机器上每天15点分隔日子，也就是方便每天查找慢的执行语句，或者查看某某天执行慢的php语句，这个是一个不错的东东。

    贴出我的执行脚本，很简单的哦~

    #!/bin/bashcd /usr/local/php/logs                                              logfile="./slow.log"mkdir -p `date +%Y%m%d`mv $logfile `date +%Y%m%d`/`date +%Y%m%d`_slow.logkill -USR1 `cat php-fpm.pid`
    然后crontab -e

    添加定时执行语句：

    0 15 * * * /usr/local/php/logs/cut_php_log.sh
    如此即可！
    
    
      
来自:http://www.i5good.com/20120802114.html