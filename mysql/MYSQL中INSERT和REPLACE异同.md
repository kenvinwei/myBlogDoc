              
          
用于操作数据库的SQL一般分为两种，一种是查询语句，也就是我们所说的 SELECT语句，另外一种就是更新语句，也叫做数据操作语句。言外之 意，就是对数据进行修改。在标准的SQL中有3个语句，它们是INSERT、UPDATE以及DELETE。在MySQL中又多了一个REPLACE语句，因此，本文以MySQL为背景来讨论如何使有SQL中的更新语句。

一、INSERT和REPLACE

INSERT和REPLACE语句的功能都是向表中插入新的数据。这两条语句的语法类似。它们的主要区别是如何处理重复的数据。

1. INSERT的一般用法

MySQL中的INSERT语句和标准的INSERT不太一样，在标准的SQL语句中，一次插入一条记录的INSERT语句只有一种形式。

INSERT INTO tablename(列名…) VALUES(列值);

而在MySQL中还有另外一种形式。

INSERT INTO tablename SET column_name1 = value1, column_name2 = value2，…;

第一种方法将列名和列值分开了，在使用时，列名必须和列值的数一致。如下面的语句向users表中插入了一条记录：

INSERT INTO users(id, name, age) VALUES(123, &#39;姚明&#39;, 25);

第二种方法允许列名和列值成对出现和使用，如下面的语句将产生中样的效果。

INSERT INTO users SET id = 123, name = &#39;姚明&#39;, age = 25;

如果使用了SET方式，必须至少为一列赋值。如果某一个字段使用了省缺值（如默认或自增值），这两种方法都可以省略这些字段。如id字段上使用了自增值，上面两条语句可以写成如下形式：

INSERT INTO users (name, age) VALUES(&#39;姚明&#39;,25);

INSERT INTO uses SET name = &#39;姚明&#39;, age = 25;

MySQL在VALUES上也做了些变化。如果VALUES中什么都不写，那MySQL将使用表中每一列的默认值来插入新记录。

INSERT INTO users () VALUES();

如果表名后什么都不写，就表示向表中所有的字段赋值。使用这种方式，不仅在VALUES中的值要和列数一致，而且顺序不能颠倒。 INSERT INTO users VALUES(123, &#39;姚明&#39;, 25);

如果将INSERT语句写成如下形式MySQL将会报错。

INSERT INTO users VALUES(&#39;姚明&#39;,25);

2. 使用INSERT插入多条记录

看到这个标题也许大家会问，这有什么好说的，调用多次INSERT语句不就可以插入多条记录了吗！但使用这种方法要增加服务器的负荷，因为，执行每一次SQL服务器都要同样对SQL进行分析、优化等操作。幸好MySQL提供了另一种解决方案，就是使用一条INSERT语句来插入多条记录。这并不是标准的SQL语法，因此只能在MySQL中使用。

INSERT INTO users(name, age)

VALUES(&#39;姚明&#39;, 25), (&#39;比尔.盖茨&#39;, 50), (&#39;火星人&#39;, 600);

上面的INSERT 语句向users表中连续插入了3条记录。值得注意的是，上面的INSERT语句中的VALUES后必须每一条记录的值放到一对(…)中，中间使用&quot;,&quot;分割。假设有一个表table1

CREATE TABLE table1(n INT)；

如果要向table1中插入5条记录，下面写法是错误的：

INSERT INTO table1 (i) VALUES(1,2,3,4,5);

MySQL将会抛出下面的错误

ERROR 1136: Column count doesn&#39;t match value count at row 1

而正确的写法应该是这样：

INSERT INTO t able1(i) VALUES(1),(2),(3),(4),(5);

当然，这种写法也可以省略列名，这样每一对括号里的值的数目必须一致，而且这个数目必须和列数一致。如：

INSERT INTO t able1 VALUES(1),(2),(3),(4),(5);

3. REPLACE语句

我们在使用数据库时可能会经常遇到这种情况。如果一个表在一个字段上建立了唯一索引，当我们再向这个表中使用已经存在的键值插入一条记录，那将会抛出一个主键冲突的错误。当然，我们可能想用新记录的值来覆盖原来的记录值。如果使用传统的做法，必须先使用DELETE语句删除原先的记录，然后再使用 INSERT插入新的记录。而在MySQL中为我们提供了一种新的解决方案，这就是REPLACE语句。使用REPLACE插入一条记录时，如果不重复，REPLACE就和INSERT的功能一样，如果有重复记录，REPLACE就使用新记录的值来替换原来的记录值。

使用REPLACE的最大好处就是可以将DELETE和INSERT合二为一，形成一个原子操作。这样就可以不必考虑在同时使用DELETE和INSERT时添加事务等复杂操作了。

在使用REPLACE时，表中必须有唯一索引，而且这个索引所在的字段不能允许空值，否则REPLACE就和INSERT完全一样的。

在执行REPLACE后，系统返回了所影响的行数，如果返回1，说明在表中并没有重复的记录，如果返回2，说明有一条重复记录，系统自动先调用了 DELETE删除这条记录，然后再记录用INSERT来插入这条记录。如果返回的值大于2，那说明有多个唯一索引，有多条记录被删除和插入。

REPLACE的语法和INSERT非常的相似，如下面的REPLACE语句是插入或更新一条记录。

REPLACE INTO users (id,name,age) VALUES(123, &#39;赵本山&#39;, 50);

插入多条记录：

REPLACE INTO users(id, name, age)

VALUES(123, &#39;赵本山&#39;, 50), (134,&#39;Mary&#39;,15);

REPLACE也可以使用SET语句

REPLACE INTO users SET id = 123, name = &#39;赵本山&#39;, age = 50;

上面曾提到REPLACE可能影响3条以上的记录，这是因为在表中有超过一个的唯一索引。在这种情况下，REPLACE将考虑每一个唯一索引，并对 每一个索引对应的重复记录都删除，然后插入这条新记录。假设有一个table1表，有3个字段a, b, c。它们都有一个唯一索引。

CREATE TABLE table1(a INT NOT NULL UNIQUE,b INT NOT NULL UNIQUE,c INT NOT NULL UNIQUE);

假设table1中已经有了3条记录

a b c

1 1 1

2 2 2

3 3 3

下面我们使用REPLACE语句向table1中插入一条记录。

REPLACE INTO table1(a, b, c) VALUES(1,2,3);

返回的结果如下

Query OK, 4 rows affected (0.00 sec)

在table1中的记录如下

a b c

1 2 3

我们可以看到，REPLACE将原先的3条记录都删除了，然后将（1, 2, 3）插入。
    
    
      
来自:http://www.i5good.com/20121008127.html