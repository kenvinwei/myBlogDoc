              
          
    PHP 手册中对 htmlspecialchars 写道：

    The translations performed are:
&#39;&;&#39; (ampersand) becomes &#39;&;amp;&#39;&#39;&quot;&#39; (double quote) becomes &#39;&;quot;&#39; when ENT_NOQUOTES is not set.&#39;&#39;&#39; (single quote) becomes &#39;&;#039;&#39; only when ENT_QUOTES is set.&#39;<&#39; (less than) becomes &#39;&;lt;&#39;&#39;>&#39; (greater than) becomes &#39;&;gt;&#39;


    htmlspecialchars 只转化上面这几个html代码，而 htmlentities 却会转化所有的html代码，连同里面的它无法识别的中文字符也给转化了。

    我们可以拿一个简单的例子来做比较：

    $str='<a href="test.html">测试页面</a>';echo htmlentities($str);// &;lt;a href=&;quot;test.html&;quot;&;gt;&;sup2;&;acirc;&;Ecirc;&;Ocirc;&;Ograve;&;sup3;&;Atilde;&;aelig;&;lt;/a&;gt;  $str='<a href="test.html">测试页面</a>';echo htmlspecialchars($str);// &;lt;a href=&;quot;test.html&;quot;&;gt;测试页面&;lt;/a&;gt;
    结论是，有中文的时候，最好用 htmlspecialchars ，否则可能乱码！
    
    
      
来自:http://www.i5good.com/20121009128.html