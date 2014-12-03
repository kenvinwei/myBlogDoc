              
          
    今天突然发现grep-q用于if逻辑判断很好用。-q参数，本意是Quiet;donotwriteanythingtostandardoutput.Exitimmediatelywithzerostatusifanymatchisfound,evenifanerrorwasdetected.中文意思为，安静模式，不打印任何标准输出。如果有匹配的内容则立即返回状态值0。例如：

    # cat a.txtnihaonihaooohello #  if  grep -q hello a.txt ; then echo yes;else echo no; fiyes# if grep -q word a.txt; then echo yes; else echo no; fino    
    
      
来自:http://www.i5good.com/20120518100.html