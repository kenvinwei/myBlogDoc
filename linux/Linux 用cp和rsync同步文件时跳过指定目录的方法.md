              
          
    �����ǣ�ĳ����վ�㣬��ĳ���ڵ��ʱ����Ҫͬ������ʽվ��ȥ�����������configĿ¼���ܸ���

    ����һ���ն���������ִ���������� cp -R `find /projectA -type d -path /projectA/common/config  -prune -o -print | sed 1d ` /projectB/ �������� localhost # find projectB/ommon/config | xargs touch �޸�Ŀ��Ŀ¼��congfigĿ¼�ļ���access time����ǰ������cp��ʱ���update�������Աܿ���Ŀ¼ localhost # cp -r -u -v projectA/* projectB/ �������Ḵ������projectA�����һ��������Ŀ¼�����Ƕ��������Ļ��ǻḴ�ƹ�ȥ ����������û������Ŀ¼������£��ȽϷ���. �������ǵ���Ŀ��Ϊǣ��SVNʲô�ģ����Ի��кܶ�����Ŀ¼�����汾������Ϣ���ͻ���ң��������˵ڶ��ַ��� �������� rsync -vauP --exclude=&quot;.*�� --exclude=��common/config�� projectA/ projectB ��ע���� -a �������൱��-rlptgoD��-r �ǵݹ� -l �������ļ�����˼�ǿ��������ļ���-p ��ʾ�����ļ�ԭ��Ȩ�ޣ�-t �����ļ�ԭ��ʱ�䣻-g �����ļ�ԭ���û��飻-o �����ļ�ԭ��������-D �൱�ڿ��豸�ļ��� -P ������ȣ� -v ����ģʽ���鿴���ļ��б�� -u updateģʽ�����Ŀ���ļ�����Դ�ļ��������� ��һ��exclude��ʾ��������.��ͷ�������ļ� �ڶ�����ʾ����projectA/common/configĿ¼����ΪconfigĿ¼�µ��ļ������ײ���ı䣬�����Ҫ�ֶ��������ɣ�ע����������Ǻ���SRC���������·��
    
    
      
����:http://www.i5good.com/20121205149.html