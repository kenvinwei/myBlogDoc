              
          
    现在普遍的Nginx+PHPcgi的做法是在配置文件中,　通过正则匹配( Nginx(PHP/fastcgi)的PATH_INFO问题)设置SCRIPT_FILENAME,今天 小顿发现了一个这种方式的安全漏洞.

    比如,有http://www.laruence.com/fake.jpg,那么通过构造如下的URL,就可以看到fake.jpg的二进制内容:

    
    

    http://www.laruence.com/fake.jpg/foo.php

    为什么会这样呢?

    比如,如下的nginxconf:

    
    location~.php($|/){

    fastcgi_pass127.0.0.1:9000;

    fastcgi_indexindex.php;

    

    set$script$uri;

    set$path_info&quot;&quot;;

    if($uri~&quot;^(.+.php)(/.*)&quot;){

    set$script$1;

    set$path_info$2;

    }

    

    includefastcgi_params;

    fastcgi_paramSCRIPT_FILENAME$document_root$script;

    fastcgi_paramSCRIPT_NAME$script;

    fastcgi_paramPATH_INFO$path_info;

    }

    通过正则匹配以后,SCRIPT_NAME会被设置为”fake.jpg/foo.php”,继而构造成SCRIPT_FILENAME传递个PHPCGI,但是PHP又为什么会接受这样的参数,并且把a.jpg解析呢?

    这就要说到PHP的cgiSAPI中的参数,fix_pathinfo了:

    
    ;cgi.fix_pathinfoprovides*real*PATH_INFO/PATH_TRANSLATEDsupportforCGI.PHP&#39;s

    ;previousbehaviourwastosetPATH_TRANSLATEDtoSCRIPT_FILENAME,andtonotgrok

    ;whatPATH_INFOis.FormoreinformationonPATH_INFO,seethecgispecs.Setting

    ;thisto1willcausePHPCGItofixit&#39;spathstoconformtothespec.Asetting

    ;ofzerocausesPHPtobehaveasbefore.Defaultis1.Youshouldfixyourscripts

    ;touseSCRIPT_FILENAMEratherthanPATH_TRANSLATED.

    cgi.fix_pathinfo=1

    如果开启了这个选项,那么就会触发在PHP中的如下逻辑:

    
    /*

    *ifthefiledoesn&#39;texist,trytoextractPATH_INFOout

    *ofitbystat&#39;ingbackthroughthe&#39;/&#39;

    *thisfixesurl&#39;slike/info.php/test

    */

    if(script_path_translated&;&;

    (script_path_translated_len=strlen(script_path_translated))>0&;&;

    (script_path_translated[script_path_translated_len-1]==&#39;/&#39;||

    ....//以下省略.

    到这里,PHP会认为SCRIPT_FILENAME是fake.jpg,而foo.php是PATH_INFO,然后PHP就把fake.jpg当作一个PHP文件来解释执行…So…

    这个隐患的危害用小顿的话来说,是巨大的.

    对于一些论坛来说,如果上传一个图片(实际上是恶意的PHP脚本),继而构造这样的访问请求…

    所以,大家如果有用这种服务器搭配的,请排查,如果有隐患,请关闭fix_pathinfo(默认是开启的).

    本文地址: http://www.laruence.com/2009/11/13/1138.html
    
    
      
来自:http://www.i5good.com/2012033084.html