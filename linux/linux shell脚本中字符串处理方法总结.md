              
          
    Shell�ַ�����ȡһ��Linuxshell��ȡ�ַ�������ǰ8λ���з������£�

    1.exprsubstr��$a��182.echo$a|awk��{printsubstr(,1,8)}��3.echo$a|cut-c1-84.echo$5.expr$a:��(.\).*��6.echo$a|ddbs=1count=82>/dev/null

    ������ָ�����ַ�����ȡ

    1����һ�ַ���:

    *${varible##*string}�������ҽ�ȡ���һ��string����ַ���*${varible#*string}�������ҽ�ȡ��һ��string����ַ���*${varible%%string*}���������ȡ���һ��string����ַ���*${varible%string*}���������ȡ��һ��string����ַ���

    ��*��ֻ��һ��ͨ������Բ�Ҫ

    ���ӣ�$MYVAR=foodforthought.jpg$echo${MYVAR##*fo}rthought.jpg$echo${MYVAR#*fo}odforthought.jpg

    2���ڶ��ַ�����${varible:n1:n2}:��ȡ����varible��n1��n2֮����ַ�����

    ���Ը����ض��ַ�ƫ�ƺͳ��ȣ�ʹ����һ����ʽ�ı�����չ����ѡ���ض����ַ�����������bash�����������У�$EXCLAIM=cowabunga$echo${EXCLAIM:0:3}cow$echo${EXCLAIM:3:7}abunga

    ������ʽ���ַ����ضϷǳ���㣬ֻ����ð�ŷֿ���ָ����ʼ�ַ������ַ������ȡ�

    ��������ָ��Ҫ��ָ�����ȡ��׺��ls-al|cut-d��.��-f2

    
    
      
����:http://www.i5good.com/2012040585.html