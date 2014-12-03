              
          
    最近开发中遇到一个奇怪的问题，我的一个网站头部，代码固定不变，放在了不同的模板进行展示，一部分出现了问题，总是距离相差8个像素，用firebug查看发现：meta 跑到 body 下面去了，并且发现了一段奇怪的样式:

    

    user agent stylesheetbody {    display: block;    margin: 8px;}
    百度一下就知道相关的原因了，我的文件是utf-8, 用EditPlus　保存时正确选择编码为“UTF-8”而不是“UTF-8+DOM”,这样就不会出现，空文本节点问题。
    
    
      
来自:http://www.i5good.com/20121019131.html