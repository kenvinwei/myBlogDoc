              
          
    

     

    如今主流浏览器都在比拼JavaScript引擎的执行速度，但最终都会达到一个理论极限，即无限接近编译后程序执行速度。 这种情况下决定程序速度的另一个重要因素就是代码本身。

    在这里我们会分门别类的介绍JavaScript性能优化的技巧，并提供相应的测试用例，供大家在自己使用的浏览器上验证， 同时会对特定的JavaScript背景知识做一定的介绍。
变量声明带上var
    如果声明变量忘记了var，那么js引擎将会遍历整个作用域查找这个变量，结果不管找到与否，都是悲剧。

    如果在上级作用域找到了这个变量，上级作用域变量的内容将被无声的改写，导致莫名奇妙的错误发生。如果在上级作用域没有找到该变量，这个变量将自动被声明为全局变量，然而却都找不到这个全局变量的定义。

    基于上面逻辑，性能方面不带var声明变量自然要比带var速度慢
慎用全局变量
    全局变量需要搜索更长的作用域链。

    全局变量的生命周期比局部变量长，不利于内存释放。

    过多的全局变量容易造成混淆，增大产生bug的可能性。
缓存重复使用的全局变量
    全局变量要比局部变量需要搜索的作用域长

    重复调用的方法也可以通过局部缓存来提速

    该项优化在IE上体现比较明显

    JQuery源代码中也是用了类似的方法:

    var docElem = window.document.documentElement, selector_hasDuplicate,matches = docElem.webkitMatchesSelector || docElem.mozMatchesSelector || docElem.oMatchesSelector || docElem.msMatchesSelector,selector_sortOrder = function( a, b ) {// Flag for duplicate removalif ( a === b ) {selector_hasDuplicate = true;return 0;}避免使用with
    with语句将一个新的可变对象推入作用域链的头部，函数的所有局部变量现在处于第二个作用域链对象中，从而使局部变 量的访问代价提高。
通过原型优化方法定义
    如果一个方法类型将被频繁构造，通过方法原型从外面定义附加方法，从而避免方法的重复定义。 

    可以通过外 部原型的构造方式初始化值类型的变量定义。（这里强调值类型的原因是，引用类型如果在原型中定义， 一个实例对引用类型的更改会影响到其他实例。）

    这条规则中涉及到JavaScript中原型的概念:

    构造函数都有一个prototype属性，指向另一个对象。这个对象的所有属性和方法，都会被构造函数的实例继承。我们可 以把那些不变的属性和方法，直接定义在prototype对象上。可以通过对象实例访问保存在原型中的值，不能通过对象实例重写原型中的值。在实例中添加一个与实例原型同名属性，那该属性就会屏蔽原型中的属性。通过delete操作符可以删除实例中的属性。

    例如以下代码以及相应的内存中原型表示如下:

    function Person(){}Person.prototype.name = "Nicholas";Person.prototype.age = 29;Person.prototype.job = "Software Engineer";Person.prototype.sayName = function(){alert(this.name);};var person1 = new Person();person1.sayName(); //”Nicholas”var person2 = new Person();person2.sayName(); //”Nicholas”避开闭包陷阱
    闭包是个强大的工具，但同时也是性能问题的主要诱因之一。不合理的使用闭包会导致内存泄漏。

    闭包的性能不如使用内部方法，更不如重用外部方法。

    由于IE浏览器的DOM是用COM来实现的， COM的内存管理是通过引用计数的方式，引用计数有个难题就是循环引用，一旦DOM 引用了闭包(例如event handler)，闭包的上层元素又引用了这个DOM，就会造成循环引用从而导致内存泄漏。

    关于Js内存泄漏可以参考 http://www.crockford.com/javascript/memory/leak.html http://msdn.microsoft.com/en-us/library/bb250448%28v=vs.85%29.aspx
避免使用属性访问方法
    JavaScript不需要属性访问方法，因为所有的属性都是外部可见的。 

    添加属性访问方法只是增加了一层重定向 ，对于访问控制没有意义。

    使用属性访问方法示例

    function Car() {       this.m_tireSize = 17;       this.m_maxSpeed = 250;  this.GetTireSize = Car_get_tireSize;       this.SetTireSize = Car_put_tireSize;} function Car_get_tireSize() {       return this.m_tireSize;} function Car_put_tireSize(value) {       this.m_tireSize = value;}var ooCar = new Car();var iTireSize = ooCar.GetTireSize();ooCar.SetTireSize(iTireSize + 1);
    直接访问属性示例

    function Car() {       this.m_tireSize = 17;       this.m_maxSpeed = 250;}var perfCar = new Car();var iTireSize = perfCar.m_tireSize;perfCar.m_tireSize = iTireSize + 1;避免在循环中使用try-catch
    try-catch-finally语句在catch语句被执行的过程中会动态构造变量插入到当前域中，对性能有一定影响。 

    如 果需要异常处理机制，可以将其放在循环外层使用。
使用for代替for…in…遍历数组
    for…in…内部实现是构造一个所有元素的列表，包括array继承的属性，然后再开始循环。相对for循环性能要慢。
使用原始操作代替方法调用
    方法调用一般封装了原始操作，在性能要求高的逻辑中，可以使用原始操作代替方法调用来提高性能。

    原始操作:

    var min = a < b ? a : b;
    方法实例

    var min = Math.min(a, b);传递方法取代方法字符串
    一些方法例如setTimeout()/setInterval()，接受字符串或者方法实例作为参数。直接传递方法对象作为参数来避免对字符串的二次解析。

    传递方法:

    setTimeout(test, 1);
    传递方法字符串:

    setTimeout('test()', 1);使用工具精简脚本
    精简代码就是将代码中的空格和注释去除，也有更进一步的会对变量名称混淆+精简。根据统计精简后文件大小平均减少21%，即使Gzip之后文件也会减少5%。

    常用的工具如下:JSMin,Closure compiler,YUICompressor
启用Gzip压缩
    Gzip通常可以减少70%网页内容的大小，包括脚本、样式表、图片等文件。Gzip比deflate更高效，主流服务器都有相应的 压缩支持模块。

    Gzip的工作流程为：

    客户端在请求Accept-Encoding中声明可以支持gzip服务器将请求文档压缩，并在Content-Encoding中声明该回复为gzip格式客户端收到之后按照gzip解压缩
异步加载脚本
    脚本加载与解析会阻塞HTML渲染，可以通过异步加载方式来避免渲染阻塞。异步加载的方式很多，比较通用的方法是通过类似下面的代码实现

    var loadjs = function(script_filename){    var script = document.createElement('script');    script.setAttribute('type', 'text/javascript');    script.setAttribute('src', script_filename);    script.setAttribute('id', 'script-id');    scriptElement = document.getElementById('script-id');    if(scriptElement){        document.getElementsByTagName('head')[0].removeChild(scriptElement);    }    document.getElementsByTagName('head')[0].appendChild(script);}var script = 'scripts/alert.js';loadjs(script);DOM操作优化
    DOM操作性能问题主要有以下原因:

    DOM元素过多导致元素定位缓慢大量的DOM接口调用DOM操作触发频繁的reflow(layout)和repaint

    关于reflow(layout)和repaint可以参考下图，可以看到layout发生在repaint之前，所以layout相对来说会造成更多性能 损耗。

    reflow(layout)就是计算页面元素的几何信息repaint就是绘制页面元素
DOM操作性能问题主要有以下原因，
    DOM元素过多导致元素定位缓慢大量的DOM接口调用DOM操作触发频繁的reflow(layout)和repaint关于reflow(layout)和repaint可以参考下图，可以看到layout发生在repaint之前，所以layout相对来说会造成更多性能 损耗。

    reflow(layout)就是计算页面元素的几何信息repaint就是绘制页面元素
减少DOM元素数量
    在console中执行命令查看DOM元素数量

    Yahoo首页DOM元素数量在1200左右。正常页面大小一般不应该超过 1000。 

    DOM元素过多会使DOM元素查询效率，样式表匹配效率降低，是页面性能最主要的瓶颈之一。
优化CSS样式转换
    如果需要动态更改CSS样式，尽量采用触发reflow次数较少的方式。例如以下代码逐条更改元素的几何属性，理论上会触发多次reflow.
    
    
      
来自:http://www.i5good.com/20140410159.html