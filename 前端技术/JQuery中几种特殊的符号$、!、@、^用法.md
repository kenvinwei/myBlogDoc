              
          
    �ڸսӴ�JQuery��ʱ�򣬸о����������֣���������һ��ʱ�俪��ǰ̨��JSʱ���ܸо��е��Ժ���������⣬�������õ���������ķ��Ž���ѡ����ˢѡ��ʱ�򣬲��ܺܺõĴ���ʹ�ã������ܽ�һ�¶����ǵ���⣬�԰�������һ����JQuery��ã�����ǡ�

    1.$����jQuery ��$(&quot;<span>&quot;)������﷨��ͬ��$(document.createElement(&quot;span&quot;)) ������һ���÷�����ѡ��Ԫ�ص�ʱ�򻹻������ӵ��ã�[attribute$=value]��ƥ���������������ĳЩֵ��β��Ԫ�ء�����ٸ�������˵��һ��:

    html����:

    <input name="newsletter" /><input name="milkman" /><input name="jobletter" />
    jQuery ����:

    $("input[name$='letter']")
    ���:

    [ <input name=&quot;newsletter&quot; />, <input name=&quot;jobletter&quot; /> ]

    2.!��ѡ������[attribute!=value]��ƥ�����в�����ָ�������ԣ��������Բ������ض�ֵ��Ԫ�أ���ѡ�����ȼ���:not([attr=value])��

    html����:

    <input type="checkbox" name="newsletter" value="Hot Fuzz" /><input type="checkbox" name="newsletter" value="Cold Fusion" /><input type="checkbox" name="accept" value="Evil Plans" />
    jQuery ����:

    $("input[name!='newsletter']").attr("checked", true);
    ���:[ <input type=&quot;checkbox&quot; name=&quot;accept&quot; value=&quot;Evil Plans&quot; checked=&quot;true&quot; /> ]

    3.*��ѡ������[attribute*=value]��ƥ��������������԰���ĳЩֵ��Ԫ�ء��ٸ�����˵��һ��:

    html����:

    <input name="man-news" /><input name="milkman" /><input name="letterman2" /><input name="newmilk" />
    jQuery ����:

    $("input[name*='man']")
    ���:[ <input name=&quot;man-news&quot; />, <input name=&quot;milkman&quot; />, <input name=&quot;letterman2&quot; /> ]

    4.@��ƥ������������Ե�Ԫ�ء�ע�⣬��jQuery 1.3�У�ǰ����@�����Ѿ����ϳ��������Ҫ�������°汾��ֻ��Ҫ��ȥ��@���ż��ɡ�

    5.^��ѡ������[attribute^=value]��ƥ���������������ĳЩֵ��ʼ��Ԫ�أ�����ٸ�������˵��һ�£�

    html����:

    <input name="newsletter" /><input name="milkman" /><input name="newsboy" />
    jQuery ����:

    $("input[name^='news']")
    ���:[ <input name=&quot;newsletter&quot; />, <input name=&quot;newsboy&quot; /> ]
    
    
      
����:http://www.i5good.com/20121109136.html