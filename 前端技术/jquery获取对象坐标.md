              
          最近在写轮播效果，显示层下本身就有另外一个层absolute，如果在放一个absolute那么第一个层在做超出隐藏就会失败，改了大量的css都失败了，最后还是把最后一个absolute的层放到 body节点中处理，然后用绝对定位 left和top去在对应节点上弹出层，但是在不同电脑分辨率下 left和top位置不同，为了解决这个问题，还是用jquery做了处理，jquery获取对象坐标的方法：获取某一元素的绝对X,Y坐标，可以用offset()方法：var X = $('#DivID').offset().top;var Y = $('#DivID').offset().left;获取相对(父元素)位置:var X = $('#DivID').position().top;var Y = $('#DivID').position().left;效果地址：http://www.winesino.com/index.php/Book 观察鼠标移到轮播图上，调整分辨率，不会受到影响了！     
    
      
来自:http://www.i5good.com/2011123140.html