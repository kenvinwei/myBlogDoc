              
          
    ��һ����ѯ���£�

    SELECT c.CustomerId, CompanyName FROM Customers c WHERE EXISTS(    SELECT OrderID     FROM Orders o     WHERE o.CustomerID     = cu.CustomerID)
      �������EXISTS����������أ��Ӳ�ѯ���ص���OrderId�ֶΣ���������Ĳ�ѯҪ�ҵ���CustomerID��CompanyName�ֶΣ��������ֶο϶�����OrderID���氡���������ƥ����أ�EXISTS���ڼ���Ӳ�ѯ�Ƿ����ٻ᷵��һ�����ݣ����Ӳ�ѯʵ���ϲ��������κ����ݣ����Ƿ���ֵTrue��False��EXISTS ָ��һ���Ӳ�ѯ������еĴ��ڡ��﷨��EXISTS subquery������ subquery ��һ�����޵� SELECT ��� ���������� COMPUTE �Ӿ�� INTO �ؼ��֣����������Ϊ Boolean������Ӳ�ѯ�����У��򷵻� TRUE��  ���Ӳ�ѯ��ʹ�� NULL ��Ȼ���ؽ����  ����������Ӳ�ѯ��ָ�� NULL�������ؽ������ͨ��ʹ�� EXISTS ��ȡֵΪ TRUE��

    SELECT CategoryNameFROM CategoriesWHERE EXISTS (SELECT NULL)ORDER BY CategoryName ASC
    �Ƚ�ʹ�� EXISTS �� IN �Ĳ�ѯ

    ������ӱȽ��������������ƵĲ�ѯ����һ����ѯʹ�� EXISTS ���ڶ�����ѯʹ�� IN��ע��������ѯ������ͬ����Ϣ��

    SELECT DISTINCT pub_nameFROM publishersWHERE EXISTS     (SELECT * FROM titles WHERE pub_id = publishers.pub_idAND type = 'business')
    SELECT distinct pub_nameFROM publishersWHERE pub_id IN    (SELECT pub_idFROM titlesWHERE type = 'business')
    �Ƚ�ʹ�� EXISTS �� = ANY �Ĳ�ѯ

    ��ʾ����ʾ�����������ס��ͬһ�����е����ߵ����ֲ�ѯ��������һ�ַ���ʹ�� = ANY���ڶ��ַ���ʹ�� EXISTS��ע�������ַ���������ͬ����Ϣ��

    SELECT au_lname, au_fnameFROM authorsWHERE exists(SELECT *FROM publishersWHERE authors.city = publishers.city)
    SELECT au_lname, au_fnameFROM authorsWHERE city = ANY(SELECT cityFROM publishers)
    �Ƚ�ʹ�� EXISTS �� IN �Ĳ�ѯ

    ��ʾ����ʾ��ѯ������λ������ĸ B ��ͷ�ĳ����е���һ�����̳����������

    SELECT titleFROM titlesWHERE EXISTS(SELECT *FROM publishersWHERE pub_id = titles.pub_idAND city LIKE 'B%')
    SELECT titleFROM titlesWHERE pub_id IN(SELECT pub_idFROM publishersWHERE city LIKE 'B%')
    ʹ�� NOT EXISTS

    NOT EXISTS �������� EXISTS ���෴������Ӳ�ѯû�з����У������� NOT EXISTS �е� WHERE �Ӿ䡣��ʾ�����Ҳ�������ҵ�鼮�ĳ����̵����ƣ�

    SELECT pub_nameFROM publishersWHERE NOT EXISTS(SELECT *FROM titlesWHERE pub_id = publishers.pub_idAND type = 'business')ORDER BY pub_name
    �ֱ������� SQL ��䣺

    select distinct ���� from xswhere not exists (select * from kcwhere not exists (select * from xs_kcwhere ѧ��=xs.ѧ�� and �γ̺�=kc.�γ̺�)
    �������Ĳ�ѯxs�������һ��һ�е��������Ӳ�ѯ��

    �м�� exists ���ֻ��������һ��ķ��� true �� false����Ϊ��ѯ���������� where ѧ��=xs.ѧ�� and �γ̺�=kc.�γ̺���仰�ÿһ�� exists ������һ��ֵ����ֻ�Ǹ���һ�㣬�����Ĳ�ѯ��������������򶼲����������ص�ʱ��ֵҲһ���ط�����ȥ��ֱ����߲��ʱ������� true���棩�ͷ��ص��������Ϊ false���٣�������

    where not existsselect * from xs_kcwhere ѧ��=xs.ѧ�� and �γ̺�=kc.�γ̺�
    ��� exists ���Ǹ�����һ�㣬��һ������������ﲻ��������Ϊ��������߲㣬���Ի�Ҫ�������Ϸ��ء�

    select distinct ���� from xswhere not exists ������� exists ����յ���һ��Ϊ false ��ֵ�������ж�һ�£��������Ϊ true������������������߲����Ծͻ�����еĽ��������ָ���ǲ�ѯ���������ص��������

    ������Ҫ�ĵ㣺

    �����Ҫ�õ�����ѯ�����ı����:xs.ѧ�š�kc.�γ̺ŵȶ�Ҫ��ǰ���ʱ��˵��һ��select * from kc,select distinct ���� from xs

    ��Ҫ��̫ע���м��exists���.

    ��exists��not existsǶ��ʱ�ķ���ֵŪ����
    
    
      
����:http://www.i5good.com/20121204146.html