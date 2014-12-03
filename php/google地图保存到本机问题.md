              
          
    最近一直在开发 逸香酒会,今天在处理google地图的时候出现了一个神奇的现象。

    由于google地图不太稳定，所以产品那边需要把选择好的地图，生成一张图片，保存在服务器上，看了看google地图的api也没看到有方法是保存在本机的。

    所以，我初步想用自己的 逻辑处理，首先要建一个空文件，然后读取google地图图片的二进制文件，然后把这个文件写到这个空文件进行保存。

    下面贴一下具体代码：

    /**     * 获取远程服务器HTTP状态     *     * @param unknown_type $url     * @return string     */    function GetHttpStatusCode($url){              $curl = curl_init();             curl_setopt($curl,CURLOPT_URL,$url);//获取内容url              curl_setopt($curl,CURLOPT_HEADER,1);//获取http头信息              curl_setopt($curl,CURLOPT_NOBODY,1);//不返回html的body信息              curl_setopt($curl,CURLOPT_RETURNTRANSFER,1);//返回数据流，不直接输出              curl_setopt($curl,CURLOPT_TIMEOUT,5); //超时时长，单位秒              curl_exec($curl);             $rtn= curl_getinfo($curl,CURLINFO_HTTP_CODE);             curl_close($curl);             return  $rtn;    }
    google地图不稳定，要先判断地图是不是可以正常访问，不然程序会一直下载google地图，导致程序一直处理， CPU负载严重～

    /**     * 下载Google地图     *     */    function DownMap($url,$path){        $http_status = $this->GetHttpStatusCode($url);        if($http_status==200){            $content = file_get_contents($url);            if(is_file($path)){                unlink($path);            }            $map = fopen($path,'w+');            fwrite($map,$content);            fclose($map);            return true;        }        return false;    }
    这个没啥解释的～～

    function mydowntest(){        $this->DownMap("http://maps.google.com/maps/api/staticmap?center=39.94083345849863,116.43591500000004&;zoom=16&;size=520x340&;maptype=roadmap&;markers=39.94038925940741,116.43467045501711&;sensor=false","/usr/data0/wwwroot/news.tiger/release/map.jpg");    }
    简单的写给测试！

    问题：

    生成的图片居然有的中文变英文了！

    生成如下图片：

     

    感谢同事帮忙，解决了此问题，google用浏览器访问，会自动判断语言，由于用php抓取没有指定模拟浏览器的语言，google自动加载英文，所以我们在抓取google地图的时候手动指定语言：language=zh-cn。

    function mydowntest(){        $this->DownMap("http://maps.google.com/maps/api/staticmap?center=39.94083345849863,116.43591500000004&;zoom=16&;size=520x340&;maptype=roadmap&;markers=39.94038925940741,116.43467045501711&;sensor=false&;language=zh-cn","/usr/data0/wwwroot/news.tiger/release/map.jpg");    }
    即可！
    
    
      
来自:http://www.i5good.com/2012042593.html