              
          
    在linux下操作的时候经常会遇到，bash: service: command not found这个错误，以前在网上找了，照着弄了，也没细看原因，今天又碰到这个问题，就顺便研究一下。 1、通常这种情况是出现在 通过su root命令来进行操作的时候。 su或者su root 只是相当于以root用户身份来操作，实际的系统环境并没有切换到root用户的环境，而只是当前登录用户； su -,-l,--login都是已经完全的切换的root环境下，相当于完全用root用户登录。 这里就看下su命令：su --help 看到su命令的帮助信息： 

    用法：su [选项]... [-] [用户 [参数]...]  Change the effective user id and group id to that of USER.       -, -l, --login               make the shell a login shell    -c, --command=COMMAND       pass a single COMMAND to the shell with -c    --session-command=COMMAND    pass a single COMMAND to the shell with -c                                 and do not create a new session    -f, --fast                   pass -f to the shell (for csh or tcsh)    -m, --preserve-environment   do not reset environment variables    -p                           same as -m    -s, --shell=SHELL            run SHELL if /etc/shells allows it        --help     显示此帮助信息并退出        --version  输出版本信息并退出     单独的 - 代表 -l。如果未给出[用户]，则假定为 root。
    2、service命令目录在/sbin/下 故解决此问题有两种方式： a、直接使用su - root来切换到root用户，然后使用 service b、使用su root切换到root用户，并同时使用/sbin/service来操作，如/sbin/service mysql restart.
    
    
      
来自:http://www.i5good.com/20130115155.html