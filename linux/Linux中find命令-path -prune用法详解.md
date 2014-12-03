              
          
    
    在Windows中可以在某些路径中查找文件，也可以设定不在某些路径中查找文件，下面用Linux中的find的命令结合其-path -prune参数来看看在Linux中怎么实现此功能。

    假如在当前目录下查找文件，且当前目录下有很多文件及目录（多层目录），包括dir0、dir1和dir2 ...等目录及dir00、dir01...dir10、dir11...等子目录。

    1. 在当前目录下查找所有txt后缀文件

      find ./ -name *.txt

    2.在当前目录下的dir0目录及子目录下查找txt后缀文件

      find ./ -path &#39;./dir0*&#39; -name *.txt

    3.在当前目录下的dir0目录下的子目录dir00及其子目录下查找txt后缀文件

      find ./ -path &#39;*dir00*&#39; -name *.txt

    4.在除dir0及子目录以外的目录下查找txt后缀文件

      find ./ -path &#39;./dir0*&#39; -a -prune -o -name *.txt -print

    说明：-a 应该是and的缩写，意思是逻辑运算符‘或’(&;&;); -o应该是or的缩写,意思是逻辑运算符‘与’(||), -not 表示非.

    命令行的意思是：如果目录dir0存在（即-a左边为真），则求-prune的值，-prune 返回真，‘与’逻辑表达式为真（即-path &#39;./dir0*&#39; -a -prune 为真），find命令将在除这个目录以外的目录下查找txt后缀文件并打印出来；如果目录dir0不存在（即-a左边为假），则不求值-prune ，‘与’逻辑表达式为假，则在当前目录下查找所有txt后缀文件。

    5.在除dir0、dir1及子目录以外的目录下查找txt后缀文件

      find ./ ( -path &#39;./dir0*&#39; -o -path &#39;./dir1*&#39; ) -a -prune -o -name *.txt -print

    注意：圆括号()表示表达式的结合。即指示 shell 不对后面的字符作特殊解释，而留给 find 命令去解释其意义。由于命令行不能直接使用圆括号，所以需要用反斜杠&#39;&#39;进行转意(即&#39;&#39;转意字符使命令行认识圆括号)。同时注意&#39;(&#39;，&#39;)&#39;两边都需空格。

    6.在dir0、dir1及子目录下查找txt后缀文件

      find ./ ( -path &#39;./dir0*&#39; -o -path &#39;./dir1*&#39; ) -a -name *.txt -print

    +1. 在所有以名为dir_general的目录下查找txt后缀文件

    find ./ -path &#39;*/dir_general/*&#39; -name *.txt -prin

    
    
      
来自:http://www.i5good.com/20121205148.html