              
          
    Ŀǰ��Ū�ļ������ʱ���õ����ж��ļ��������is_file()����file_exists()�أ�is_file��file_exists����Ч�ʱȽ�������˭�������ٶȸ����أ������������԰ɣ�

    <?php$start_time = get_microtime();for($i=0;$i<10000;$i++)//Ĭ��1��Σ����ֶ��޸�{if(is_file('test.txt')) {//do nothing;}}echo 'is_file'.(get_microtime() - $start_time).'<br>';$start_time = get_microtime();for($i=0;$i<10000;$i++)//Ĭ��1��Σ����ֶ��޸�{if(file_exists('test.txt')) { //do nothing;}}echo 'file_exits'.(get_microtime() - $start_time).'<br>';function get_microtime()//ʱ��{list($usec, $sec) = explode(' ', microtime());return ((float)$usec + (float)$sec);}?>���Խ����
    ���ļ�����ʱ������1��Σ�is_file�C>0.0067121982574463file_exits�C>0.11532402038574

    ����10��Σ�is_file�C>0.069056034088135file_exits�C>1.1521670818329

    ������100��Σ�is_file�C>0.6924250125885file_exits�C>11.497637987137

    ���ļ�������ʱ��

    ����1��Σ�is_file�C>0.72184419631958file_exits�C>0.71474003791809

    ����10��Σ�is_file�C>7.1535291671753file_exits�C>7.0911409854889

    ������100��Σ�is_file�C>72.042867183685file_exits�C>71.789203166962

    ����1�����ˣ���������php��һ�мӾ䣺set_time_limit(120);//ʱ������120��
���ۣ�
    is_file()��file_exists()Ч�ʱȽϣ�������ļ�����ʱ�� is_file������file_exists�����ٶȿ�14�������ļ�������ʱ�������ٶ��൱��ͬ�����ļ�Ŀ¼����ʱ��is_dir()��file_exists()��18����������ʱ����Ч���൱��PHP��file_exists = is_dir + is_file��* ���Ҫ�ж�Ŀ¼�Ƿ���ڣ������ȿ��Ǻ��� is_dir(directory)* ���Ҫ�ж��ļ��Ƿ���ڣ������ȿ��Ǻ��� is_file(filepath)
is_dir()�Ա�file_exists()���Խ����
    ��Ŀ¼����ʱ������1���is_dir�C>0.0058560371398926file_exits�C>0.11063098907471��Ŀ¼������ʱ������1���is_dir�C>0.7159481048584file_exits�C>0.71305584907532
    
    
      
����:http://www.i5good.com/20120817118.html