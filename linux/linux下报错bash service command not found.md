              
          
    ��linux�²�����ʱ�򾭳���������bash: service: command not found���������ǰ���������ˣ�����Ū�ˣ�Ҳûϸ��ԭ�򣬽���������������⣬��˳���о�һ�¡� 1��ͨ����������ǳ����� ͨ��su root���������в�����ʱ�� su����su root ֻ���൱����root�û������������ʵ�ʵ�ϵͳ������û���л���root�û��Ļ�������ֻ�ǵ�ǰ��¼�û��� su -,-l,--login�����Ѿ���ȫ���л���root�����£��൱����ȫ��root�û���¼�� ����Ϳ���su���su --help ����su����İ�����Ϣ�� 

    �÷���su [ѡ��]... [-] [�û� [����]...]  Change the effective user id and group id to that of USER.       -, -l, --login               make the shell a login shell    -c, --command=COMMAND       pass a single COMMAND to the shell with -c    --session-command=COMMAND    pass a single COMMAND to the shell with -c                                 and do not create a new session    -f, --fast                   pass -f to the shell (for csh or tcsh)    -m, --preserve-environment   do not reset environment variables    -p                           same as -m    -s, --shell=SHELL            run SHELL if /etc/shells allows it        --help     ��ʾ�˰�����Ϣ���˳�        --version  ����汾��Ϣ���˳�     ������ - ���� -l�����δ����[�û�]����ٶ�Ϊ root��
    2��service����Ŀ¼��/sbin/�� �ʽ�������������ַ�ʽ�� a��ֱ��ʹ��su - root���л���root�û���Ȼ��ʹ�� service b��ʹ��su root�л���root�û�����ͬʱʹ��/sbin/service����������/sbin/service mysql restart.
    
    
      
����:http://www.i5good.com/20130115155.html