              
          这是我在项目里做的一个下拉菜单，当鼠标移上去的时候就菜单显示，当鼠标离开的时候菜单隐藏
如果我快速不断地将鼠标移入移出菜单（即，当菜单下拉动画未完成时，鼠标又移出了菜单）就会产生“动画积累&quot;，当鼠标停止移动后，积累的动画还会持续执行，直到动画序列执行完毕。这样导致动画效果与鼠标动作不一致。要解决此问题只需要在移入移出动画之前加入stop()，结束当前动画进入下个动画即可。代码如下：

    $(function(){      $(".menu li").hover(function(){          $(this).find(".submenu").show( 'fast');               }, function(){                        $(this).find(".submenu").hide( 'fast');                                   })      })
    如果需到组合动画，在移入移出动画之前加入stop()来停止当前动画，如下：

    $(function(){      $(".menu li").hover(function(){          $(this).find(".submenu").stop().show( 'fast');                }, function(){                        $(this).find(".submenu").hide( 'fast');                                   })      })
    效果并不好，因为stop()只是停止了当前第一步的动画，然后又进入了第二步的动画。此时stop()的参数就派上了用场，它会把下面没有执行的动画序列都清空掉。

    $(function(){      $(".menu li").hover(function(){          $(this).find(".submenu").stop(true，true).show( 'fast');               }, function(){                        $(this).find(".submenu").hide( 'fast');                                   })      })    
    
      
来自:http://www.i5good.com/2012042392.html