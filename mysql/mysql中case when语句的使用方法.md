              
          mysql��case when����ʹ�÷�����ѧϰmysql���ݿⲻ�ɲ�ѧ�ģ����ľ��о�������mysql��case when���ʹ�÷�������������ο���
    1.

    selectname, case whenbirthday<'1981'then'old' whenbirthday>'1988'then'yong' else'ok'ENDYORN fromlee;
    2.

    selectNAME, casename when'sam'then'yong' when'lee'then'handsome' else'good'end fromlee;
    ��Ȼ��case when��仹���Ը���

    3.

    selectname,birthday, case whenbirthday>'1983'then'yong' whenname='lee'then'handsome' else'justsoso'end fromlee; 
    ���Ͼ���mysql��case when����ʹ��ʾ���Ľ��ܡ�
      
    
      
����:http://www.i5good.com/2012011249.html