              
          
    ����Ҫ����ôһ����չ���ṩһ����ccvita_string�ĺ�����������Ҫ�����Ƿ���һ���ַ�����Ӧ��PHP���������������

    functionccvita_string($str){     $result= '<a href="'.$str.'">Link</a>'��     return$result;}
    ��һ�������ɴ���

    PHPΪ����չ�����ķ��㣬�ṩ��һ�����ƴ����������Ĺ���ext_skel��������Բμ�˵�����������Ǵ���һ���ļ�ccvita.skel����������Ϊ

    string ccvita_string(string str)

    ���Ǹ���ext_skel�������������Ҫ������չ�����и�������ccvita_string��Ȼ��ִ��

    cdMooENV/src/php-5.3.8/ext/./ext_skel--extname=ccvita --proto=ccvita.skelcdccvita/

    ��ʱ��ccvita�����չ�Ĵ����ܾ��Ѿ������ˡ�

    �ڶ������޸�����Ȼ���޸�config.m4�ļ���10��11��12������ǰ���dnlɾ���������ǽ�

    dnl PHP_ARG_WITH(ccvita, forccvita support,dnl Make sure that the comment is aligned:dnl [  --with-ccvita             Include ccvita support])

    �޸�Ϊ

    PHP_ARG_WITH(ccvita, forccvita support,Make sure that the comment is aligned:[  --with-ccvita             Include ccvita support])

    ��������ʵ�ֹ����޸�Դ��ccvita.c�ļ��ҵ���ccvita_string��������޸�Ϊ

    PHP_FUNCTION(ccvita_string){    char*str = NULL;    intargc = ZEND_NUM_ARGS();    intstr_len;    char*result;      if(zend_parse_parameters(argc TSRMLS_CC, "s", &;str, &;str_len) == FAILURE)         return;      str_len = spprintf(&;result, 0, "<a href="%.78s">Link</a>", str);    RETURN_STRINGL(result, str_len, 0); }

    ���Ĳ���������չ����󣬿�ʼ����

    /usr/local/php/bin/phpize./configure--with-php-config=/usr/local/php/bin/php-configmake

    ���岽�������չ��ʱ��һ��˳���Ļ�������չ�Ѿ���modules/ccvita.so���λ���ˡ�������ǽ������չ���뵽 PHP��ȥ��������PHP������Ե��õ���

    cpmodules/ccvita.so /usr/local/php/ext/vim /usr/local/php/etc/php.ini#��php.ini�ļ����������һ��extension=/usr/local/php/ext/ccvita.so#����PHP����service php-fpm restartcpccvita.php /data/www/wwwroot/default/

    �������Ϳ��Է���ccvita.php����ļ���������չ�ˡ�
    
    
      
����:http://www.i5good.com/20121009129.html