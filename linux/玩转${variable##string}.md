              
          
    ${varible##*string}���������ҽ�ȡ���һ��string����ַ���

    ���磺

    [wei@localhost Book]$ str=1314[wei@localhost Book]$ echo ${str##*1}4
    ${varible#*string}���������ҽ�ȡ��һ��string����ַ���

    ���磺

    [wei@localhost Book]$ str=1314[wei@localhost Book]$ echo ${str#*1}314
    ${varible%%string*}�����������ȡ���һ��string����ַ���

    [wei@localhost Book]$ str=1314[wei@localhost Book]$ echo ${str%%3*}1
    ${varible%string*}�����������ȡ��һ��string����ַ���

    [wei@localhost Book]$ str=1314[wei@localhost Book]$ echo ${str%1*}13
                
    
    
      
����:http://www.i5good.com/2012032079.html