              
          
     reload�������÷���ǿ�������ˢ�µ�ǰҳ�档�﷨��location.reload([bForceGet])

    ������bForceGet����ѡ������Ĭ��Ϊfalse���ӿͻ��˻�����ȡ��ǰҳ��

    true����GET��ʽ���ӷ����ȡ���µ�ҳ��,�൱�ڿͻ��˵��F5(&quot;ˢ��&quot;)��

    ��ôҪˢ�µ�ǰ��ǰһ��ҳ��������أ�

    history.go(-1)����history.back()??

    ��������������ˢ����ʷҳ�棬ֻ�ܻ��˻���һ��ҳ�棬����û��ˢ�£�����ô���ܼ��ܻ��˻���ʷҳ�棬Ȼ�����������ˢ�����ҳ���أ�

    replace�������÷���ͨ��ָ��URL�滻��ǰ��������ʷ��ͻ��ˣ�����Ŀ����˵�ʹ��replace����֮���㲻��ͨ����ǰ�����͡����ˡ��������Ѿ����滻��URL���﷨��location.replace(URL);

    ��ʵ��Ӧ�õ�ʱ������ˢ��ҳ���ʱ������ͨ��ʹ�ã�location.reload()������history.go(0)��������Ϊ�������������ǿͻ��˵�F5ˢ��ҳ�棬����ҳ���method=&quot;post&quot;��ʱ�򣬻����&quot;��ҳ����&quot;����ʾ��������ΪSession�İ�ȫ�������ơ������뵽��������location.reload()������ʱ��phpҳ���ʱ�ڷ�����ڴ����Ѿ����ڡ����������Ӧ�ã�������Ҫ���¼��ظ�ҳ�棬Ҳ����˵��������ҳ���ܹ��ڷ�������±�����������������NotIsPostback�ġ����location.replace()�Ϳ�����ɴ����񡣱�replace��ҳ��ÿ�ζ��ڷ�����������ɡ�

    �������ôд��location.replace(location.href);

     ���ز�ˢ��ҳ�棺

    location.replace(document.referrer);

    document.referrer//ǰһ��ҳ���URL

    ��Ҫ��history.go(-1)����history.back();�����ز�ˢ��ҳ�棬�����ַ�������ˢ��ҳ�档

    javascriptˢ��ҳ��ļ��ַ����ܽ᣺1history.go(0)2location.reload()3location=location4location.assign(location)5document.execCommand(&#39;Refresh&#39;)6window.navigate(location)7location.replace(location)8document.URL=location.href
    
    
      
����:http://www.i5good.com/20120529104.html