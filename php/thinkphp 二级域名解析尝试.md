              
          
    ��������Ҫ��������������д������

    ���Ե�ַ  ��http://news.news.tiger

    ʵ�ʵ�ַ��  http://news.tiger/index.php?s=News

    ��������д�������ļ���

    server {              listen       80;        server_name *.news.tiger;        root  /usr/data0/wwwroot/news.tiger/release;        set $tt "";        set $st "";        location ~ .*.(php|php5)?$        {            #fastcgi_pass  unix:/tmp/php-cgi.sock;            fastcgi_pass   127.0.0.1:9000;            fastcgi_index index.php;            #include fcgi.conf;            fastcgi_param SCRIPT_FILENAME  /usr/data0/wwwroot/news.tiger/release/$fastcgi_script_name;            include fastcgi_params;        }        if ( $http_host ~ "^(.*).news.tiger$" )         {                       set $my_file $1;        }        location ~ .*.(gif|jpg|jpeg|png|bmp|swf)$        {                expires      30d;        }         if ($request_uri !~ .*.(ico|cur|gif|jpg|jpeg|png|bmp|swf|js|css|php|html|xml|htm))         {             set $tt 0;         }        if ( $my_file ~ "news") {            #rewrite ^/(.*) /News;            set $st  1$tt;        }        if ($st ~ "10"){            rewrite ^/(.*) /News;        }        location / {                                     index  index.php;                     if (!-e $request_filename) {                        rewrite  ^/(.*)index.php(.*)$  $1/index.php?s=$2  last;                        rewrite  ^/(.*)en.php(.*)$  $1/en.php?s=$2                 last;                                                                  break;                               }                           }         if ($request_uri !~ .*.(ico|cur|gif|jpg|jpeg|png|bmp|swf|js|css|php|html|xml|htm)) {                rewrite ^/(.*) /index.php/$1 last;                break;        }        #rewrite ^/(.*)    http://news.tiger/$domain/$1 permanent; }
     nginx ��if ֧��Ƕ�׵�д����if�������дif �ͻᱨ�﷨���󣬻��������������set ��������û��ж��������������ǱȽϲ����ѡ��

    ����־�������Ի�������ƽ��ʹ�þ��飬����һ�·����պ�ο���������ʽƥ�䣬���У�  * ~ Ϊ���ִ�Сдƥ��  * ~* Ϊ�����ִ�Сдƥ��  * !~��!~*�ֱ�Ϊ���ִ�Сд��ƥ�估�����ִ�Сд��ƥ���ļ���Ŀ¼ƥ�䣬���У�  * -f��!-f�����ж��Ƿ�����ļ�  * -d��!-d�����ж��Ƿ����Ŀ¼  * -e��!-e�����ж��Ƿ�����ļ���Ŀ¼  * -x��!-x�����ж��ļ��Ƿ��ִ��flag����У�  * last �൱��Apache���[L]��ǣ���ʾ���rewrite  * break ��ֹƥ��, ����ƥ�����Ĺ���  * redirect ����302��ʱ�ض��� ��ַ������ʾ��ת��ĵ�ַ  * permanent ����301�����ض��� ��ַ������ʾ��ת��ĵ�ַһЩ���õ�ȫ�ֱ����У��������������ж�(����ȫ)  $args  $content_length  $content_type  $document_root  $document_uri  $host  $http_user_agent  $http_cookie  $limit_rate  $request_body_file  $request_method  $remote_addr  $remote_port  $remote_user  $request_filename  $request_uri  $query_string  $scheme  $server_protocol  $server_addr  $server_name  $server_port  $uri 
    
    
      
����:http://www.i5good.com/20120814117.html