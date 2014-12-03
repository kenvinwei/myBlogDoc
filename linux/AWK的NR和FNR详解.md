              
          
    NR：表示awk开始执行程序后所读取的数据行数.

    FNR：与NR功用类似,不同的是awk每打开一个新文件,FNR便从0重新累计.

    下面看两个例子: 

    1,对于单个文件NR 和FNR 的 输出结果一样的 ：

    # awk &#39;{print NR,$0}&#39; file1 1 a b c d2 a b d c

    3 a c b d

    #awk &#39;{print FNR,$0}&#39; file1 1 a b c d2 a b d c3 a c b d 

    2,但是对于多个文件 ：

    # awk &#39;{print NR,$0}&#39; file1 file21 a b c d2 a b d c3 a c b d4 aa bb cc dd5 aa bb dd cc6 aa cc bb dd

    # awk &#39;{print FNR,$0}&#39; file1 file21 a b c d2 a b d c3 a c b d1 aa bb cc dd2 aa bb dd cc3 aa cc bb dd

    在看一个例子关于NR和FNR的典型应用:

    现在有两个文件格式如下：

    #cat account张三|000001李四|000002#cat cdr000001|10000001|20000002|30000002|15

    想要得到的结果是将用户名，帐号和金额在同一行打印出来,如下:

    张三|000001|10张三|000001|20李四|000002|30李四|000002|15

    执行如下代码

    #awk -F | &#39;NR==FNR{a[$2]=$0;next}{print a[$1]&quot;|&quot;$2}&#39; account cdr

    注释:

    由 NR=FNR为真时,判断当前读入的是第一个文件account,然后使用{a[$2]=$0;next}循环将account文件的每行记录都存入数组a,并使用$2第2个字段作为下标引用.

    由NR=FNR为假时,判断当前读入了第二个文件cdr,然后跳过{a[$2]=$0;next},对第二个文件cdr的每一行都无条件执行{print a[$1]&quot;|&quot;$2},此时变量$1为第二个文件的第一个字段,与读入第一个文件时,采用第一个文件第二个字段$2为数组下标相同.因此可以在此使用a[$1]引用数组。
    
    
      
来自:http://www.i5good.com/20120807116.html