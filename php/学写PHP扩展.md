              
          
    假设要有这么一个扩展，提供一个叫ccvita_string的函数，他的主要作用是返回一段字符。对应的PHP代码可能是这样：

    functionccvita_string($str){     $result= '<a href="'.$str.'">Link</a>'；     return$result;}
    第一步，生成代码

    PHP为了扩展开发的方便，提供了一个类似代码生成器的工具ext_skel，具体可以参见说明。首先我们创建一个文件ccvita.skel，它的内容为

    string ccvita_string(string str)

    就是告诉ext_skel这个东西，我们要做的扩展里面有个函数叫ccvita_string。然后执行

    cdMooENV/src/php-5.3.8/ext/./ext_skel--extname=ccvita --proto=ccvita.skelcdccvita/

    这时候，ccvita这个扩展的代码框架就已经出来了。

    第二步，修改配置然后修改config.m4文件将10、11、12三行最前面的dnl删除掉，就是将

    dnl PHP_ARG_WITH(ccvita, forccvita support,dnl Make sure that the comment is aligned:dnl [  --with-ccvita             Include ccvita support])

    修改为

    PHP_ARG_WITH(ccvita, forccvita support,Make sure that the comment is aligned:[  --with-ccvita             Include ccvita support])

    第三步，实现功能修改源码ccvita.c文件找到将ccvita_string这个函数修改为

    PHP_FUNCTION(ccvita_string){    char*str = NULL;    intargc = ZEND_NUM_ARGS();    intstr_len;    char*result;      if(zend_parse_parameters(argc TSRMLS_CC, "s", &;str, &;str_len) == FAILURE)         return;      str_len = spprintf(&;result, 0, "<a href="%.78s">Link</a>", str);    RETURN_STRINGL(result, str_len, 0); }

    第四步，编译扩展保存后，开始编译

    /usr/local/php/bin/phpize./configure--with-php-config=/usr/local/php/bin/php-configmake

    第五步，添加扩展这时候，一切顺利的话，该扩展已经在modules/ccvita.so这个位置了。下面就是将这个扩展加入到 PHP中去，让我们PHP程序可以调用到。

    cpmodules/ccvita.so /usr/local/php/ext/vim /usr/local/php/etc/php.ini#在php.ini文件最后增加这一行extension=/usr/local/php/ext/ccvita.so#重启PHP服务service php-fpm restartcpccvita.php /data/www/wwwroot/default/

    接下来就可以访问ccvita.php这个文件，测试扩展了。
    
    
      
来自:http://www.i5good.com/20121009129.html