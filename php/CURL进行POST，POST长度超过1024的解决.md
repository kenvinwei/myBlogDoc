              
          
    ����

    ʹ��PHP��CURL��غ�������POST����ҪPOST�Ĳ������ݳ��ȳ���1024ʱ�����޷����response�����ݡ�

    ����


    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); 

    curl_setopt($ch, CURLOPT_POSTFIELDS, $data); 

�� strlen($data) > 1024 ʱ��curl_exec���������ؿ��ַ��������ߴ��� ���������ַ�޷���ȡ���� 
    

    �����

    ����һ��HTTP header
curl_setopt($ch, CURLOPT_HTTPHEADER, array(&#39;Expect:&#39;));     
    
      
����:http://www.i5good.com/20140626166.html