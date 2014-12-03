              
          
    ('|")首先匹对单引号还是双引号(.*?)匹对任意字符/1匹对第一个('|")中成功匹对的引号/1是保证前后引号一致
    官方例子:

    <?php//2是一个后向引用的示例. 这会告诉pcre它必须匹配正则表达式中第二个圆括号(这里是([w]+))//匹配到的结果. 这里使用两个反斜线是因为这里使用了双引号.$html = "<b>bold text</b><a href=howdy.html>click me</a>";   preg_match_all("/(<([w]+)[^>]*>)(.*?)(</2>)/", $html, $matches, PREG_SET_ORDER);   foreach ($matches as $val) {    echo "matched: " . $val[0] . "n";    echo "part 1: " . $val[1] . "n";    echo "part 2: " . $val[2] . "n";    echo "part 3: " . $val[3] . "n";    echo "part 4: " . $val[4] . "nn";}?


    官方地址：http://www.php.net/manual/zh/function.preg-match-all.php
    
    
      
来自:http://www.i5good.com/20140417162.html