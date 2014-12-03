              
          
    javascript在执行onmouserover或者onmouseout的时候，子标签会执行父标签时间，这样就产生了时间冒泡，最常见的就是onmouserover和onmouserout

    比如我们在

    <div id="test1" onmuseout="leaveparent(e,this)">    <div id="test1">test1<div>    <div id="test2">test2<div></div>
    在执行leaveparent时间的时候，鼠标test1移到test2也会执行leaveparent方法，所以这种情况是我们不想要的，网上找了好多解决方法，包括：

    onmouseleave等等，可是存在兼容问题，最后找到如下方法：

    function isMouseLeaveOrEnter(e, handler) {if (e.type != 'mouseout' &;&; e.type != 'mouseover') return false;var reltg = e.relatedTarget ? e.relatedTarget : e.type == 'mouseout' ? e.toElement : e.fromElement;while (reltg &;&; reltg != handler)reltg = reltg.parentNode;return (reltg != handler);}
    然后做判断：

    function leaveparent(a,b){    if(isMouseLeaveOrEnter(a,b)){        //code here    }}
    然后测试搞定~~
    
    
      
来自:http://www.i5good.com/2012022074.html