              
          
    第一步：      

          下载zenddebugger，下载地址：http://www.zend.com/en/products/studio/downloads，注意自己系统是32位还是64位，不然会出错。

    第二步：

          解压下载完的 zenddebugger：   

    tar -zxvf ZendDebugger-20110410-linux-glibc23-i386.tar.gz ZendDebugger-20110410-linux-glibc23-i386/ZendDebugger-20110410-linux-glibc23-i386/4_3_x_comp/ZendDebugger-20110410-linux-glibc23-i386/4_3_x_comp/ZendDebugger.soZendDebugger-20110410-linux-glibc23-i386/4_4_x_comp/ZendDebugger-20110410-linux-glibc23-i386/4_4_x_comp/ZendDebugger.soZendDebugger-20110410-linux-glibc23-i386/5_0_x_comp/ZendDebugger-20110410-linux-glibc23-i386/5_0_x_comp/ZendDebugger.soZendDebugger-20110410-linux-glibc23-i386/5_1_x_comp/ZendDebugger-20110410-linux-glibc23-i386/5_1_x_comp/ZendDebugger.soZendDebugger-20110410-linux-glibc23-i386/5_2_x_comp/ZendDebugger-20110410-linux-glibc23-i386/5_2_x_comp/ZendDebugger.soZendDebugger-20110410-linux-glibc23-i386/5_3_x_comp/ZendDebugger-20110410-linux-glibc23-i386/5_3_x_comp/ZendDebugger.soZendDebugger-20110410-linux-glibc23-i386/dummy.phpZendDebugger-20110410-linux-glibc23-i386/README.txt
    第三步： 

          放到zend对应php版本下：

    cp ZendDebugger.so  /home/wei/Zend/ZendStudio-5.5.1/lib/php5
    第四步：

          在php.ini中添加加载项：

    [wei@localhost php]$>vim ./etc/php.ini
          在最末尾添加如下代码：

    [Zend Optimizer]zend_optimizer.optimization_level=1zend_extension=&quot;/usr/local/zend/ZendOptimizer.so&quot;   [Zend Debug]zend_extension=/home/wei/Zend/ZendStudio-5.5.1/lib/php5/ZendDebugger.sozend_debugger.allow_hosts=127.0.0.1/192.168.1.243/32zend_debugger.expose_remotely=always

    最后：

          重启php-fpm:

    [wei@localhost sbin]$>sudo ./php-fpm restart[sudo] password for wei: Shutting down php_fpm . doneStarting php_fpm Failed loading /home/wei/Zend/ZendStudio-5.5.1/lib/php5/ZendDebugger.so:  libssl.so.0.9.8: cannot open shared object file: No such file or directory done
    问题：

           Failed loading /home/wei/Zend/ZendStudio-5.5.1/lib      /php5/ZendDebugger.so: libssl.so.0.9.8: cannot open shared object file: No such file or directory

    解决：

       此问题是下载的ZendDebugger是32位，而你的系统是64位导致的，下载64的重复以上过程，问题解决！

       如果出现错误“Failed loading /usr/lib64/php/modules/ZendDebugger.so: libssl.so.0.9.8: cannot open shared object file: No such file or directory”

      原因：因为最新的linux发行版本 libssl 和 libcrypto 已升级到1.0.0

       解决：     只要创建相应的软链接就可以     sudo ln -s /usr/lib64/libcrypto.so /usr/lib64/libcrypto.so.0.9.8     sudo ln -s /usr/lib64/libssl.so.10 /usr/lib64/libssl.so.0.9.8

    查看：

     
    
    
      
来自:http://www.i5good.com/20120613107.html