              
          
    

     

    ���������������ڱ�ƴJavaScript�����ִ���ٶȣ������ն���ﵽһ�����ۼ��ޣ������޽ӽ���������ִ���ٶȡ� ��������¾��������ٶȵ���һ����Ҫ���ؾ��Ǵ��뱾��

    ���������ǻ���ű���Ľ���JavaScript�����Ż��ļ��ɣ����ṩ��Ӧ�Ĳ�����������������Լ�ʹ�õ����������֤�� ͬʱ����ض���JavaScript����֪ʶ��һ���Ľ��ܡ�
������������var
    �����������������var����ôjs���潫�����������������������������������ҵ���񣬶��Ǳ��硣

    ������ϼ��������ҵ�������������ϼ���������������ݽ��������ĸ�д������Ī������Ĵ�������������ϼ�������û���ҵ��ñ���������������Զ�������Ϊȫ�ֱ�����Ȼ��ȴ���Ҳ������ȫ�ֱ����Ķ��塣

    ���������߼������ܷ��治��var����������ȻҪ�ȴ�var�ٶ���
����ȫ�ֱ���
    ȫ�ֱ�����Ҫ��������������������

    ȫ�ֱ������������ڱȾֲ����������������ڴ��ͷš�

    �����ȫ�ֱ���������ɻ������������bug�Ŀ����ԡ�
�����ظ�ʹ�õ�ȫ�ֱ���
    ȫ�ֱ���Ҫ�Ⱦֲ�������Ҫ������������

    �ظ����õķ���Ҳ����ͨ���ֲ�����������

    �����Ż���IE�����ֱȽ�����

    JQueryԴ������Ҳ���������Ƶķ���:

    var docElem = window.document.documentElement, selector_hasDuplicate,matches = docElem.webkitMatchesSelector || docElem.mozMatchesSelector || docElem.oMatchesSelector || docElem.msMatchesSelector,selector_sortOrder = function( a, b ) {// Flag for duplicate removalif ( a === b ) {selector_hasDuplicate = true;return 0;}����ʹ��with
    with��佫һ���µĿɱ������������������ͷ�������������оֲ��������ڴ��ڵڶ����������������У��Ӷ�ʹ�ֲ��� ���ķ��ʴ�����ߡ�
ͨ��ԭ���Ż���������
    ���һ���������ͽ���Ƶ�����죬ͨ������ԭ�ʹ����涨�帽�ӷ������Ӷ����ⷽ�����ظ����塣 

    ����ͨ���� ��ԭ�͵Ĺ��췽ʽ��ʼ��ֵ���͵ı������塣������ǿ��ֵ���͵�ԭ���ǣ��������������ԭ���ж��壬 һ��ʵ�����������͵ĸ��Ļ�Ӱ�쵽����ʵ������

    �����������漰��JavaScript��ԭ�͵ĸ���:

    ���캯������һ��prototype���ԣ�ָ����һ���������������������Ժͷ��������ᱻ���캯����ʵ���̳С����ǿ� �԰���Щ��������Ժͷ�����ֱ�Ӷ�����prototype�����ϡ�����ͨ������ʵ�����ʱ�����ԭ���е�ֵ������ͨ������ʵ����дԭ���е�ֵ����ʵ�������һ����ʵ��ԭ��ͬ�����ԣ��Ǹ����Ծͻ�����ԭ���е����ԡ�ͨ��delete����������ɾ��ʵ���е����ԡ�

    �������´����Լ���Ӧ���ڴ���ԭ�ͱ�ʾ����:

    function Person(){}Person.prototype.name = "Nicholas";Person.prototype.age = 29;Person.prototype.job = "Software Engineer";Person.prototype.sayName = function(){alert(this.name);};var person1 = new Person();person1.sayName(); //��Nicholas��var person2 = new Person();person2.sayName(); //��Nicholas���ܿ��հ�����
    �հ��Ǹ�ǿ��Ĺ��ߣ���ͬʱҲ�������������Ҫ����֮һ���������ʹ�ñհ��ᵼ���ڴ�й©��

    �հ������ܲ���ʹ���ڲ������������������ⲿ������

    ����IE�������DOM����COM��ʵ�ֵģ� COM���ڴ������ͨ�����ü����ķ�ʽ�����ü����и��������ѭ�����ã�һ��DOM �����˱հ�(����event handler)���հ����ϲ�Ԫ�������������DOM���ͻ����ѭ�����ôӶ������ڴ�й©��

    ����Js�ڴ�й©���Բο� http://www.crockford.com/javascript/memory/leak.html http://msdn.microsoft.com/en-us/library/bb250448%28v=vs.85%29.aspx
����ʹ�����Է��ʷ���
    JavaScript����Ҫ���Է��ʷ�������Ϊ���е����Զ����ⲿ�ɼ��ġ� 

    ������Է��ʷ���ֻ��������һ���ض��� �����ڷ��ʿ���û�����塣

    ʹ�����Է��ʷ���ʾ��

    function Car() {       this.m_tireSize = 17;       this.m_maxSpeed = 250;  this.GetTireSize = Car_get_tireSize;       this.SetTireSize = Car_put_tireSize;} function Car_get_tireSize() {       return this.m_tireSize;} function Car_put_tireSize(value) {       this.m_tireSize = value;}var ooCar = new Car();var iTireSize = ooCar.GetTireSize();ooCar.SetTireSize(iTireSize + 1);
    ֱ�ӷ�������ʾ��

    function Car() {       this.m_tireSize = 17;       this.m_maxSpeed = 250;}var perfCar = new Car();var iTireSize = perfCar.m_tireSize;perfCar.m_tireSize = iTireSize + 1;������ѭ����ʹ��try-catch
    try-catch-finally�����catch��䱻ִ�еĹ����лᶯ̬����������뵽��ǰ���У���������һ��Ӱ�졣 

    �� ����Ҫ�쳣������ƣ����Խ������ѭ�����ʹ�á�
ʹ��for����for��in����������
    for��in���ڲ�ʵ���ǹ���һ������Ԫ�ص��б�����array�̳е����ԣ�Ȼ���ٿ�ʼѭ�������forѭ������Ҫ����
ʹ��ԭʼ�������淽������
    ��������һ���װ��ԭʼ������������Ҫ��ߵ��߼��У�����ʹ��ԭʼ�������淽��������������ܡ�

    ԭʼ����:

    var min = a < b ? a : b;
    ����ʵ��

    var min = Math.min(a, b);���ݷ���ȡ�������ַ���
    һЩ��������setTimeout()/setInterval()�������ַ������߷���ʵ����Ϊ������ֱ�Ӵ��ݷ���������Ϊ������������ַ����Ķ��ν�����

    ���ݷ���:

    setTimeout(test, 1);
    ���ݷ����ַ���:

    setTimeout('test()', 1);ʹ�ù��߾���ű�
    ���������ǽ������еĿո��ע��ȥ����Ҳ�и���һ���Ļ�Ա������ƻ���+���򡣸���ͳ�ƾ�����ļ���Сƽ������21%����ʹGzip֮���ļ�Ҳ�����5%��

    ���õĹ�������:JSMin,Closure compiler,YUICompressor
����Gzipѹ��
    Gzipͨ�����Լ���70%��ҳ���ݵĴ�С�������ű�����ʽ��ͼƬ���ļ���Gzip��deflate����Ч������������������Ӧ�� ѹ��֧��ģ�顣

    Gzip�Ĺ�������Ϊ��

    �ͻ���������Accept-Encoding����������֧��gzip�������������ĵ�ѹ��������Content-Encoding�������ûظ�Ϊgzip��ʽ�ͻ����յ�֮����gzip��ѹ��
�첽���ؽű�
    �ű����������������HTML��Ⱦ������ͨ���첽���ط�ʽ��������Ⱦ�������첽���صķ�ʽ�ܶ࣬�Ƚ�ͨ�õķ�����ͨ����������Ĵ���ʵ��

    var loadjs = function(script_filename){    var script = document.createElement('script');    script.setAttribute('type', 'text/javascript');    script.setAttribute('src', script_filename);    script.setAttribute('id', 'script-id');    scriptElement = document.getElementById('script-id');    if(scriptElement){        document.getElementsByTagName('head')[0].removeChild(scriptElement);    }    document.getElementsByTagName('head')[0].appendChild(script);}var script = 'scripts/alert.js';loadjs(script);DOM�����Ż�
    DOM��������������Ҫ������ԭ��:

    DOMԪ�ع��ർ��Ԫ�ض�λ����������DOM�ӿڵ���DOM��������Ƶ����reflow(layout)��repaint

    ����reflow(layout)��repaint���Բο���ͼ�����Կ���layout������repaint֮ǰ������layout�����˵����ɸ������� ��ġ�

    reflow(layout)���Ǽ���ҳ��Ԫ�صļ�����Ϣrepaint���ǻ���ҳ��Ԫ��
DOM��������������Ҫ������ԭ��
    DOMԪ�ع��ർ��Ԫ�ض�λ����������DOM�ӿڵ���DOM��������Ƶ����reflow(layout)��repaint����reflow(layout)��repaint���Բο���ͼ�����Կ���layout������repaint֮ǰ������layout�����˵����ɸ������� ��ġ�

    reflow(layout)���Ǽ���ҳ��Ԫ�صļ�����Ϣrepaint���ǻ���ҳ��Ԫ��
����DOMԪ������
    ��console��ִ������鿴DOMԪ������

    Yahoo��ҳDOMԪ��������1200���ҡ�����ҳ���Сһ�㲻Ӧ�ó��� 1000�� 

    DOMԪ�ع����ʹDOMԪ�ز�ѯЧ�ʣ���ʽ��ƥ��Ч�ʽ��ͣ���ҳ����������Ҫ��ƿ��֮һ��
�Ż�CSS��ʽת��
    �����Ҫ��̬����CSS��ʽ���������ô���reflow�������ٵķ�ʽ���������´�����������Ԫ�صļ������ԣ������ϻᴥ�����reflow.
    
    
      
����:http://www.i5good.com/20140410159.html