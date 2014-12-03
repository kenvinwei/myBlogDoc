              
          
    解决php通过localhost不能连接mysql(Percona Server)数据库,通过127.0.0.1等ip能链接mysql数据库的问题.
问题产生
    使用Percona Server官网的在线生成工具生成了my.cnf配置文件.做好左右配置启动ok之后,php无法通过localhost连接mysql数据库.

    但是通过ip地址却可以连接.
mysql的localhost和127.0.0.1的区别
    localhost走的是 unix sock,127.0.0.1走的是 tcp
原因分析
产生localhost不能连接的问题是,php默认中使用的mysql unix sock使用的是 /tmp/mysql.sock如果你修改了mysql的的sock的路径,那么需要在php.ini中指定.

解决问题
    so:解决php连接mysql localhost不能连接,通过127.0.0.1等ip能链接的问题.

    1.修改php.ini中配置,指定mysql.sock位置. (我的是ubuntu 位置在 /var/run/mysqld/mysqld.sock )；或者2.修改my.cnf配置,改为 /tmp/mysql.sock (配置无效,配置了这个位置，但是实际位置在 /var/run/mysqld/mysqld.sock)

    //可能是ubuntu 系统问题，my.cnf 存在两个位置 分别是：/etc/my.cnf 和 /etc/mysql/my.cnf 后者的优先级高，后者可以查看到 mysqld.sock的具体位置

    原文地址： http://www.iamle.com/archives/1265.html?utm_source=rss&;utm_medium=rss&;utm_campaign=centos%25e4%25b8%258a%25e7%2594%25a8yum%25e6%2596%25b9%25e5%25bc%258f%25e5%25ae%2589%25e8%25a3%2585mysql%25e8%25a1%258d%25e7%2594%259f%25e5%258f%2591%25e8%25a1%258c%25e7%2589%2588percona-server-3, 感谢原作者分享。  

    
    
      
来自:http://www.i5good.com/20140618164.html