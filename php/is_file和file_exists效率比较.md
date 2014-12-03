              
          
    目前在弄文件缓存的时候用到了判定文件存在与否，is_file()还是file_exists()呢？is_file和file_exists两者效率比较起来，谁的运行速度更快呢？还是做个测试吧：

    <?php$start_time = get_microtime();for($i=0;$i<10000;$i++)//默认1万次，可手动修改{if(is_file('test.txt')) {//do nothing;}}echo 'is_file'.(get_microtime() - $start_time).'<br>';$start_time = get_microtime();for($i=0;$i<10000;$i++)//默认1万次，可手动修改{if(file_exists('test.txt')) { //do nothing;}}echo 'file_exits'.(get_microtime() - $start_time).'<br>';function get_microtime()//时间{list($usec, $sec) = explode(' ', microtime());return ((float)$usec + (float)$sec);}?>测试结果：
    当文件存在时：运行1万次：is_file–>0.0067121982574463file_exits–>0.11532402038574

    运行10万次：is_file–>0.069056034088135file_exits–>1.1521670818329

    当运行100万次：is_file–>0.6924250125885file_exits–>11.497637987137

    当文件不存在时：

    运行1万次：is_file–>0.72184419631958file_exits–>0.71474003791809

    运行10万次：is_file–>7.1535291671753file_exits–>7.0911409854889

    当运行100万次：is_file–>72.042867183685file_exits–>71.789203166962

    超过1分钟了，别忘了在php第一行加句：set_time_limit(120);//时间限制120秒
结论：
    is_file()和file_exists()效率比较，结果当文件存在时， is_file函数比file_exists函数速度快14倍，当文件不存在时，两者速度相当。同理，当文件目录存在时，is_dir()比file_exists()快18倍。不存在时两者效率相当。PHP的file_exists = is_dir + is_file。* 如果要判断目录是否存在，请优先考虑函数 is_dir(directory)* 如果要判断文件是否存在，请优先考虑函数 is_file(filepath)
is_dir()对比file_exists()测试结果：
    当目录存在时，运行1万次is_dir–>0.0058560371398926file_exits–>0.11063098907471当目录不存在时，运行1万次is_dir–>0.7159481048584file_exits–>0.71305584907532
    
    
      
来自:http://www.i5good.com/20120817118.html