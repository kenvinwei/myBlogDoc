              
          
    ����ǰ�˹���ʦд��һ������ע���¼�������ȡ�±�ķ����������õ�������forѭ�������¿���һ�´��룬���û������к�һ���˼·ȥ�Ż���ԭ����������

    window.onload=function(){    var omain=document.getElementById('main');    var ospan=omain.getElementsByTagName('span');    var oimg=document.getElementById('img');    for (i=0;i<ospan.length;i++ )    {        ospan[i].onmouseover=go;        this.style.background='red';        ospan[i].onmouseout=function()        {            this.style.background='';        };    }    function go(){      for(i=0;i<ospan.length;i++){      if(ospan[i]==this){                   oimg.src='img/'+(i+1)+".jpg";                           }       }    }}
    

    ���޸ĺ����£�

    window.onload=function(){    var omain=document.getElementById('main');    var ospan=omain.getElementsByTagName('span');    var oimg=document.getElementById('img');    for (i=0;i<ospan.length;i++ )    {        ospan[i]["n"]=i;        ospan[i].onmouseover=function(){                            oimg.src='img/'+(this["n"]+1)+".jpg";            this.style.background='red';        };        ospan[i].onmouseout=function()        {            this.style.background='';        };    }}
    ������ʡ��һ��forඡ��� 
    
    
      
����:http://www.i5good.com/2012051198.html