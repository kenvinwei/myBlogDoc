              
          
    PATH_INFO��һ��CGI1.1�ı�׼������������Ϊ��������.

    ����,���ǿ���ʹ��PATH_INFO������Rewrite��ʵ��α��̬ҳ��,���ⲻ��PHP���Ҳʹ��PATH_INFO����Ϊ·������.

    ��Apache��,���������õ�ʱ��,����PHP�ű�,AcceptPathInfo��Ĭ�Ͻ��ܵ�,Ҳ����˵:

    ����ڷ������ڴ���һ��/laruence/index.php

    ��ô,������������,

    
    /laruence/index.php/dummy

    /laruence/dummy

    Apache������,������Ϊ�Ƕ�info.php�ķ���,��������PATH_INFOΪdummy

    ������Nginx��,�ǲ�֧��PATHINFO��,Ҳ����������Ĭ������PATH_INFO.

    ����ΪĬ�ϵ������ļ���PHP��֧��ֻ�Ǻܻ�����,���Զ���Ĭ��������˵��������ķ���Ҳ����404,��ʾ�Ҳ����ļ�����.

    �����һЩʹ��PATH_INFO�����ݹؼ���Ϣ��PHP�����˵(����Kohana,Thinkphp),��ֱ��������.

    �����������,һ����˵�����ֽ������,��һ�־���ʹ��rewrite,�������������ȱ��Ҳ�Ǻ����Ե�,��Ҫ��PATH_INFOת����QueryString.�˴��Ͳ�˵�����ַ�����~

    ��,�ڶ��ַ��������ҽ���Ҫ���,ģ��PATH_INFO:

    ����,����֪����Nginx��,��ͨ�����ļ�������չ��ƥ��,�������Ƿ�Ҫ����phpcgi������ȥ���͵�.��nginx.conf��һ�㶼�����µ�Ĭ�����ö�:

    
    location~.php${

    fastcgi_indexindex.php;

    fastcgi_pass127.0.0.1:9000;

    includefastcgi_params;

    }

    ����,��������/laruence/info.php/pathinfo�������ļ�·��,Nginx�ǲ�����ȷ�Ľ���phpcgi��������.����������Ҫ��д�������Ϊ:

    
    location~.php{//Ƭ��ƥ��

    fastcgi_indexindex.php;

    fastcgi_pass127.0.0.1:9000;

    includefastcgi_params;

    }

    ����,�ű�·���Ѿ�����PHP�Լ�������.����ô����PATH_INFO��?

    ����,������Ҫ��PHP��cgi.fix_pathinfo������,������������Ժ�,PHP��ȥ����CGI�淶�����SCRIPT_FILENAME���ǲ����Ƿ��ʽű���PATH_INFO( ini���ý���),������SCRIPT_NAME���޸�PATH_INFO(��PATH_TRANSLATED)Ϊ��ȷ��ֵ(��ʵҲ����˵��,PHP�����CGI1.1��֧�ֲ�����λ)

    Ȼ��,��ֻҪ���һ��FASTCGI_PARAM��ͺ���:

    
    location~.php{

    fastcgi_indexindex.php;

    fastcgi_pass127.0.0.1:9000;

    includefastcgi_params;

    fastcgi_paramPATH_INFO$fastcgi_script_name;

    }

    �������԰ɡ�

    btw:��Ȼ,����Ľ������,�Ѷ�·���ķ���������PHPȥ����,����Ҳ�����Ѹ���������һ�����÷���,�����������Nginx������·��(Ҳ�Ͳ���Ҫfix_pathinfo):

    
    location~.php

    {

    fastcgi_indexindex.php;

    fastcgi_pass127.0.0.1:9000;

    includefastcgi_params;

    set$path_info&quot;&quot;;

    set$real_script_name$fastcgi_script_name;

    if($fastcgi_script_name~&quot;^(.+?.php)(/.+)$&quot;){

    set$real_script_name$1;

    set$path_info$2;

    }

    fastcgi_paramSCRIPT_FILENAME/var/html/$real_script_name;

    fastcgi_paramSCRIPT_NAME$real_script_name;

    fastcgi_paramPATH_INFO$path_info;

    }
���,������ֵ�һ����ȫ©��( Nginx+PHPCGI��һ�����ܵİ�ȫ©��)����������й�ϵ,���������ʹ�õڶ������õ�ʱ��,�ر�cgi.fix_pathinfo.����������©���Ҹ�����Ϊ�����Nginxûɶ��ϵ,������Nginx��©��.�����õ�����,���ڵ�������˵��Nginx��Bug,���ײ���.
    ���ĵ�ַ: http://www.laruence.com/2009/11/13/1138.html
    
    
      
����:http://www.i5good.com/2012033083.html