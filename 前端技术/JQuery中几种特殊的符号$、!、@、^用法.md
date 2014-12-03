              
          
    在刚接触JQuery的时候，感觉很容易上手，但是用了一段时间开发前台的JS时候，总感觉有点迷糊对它的理解，尤其是用到几个特殊的符号进行选择器刷选的时候，不能很好的搭配使用，现在总结一下对它们的理解，以帮助和我一样对JQuery迷茫的人们。

    1.$。在jQuery 中$(&quot;<span>&quot;)，这个语法等同于$(document.createElement(&quot;span&quot;)) ，这是一种用法，在选择元素的时候还会这样子的用：[attribute$=value]，匹配给定的属性是以某些值结尾的元素。下面举个例子来说明一下:

    html代码:

    <input name="newsletter" /><input name="milkman" /><input name="jobletter" />
    jQuery 代码:

    $("input[name$='letter']")
    结果:

    [ <input name=&quot;newsletter&quot; />, <input name=&quot;jobletter&quot; /> ]

    2.!。选择器：[attribute!=value]，匹配所有不含有指定的属性，或者属性不等于特定值的元素，此选择器等价于:not([attr=value])。

    html代码:

    <input type="checkbox" name="newsletter" value="Hot Fuzz" /><input type="checkbox" name="newsletter" value="Cold Fusion" /><input type="checkbox" name="accept" value="Evil Plans" />
    jQuery 代码:

    $("input[name!='newsletter']").attr("checked", true);
    结果:[ <input type=&quot;checkbox&quot; name=&quot;accept&quot; value=&quot;Evil Plans&quot; checked=&quot;true&quot; /> ]

    3.*。选择器：[attribute*=value]，匹配给定的属性是以包含某些值的元素。举个例子说明一下:

    html代码:

    <input name="man-news" /><input name="milkman" /><input name="letterman2" /><input name="newmilk" />
    jQuery 代码:

    $("input[name*='man']")
    结果:[ <input name=&quot;man-news&quot; />, <input name=&quot;milkman&quot; />, <input name=&quot;letterman2&quot; /> ]

    4.@。匹配包含给定属性的元素。注意，在jQuery 1.3中，前导的@符号已经被废除！如果想要兼容最新版本，只需要简单去掉@符号即可。

    5.^。选择器：[attribute^=value]，匹配给定的属性是以某些值开始的元素，下面举个例子来说明一下：

    html代码:

    <input name="newsletter" /><input name="milkman" /><input name="newsboy" />
    jQuery 代码:

    $("input[name^='news']")
    结果:[ <input name=&quot;newsletter&quot; />, <input name=&quot;newsboy&quot; /> ]
    
    
      
来自:http://www.i5good.com/20121109136.html