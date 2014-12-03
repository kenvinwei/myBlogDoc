              
          mysql中case when语句的使用方法是学习mysql数据库不可不学的，下文就列举了三种mysql中case when语句使用方法，供您借鉴参考。
    1.

    selectname, case whenbirthday<'1981'then'old' whenbirthday>'1988'then'yong' else'ok'ENDYORN fromlee;
    2.

    selectNAME, casename when'sam'then'yong' when'lee'then'handsome' else'good'end fromlee;
    当然了case when语句还可以复合

    3.

    selectname,birthday, case whenbirthday>'1983'then'yong' whenname='lee'then'handsome' else'justsoso'end fromlee; 
    以上就是mysql中case when语句的使用示例的介绍。
      
    
      
来自:http://www.i5good.com/2012011249.html