              
          
    今天前端工程师写了一个批量注册事件，并获取下表的方法，其中用到了两给for循环，大致看了一下代码，觉得还可以有好一点的思路去优化，原来方法如下

    window.onload=function(){    var omain=document.getElementById('main');    var ospan=omain.getElementsByTagName('span');    var oimg=document.getElementById('img');    for (i=0;i<ospan.length;i++ )    {        ospan[i].onmouseover=go;        this.style.background='red';        ospan[i].onmouseout=function()        {            this.style.background='';        };    }    function go(){      for(i=0;i<ospan.length;i++){      if(ospan[i]==this){                   oimg.src='img/'+(i+1)+".jpg";                           }       }    }}
    

    我修改后如下：

    window.onload=function(){    var omain=document.getElementById('main');    var ospan=omain.getElementsByTagName('span');    var oimg=document.getElementById('img');    for (i=0;i<ospan.length;i++ )    {        ospan[i]["n"]=i;        ospan[i].onmouseover=function(){                            oimg.src='img/'+(this["n"]+1)+".jpg";            this.style.background='red';        };        ospan[i].onmouseout=function()        {            this.style.background='';        };    }}
    这样就省下一个for喽～～ 
    
    
      
来自:http://www.i5good.com/2012051198.html