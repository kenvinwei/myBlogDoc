              
          
    javascript��ִ��onmouserover����onmouseout��ʱ���ӱ�ǩ��ִ�и���ǩʱ�䣬�����Ͳ�����ʱ��ð�ݣ�����ľ���onmouserover��onmouserout

    ����������

    <div id="test1" onmuseout="leaveparent(e,this)">    <div id="test1">test1<div>    <div id="test2">test2<div></div>
    ��ִ��leaveparentʱ���ʱ�����test1�Ƶ�test2Ҳ��ִ��leaveparent����������������������ǲ���Ҫ�ģ��������˺ö���������������

    onmouseleave�ȵȣ����Ǵ��ڼ������⣬����ҵ����·�����

    function isMouseLeaveOrEnter(e, handler) {if (e.type != 'mouseout' &;&; e.type != 'mouseover') return false;var reltg = e.relatedTarget ? e.relatedTarget : e.type == 'mouseout' ? e.toElement : e.fromElement;while (reltg &;&; reltg != handler)reltg = reltg.parentNode;return (reltg != handler);}
    Ȼ�����жϣ�

    function leaveparent(a,b){    if(isMouseLeaveOrEnter(a,b)){        //code here    }}
    Ȼ����Ը㶨~~
    
    
      
����:http://www.i5good.com/2012022074.html