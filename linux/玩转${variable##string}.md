              
          
    ${varible##*string}：从左向右截取最后一个string后的字符串

    例如：

    [wei@localhost Book]$ str=1314[wei@localhost Book]$ echo ${str##*1}4
    ${varible#*string}：从左向右截取第一个string后的字符串

    例如：

    [wei@localhost Book]$ str=1314[wei@localhost Book]$ echo ${str#*1}314
    ${varible%%string*}：从右向左截取最后一个string后的字符串

    [wei@localhost Book]$ str=1314[wei@localhost Book]$ echo ${str%%3*}1
    ${varible%string*}：从右向左截取第一个string后的字符串

    [wei@localhost Book]$ str=1314[wei@localhost Book]$ echo ${str%1*}13
                
    
    
      
来自:http://www.i5good.com/2012032079.html