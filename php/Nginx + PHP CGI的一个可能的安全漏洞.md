              
          
    �����ձ��Nginx+PHPcgi���������������ļ���,��ͨ������ƥ��( Nginx(PHP/fastcgi)��PATH_INFO����)����SCRIPT_FILENAME,���� С�ٷ�����һ�����ַ�ʽ�İ�ȫ©��.

    ����,��http://www.laruence.com/fake.jpg,��ôͨ���������µ�URL,�Ϳ��Կ���fake.jpg�Ķ���������:

    
    

    http://www.laruence.com/fake.jpg/foo.php

    Ϊʲô��������?

    ����,���µ�nginxconf:

    
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

    ͨ������ƥ���Ժ�,SCRIPT_NAME�ᱻ����Ϊ��fake.jpg/foo.php��,�̶������SCRIPT_FILENAME���ݸ�PHPCGI,����PHP��Ϊʲô����������Ĳ���,���Ұ�a.jpg������?

    ���Ҫ˵��PHP��cgiSAPI�еĲ���,fix_pathinfo��:

    
    ;cgi.fix_pathinfoprovides*real*PATH_INFO/PATH_TRANSLATEDsupportforCGI.PHP&#39;s

    ;previousbehaviourwastosetPATH_TRANSLATEDtoSCRIPT_FILENAME,andtonotgrok

    ;whatPATH_INFOis.FormoreinformationonPATH_INFO,seethecgispecs.Setting

    ;thisto1willcausePHPCGItofixit&#39;spathstoconformtothespec.Asetting

    ;ofzerocausesPHPtobehaveasbefore.Defaultis1.Youshouldfixyourscripts

    ;touseSCRIPT_FILENAMEratherthanPATH_TRANSLATED.

    cgi.fix_pathinfo=1

    ������������ѡ��,��ô�ͻᴥ����PHP�е������߼�:

    
    /*

    *ifthefiledoesn&#39;texist,trytoextractPATH_INFOout

    *ofitbystat&#39;ingbackthroughthe&#39;/&#39;

    *thisfixesurl&#39;slike/info.php/test

    */

    if(script_path_translated&;&;

    (script_path_translated_len=strlen(script_path_translated))>0&;&;

    (script_path_translated[script_path_translated_len-1]==&#39;/&#39;||

    ....//����ʡ��.

    ������,PHP����ΪSCRIPT_FILENAME��fake.jpg,��foo.php��PATH_INFO,Ȼ��PHP�Ͱ�fake.jpg����һ��PHP�ļ�������ִ�С�So��

    ���������Σ����С�ٵĻ���˵,�Ǿ޴��.

    ����һЩ��̳��˵,����ϴ�һ��ͼƬ(ʵ�����Ƕ����PHP�ű�),�̶����������ķ�������

    ����,�������������ַ����������,���Ų�,���������,��ر�fix_pathinfo(Ĭ���ǿ�����).

    ���ĵ�ַ: http://www.laruence.com/2009/11/13/1138.html
    
    
      
����:http://www.i5good.com/2012033084.html