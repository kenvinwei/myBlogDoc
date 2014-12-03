              
          
    现象：

    使用PHP的CURL相关函数进行POST，当要POST的参数内容长度超过1024时，将无法获得response的数据。

    即：


    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); 

    curl_setopt($ch, CURLOPT_POSTFIELDS, $data); 

当 strlen($data) > 1024 时，curl_exec函数将返回空字符串（或者错误 你请求得网址无法获取）。 
    

    解决：

    增加一个HTTP header
curl_setopt($ch, CURLOPT_HTTPHEADER, array(&#39;Expect:&#39;));     
    
      
来自:http://www.i5good.com/20140626166.html