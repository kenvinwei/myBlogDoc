              
          
      php�����У���ôȷ������ִ������أ�php-fpm�Ϳ��������������php-fpm.conf����һ��request_slowlog_timeoutѡ����ѡ�����������ִ�л����Ľű�����������ͬ����ջһ���¼����־�ļ��С������������ã�����<value name=&quot;request_slowlog_timeout&quot;>5s</value>����<value name=&quot;slowlog&quot;>logs/slow.log</value>�����������������п����ģ��ű������� 5 �����ϣ����ܿ��������� mysql ��Ӧ����ɵģ�top backtrace����Ҳ������ѭ����ɵģ�Ҳ����.....

      �������ѡ������ף�����2���ӾͿ��ԣ���ʵ���ǻ����Խ�һ����һ�´����ҵĻ�����ÿ��15��ָ����ӣ�Ҳ���Ƿ���ÿ���������ִ����䣬���߲鿴ĳĳ��ִ������php��䣬�����һ������Ķ�����

    �����ҵ�ִ�нű����ܼ򵥵�Ŷ~

    #!/bin/bashcd /usr/local/php/logs                                              logfile="./slow.log"mkdir -p `date +%Y%m%d`mv $logfile `date +%Y%m%d`/`date +%Y%m%d`_slow.logkill -USR1 `cat php-fpm.pid`
    Ȼ��crontab -e

    ��Ӷ�ʱִ����䣺

    0 15 * * * /usr/local/php/logs/cut_php_log.sh
    ��˼��ɣ�
    
    
      
����:http://www.i5good.com/20120802114.html