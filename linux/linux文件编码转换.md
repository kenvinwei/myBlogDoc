              
          
    iconv 命令用途：将字符编码从一个代码页编码方案转换到另一个。语法：iconv -f FromCode -t ToCode [ FileName…描述：iconv 命令把从标准输入或指定文件读取的字符的编码从一个编码字符集转换到另一个，然后将结果写入标准输出。可以通过 FromCode 和 ToCode 参数识别输入和输出的编码字符集。输入数据应该包含由 FromCode 参数指定的代码集中的字符。如果在命令行中没有指定 FileName 参数，iconv 命令从标准输入读取。可以使用 基于 Web 的系统管理器 系统应用程序（wsm system 快速路径）运行该命令。也可以使用系统管理接口工具（SMIT）smit iconv 快速路径运行该命令。标志-f FromCode 指定输入数据已编码的代码集。在 -f 标记和 FromCode 参数之间的空格是可选的。-t ToCode 指定输出数据要转换的代码集。在 -t 标记和 ToCode 参数之间的空格是可选的。FileName 指定要转换的文件。受支持代码集转换器的列表在 AIX 5L Version 5.2 General Programming Concepts: Writing and Debugging Programs 中的“转换器列表”中提供。退出状态命令返回下列退出值：0 输入数据成功转换。1 不支持指定转换；不能打开给定的输入文件供读取；或用法语法错误。2 输入流中的遇到不可用字符。示例1. 要从 IBM-850 代码集转换 mail.x400 文件的内容并在 mail.local 文件中存储结果，请输入：iconv -f IBM-850 -t ISO8859-1 mail.x400 > mail.local2. 要将 mail.japan 文件内容从 7 位交换（ISO2022）编码转换到日语 EUC 编码集（IBM-eucJP），请输入：iconv -f fold7 -t IBM-eucJP mail.japan > mail.local3. 要转换本地文件内容到 mail-interchange 格式且发送邮件，请输入：iconv -f IBM-943 -t fold7 mail.local | mail fxrojas
    
    
      
来自:http://www.i5good.com/20120906120.html