              
          
BLOB字段

BLOB(binarylargeobject),用来存储二进制大对象的字段类型。

BLOB往往是一个大文件，典型的BLOB是一张图片、一个声音或一个视频文件，由于它们的尺寸，必须使用特殊的方式来处理（例如：上传、下载或者存放到一个数据库）。

处理BLOB的思想就是让文件处理器（如数据库管理器）不会理会文件是什么，而是关心如何去处理它。但也有专家强调，这种处理大数据对象的方法是把双刃剑，它有可能引发一些问题，如存储的二进制文件过大，会使数据库的性能下降。

BLOB和CLOB的区别

BLOB就是使用二进制保存文件，如：保存位图。

CLOB使用CHAR来保存数据。如：保存XML文档。

MySQL中的BLOB类型系列

MySQL中，BLOB是个类型系列，共包括四种BLOB类型：TinyBlob、Blob、MediumBlob、LongBlob，这几个类型之间的唯一区别是在存储文件的最大尺寸不同



    字段类型

    最大长度（字节）

    字节范围

    存储需求


    TinyBlob

    255

    0到28－1

    值的长度加上用于记录长度的1个字节


    Blob

    65K

    0到216－1

    值的长度加上用于记录长度的2个字节


    MediumBlob

    16M

    0到224－1

    值的长度加上用于记录长度的3个字节


    LongBlob

    4G

    0到232－1

    值的长度加上用于记录长度的4个字节


MySQL中的BLOB类型特点

允许的属性：除通用属性外无其他属性

缺省值：如果列可为NULL，则为NULL；如果列为NOTNULL，则为&quot;&quot;

比较：区分大小写

MySQL中的BLOB类型大小限制

MySQL中对LongBlob类型字段的最大存储容量默认限定为1M，即如果你要存储大于1M的二进制大对象，需要修改MySQL数据库的大小，使其能支持更大的二进制容量。可在my.cnf文件中增加设置如下：

[mysqld]

set-variable=max_allowed_packet=16M
    
    
      
来自:http://www.i5good.com/2012040989.html