              
          
    由于PHP的工作机制，它并没有一个daemon线程，来定时地扫描session信息并判断其是否失效。当一个有效请求发生时，PHP会根据全局变量 session.gc_probability/session.gc_divisor（同样可以通过php.ini或者ini_set()函数来修改） 的值，来决定是否启动一个GC（Garbage Collector）。默认情况下，session.gc_probability ＝ 1，session.gc_divisor ＝100，也就是说有1%的可能性会启动GC。

    GC的工作，就是扫描所有的session信息， 用当前时间减去session的最后修改时间（modified date），同session.gc_maxlifetime参数进行比较，如果生存时间已经超过gc_maxlifetime，就把该session删 除。

    那为什么会发生gc_maxlifetime无效的情况呢？

    在默认情况下，session信息会以文本文件的形式，被保存在系统 的临时文件目录中。在Linux下，这一路径通常为tmp，在Windows下通常为C:WindowsTemp。当服务器上有多个PHP应用时， 它们会把自己的session文件都保存在同一个目录中。同样地，这些PHP应用也会按一定机率启动GC，扫描所有的session文件。

    问 题在于，GC在工作时，并不会区分不同站点的session。举例言之，站点A的gc_maxlifetime设置为2小时，站点B的 gc_maxlifetime设置为默认的24分钟。当站点B的GC启动时，它会扫描公用的临时文件目录，把所有超过24分钟的session文件全部删 除掉，而不管它们来自于站点A或B。这样，站点A的gc_maxlifetime设置就形同虚设了。

    找到问题所在，解决起来就很简单了。修改session.save_path参数，或者使用session_save_path()函数，把保存session的目录指向一个专用的目录，gc_maxlifetime参数工作正常了。
还有一个问题就是，gc_maxlifetime只能保证session生存的最短时间，并不能够保存在超过这一时间之后session信息立即会得到 删除。因为GC是按机率启动的，可能在某一个长时间内都没有被启动，那么大量的session在超过gc_maxlifetime以后仍然会有效。解决这 个问题的一个方法是，把session.gc_probability/session.gc_divisor的机率提高，如果提到100%，就会彻底解 决这个问题，但显然会对性能造成严重的影响。另一个方法是自己在代码中判断当前session的生存时间，如果超出了gc_maxlifetime，就清 空当前session。    
    
      
来自:http://www.i5good.com/20140414160.html