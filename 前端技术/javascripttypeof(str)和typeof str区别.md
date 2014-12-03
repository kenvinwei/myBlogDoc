              
          
    写javascript脚本的时候，常常会遇到判断数据类型的情况，大多情况下我们用typeof解决问题。

    今天在读代码的时候发现跟我以前的写法有写不同，以前如果我要写判断str类型常常会写成：

    var type = typeof(str);
    然而今天看到了，typeof写成如下形式：

    var type = typeof str;
    同样可以得到想要的结果，为什么typeof有这样的写法呢？

    原来typeof是运算符，其优先级高于加、减、乘、除，所以我们在写代码的时候应到区分这样的两种情况哦！！

    var str = '11';var type1 = typeof(str*1);var type2 = typeof str*1;
    得到的结果type1为number而type2为NAN，所以，我们在用typeof的时候特别要注意这样的情况哦～～～

    
    
    
      
来自:http://www.i5good.com/2012022877.html