              
          
    ���phpͨ��localhost��������mysql(Percona Server)���ݿ�,ͨ��127.0.0.1��ip������mysql���ݿ������.
�������
    ʹ��Percona Server�������������ɹ���������my.cnf�����ļ�.����������������ok֮��,php�޷�ͨ��localhost����mysql���ݿ�.

    ����ͨ��ip��ַȴ��������.
mysql��localhost��127.0.0.1������
    localhost�ߵ��� unix sock,127.0.0.1�ߵ��� tcp
ԭ�����
����localhost�������ӵ�������,phpĬ����ʹ�õ�mysql unix sockʹ�õ��� /tmp/mysql.sock������޸���mysql�ĵ�sock��·��,��ô��Ҫ��php.ini��ָ��.

�������
    so:���php����mysql localhost��������,ͨ��127.0.0.1��ip�����ӵ�����.

    1.�޸�php.ini������,ָ��mysql.sockλ��. (�ҵ���ubuntu λ���� /var/run/mysqld/mysqld.sock )������2.�޸�my.cnf����,��Ϊ /tmp/mysql.sock (������Ч,���������λ�ã�����ʵ��λ���� /var/run/mysqld/mysqld.sock)

    //������ubuntu ϵͳ���⣬my.cnf ��������λ�� �ֱ��ǣ�/etc/my.cnf �� /etc/mysql/my.cnf ���ߵ����ȼ��ߣ����߿��Բ鿴�� mysqld.sock�ľ���λ��

    ԭ�ĵ�ַ�� http://www.iamle.com/archives/1265.html?utm_source=rss&;utm_medium=rss&;utm_campaign=centos%25e4%25b8%258a%25e7%2594%25a8yum%25e6%2596%25b9%25e5%25bc%258f%25e5%25ae%2589%25e8%25a3%2585mysql%25e8%25a1%258d%25e7%2594%259f%25e5%258f%2591%25e8%25a1%258c%25e7%2589%2588percona-server-3, ��лԭ���߷���  

    
    
      
����:http://www.i5good.com/20140618164.html