              
          
    Shell字符串截取一、Linuxshell截取字符变量的前8位，有方法如下：

    1.exprsubstr“$a”182.echo$a|awk‘{printsubstr(,1,8)}’3.echo$a|cut-c1-84.echo$5.expr$a:‘(.\).*’6.echo$a|ddbs=1count=82>/dev/null

    二、按指定的字符串截取

    1、第一种方法:

    *${varible##*string}从左向右截取最后一个string后的字符串*${varible#*string}从左向右截取第一个string后的字符串*${varible%%string*}从右向左截取最后一个string后的字符串*${varible%string*}从右向左截取第一个string后的字符串

    “*”只是一个通配符可以不要

    例子：$MYVAR=foodforthought.jpg$echo${MYVAR##*fo}rthought.jpg$echo${MYVAR#*fo}odforthought.jpg

    2、第二种方法：${varible:n1:n2}:截取变量varible从n1到n2之间的字符串。

    可以根据特定字符偏移和长度，使用另一种形式的变量扩展，来选择特定子字符串。试着在bash中输入以下行：$EXCLAIM=cowabunga$echo${EXCLAIM:0:3}cow$echo${EXCLAIM:3:7}abunga

    这种形式的字符串截断非常简便，只需用冒号分开来指定起始字符和子字符串长度。

    三、按照指定要求分割：比如获取后缀名ls-al|cut-d“.”-f2

    
    
      
来自:http://www.i5good.com/2012040585.html