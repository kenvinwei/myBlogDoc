              
          
    PATH_INFO是一个CGI1.1的标准，经常用来做为传参载体.

    比如,我们可以使用PATH_INFO来代替Rewrite来实现伪静态页面,另外不少PHP框架也使用PATH_INFO来作为路由载体.

    在Apache中,当不加配置的时候,对于PHP脚本,AcceptPathInfo是默认接受的,也就是说:

    如果在服务器在存在一个/laruence/index.php

    那么,对于如下请求,

    
    /laruence/index.php/dummy

    /laruence/dummy

    Apache都接受,都会认为是对info.php的访问,并会设置PATH_INFO为dummy

    而对于Nginx下,是不支持PATHINFO的,也就是它不会默认设置PATH_INFO.

    而因为默认的配置文件对PHP的支持只是很基础的,所以对于默认配置来说对于上面的访问也会是404,提示找不到文件出错.

    这对于一些使用PATH_INFO来传递关键信息的PHP框架来说(比如Kohana,Thinkphp),简直是致命的.

    对于这个问题,一般来说有俩种解决方法,第一种就是使用rewrite,但是这个方法的缺点也是很明显的,需要把PATH_INFO转换成QueryString.此处就不说明这种方法了~

    而,第二种方法就是我今天要提的,模拟PATH_INFO:

    首先,我们知道在Nginx中,是通过对文件名的扩展名匹配,来决定是否要交给phpcgi服务器去解释的.在nginx.conf中一般都有如下的默认配置段:

    
    location~.php${

    fastcgi_indexindex.php;

    fastcgi_pass127.0.0.1:9000;

    includefastcgi_params;

    }

    所以,对于形如/laruence/info.php/pathinfo这样的文件路径,Nginx是不会正确的交给phpcgi服务器的.所以我们需要改写这段配置为:

    
    location~.php{//片段匹配

    fastcgi_indexindex.php;

    fastcgi_pass127.0.0.1:9000;

    includefastcgi_params;

    }

    现在,脚本路径已经交由PHP自己处理了.那怎么增加PATH_INFO呢?

    首先,我们需要打开PHP中cgi.fix_pathinfo配置项,打开这个配置项以后,PHP会去根据CGI规范来检查SCRIPT_FILENAME中那部分是访问脚本和PATH_INFO( ini配置解释),并根据SCRIPT_NAME来修改PATH_INFO(和PATH_TRANSLATED)为正确的值(其实也就是说明,PHP最初对CGI1.1的支持并不到位)

    然后,就只要添加一个FASTCGI_PARAM项就好了:

    
    location~.php{

    fastcgi_indexindex.php;

    fastcgi_pass127.0.0.1:9000;

    includefastcgi_params;

    fastcgi_paramPATH_INFO$fastcgi_script_name;

    }

    现在试试吧…

    btw:当然,上面的解决方法,把对路径的分析交给了PHP去处理,网上也有朋友给出了另外一种配置方法,这个方法是由Nginx来分析路径(也就不需要fix_pathinfo):

    
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
后记,最近发现的一个安全漏洞( Nginx+PHPCGI的一个可能的安全漏洞)和这个配置有关系,请大家务必在使用第二种配置的时候,关闭cgi.fix_pathinfo.另外关于这个漏洞我个人认为这个和Nginx没啥关系,不属于Nginx的漏洞.是配置的问题,现在到处都在说是Nginx的Bug,不妥不妥.
    本文地址: http://www.laruence.com/2009/11/13/1138.html
    
    
      
来自:http://www.i5good.com/2012033083.html