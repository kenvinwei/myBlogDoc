              
          
    mytop 是一个类似 Linux 下的 top 命令风格的 MySQL 监控工具，可以监控当前的连接用户和正在执行的命令。　　mytop的安装过程:

    wget ftp://ftp.sunet.se/pub/Linux/distributions/scientific/6.0/x86_64/os/Packages/epel-release-6-5.noarch.rpmrpm -ivh epel-release-6-5.noarch.rpmyum -y install mytop
    安装完成之后还需要配置一下环境　　运行 vim ~/.mytop 然后添加以下内容:

    user=你的mysql用户pass=你的mysql密码host=localhostdb=你要监控的数据库名delay=5port=3306socket=/tmp/mysql.sockbatchmode=0header=1color=1idle=1
    好了，这样安装就完成了，你可以运行直接在shell下运行 mytop 命令将会看到以下画面.

     
    
    
      
来自:http://www.i5good.com/20121023133.html