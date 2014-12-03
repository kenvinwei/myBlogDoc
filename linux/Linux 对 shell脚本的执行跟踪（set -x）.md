              
          
    在编写较长的shell脚本时执行跟踪还是很有用处的。

    前提：

    有shell脚本nusers基本内容如下：

    [wei@localhost桌面]$set-x

    [wei@localhost桌面]$who|wc-l

    #!/bin/bash    # get the count of user logon     who | wc -l    [wei@localhost 桌面]$ chmod 755 nusers     [wei@localhost 桌面]$ sh -x nusers     + who    + wc -l    2
    ===========

    在sh脚本中打开跟踪功能set-x；set+x用来关闭，例子如下：

    [wei@localhost 桌面]$ cat > trace1.sh    #! /bin/sh    set -x    echo the 1 echo    set +x    echo the 2 echo    [wei@localhost 桌面]$ chmod 755 trace1.sh     [wei@localhost 桌面]$ ./trace1.sh     ---执行脚本    + echo the 1 echo   -----被跟踪的diyih    the 1 echo  ------命令的输出    + set +x  -----被跟踪的第二个命令    the 2 echo
    ---------------------------------------------------------------------------------------------

    set指令能设置所使用shell的执行方式，可依照不同的需求来做设置　-a　标示已修改的变量，以供输出至环境变量。　-b　使被中止的后台程序立刻回报执行状态。　-C　转向所产生的文件无法覆盖已存在的文件。　-d　Shell预设会用杂凑表记忆使用过的指令，以加速指令的执行。使用-d参数可取消。　-e　若指令传回值不等于0，则立即退出shell。　　　-f　　取消使用通配符。　-h　自动记录函数的所在位置。　-HShell　可利用&quot;!&quot;加<指令编号>的方式来执行history中记录的指令。　-k　指令所给的参数都会被视为此指令的环境变量。　-l　记录for循环的变量名称。　-m　使用监视模式。　-n　只读取指令，而不实际执行。　-p　启动优先顺序模式。　-P　启动-P参数后，执行指令时，会以实际的文件或目录来取代符号连接。　-t　执行完随后的指令，即退出shell。　-u　当执行时使用到未定义过的变量，则显示错误信息。　-v　显示shell所读取的输入值。　-x　执行指令后，会先显示该指令及所下的参数。　+<参数>　取消某个set曾启动的参数。

    
    
    
      
来自:http://www.i5good.com/20120606106.html