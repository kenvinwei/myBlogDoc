              
          
    刚刚测试发现一段很简单的、看似正确的代码却是错误的：

    <?php  $json_str = "{'name':'Eric', 'age':23}";  var_dump(json_decode($json_str));
    大家知道PHP 版本自从5.2.0 之后添加了两个支持json 的函数，分别是json_encode 和json_decode，其中json_decode 函数是把json 字符串转换为json 对象，如上例所示。但上面的例子的输出却为null，即转换失败了。这究竟是为什么呢，baidu 了一下，有人说是PHP 的这两个函数对json 的支持不够完全导致的，解决办法是写成以下的形式：

    <?php  $json_str = '{"name":"Eric", "age":23,}';   //$json_str = "{/"name/":/"Eric/", /"age/":23}"; //这样也行  var_dump(json_decode($json_str));
    把单引号改成双引号就行了，可这真的是PHP 的一个失误吗？随后上了json 官网 一查发现，双引号才是json 的标准，单引号是不规范的（虽然在js 中是行的通的）！所以大家以后养成习惯，把json 的名称和字符串值用双引号引起来咯~

     
    
    
      
来自:http://www.i5good.com/20121106135.html