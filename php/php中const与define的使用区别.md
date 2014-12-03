              
          
    1、const用于类成员变量定义，一旦定义且不能改变其值。define定义全局常量，在任何地方都可以访问。2、define不能在类中定义而const可以。3、const不能在条件语句中定义常量if (...) {   const FOO = &#39;BAR&#39;;  // invalid } but if (...) {   define(&#39;FOO&#39;, &#39;BAR&#39;); // valid } 4、const采用一个普通的常量名称，define可以采用表达式作为名称。const FOO = &#39;BAR&#39;; for ($i = 0; $i < 32; ++$i) {   define(&#39;BIT_&#39; . $i, 1 << $i); } 5、const只能接受静态的标量，而define可以采用任何表达式。const BIT_5 = 1 << 5;  // invalid but define(&#39;BIT_5&#39;, 1 << 5); // valid 6、const 总是大小写敏感，然而define()可以通过第三个参数来定义大小写不敏感的常量define(&#39;FOO&#39;, &#39;BAR&#39;, true); echo FOO; // BAR echo foo; // BAR 总结：使用const简单易读，它本身是一个语言结构，而define是一个方法，用const定义在编译时比define快很多。
    
    
      
来自:http://www.i5good.com/20121112137.html