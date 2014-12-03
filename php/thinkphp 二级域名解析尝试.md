              
          
    本测试主要二级域名进行重写操作：

    测试地址  ：http://news.news.tiger

    实际地址：  http://news.tiger/index.php?s=News

    以下是我写的配置文件：

    server {              listen       80;        server_name *.news.tiger;        root  /usr/data0/wwwroot/news.tiger/release;        set $tt "";        set $st "";        location ~ .*.(php|php5)?$        {            #fastcgi_pass  unix:/tmp/php-cgi.sock;            fastcgi_pass   127.0.0.1:9000;            fastcgi_index index.php;            #include fcgi.conf;            fastcgi_param SCRIPT_FILENAME  /usr/data0/wwwroot/news.tiger/release/$fastcgi_script_name;            include fastcgi_params;        }        if ( $http_host ~ "^(.*).news.tiger$" )         {                       set $my_file $1;        }        location ~ .*.(gif|jpg|jpeg|png|bmp|swf)$        {                expires      30d;        }         if ($request_uri !~ .*.(ico|cur|gif|jpg|jpeg|png|bmp|swf|js|css|php|html|xml|htm))         {             set $tt 0;         }        if ( $my_file ~ "news") {            #rewrite ^/(.*) /News;            set $st  1$tt;        }        if ($st ~ "10"){            rewrite ^/(.*) /News;        }        location / {                                     index  index.php;                     if (!-e $request_filename) {                        rewrite  ^/(.*)index.php(.*)$  $1/index.php?s=$2  last;                        rewrite  ^/(.*)en.php(.*)$  $1/en.php?s=$2                 last;                                                                  break;                               }                           }         if ($request_uri !~ .*.(ico|cur|gif|jpg|jpeg|png|bmp|swf|js|css|php|html|xml|htm)) {                rewrite ^/(.*) /index.php/$1 last;                break;        }        #rewrite ^/(.*)    http://news.tiger/$domain/$1 permanent; }
     nginx 中if 支持嵌套的写法，if语句中再写if 就会报语法错误，基于这种情况，用set 变量组合用户判定复合条件，还是比较不错的选择。

    本日志内容来自互联网和平日使用经验，整理一下方便日后参考。正则表达式匹配，其中：  * ~ 为区分大小写匹配  * ~* 为不区分大小写匹配  * !~和!~*分别为区分大小写不匹配及不区分大小写不匹配文件及目录匹配，其中：  * -f和!-f用来判断是否存在文件  * -d和!-d用来判断是否存在目录  * -e和!-e用来判断是否存在文件或目录  * -x和!-x用来判断文件是否可执行flag标记有：  * last 相当于Apache里的[L]标记，表示完成rewrite  * break 终止匹配, 不再匹配后面的规则  * redirect 返回302临时重定向 地址栏会显示跳转后的地址  * permanent 返回301永久重定向 地址栏会显示跳转后的地址一些可用的全局变量有，可以用做条件判断(待补全)  $args  $content_length  $content_type  $document_root  $document_uri  $host  $http_user_agent  $http_cookie  $limit_rate  $request_body_file  $request_method  $remote_addr  $remote_port  $remote_user  $request_filename  $request_uri  $query_string  $scheme  $server_protocol  $server_addr  $server_name  $server_port  $uri 
    
    
      
来自:http://www.i5good.com/20120814117.html