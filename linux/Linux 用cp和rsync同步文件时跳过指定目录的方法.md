              
          
    需求是：某测试站点，在某个节点的时候需要同步到正式站点去，但是里面的config目录不能覆盖

    方法一：终端命令行下执行以下命令 cp -R `find /projectA -type d -path /projectA/common/config  -prune -o -print | sed 1d ` /projectB/ 方法二： localhost # find projectB/ommon/config | xargs touch 修改目标目录的congfig目录文件的access time到当前，这样cp的时候加update参数可以避开该目录 localhost # cp -r -u -v projectA/* projectB/ 这样不会复不复制projectA下面第一级的隐藏目录，但是二级三级的还是会复制过去 所以适用于没有隐藏目录的情况下，比较方便. 但是我们的项目因为牵涉SVN什么的，所以会有很多隐藏目录包含版本控制信息，就会很乱，所以有了第二种方案 方法三： rsync -vauP --exclude=&quot;.*“ --exclude=”common/config“ projectA/ projectB 简单注释下 -a 参数，相当于-rlptgoD，-r 是递归 -l 是链接文件，意思是拷贝链接文件；-p 表示保持文件原有权限；-t 保持文件原有时间；-g 保持文件原有用户组；-o 保持文件原有属主；-D 相当于块设备文件； -P 传输进度； -v 冗余模式，查看到文件列表等 -u update模式，如果目标文件新于源文件，则跳过 第一个exclude表示跳过所有.开头的隐藏文件 第二个表示调过projectA/common/config目录，因为config目录下的文件，轻易不需改变，如果需要手动调整即可，注意这个参数是后面SRC参数的相对路径
    
    
      
来自:http://www.i5good.com/20121205149.html