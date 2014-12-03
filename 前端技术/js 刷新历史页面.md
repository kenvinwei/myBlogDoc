              
          
     reload方法，该方法强迫浏览器刷新当前页面。语法：location.reload([bForceGet])

    参数：bForceGet，可选参数，默认为false，从客户端缓存里取当前页。

    true则以GET方式，从服务端取最新的页面,相当于客户端点击F5(&quot;刷新&quot;)；

    那么要刷新当前的前一个页面如何做呢？

    history.go(-1)或者history.back()??

    这样的做法不能刷新历史页面，只能回退回上一个页面，但是没有刷新，那怎么才能既能回退回历史页面，然后再让浏览器刷新这个页面呢？

    replace方法，该方法通过指定URL替换当前缓存在历史里（客户端）的项目，因此当使用replace方法之后，你不能通过“前进”和“后退”来访问已经被替换的URL。语法：location.replace(URL);

    在实际应用的时候，重新刷新页面的时候，我们通常使用：location.reload()或者是history.go(0)来做。因为这种做法就像是客户端点F5刷新页面，所以页面的method=&quot;post&quot;的时候，会出现&quot;网页过期&quot;的提示。那是因为Session的安全保护机制。可以想到：当调用location.reload()方法的时候，php页面此时在服务端内存里已经存在。如果有这种应用：我们需要重新加载该页面，也就是说我们期望页面能够在服务端重新被创建，我们期望是NotIsPostback的。这里，location.replace()就可以完成此任务。被replace的页面每次都在服务端重新生成。

    你可以这么写：location.replace(location.href);

     返回并刷新页面：

    location.replace(document.referrer);

    document.referrer//前一个页面的URL

    不要用history.go(-1)，或history.back();来返回并刷新页面，这两种方法不会刷新页面。

    javascript刷新页面的几种方法总结：1history.go(0)2location.reload()3location=location4location.assign(location)5document.execCommand(&#39;Refresh&#39;)6window.navigate(location)7location.replace(location)8document.URL=location.href
    
    
      
来自:http://www.i5good.com/20120529104.html