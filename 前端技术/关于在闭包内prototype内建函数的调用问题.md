              
          
    　如题，这是个蛮基础、满细节、却又蛮重要的问题。（所以说对于把原型，constructor，new关键字等都理解的透彻的高手来说，此文乃小儿科。敬请绕道）

    　　由于之前的编码习惯，一致也没注意这个问题，直到有一天，我突然想换一种方式表达同样的意思的时候，发现了一个小问题。且听我细细道来：

    先看一段很傻很天真的代码：

    var a = function(){     function b(){this.c()}    b.prototype.c = function(){alert('worked!')}    return {b:b};}a.b();
    我相信很多同仁应该第一眼就发现问题了...

    

    是啊，这段代码是有误的！！

    肯定会有人说，你创建一个匿名函数，这种方式函数只能按照程序流程执行到定义的那一行代码才被声明，都没执行怎么可能调用呢？！

    恩，是的。所以匿名函数要先执行才能调用，不然就是undefined，因此我们稍微改一下：

    var a = function(){     function b(){this.c()}    b.prototype.c = function(){alert('worked!')}    return {b:b};}(); a.b();
    呵呵，好了，现在我们让匿名函数先执行了，应该可以了吧，结果试一下，发现console会报错，this.cisnotafunction!纳尼？？

    

    一定又会有人吼了，prototype是需要在一个函数对象创建的时候才会生成，你外层匿名函数执行了，但是b()却是没有实例化的，prototype对像都没有生成，当然c没有定义也不可能执行的。

    所以，我们还需要对b()实例化，众所周知，用new关键字！！

    /* === for example === */var a = function(){ //用匿名函数创建    function b(){this.c()}    b.prototype.c = function(){alert('worked!')}    return {b:b};}(); //匿名函数必须运行之后才能调用new a.b(); //必须通过new关键字实例化,否则取不到c()的实例,因为c是通过prototype内建的
    好了，这下终于对了吧。所以说，在这种情况下，new关键字是很重要的！！也是必不可少的。

    

    先不慌着松口气，咱们接着看下面的代码：

    

 ?




    /* == */var a2 = function(){    return{        b2:function(){            this.c2();        },        c2:function(){            alert('worked!');        }    } //a2返回的其实是一个对象；所以用a()的方式显式调用会发现报错，a2 is not a function }();a2.b2();
    把刚才的代码稍微换了一下，不用原型了，直接写到返回对象里，同样的，也是创建一个匿名函数赋给a2,但是其实和上面的一样，a2执行完毕之后，它就不再是一个Function对象了，而是一个Object对象了，这个应该很容易理解。那么，上面的代码其实和前一段执行结果是一致的。

    

    我在这里只是想说没有人会在这里还用new关键字了吧。因为这里的c2不是通过prototype内建的，于是，a2对象里的b2函数是可以直接调用的。

    （另外，这里还想提一下，两种方式中this.c()和this.c2()中的this指向其实也是不一样的。前一种是指向b,后一种指向对象a2）

    　　还有一点，需要提一下。

    /* == */var a2 = function(){    return{        b2:function(){            this.c2();        },        c2:function(){            alert('worked!');        }    } //a2返回的其实是一个对象；所以用a()的方式显式调用会发现报错，a2 is not a function }();a2.b2(); alert(typeof a2.constructor); // functionalert(typeof a2); //Object
    如上，咱们再看看a2和a2.constructor有什么不一样，a2.constructor返回的是function，而a2本身却是一个Object，有人可能不太理解。其实这个很简单，仔细想想constructor属性的定义应该就可以明白。

    

    constructor属性是创建对象返回的一个函数参考。所谓函数参考，理所应当就应该是function，a2为Object这个没有争议。

    好的，此文大概到这儿。结尾之余还想请各位看官看看下面这几行代码：

    /* == */function a1(){    function b1(){this.c1()}    b1.prototype.c1 = function(){alert('worked!')}    return b1();}
    通过显式的方式创建的函数，各位觉得怎么才能正确的运行出‘worked!’呢？？
    
    
      
来自:http://www.i5good.com/2012020461.html