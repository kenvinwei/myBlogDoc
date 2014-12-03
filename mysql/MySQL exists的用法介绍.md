              
          
    有一个查询如下：

    SELECT c.CustomerId, CompanyName FROM Customers c WHERE EXISTS(    SELECT OrderID     FROM Orders o     WHERE o.CustomerID     = cu.CustomerID)
      这里面的EXISTS是如何运作呢？子查询返回的是OrderId字段，可是外面的查询要找的是CustomerID和CompanyName字段，这两个字段肯定不在OrderID里面啊，这是如何匹配的呢？EXISTS用于检查子查询是否至少会返回一行数据，该子查询实际上并不返回任何数据，而是返回值True或False。EXISTS 指定一个子查询，检测行的存在。语法：EXISTS subquery。参数 subquery 是一个受限的 SELECT 语句 （不允许有 COMPUTE 子句和 INTO 关键字）。结果类型为 Boolean，如果子查询包含行，则返回 TRUE。  在子查询中使用 NULL 仍然返回结果集  这个例子在子查询中指定 NULL，并返回结果集，通过使用 EXISTS 仍取值为 TRUE。

    SELECT CategoryNameFROM CategoriesWHERE EXISTS (SELECT NULL)ORDER BY CategoryName ASC
    比较使用 EXISTS 和 IN 的查询

    这个例子比较了两个语义类似的查询。第一个查询使用 EXISTS 而第二个查询使用 IN。注意两个查询返回相同的信息。

    SELECT DISTINCT pub_nameFROM publishersWHERE EXISTS     (SELECT * FROM titles WHERE pub_id = publishers.pub_idAND type = 'business')
    SELECT distinct pub_nameFROM publishersWHERE pub_id IN    (SELECT pub_idFROM titlesWHERE type = 'business')
    比较使用 EXISTS 和 = ANY 的查询

    本示例显示查找与出版商住在同一城市中的作者的两种查询方法：第一种方法使用 = ANY，第二种方法使用 EXISTS。注意这两种方法返回相同的信息。

    SELECT au_lname, au_fnameFROM authorsWHERE exists(SELECT *FROM publishersWHERE authors.city = publishers.city)
    SELECT au_lname, au_fnameFROM authorsWHERE city = ANY(SELECT cityFROM publishers)
    比较使用 EXISTS 和 IN 的查询

    本示例所示查询查找由位于以字母 B 开头的城市中的任一出版商出版的书名：

    SELECT titleFROM titlesWHERE EXISTS(SELECT *FROM publishersWHERE pub_id = titles.pub_idAND city LIKE 'B%')
    SELECT titleFROM titlesWHERE pub_id IN(SELECT pub_idFROM publishersWHERE city LIKE 'B%')
    使用 NOT EXISTS

    NOT EXISTS 的作用与 EXISTS 正相反。如果子查询没有返回行，则满足 NOT EXISTS 中的 WHERE 子句。本示例查找不出版商业书籍的出版商的名称：

    SELECT pub_nameFROM publishersWHERE NOT EXISTS(SELECT *FROM titlesWHERE pub_id = publishers.pub_idAND type = 'business')ORDER BY pub_name
    又比如以下 SQL 语句：

    select distinct 姓名 from xswhere not exists (select * from kcwhere not exists (select * from xs_kcwhere 学号=xs.学号 and 课程号=kc.课程号)
    把最外层的查询xs里的数据一行一行的做里层的子查询。

    中间的 exists 语句只做出对上一层的返回 true 或 false，因为查询的条件都在 where 学号=xs.学号 and 课程号=kc.课程号这句话里。每一个 exists 都会有一行值。它只是告诉一层，最外层的查询条件在这里成立或都不成立，返回的时候值也一样回返回上去。直到最高层的时候如果是 true（真）就返回到结果集。为 false（假）丢弃。

    where not existsselect * from xs_kcwhere 学号=xs.学号 and 课程号=kc.课程号
    这个 exists 就是告诉上一层，这一行语句在我这里不成立。因为他不是最高层，所以还要继续向上返回。

    select distinct 姓名 from xswhere not exists （这里的 exists 语句收到上一个为 false 的值。他在判断一下，结果就是为 true（成立），由于是最高层所以就会把这行的结果（这里指的是查询条件）返回到结果集。

    几个重要的点：

    最里层要用到的醒询条件的表比如:xs.学号、kc.课程号等都要在前面的时候说明一下select * from kc,select distinct 姓名 from xs

    不要在太注意中间的exists语句.

    把exists和not exists嵌套时的返回值弄明白
    
    
      
来自:http://www.i5good.com/20121204146.html