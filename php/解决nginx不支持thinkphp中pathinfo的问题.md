              
          
    ���⣺thinkphp���������£���URL_MODEL��=>2Ȼ�����·���мӡ�/����·������404״̬�����Ϻܶ������������Ƕ�һ�������й��ĸ�������̫ǿ�ˣ����ڷ���web����Ž����������Ҫ��δ�ҵ�����������ƥ�䣬nginx.conf���������·�����location / {                 index index.php;         if (!-e $request_filename) {          rewrite ^/(.*)index.php(.*)$ $1/index.php?s=$2 last;  //�ؼ����                               break;              }                }  �¼ӡ�rewrite ^/(.*)index.php(.*)$ $1/index.php?s=$2 last;�� Ȼ�� ��thinkphp ͨ�õļ��ݵĽ���������������õ������   

    ��������ٽ���php�ĸĳ����£�

    location ~ .php($|/) { fastcgi_pass   127.0.0.1:9000;fastcgi_index index.php;include fcgi.conf;fastcgi_param PATH_INFO $fastcgi_script_name;fastcgi_param SCRIPT_FILENAME  /usr/data0/wwwroot/$fastcgi_script_name;include        fastcgi_params;}
    ����õ������   
    
    
      
����:http://www.i5good.com/2011122939.html