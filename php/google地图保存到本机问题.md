              
          
    ���һֱ�ڿ��� ����ƻ�,�����ڴ���google��ͼ��ʱ�������һ�����������

    ����google��ͼ��̫�ȶ������Բ�Ʒ�Ǳ���Ҫ��ѡ��õĵ�ͼ������һ��ͼƬ�������ڷ������ϣ����˿�google��ͼ��apiҲû�����з����Ǳ����ڱ����ġ�

    ���ԣ��ҳ��������Լ��� �߼���������Ҫ��һ�����ļ���Ȼ���ȡgoogle��ͼͼƬ�Ķ������ļ���Ȼ�������ļ�д��������ļ����б��档

    ������һ�¾�����룺

    /**     * ��ȡԶ�̷�����HTTP״̬     *     * @param unknown_type $url     * @return string     */    function GetHttpStatusCode($url){              $curl = curl_init();             curl_setopt($curl,CURLOPT_URL,$url);//��ȡ����url              curl_setopt($curl,CURLOPT_HEADER,1);//��ȡhttpͷ��Ϣ              curl_setopt($curl,CURLOPT_NOBODY,1);//������html��body��Ϣ              curl_setopt($curl,CURLOPT_RETURNTRANSFER,1);//��������������ֱ�����              curl_setopt($curl,CURLOPT_TIMEOUT,5); //��ʱʱ������λ��              curl_exec($curl);             $rtn= curl_getinfo($curl,CURLINFO_HTTP_CODE);             curl_close($curl);             return  $rtn;    }
    google��ͼ���ȶ���Ҫ���жϵ�ͼ�ǲ��ǿ����������ʣ���Ȼ�����һֱ����google��ͼ�����³���һֱ���� CPU�������ء�

    /**     * ����Google��ͼ     *     */    function DownMap($url,$path){        $http_status = $this->GetHttpStatusCode($url);        if($http_status==200){            $content = file_get_contents($url);            if(is_file($path)){                unlink($path);            }            $map = fopen($path,'w+');            fwrite($map,$content);            fclose($map);            return true;        }        return false;    }
    ���ûɶ���͵ġ���

    function mydowntest(){        $this->DownMap("http://maps.google.com/maps/api/staticmap?center=39.94083345849863,116.43591500000004&;zoom=16&;size=520x340&;maptype=roadmap&;markers=39.94038925940741,116.43467045501711&;sensor=false","/usr/data0/wwwroot/news.tiger/release/map.jpg");    }
    �򵥵�д�����ԣ�

    ���⣺

    ���ɵ�ͼƬ��Ȼ�е����ı�Ӣ���ˣ�

    ��������ͼƬ��

     

    ��лͬ�°�æ������˴����⣬google����������ʣ����Զ��ж����ԣ�������phpץȡû��ָ��ģ������������ԣ�google�Զ�����Ӣ�ģ�����������ץȡgoogle��ͼ��ʱ���ֶ�ָ�����ԣ�language=zh-cn��

    function mydowntest(){        $this->DownMap("http://maps.google.com/maps/api/staticmap?center=39.94083345849863,116.43591500000004&;zoom=16&;size=520x340&;maptype=roadmap&;markers=39.94038925940741,116.43467045501711&;sensor=false&;language=zh-cn","/usr/data0/wwwroot/news.tiger/release/map.jpg");    }
    ���ɣ�
    
    
      
����:http://www.i5good.com/2012042593.html