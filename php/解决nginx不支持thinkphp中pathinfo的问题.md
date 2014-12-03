              
          
    问题：thinkphp中设置如下：“URL_MODEL”=>2然后访问路径中加“/”的路径都是404状态；网上很多解决方法，但是都一个样，中国的复制能力太强了，现在发表web集结号解决方法：主要对未找到的链接在做匹配，nginx.conf的配置如下方法：location / {                 index index.php;         if (!-e $request_filename) {          rewrite ^/(.*)index.php(.*)$ $1/index.php?s=$2 last;  //关键语句                               break;              }                }  新加“rewrite ^/(.*)index.php(.*)$ $1/index.php?s=$2 last;” 然后 用thinkphp 通用的兼容的解析方法处理，问题得到解决～   

    另外可以再解析php的改成如下：

    location ~ .php($|/) { fastcgi_pass   127.0.0.1:9000;fastcgi_index index.php;include fcgi.conf;fastcgi_param PATH_INFO $fastcgi_script_name;fastcgi_param SCRIPT_FILENAME  /usr/data0/wwwroot/$fastcgi_script_name;include        fastcgi_params;}
    问题得到解决～   
    
    
      
来自:http://www.i5good.com/2011122939.html