              
          
    ��һ����      

          ����zenddebugger�����ص�ַ��http://www.zend.com/en/products/studio/downloads��ע���Լ�ϵͳ��32λ����64λ����Ȼ�����

    �ڶ�����

          ��ѹ������� zenddebugger��   

    tar -zxvf ZendDebugger-20110410-linux-glibc23-i386.tar.gz ZendDebugger-20110410-linux-glibc23-i386/ZendDebugger-20110410-linux-glibc23-i386/4_3_x_comp/ZendDebugger-20110410-linux-glibc23-i386/4_3_x_comp/ZendDebugger.soZendDebugger-20110410-linux-glibc23-i386/4_4_x_comp/ZendDebugger-20110410-linux-glibc23-i386/4_4_x_comp/ZendDebugger.soZendDebugger-20110410-linux-glibc23-i386/5_0_x_comp/ZendDebugger-20110410-linux-glibc23-i386/5_0_x_comp/ZendDebugger.soZendDebugger-20110410-linux-glibc23-i386/5_1_x_comp/ZendDebugger-20110410-linux-glibc23-i386/5_1_x_comp/ZendDebugger.soZendDebugger-20110410-linux-glibc23-i386/5_2_x_comp/ZendDebugger-20110410-linux-glibc23-i386/5_2_x_comp/ZendDebugger.soZendDebugger-20110410-linux-glibc23-i386/5_3_x_comp/ZendDebugger-20110410-linux-glibc23-i386/5_3_x_comp/ZendDebugger.soZendDebugger-20110410-linux-glibc23-i386/dummy.phpZendDebugger-20110410-linux-glibc23-i386/README.txt
    �������� 

          �ŵ�zend��Ӧphp�汾�£�

    cp ZendDebugger.so  /home/wei/Zend/ZendStudio-5.5.1/lib/php5
    ���Ĳ���

          ��php.ini����Ӽ����

    [wei@localhost php]$>vim ./etc/php.ini
          ����ĩβ������´��룺

    [Zend Optimizer]zend_optimizer.optimization_level=1zend_extension=&quot;/usr/local/zend/ZendOptimizer.so&quot;   [Zend Debug]zend_extension=/home/wei/Zend/ZendStudio-5.5.1/lib/php5/ZendDebugger.sozend_debugger.allow_hosts=127.0.0.1/192.168.1.243/32zend_debugger.expose_remotely=always

    ���

          ����php-fpm:

    [wei@localhost sbin]$>sudo ./php-fpm restart[sudo] password for wei: Shutting down php_fpm . doneStarting php_fpm Failed loading /home/wei/Zend/ZendStudio-5.5.1/lib/php5/ZendDebugger.so:  libssl.so.0.9.8: cannot open shared object file: No such file or directory done
    ���⣺

           Failed loading /home/wei/Zend/ZendStudio-5.5.1/lib      /php5/ZendDebugger.so: libssl.so.0.9.8: cannot open shared object file: No such file or directory

    �����

       �����������ص�ZendDebugger��32λ�������ϵͳ��64λ���µģ�����64���ظ����Ϲ��̣���������

       ������ִ���Failed loading /usr/lib64/php/modules/ZendDebugger.so: libssl.so.0.9.8: cannot open shared object file: No such file or directory��

      ԭ����Ϊ���µ�linux���а汾 libssl �� libcrypto ��������1.0.0

       �����     ֻҪ������Ӧ�������ӾͿ���     sudo ln -s /usr/lib64/libcrypto.so /usr/lib64/libcrypto.so.0.9.8     sudo ln -s /usr/lib64/libssl.so.10 /usr/lib64/libssl.so.0.9.8

    �鿴��

     
    
    
      
����:http://www.i5good.com/20120613107.html