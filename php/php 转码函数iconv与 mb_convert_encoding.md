              
          
    在使用PHP处理字符串时，我们经常会碰到字符编码转换的问题，你碰到过iconv转换失败吗？

    发现问题时，网上搜了搜，才发现iconv原来有bug ，碰到一些生僻字就会无法转换，当然了配置第二个参数时，可以稍微弥补一下默认缺陷，不至于无法转换是截断，用法如下：

    iconv(“UTF-8″,”GB2312//IGNORE”,$data) ;

    这样碰到生僻字转换失败时，它就会忽略失败，继续转换下面的内容，这算解决问题的一个办法，不过为了确保转换的成功率，我们可以用另一个转换函数（mb_convert_encoding），查资料网上说，这个函数效率不是很高，另外这个函数还可以省略第三个参数，自动识别内容编码，不过最好不要用，影响效率，还需要注意的时，mb_convert_encoding和iconv参数顺序不一样，一定要注意。

    附两个函数简单的用法：
iconv：
    string iconv ( string $in_charset , string $out_charset , string $str )

    第一个参数：内容原的编码

    第二个参数：目标编码

    第三个参数：要转的字符串

    函数返回字符串

    <?php

    $instr = ‘测试’;

    // GBK转UTF-8

    $outstr = iconv(‘GBK’,&#39;UTF-8′,$instr);

    ?>
mb_convert_encoding
    string mb_convert_encoding ( string $str , string $to_encoding [, mixed $from_encoding ] )

    第一个参数：要处理的字符串

    第二个参数：目标编码

    第三个参数：内容原编码

    <?php$instr = &#39;测试&#39;;// GBK转UTF-8$outstr = mb_convert_encoding($instr,&#39;UTF-8&#39;,&#39;GBK&#39;,);?>

    个人建议碰到转码问题时采用mb_convert_encoding比较保险。
    
    
      
来自:http://www.i5good.com/20140416161.html