              
          
    PHP �ֲ��ж� htmlspecialchars д����

    The translations performed are:
&#39;&;&#39; (ampersand) becomes &#39;&;amp;&#39;&#39;&quot;&#39; (double quote) becomes &#39;&;quot;&#39; when ENT_NOQUOTES is not set.&#39;&#39;&#39; (single quote) becomes &#39;&;#039;&#39; only when ENT_QUOTES is set.&#39;<&#39; (less than) becomes &#39;&;lt;&#39;&#39;>&#39; (greater than) becomes &#39;&;gt;&#39;


    htmlspecialchars ֻת�������⼸��html���룬�� htmlentities ȴ��ת�����е�html���룬��ͬ��������޷�ʶ��������ַ�Ҳ��ת���ˡ�

    ���ǿ�����һ���򵥵����������Ƚϣ�

    $str='<a href="test.html">����ҳ��</a>';echo htmlentities($str);// &;lt;a href=&;quot;test.html&;quot;&;gt;&;sup2;&;acirc;&;Ecirc;&;Ocirc;&;Ograve;&;sup3;&;Atilde;&;aelig;&;lt;/a&;gt;  $str='<a href="test.html">����ҳ��</a>';echo htmlspecialchars($str);// &;lt;a href=&;quot;test.html&;quot;&;gt;����ҳ��&;lt;/a&;gt;
    �����ǣ������ĵ�ʱ������� htmlspecialchars ������������룡
    
    
      
����:http://www.i5good.com/20121009128.html