              
          
    mytop ��һ������ Linux �µ� top ������� MySQL ��ع��ߣ����Լ�ص�ǰ�������û�������ִ�е��������mytop�İ�װ����:

    wget ftp://ftp.sunet.se/pub/Linux/distributions/scientific/6.0/x86_64/os/Packages/epel-release-6-5.noarch.rpmrpm -ivh epel-release-6-5.noarch.rpmyum -y install mytop
    ��װ���֮����Ҫ����һ�»����������� vim ~/.mytop Ȼ�������������:

    user=���mysql�û�pass=���mysql����host=localhostdb=��Ҫ��ص����ݿ���delay=5port=3306socket=/tmp/mysql.sockbatchmode=0header=1color=1idle=1
    ���ˣ�������װ������ˣ����������ֱ����shell������ mytop ����ῴ�����»���.

     
    
    
      
����:http://www.i5good.com/20121023133.html