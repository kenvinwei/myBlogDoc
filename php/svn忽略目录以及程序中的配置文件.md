              
          
    已经在版本控制的目录或者文件是不能加入svn:ignore，加入了也无效，如果要加入，必须先删除然后commit,然后再加入svn:ignoresvnpropsetsvn:ignore&quot;*&quot;log/svnpropsetsvn:ignore&quot;*&quot;tmp/svnpropsetsvn:ignore&quot;*&quot;cache/svnpropsetsvn:ignore&quot;*&quot;sessions/svn全局忽略,修改目录下.subversion/config文件，取消global-ignroes的注释global-ignores=CVS.DS_StoreThumbs.dbWS_FTP.LOG_notes_vti_**.LCK最近遇到一个需求，就是把一些文件从svn版本库中移除而保留现有文件不变。比如数据库配置文件，每个程序员的本地配置不同，如果一更新提交上去就乱套了。用svndel会从版本库中删除但是文件也被删了,这样会造成一更新所有人的文件都被删除掉。用带参数--keep-local可以保留本地副本,注意别人的副本如果没有更新过也会被删除掉svndel--keep-localconfig.phpdelete(del,remove,rm):从版本库中删除文件和目录。用法:1、deletePATH...2、deleteURL...1、每个PATH指定的项目会被调度到下次提交时从版本库删除。除非给出--keep-local参数，工作副本中没有提交的文件和目录会被立即删除。如果PATH是未版本控制或者已修改的项目，或者包含这些项目，那么仅当给出--force参数时这些项目才会被删除。2、每个URL指定的项目会通过立即提交从版本库中删除。
    
    
      
来自:http://www.i5good.com/2012022175.html