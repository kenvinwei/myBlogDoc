              
          
    ('|")����ƥ�Ե����Ż���˫����(.*?)ƥ�������ַ�/1ƥ�Ե�һ��('|")�гɹ�ƥ�Ե�����/1�Ǳ�֤ǰ������һ��
    �ٷ�����:

    <?php//2��һ���������õ�ʾ��. ������pcre������ƥ��������ʽ�еڶ���Բ����(������([w]+))//ƥ�䵽�Ľ��. ����ʹ��������б������Ϊ����ʹ����˫����.$html = "<b>bold text</b><a href=howdy.html>click me</a>";   preg_match_all("/(<([w]+)[^>]*>)(.*?)(</2>)/", $html, $matches, PREG_SET_ORDER);   foreach ($matches as $val) {    echo "matched: " . $val[0] . "n";    echo "part 1: " . $val[1] . "n";    echo "part 2: " . $val[2] . "n";    echo "part 3: " . $val[3] . "n";    echo "part 4: " . $val[4] . "nn";}?


    �ٷ���ַ��http://www.php.net/manual/zh/function.preg-match-all.php
    
    
      
����:http://www.i5good.com/20140417162.html