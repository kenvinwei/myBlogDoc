              
          
    ǰ�ԣ�

    ��JavaScript���ģʽ������-��ߴ���������ԣ��ɶ��ԣ�ʹ��������׵�ά������չ��

    ����1.����ģʽ������ģʽ������ģʽ������Ϊ���һ������ǰ�˱������յ�ģʽ���Գ����̺ͽӿڱ�̶��ǳ��кô���

    ����2.װ����ģʽ�����ģʽ�кܶ����Ƶĵط������Ƕ�������װ�Ķ���ʵ��ͬ���Ľӿڲ��һ���κη����ĵ��ô��ݸ���Щ����װ����ģʽ�����ģʽ�Ǳ��������Ľϳ���������ģʽ���Ҹ�����ʵҲû�ù������Բ��˺ܶ�������Ϻ��ĵ������Һ�����

    ����3.����ģʽ�Ǹ��ǳ�����˼��ģʽ���������е�JavaScript�ⶼ���õ����ģʽ��������������˼ά���������̵ľ��飬��������������ģʽ������������ս����ʵһ�Ӵ����֪�����Ǹ��ܼ򵥵�ģʽ��������������ģʽ�ú�����ģʽһ������˵�����ģʽ�����нӿڽ��а�װ���������ÿ��Ժܶ�̶�����߿���Ч�ʡ�������ģʽ�����Ƶĵط�������һ�����Ļ����Ŷ���ܿ����ֵġ�

    ����4.��Ԫģʽ��һ�����Ż�ΪĿ�ĵ�ģʽ��

    ����5.����ģʽ��Ҫ���ڿ��ƶ���ķ��ʣ������Ƴٶ��䴴����Ҫ���ô���������Դ�����ʵ������

    ����6.�۲���ģʽ���ڶԶ����״̬���й۲죬���ҵ��������仯ʱ�ܵõ�֪ͨ�ķ����������ö�����¼����м����Ա����������Ӧ���۲���ģʽҲ����Ϊ��������ģʽ����

    ����7.����ģʽ�ǶԷ������ý��з�װ�ķ�ʽ��������ģʽ���ԶԷ������ý��в������ʹ��ݣ�Ȼ������Ҫ��ʱ���ټ���ִ�С�

    ����8.ְ����ģʽ������������ķ����ߺͽ�����֮�����ϡ�

    ����JavaScript���ģʽ������Щ��

    �������壨Singleton��ģʽ��������JavaScript������������õ�ģʽ��

    ����������JavaScript���ж�����;�����������������ռ䡣���Լ�����ҳ��ȫ�ֱ���������(����ҳ��ʹ��ȫ�ֱ����з���)�������ڶ��˿���ʱ�������ĳ�ͻ(ʹ�ú���������ռ�)�ȵȡ�

    ��������С����Ŀ���߹����У�����������������ռ���Լ��Ĵ�����֯��һ��ȫ�ֱ������£����Դ���߸��ӵĹ����У����������������ش�����֯��һ���Ա��պ��ά��������

    ����ʹ�õ���ķ���������һ�������ռ�����Լ������д����ȫ�ֶ���ʾ����


    1 ����var functionGroup = {2 ��������name:'Darren',3 ��������method1:function(){4 ������������//code5 ��������},6 ��������init:function(){7 ������������//code8 ��������}9 ����}

    ��������


    1 ����var functionGroup  =newfunction myGroup(){2 ��������this.name ='Darren';3 ��������this.getName =function(){4 ������������returnthis.name5 ��������}6 ��������this.method1 =function(){}7 ��������...8 ����}

    ������

    ����������Factory��ģʽ���ṩһ������һϵ����ػ��໥��������Ľӿڣ�������ָ�����Ǿ�����ࡣ

    �����������ǰѳ�Ա����Ĵ�������ת����һ���ⲿ���󣬺ô�������������֮������(��Ϊ��ϣ������໥Ӱ��)��ͨ��ʹ�ù�������������new�ؼ��ּ������࣬���԰�����ʵ�����Ĵ��붼������һ��λ�ã������ڴ���ģ�黯�Ĵ��룬����ǹ���ģʽ��Ŀ�ĺ����ơ�

    �����ٸ����ӣ�����һ����Ĺ���Ҫ����������һ������Ҫ������չ�Եģ���ô�ⲿ�ִ���Ϳ��Կ��ǳ������������һ��ȫ�µĶ����������ô����ǽ�����չ��ʱ������ά��-ֻ��Ҫ������������ڲ����������ԣ��ﵽ�˶�̬ʵ�ֵ�Ŀ�ġ��ǳ�������һ��ʾ��-XHR������


    1���� var XMLHttpFactory =function(){};������������//����һ���򵥹���ģʽ2 ����XMLHttpFactory.createXMLHttp =function(){3�������� var XMLHttp = null;4 ��������if (window.XMLHttpRequest){5 ������������XMLHttp = new XMLHttpRequest()6�������� }elseif (window.ActiveXObject){7 ������������XMLHttp = new ActiveXObject("Microsoft.XMLHTTP")8 ��������}10 ����return XMLHttp;11 ����}12 ����//XMLHttpFactory.createXMLHttp()����������ݵ�ǰ�����ľ����������һ��XHR����13 ����var AjaxHander =function(){14 ��������var XMLHttp = XMLHttpFactory.createXMLHttp();15 ��������...16 ����}

    ����ģʽ�����ּ򵥹���ģʽ�ͳ��󹤳�ģʽ��������ܵ��Ǽ򵥹���ģʽ������ģʽ�õĸ���Ҳ�������á����󹤳�ģʽ��ʹ�÷�������-�����һ�������࣬����಻�ܱ�ʵ������ֻ�������������࣬���ͨ�����������չʵ�ֹ���������ʾ����


    1 ����var XMLHttpFactory =function(){};��     //����һ�����󹤳�ģʽ2 ����XMLHttpFactory.prototype = {3    ����//������Ҫ��������������׳�һ�����������ܱ�ʵ������ֻ��������������4    ����createFactory:function(){5       ����thrownew Error('This is an abstract class');6    ����}7 ����}8 ����//�������࣬���¿�ʼ���л����������н���̳е�ģʽ�������׿���ȥ�ο�ԭ��9 ����var XHRHandler =function(){10    ����XMLHttpFactory.call(this);11 ����};12 ����XHRHandler.prototype =new XMLHttpFactory();13 ����XHRHandler.prototype.constructor = XHRHandler;14 ����//���¶���createFactory ����15 ����XHRHandler.prototype.createFactory =function(){16    ����var XMLHttp =null;17    ����if (window.XMLHttpRequest){18       ����XMLHttp =new XMLHttpRequest()19    ����}elseif (window.ActiveXObject){20       ����XMLHttp =new ActiveXObject("Microsoft.XMLHTTP")21    ����}22    ����return XMLHttp;23 ����}

    ����

    �����Žӣ�bridge��ģʽ����ʵ��API��ʱ������ģʽ�ҳ����á�������ģʽ�У�����ģʽ��������������ʵʩ��

    ��������ģʽ����������������ʹ��������Ͷ���֮�����ϣ����ǽ���������ʵ�ָ��뿪�����Ա���߶����仯������ģʽ����JavaScript�г�����ʱ�������ı���кܴ��洦������ģʽ�����ʵ�ʵ�Ӧ�ó���֮һ��ʱ��������ص��������ȷ���һ�����õ�ʾ����


    1 ����element.onclick =function(){2    ����new setLogFunc();3 ����};



    ����Ϊʲô˵���ʾ�����ã���Ϊ����δ������޷������Ǹ�LogFunc����Ҫ��ʾ��ʲô�ط�������ʲô�����õ�ѡ���Լ�Ӧ����ôȥ�޸�������һ��˵�����ǣ�����ģʽ��Ҫ�������ýӿڡ�����������ʵ����Ҳ���ǿ����á���ҳ����һ�������ܶ������ģ�飬�ӿڿ���ʹ��ģ��֮�����Ͻ��͡�

    ������������ģʽ����ȷʹ������Ĳ�ֻ���㣬������Щ����ά���������ˡ��ѳ�������ʵ�ָ��뿪���ɶ����ع�������ĸ������֣�bugҲ��˸����ײ��ҡ�

    ��������ģʽĿ�ľ�����API���ӽ�׳����������ģ�黯�̶ȣ��ٳɸ�����ʵ�֣�����߳��������ԡ�һ���õ�ʾ����


    1 ����element.onclick =function(){����//API�ɿ���������ˣ�ʹ�����API���ӽ�׳2    ����new someFunction(element,param,callback);3 ����}

    ����ע������ģʽ�������������ӹ�����API�����˽�е�ʵ�ִ��룬�����԰Ѷ����������һ�������·�װ���ܵĲ����ᵽ����Ȩ������Ҳ������ģʽ��һ����������JS���ģʽ�����ҵ�ʾ���������Ҷ����ģʽ����⣺


    1 ����//����ķ�ʽ2 ����//���API�����¼��������ص������Ĺ������ƣ��¼�������Ϊ�������ݸ���������������в�û��ʹ�������������ֻ�Ǵ�this�����ȡID��3 ����addEvent(element,'click',getBeerById);4 ����function(e){5    ����var id =this.id;6    ����asyncRequest('GET','beer.url?id='+ id,function(resp){7       ����//Callback response8      ���� console.log('Requested Beer: '+ resp.responseText);9    ����});10 ����}11 12 ����//�õķ�ʽ13 ����//���߼��Ϸ�������id����getBeerById����ʽ������ģ��һ�Ӧ�������ͨ��һ���ٵ��������ء���ô��⣬����������������Խӿڶ�����ʵ�ֽ��б�̣�������ģʽ�ѳ�����뿪����14 ����function getBeerById(id,callback){15    ����asyncRequest('GET','beer.url?id='+ id,function(resp){16       ����callback(resp.responseText)17    ����});18 ����}19 ����addEvent(element,'click',getBeerByIdBridge);20 ����function getBeerByIdBridge(e){21    ����getBeerById(this.id,function(beer){22       ����console.log('Requested Beer: '+ beer);23    ����});24 ����}��

    

    ����װ���ߣ�Decorator��ģʽ�����ģʽ����Ϊ�������ӹ���(�򷽷�)��

    ������̬�ظ�һ���������һЩ�����ְ�𡣾���չ���ܶ��ԣ������������෽ʽ��Ϊ��

    ����װ����ģʽ�����ģʽ�кܶ๲ͬ�㣬���Ƕ�������װ�Ķ���ʵ��ͳһ�Ľӿڲ��һ���κη������ô��ݸ���Щ���󡣿������ģʽ���ڰ��ڶ��Ӷ�����֯Ϊһ�����壬��װ����ģʽ�����ڲ��޸����ж��������������ǰ����Ϊ����ӷ�����

    ����װ���ߵ�����������͸���ģ������˵�����������װ��������Ȼ�������֮ǰʹ����ô����ķ�����ʹ�ã�������������оͿ��Կ��������ǴӴ��������ɣ�


    1 ����//����һ�������ռ�ΪmyText.Decorations2 ����var myText= {};3 ����myText.Decorations={};4 ����myText.Core=function(myString){5    ����this.show =function(){return myString;}6 ����}7 ����//��һ��װ��8 ����myText.Decorations.addQuestuibMark =function(myString){9    ����this.show =function(){return myString.show()+'?';};10 ����}11 ����//�ڶ���װ��12 ����myText.Decorations.makeItalic =function(myString){13    ����this.show =function(){return'<li>'+myString.show()+'</li>'};14 ����}15 ����//�õ�myText.Core��ʵ��16 ����var theString =new myText.Core('this is a sample test String');17 ����alert(theString.show());����//output 'this is a sample test String'18 ����theString =new myText.Decorations.addQuestuibMark(theString);19 ����alert(theString.show());����//output 'this is a sample test String?'20 ����theString =new myText.Decorations.makeItalic (theString);21 ����alert(theString.show());����//output '<li>this is a sample test String</li>'

    

    ���������ʾ���п��Կ�������һ�ж����Բ�������֪���������Ľӿڣ��������Զ�̬��ʵ�֣���Ϊ���ж������������ⷽ�棬װ����ģʽ�м��������ԡ�

    ���������ҪΪ���������Ի��߷��������Ӹ�����������Ľ���취����ʵ�ʵĻ�����Ӧ��ʹ��װ����ģʽ����������֮���Ի᲻ʵ�������ԭ������Ҫ��ӵ����Ի򷽷�������Ҫ��ʹ�ô������ࡣ

    ������ϣ�Composite��ģʽ����������ϳ����νṹ�Ա�ʾ������-���塱�Ĳ�νṹ����ʹ�ÿͻ��Ե�������͸��϶����ʹ�þ���һ���ԡ�

    �������ģʽ��һ��רΪ����Web�ϵĶ�̬�û�����������Ƶ�ģʽ��ʹ������ģʽ��������һ�������ڶ�������ϼ������ӵĻ�ݹ����Ϊ�����ģʽ�ó��ڶԴ���������в�����

    �������ģʽ�ĺô���1.����Ա������ͬ���ķ����������ļ��������е��ض��Ӷ���2.������������һ���Ӷ�����֯�����νṹ������ʹ���������ɱ�������

    �������ģʽ���÷�Χ��1.����һ����֯��ĳ�������ϵ�Ķ��󣨾���ṹ�����ڿ����ڼ��޷�֪������2.ϣ����������������е�һ���ֶ���ʵ��һ��������

    ������ʵ���ģʽ���ǽ�һϵ�����ƻ�����Ķ��������һ����Ķ��������������ṩһЩ���õĽӿ�������ЩС������в�������������ã���������򵥡����磺��form�ڵ�Ԫ�أ�������ҳ����Ƶ�����£�һ���ʣ��input�ˣ�������Щinput����name��value�����ԣ���˿��Խ���ЩinputԪ����Ϊform����ĳ�Ա���������form�����ṩ����Ľӿڣ������ʵ��һЩ�򵥵Ĳ�������������ĳ��input��value�����/ɾ��ĳ��input�ȵȡ�

    ��������ģʽ���������Ƚϳ������Ҵӡ�JS���ģʽ�����Ҹ�һ��ʵ������һ��ǿ�����ɣ��ȴ�����϶�����


    1 ����// DynamicGallery Class2 ����var DynamicGallery =function (id) { // ʵ��Composite��GalleryItem��϶����� 3    ����this.children = [];4    ����this.element = document.createElement('div');5    ����this.element.id = id;6    ����this.element.className ='dynamic-gallery';7 ����}8 ����DynamicGallery.prototype = {9    ����// ʵ��Composite��϶���ӿ� 10    ����add: function (child) {11       ����this.children.push(child);12       ����this.element.appendChild(child.getElement());13    ����},14    ����remove: function (child) {15       ����for (var node, i =0; node =this.getChild(i); i++) {16          ����if (node == child) {17             ����this.children.splice(i, 1);18            ���� break;19          ����}20       ����}21       ����this.element.removeChild(child.getElement());22    ����},23    ����getChild: function (i) {24       ����returnthis.children[i];25    ����},26    ����// ʵ��DynamicGallery��϶���ӿ� 27    ����hide: function () {28       ����for (var node, i =0; node =this.getChild(i); i++) {29          ����node.hide();30       ����}31       ����this.element.style.display ='none';32    ����},33    ����show: function () {34       ����this.element.style.display ='block';35       ����for (var node, i =0; node = getChild(i); i++) {36          ����node.show();37       ����}38    ����},39    ����// �������� 40    ����getElement: function () {41       ����returnthis.element;42    ����}43 ����}

    �����ٴ���Ҷ������


    1 ����var GalleryImage =function (src) { // ʵ��Composite��GalleryItem��϶�����������ķ��� 2    ����this.element = document.createElement('img');3    ����this.element.className ='gallery-image';4    ����this.element.src = src;5 ����}6 ����GalleryImage.prototype = {7    ����// ʵ��Composite�ӿ� 8    ����// ��Щ��Ҷ��㣬�������ǲ���ʵ����Щ����������ֻ��Ҫ���弴�� 9    ����add: function () { },10    ����remove: function () { },11    ����getChild: function () { },12    ����// ʵ��GalleryItem�ӿ� 13    ����hide: function () {14       ����this.element.style.display ='none';15    ����},16    ����show: function () {17       ����this.element.style.display ='';18    ����},19    ����// �������� 20    ����getElement: function () {21       ����returnthis.element;22    ����}23 ����} 

    �����������ǿ���ʹ����������������ͼƬ��


    1 ����var topGallery =new DynamicGallery('top-gallery'); 2 ����topGallery.add(new GalleryImage('/img/image-1.jpg')); 3 ����topGallery.add(new GalleryImage('/img/image-2.jpg')); 4 ����topGallery.add(new GalleryImage('/img/image-3.jpg')); 5 ����var vacationPhotos =new DyamicGallery('vacation-photos'); 6 ����for(var i =0, i <30; i++){ 7 ��������vacationPhotos.add(new GalleryImage('/img/vac/image-'+ i +'.jpg')); 8 ����} 9 ����topGallery.add(vacationPhotos); 10 ����topGallery.show(); 11 ����vacationPhotos.hide(); 

    �������棨facade��ģʽ������ģʽ�Ǽ�������JavaScript��ĺ���ԭ����ϵͳ�е�һ��ӿ��ṩһ��һ�µĽ��棬����ģʽ������һ���߲�ӿڣ�����ӿ�ʹ����һ��ϵͳ��������ʹ�ã��򵥵�˵����һ����֯�Ե�ģʽ�������������޸���Ͷ���Ľӿڣ�ʹ�������ʹ�á�

    ��������ģʽ���������ã�1.����Ľӿڣ�2.��������ʹ�����Ŀͻ�����֮�����ϡ�

    ��������ģʽ��ʹ��Ŀ�ľ���ͼ���档

    ��������һ�¼���������ϵ���Щ��ݷ�ʽͼ�꣬���Ǿ����ڰ���һ�����û�������ĳ���ط��ĽӿڵĽ�ɫ��ÿ�β������Ǽ�ӵ�ִ��һЩĻ������

    �������ڿ���ƪ�Ĳ��͵�ʱ���Ҿͼ������Ѿ���JavaScript��ʹ�þ����ˣ���ô��һ��д�����߿��������Ĵ��룺


    1 ����var addEvent =function(el,type,fn){2    ����if(window.addEventListener){3       ����el.addEventListener(type,fn);4    ����}elseif(window.attachEvent){5       ����el.attachEvent('on'+type,fn);6    ����}else{7       ����el['on'+type] = fn;8    ����}9 ����}



    �����������һ��JavaScript�г������¼������������������������һ�����������棬��������������ΪDOM�ڵ�����¼��������ļ�㷽����

    ��������Ҫ˵����ģʽ�ľ��������ˣ�Ϊʲô˵JavaScript�⼸������������ģʽ�ࡣ��������Ҫ���һ���⣬��ô��ð��������еĹ���Ԫ�ط���һ�����������ã�������������㡣�����룺


    1 ����//_model.util��һ�������ռ�2 ����_myModel.util.Event = {3    ����getEvent:function(e){4       ����return e|| window.event;5    ����},6    ����getTarget:function(e){7       ����return e.target||e.srcElement;8    ����},9    ����preventDefault:function(e){10       ����if(e.preventDefault){11          ����e.preventDefault();12       ����}else{13          ����e.returnValue =false;14       ����}15    ����}16 ����};17 ����//�¼����ߴ�ž�����ôһ����·��Ȼ����addEvent����ʹ��18 ����addEvent(document.getElementsByTagName('body')[0],'click',function(e){19    ����alert(_myModel.util.Event.getTarget(e));20 ����});

    ����������Ϊ���ڴ�����������������ʱ��õĽ���취���ǰ���Щ�����ȡ�����淽���У����������ṩһ����һ�µĽӿڣ�addEvent��������һ�����ӡ�

    

    ��������������Adapter��ģʽ����һ����Ľӿ�ת���ɿͻ�ϣ��������һ���ӿڡ�������ģʽʹ��ԭ�����ڽӿڲ����ݶ�����һ��������Щ�����һ������ʹ������ģʽ�Ķ����ֽа�װ������Ϊ����������һ���µĽӿڰ�װ��һ������

    �����ӱ����Ͽ�����������ģʽ�е����ƣ��������������θı�ӿڣ�����ģʽչ�ֵ���һ���򻯵Ľӿڣ��������ṩ�����ѡ�񣬶�������ģʽ��Ҫ��һ���ӿ�ת��Ϊ��һ���ӿڣ����������˳�ĳЩ������Ҳ����򻯽ӿڡ�����һ���򵥵�ʾ��������


    1 ����//������һ��3���ַ��������ĺ�������������ӵ�е�ȴ��һ�����������ַ���Ԫ�صĶ�����ô�Ϳ�����һ�����������νӶ���2 ����var clientObject = {3    ����str1:'bat',4    ����str2:'foo',5    ����str3:'baz'6 ����}7 ����function interfaceMethod(str1,str2,str3){8 ��������alert(str1)9 ����}10 ����//����������11 ����function adapterMethod(o){12    ����interfaceMethod(o.str1, o.str2, o.str3);13 ����}14 ����adapterMethod(clientObject)15 ����//adapterMethod��������Ϊ�����ڶ�interfaceMethod�������а�װ�����Ѵ��ݸ����Ĳ���ת��Ϊ������Ҫ����ʽ��

    ����������ģʽ�Ĺ��������ǣ���һ���µĽӿڶ�������ýӿڽ��а�װ��

    ����ʾ�������������⡣���������Ҫʵ�ֵ��Ǵ�Prototype���$������YUI��get������ת����


    1 ����//�ȿ������ڽӿڷ���Ĳ��2 ����//Prototype $ function 3 ����function $(){4    ����var elements =new Array();5    ����for(var i=0;i<arguments.length;i++){6       ����var element = arguments[i];7       ����if(typeof element =='string'){8          ����element = document.getElementById(element);9       ����}10       ����if(typeof.length ==1)    return element;11       ����elements.push(element);12    ����}13    ����return elements;14 ����}15 ����//YUI get method16 ����YAHOO.util.Dom.get =function(el){17    ����if(YAHOO.lang.isString(el)){18       ����return document.getElementById(el);19    ����}20    ����if(YAHOO.lang.isArray(el)){21       ����var c =[];22       ����for(var i=0,len=el.length;i<len;++i){23          ����c[c.length] = YAHOO.util.Dom.get(el[i]);24       ����}25       ����return c;26    ����}27    ����if(el){28       ����return el;29    ����}30    ����returnnull;31 ����}32 ����//�������������get����һ���������ҿ�����HTML,�ַ����������飻��$ľ�����ǵĲ���������ʹ���ߴ���������Ŀ�Ĳ���������HTML�����ַ�����33 ����//�����Ҫ��ʹ��Prototype��$������Ϊʹ��YUI��get�����������෴����ô��������ģʽ��ʵ�ܼ򵥣�34 ����function PrototypeToYUIAdapter(){35    ����return YAHOO.util.Dom.get(arguments);36 ����}37 ����function YUIToPrototypeAdapter(el){38    ����return $.apply(window,el instanceof Array?el:[el]);39 ����}



    ������Ԫ��Flyweight��ģʽ�����ù�������Ч��֧�ִ���ϸ���ȵĶ���

    ������Ԫģʽ���Ա�������ǳ�������Ŀ������ڳ����������ʱ��Ҫ���ɴ���ϸ���ȵ���ʵ������ʾ���ݡ����������Щʵ�����˼�������������˶�����ͬ�ģ���ʱ���ܹ��ܴ���ȵڼ�����Ҫʵ�������������������ܰ���Щ�����Ƶ���ʵ�����棬�ڷ�������ʱ�����Ǵ��ݽ������Ϳ���ͨ���������ȵؼ��ٵ���ʵ������Ŀ��

    ������ʵ�ʳ���˵˵�Լ������ɡ���

    ��ɲ���

    ��������Ԫ��������������ⲿ���������ݣ�

    ���������������������Ĺ�����

    �������洢�������洢ʵ������Ķ�������飬������Ԫ����ͳһ���ƺ͹���

    ����Ӧ�ó���

    ����1.ҳ����ڴ�����Դ�ܼ��Ͷ���

    ����2.��Щ����߱�һ���Ĺ��ԣ����Գ�������õĲ���������

    �����ؼ�

    ����1.�������ڲ����ⲿ���ݡ�

    ������Ҫ����ÿ�������ģ���ԡ���֤��Ԫ�Ķ�������ά������Ҫ�����ܶ�ĳ����ⲿ���ݡ�

    ����2.��������ʵ��

    ������Ȼ��������ⲿ���ݺͲ���������Ԫ�ͱ�����Է��ʺͿ���ʵ��������JavaScript���ֶ�̬�����У���������Ǻ�����ʵ�ֵģ����ǿ��԰ѹ����������Ķ���򵥵�����һ�������С�Ϊÿ��������Ʊ�¶���ⲿ�ķ�����������Ԫ�Ŀ��ơ�

    �����ŵ�

    ����1.���ܺĴ�Ĳ��������һ��������Դ�ܼ���ϵͳ�У��ɴ�������Դ���ڴ�ռ�ã�

    ����2.ְ���װ����Щ���������޸ĺ�ά����

    ����ȱ��

    ����1.������ʵ�ָ��Ӷȡ�

    ������ԭ����һ����������ʵ�ֵĹ��ܣ��޸�Ϊ��һ����Ԫ+һ������+һ���洢����

    ����2.���������ٵ���������ܻ�����ϵͳ������

    ����ʾ����


    1 ����//�����Ǽ�ʾ��2 ����var Car =function(make,model,year,owner,tag,renewDate){3 ��������this.make=make;4 ��������this.model=model;5 ��������this.year=year;6 ��������this.owner=owner;7 ��������this.tag=tag;8 ��������this.renewDate=renewDate;9 ����}10 ����Car.prototype = {11 ��������getMake:function(){12 ������������returnthis.make;13 ��������},14 ��������getModel:function(){15 ������������returnthis.model;16 ��������},17 ��������getYear:function(){18 ������������returnthis.year;19 ��������},20 ��������transferOwner:function(owner,tag,renewDate){21 ������������this.owner=owner;22 ������������this.tag=tag;23 ������������this.renewDate=renewDate;24 ��������},25 ��������renewRegistration:function(renewDate){26 ������������this.renewDate=renewDate;27 ��������}28 ����}29 ����//������С��û����Ӱ�죬���������ʱ��Լ�����ڴ�����ѹ�������������Ԫģʽ�Ż���30 ����//�����������ݵ�Car��31 ����var Car=function(make,model,year){32 ��������this.make=make;33 ��������this.model=model;34 ��������this.year=year;35 ����}36 ����Car.prototype={37 ��������getMake:function(){38 ������������returnthis.make;39 ��������},40 ��������getModel:function(){41 ������������returnthis.model;42 ��������},43 ��������getYear:function(){44 ������������returnthis.year;45 ��������}46 ����}47 ����//�м��������ʵ����Car��48 ����var CarFactory=(function(){49 ��������var createdCars = {};50 ��������return {51 ������������createCar:function(make,model,year){52 ����������������var car=createdCars[make+"-"+model+"-"+year];53 ����������������return car ? car : createdCars[make +'-'+ model +'-'+ year] =(new Car(make,model,year));54 ������������}55 ��������}56 ����})();57 ����//���ݹ�������������Car��ʵ���������ϸ�������58 ����var CarRecordManager = (function() {59 ��������var carRecordDatabase = {};60 ��������return {61 ������������addCarRecord:function(make,model,year,owner,tag,renewDate){62 ����������������var car = CarFactory.createCar(make, model, year);63 ����������������carRecordDatabase[tag]={64 ��������������������owner:owner,65 ��������������������tag:tag,66 ��������������������renewDate:renewDate,67 ��������������������car:car68 ������������}69 ��������},70 ������������transferOwnership:function(tag, newOwner, newTag, newRenewDate){71 ����������������var record=carRecordDatabase[tag];72 ����������������record.owner = newOwner;73 ����������������record.tag = newTag;74 ����������������record.renewDate = newRenewDate;75 ������������},76 ������������renewRegistration:function(tag,newRenewDate){77 ����������������carRecordDatabase[tag].renewDate=newRenewDate;78 ������������},79 ������������getCarInfo:function(tag){80 ����������������return carRecordDatabase[tag];81 ������������}82 ��������}83 ����})();



    ��������Proxy��ģʽ����ģʽ���������ʽ�ǶԷ��ʽ��п��ơ�����������һ�����󣨱��壩ʵ�ֵ���ͬ���Ľӿڣ�����ʵ���Ϲ������Ǳ��������������Ǹ���ִ�������ɵ�������Ǹ�������࣬������󲻻������Զ���Ļ������޸��κη�����Ҳ������Ǹ�����Ľӿڡ�

    ������һ����������������Ǹ�������ĳ��Զ�˷������ϣ�ֱ�Ӳ������������Ϊ�����ٶ�ԭ����ܱȽ����������ǿ�������Proxy�������Ǹ�������֮���ڿ����ϴ�Ķ���ֻ����ʹ����ʱ�Ŵ��������ԭ�����Ϊ���ǽ�ʡ�ܶ��ڴ档��JS���ģʽ���ϵ�ͼ���ʾ����

    


    1 ����var Publication =new Interface('Publication', ['getIsbn', 'setIsbn', 'getTitle', 'setTitle', 'getAuthor', 'setAuthor', 'display']);2���� var Book =function(isbn, title, author) {3    ���� //...4 ����} 5 ����// implements Publication6 ����implements(Book,Publication);7 8 ����/* Library interface. */9 ����var Library =new Interface('Library', ['findBooks', 'checkoutBook', 'returnBook']);10 11 ����/* PublicLibrary class. */12 ����var PublicLibrary =function(books) {13    ���� //...14 ����};15 ����// implements Library16 ����implements(PublicLibrary,Library); 17 18 ����PublicLibrary.prototype = {19    ���� findBooks: function(searchString) {20       ���� //...21     ����},22     ����checkoutBook: function(book) {23      ����   //...24    ���� },25     ����returnBook: function(book) {26       ����  //...27    ���� }28 ����};29 30 ����/* PublicLibraryProxy class, a useless proxy. */31 ����var PublicLibraryProxy =function(catalog) { 32   ����  this.library =new PublicLibrary(catalog);33 ����};34 ����// implements Library35 ����implements(PublicLibraryProxy,Library);36 37 ����PublicLibraryProxy.prototype = {38   ����  findBooks: function(searchString) {39     ����    returnthis.library.findBooks(searchString);40     ����},41     ����checkoutBook: function(book) {42      ����   returnthis.library.checkoutBook(book);43    ���� },44    ���� returnBook: function(book) {45     ����    returnthis.library.returnBook(book);46    ���� }47 ����};



    �����۲��ߣ�Observer��ģʽ�����������һ��һ�Զ��������ϵ���Ա㵱һ�������״̬�����ı�ʱ���������������Ķ��󶼵õ�֪ͨ���Զ�ˢ�¡�

    �����۲���ģʽ�д���������ɫ,�۲��ߺͱ��۲��ߡ���DOM�ı�̻����еĸ߼��¼�ģʽ�У��¼�������˵���׾���һ�����õĹ۲��ߡ��¼�������(handler)��ʱ�������(listener)������һ���£�ǰ�߾���һ�ְ��¼�������������ĺ������ֶΣ����ں����У�һ��ʱ������뼸��������������ÿ�����������ܶ������������������ı䡣


    1 ����//ʹ��ʱ������������ö��������Ӧһ���¼�2 ����var fn1 =function(){3    ����//code4 ����}5 ����var fn2 =function(){6    ����//code7 ����}8 ����addEvent(element,'click',fn1)��9 ����addEvent(element,'click',fn2)10 11���� //��ʱ�䴦�����Ͱ첻��12 ����element.onclick = fn1;13 ����element.onclick = fn2;



    �����۲���ģʽ�ǿ���������Ϊ��Ӧ�ó���������ֶΣ�ǰ�˳���Ա�����ľ��ǽ���һ���¼����������㴦�������Ϊ���Ӷ������ڴ����ĺ���߻������ܡ�

    �������Command��ģʽ����һ�������װΪһ�����󣬴Ӷ�ʹ����ò�ͬ������Կͻ����в��������������Ŷӻ��¼������־���Լ�֧�ֿ�ȡ���Ĳ�����

    �������������һ������������������������Ķ���Ľ���壬���е�����������һ��ִ�в���������;���ǵ�������������󶨵Ĳ�����ʾ����


    1 ����car Calculator={2    ����add:function(x,y){3     ����  return x+y;4    ����},5    ����substract:function(x,y){6     ����  return x-y;7    ����},8    ����multiply:function(x,y){9     ����  return x*y;10    ����},11    ����divide:function(x,y){12     ����  return x/y;13    ����}14 ����}15 ����Calculator.calc =function(command){16    ����return Calculator[command.type](command.op1,command.opd2)17 ����};18 ����Calculator.calc({type:'add',op1:1,op2:1});19 ����Calculator.calc({type:'substract',op1:5,op2:2});20 ����Calculator.calc({type:'multiply',op1:5,op2:2});21 ����Calculator.calc({type:'divide',op1:8,op2:4});



    ��������ģʽ����Ҫ��;�ǰѵ��ö����û����棬API�ʹ���ȣ���ʵ�ֲ����Ķ�����뿪��Ҳ����˵ʹ�����Ļ�����ʽ��Ҫ���ߵ�ģ�黯ʱ�������õ�����ģʽ��

    ����ְ������ChainOfResponsibility��ģʽ��Ϊ�������ķ����ߺͽ�����֮����ϣ���ʹ��������л��ᴦ��������󡣽���Щ��������һ���������������������ݸ�����ֱ����һ������������

    ����ְ�����ɶ����ͬ���͵Ķ�����ɣ��������Ƿ�������Ķ��󣬶����������ǽ��������Ҷ�����д���򴫵ݵĶ�����������ʱҲ��һ����������װ��������йص��������ݡ�

    �������͵����̴����ǣ�

    ����1.������֪�����е�һ�������ߣ�������������߷�������

    ����2.ÿһ�������߶���������з�����Ȼ��Ҫô��������Ҫô�������´���

    ����3.ÿһ��������֪������������ֻ��һ�������������е��¼ҡ�

    ����4.���û���κν����ߴ���������ô���󽫴������뿪����ͬ��ʵ�ֶԴ�Ҳ�в�ͬ�ķ�Ӧ��һ����׳�һ������

    ����ְ����ģʽ�����÷�Χ:1.�ж���Ķ�����Դ���һ�������ĸ����������������ʱ���Զ�ȷ����2.���ڲ���ȷָ�������ߵ�����£����������е�һ���ύһ������3.�ɴ���һ������Ķ��󼯺���Ҫ����ָ̬����

    ����ȷʵ������ģʽ���˽⣬�������Ҳ���٣����Դ����Ȳ����ˡ�������Ҷ����ģʽ��ľ��ʲô�õ��������ܽϺñ������ģʽ�Ĵ��룬лл��

    ���������

    ����1.ÿ��ģʽ�����Լ�����ȱ�㣬����ÿ��ģʽ����ȷʹ�û��ÿ�������Ա����Ĺ�����

    ����2.���㲻ʹ��JavaScript���ģʽһ������д�����ӵĿ�ʹ�õĴ��룬����������������˽�JavaScript�������������ѧϰ��ߴ����ģ�黯�̶ȩp��ά���ԩp�ɿ��Ժ�Ч�ʣ���ô���������JavaScript���ģʽ������һ������ǰ�˿�������ʪ�ر���������
    
    
      
����:http://www.i5good.com/2012022876.html