              
          
    最近，和一个网友交流的时候，给我提了一个非常奇怪的问题。那就是，在一个运算中，加了一个引用之后，发现性能慢了一万倍。在我的脑海里面，引用是一个非常容易出错的问题，特别是PHP里面的引用，有非常多的陷阱。因为，以前专门研究过这一块PHP的源代码，所以，我可以比较清晰的解析引用到底是怎么一回事，希望，读了我这篇博客的PHP开发者，能彻底理解这个问题。如果，有任何疑问，或者有一些你想了解的问题，可以给我留言。

    先来看一段代码:

    class RefferTest{    private $data;    private $testKey;    function __construct()    {        $key = "hello";        $this->data[$key] = range(0, 10000);        $this->testKey = $key;    }     function reffer($key)    {        $reffer = &;$this->data[$key];        return count($reffer);    }     function noreffer($key)    {       return count($this->data[$key]);    }     function test()    {        $t1 = microtime(true);        for ($i = 0; $i < 5000; $i++)        {            $this->reffer($this->testKey);        }        $t2 = microtime(true) - $t1;        var_dump("reffer: " . round($t2, 4));                 $t1 = microtime(true);        for ($i = 0; $i < 5000; $i++)        {            $this->noreffer($this->testKey);        }        $t2 = microtime(true) - $t1;        var_dump("noreffer: " . round($t2, 4));    }}$test = new RefferTest();$test->test();
    如果你完这个代码，能说出，为了reffer和noreffer会差一万倍的性能，那下面的也就没有必要往下看了。这篇博客针对的是，PHP的新手。你可以运行一下这个代码试试看，的确差了一万倍。当然，那个网友遇到的问题的代码要比上面的复杂，上面的代码是我为了说明问题，特意简化的。或许你已经从代码里面看出问题了，但是，至于为什么会这样。我想，还是有必要分析一下。这样，以后，在使用PHP的时候，才不会犯相同的错误。

    PHP为了减少复制，采用了一种copyonwriter的机制。我想，这是一种非常常见的机制，你也一定听说过。比如，gcc的stlstring的实现，就是采用这样的机制，字符串赋值，不是真正的复制，而且，在修改的时候才会进行复制。我们先来举个最简单的例子：

    $a = str_repeat("0", 10000);$b = $a;$a[0] = "1";
    $a是一个非常大的字符串，如果$b=$a的时候，进行复制，那要耗费很多内存和cpu，这样非常的不划算，万一，下面的代码并不修改$a和$b那复制根本没有必要。当然，$a在后面又被修改了，这个时候，必须进行复制了，否则就不符合逻辑了。但是，现在问题来了，怎么知道，$a在修改的时候，要进行复制呢，必须要有这样一个标记。方法就是采用引用计数。引用计数还被用来进行内存的管理。

    基本的流程是这样的：

    1:创建一个变量，可以保存10000个0的这样一个字符串。

    2:创建一个变量符号a，这个变量符号引用这个变量。注意，变量符号和变量不是一回事情，这两者是分离的。

    如果从C语言的角度来说，PHP大概完成这样一件事情：

    char *varname = "a";size_t varname_len = strlen(varname);zend_hash_add(EG(active_symbol_table), varname, varname_len + 1, &;var, sizeof(zval*), NULL);
    active_symbol_table是PHP的一个符号表，所有能访问到的变量都在这个里面，他是一个哈希表。var这个变量，保存了10000个0这个字符串。而且是zval的结构，zval的结构如下：

    typedef struct _zval_struct {    zvalue_value value;    zend_uint refcount;    zend_uchar type;    zend_uchar is_ref;} zval; typedef union _zvalue_value {    long lval;    double dval;    struct {        char *val;        int len;    } str;    HashTable *ht;    zend_object_value obj;} zvalue_value;
    zvalue_value是一个联合，可以保存long，double，字符串，哈希表（PHPArray），还有就是对象。也就是所有的PHP的类型。zval其实就是对zvalue_value，加入了类型type和引用is_ref，引用计数refcount三个功能。这就是PHP中的普通变量。要是用PHP做比较大型的东西，就会发现，内存占用非常厉害。就是因为，他一个变量不是传统C语言的那个变量了，它加了很多东西。

    好了，第一句完成了，下面是第二句。第二句很简单，会产生一个新的变量符号b，把他加入active_symbol_table，但是不会增加新的一个变量，而只是，refcount++。赋值就完成了。如图：

     

    首先我们要注意的是，a，b只是一个符号，他是active_symbol_table表里面的一个key，都有一个指针指向一个zval，所以，a和b在C语言层面上是完全一致的。我们就得出PHP变量第一定律：

    PHP变量第一定律：如果两个变量指向同一个zval，那么这两个变量是无差别的。也就是说，任何对a的操作相对b都是对称的。这里的对称，是这样理解的。就是镜子中的你，而不是等同。比如，对a进行赋值，a就会产生copy。同样的，如果对b进行赋值，也会进行相同的操作，那就是b产生一个copy。也就是说，a和b的行为是一样的。

    

    第三句，当writer发生的时候，PHP会判断一下refcount是否大于2，如果大于2，那么就复制一下zval，然后，把原来那个zvalrefcount--。这就是copyonwriter的全部了，你一定觉得，这一切你都是非常的熟悉，你都懂。

    

    但是，PHP不仅仅是copyonwriter这样简单，它还有一个引用的问题。引入引用的概念，这样，问题就变的有些复杂了。因为，引用这个标记，意思就是说，writer的时候，你也不需要复制。这样，会修改原来的那个变量。从我们在学校里面以前经常学习的哲学上来说，这是一对矛盾。他们是对立的，又是统一的，各有各的用处。所谓，存在的就是合理的。

    好，下面我们来看看这对矛盾，我们只考虑两种组合的情况。多种组合都是类似的。两种组合的话，就是赋值在前，引用在后。

    或者引用在前，赋值在后。我们会分别讨论，先来看：就是赋值在前，引用在后的情况。

    $a = 1;$b = $a;$c = &;$a;
    $b=$a,是copyonwriter行为的赋值。而$c和$a是引用赋值。我们假设在上面这样的情况下，我们可以用一个zval表示，也就是不需要复制，那么情况是这样的：

     

    根据我们的PHP变量第一定律，那，就是说，a，b，c的操作是对称的，但是非常明显，对b操作要产生复制行为，而对a操作不会产生复制，操作行为不相同，和第一定律矛盾。也就是说，要使得上面的操作没有矛盾，必须，进行分离。分离的原则就是，谁制造矛盾，谁复制。显然是第三句话，$c=&;$a;在制造矛盾。所以，内部变量的复制过程如下图：

     

    上面情况是赋值在前，引用在后的情况。还有一种情况是，引用在前赋值在后：

    1:$a = 1;
    2:$b = &;$a;
    3:$c = $a;

    按照PHP变量的第一定律，a，b，c必须进行分离，才能保证定律的正确。可以发现，b和a明显是一伙人，就是说，b和a的操作是对称的，他们可以指向同一个zval，而c的行为和a，b不一样，改变c需要进行复制。看到这里，我想，如果你看懂了的话，为什么刚开始，贴出来的那段代码的，那个两个count差异如此之大，你也应该明白了。当我和那个网友讨论的时候，它最后说，那这样的话，PHP设计的不好，我完全可以，$c先不进行复制，等c被write了，再进行复制。看来要说懂一个东西，还是一件很难的事情，好好想想那个PHP第一定律吧。你可以假设不进行分离，c指向同一个zval，所以，c和a，b的行为是一样的，是is_ref=1，所以，c不会进行复制。最后一种内部执行情况可以用下图表示：

     

    我以前也进行搞混这个引用，现在，你可以用那个第一定律来分析所有的情况了。PHP内核分析的文章，以后我还会写一些，如果你想深入了解PHP的某些方面，可以给我留言。

    最后再补充一点，也是一个隐性的错误。

    function count_bigarray(){    global $bigarray;    returncount($bigarray);}
    这里，没有显示的引用，但是这里隐藏了一个引用。PHP会自动创建一个引用全局变量$bigarray的代码，如果你在这里使用count，那么这个效率会非常的慢。最好直接通过$GLOBAL数组进行引用。
    
    
      
来自:http://www.i5good.com/20120518101.html