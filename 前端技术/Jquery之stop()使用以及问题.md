              
          ����������Ŀ������һ�������˵������������ȥ��ʱ��Ͳ˵���ʾ��������뿪��ʱ��˵�����
����ҿ��ٲ��ϵؽ���������Ƴ��˵����������˵���������δ���ʱ��������Ƴ��˲˵����ͻ��������������&quot;�������ֹͣ�ƶ��󣬻��۵Ķ����������ִ�У�ֱ����������ִ����ϡ��������¶���Ч������궯����һ�¡�Ҫ���������ֻ��Ҫ�������Ƴ�����֮ǰ����stop()��������ǰ���������¸��������ɡ��������£�

    $(function(){      $(".menu li").hover(function(){          $(this).find(".submenu").show( 'fast');               }, function(){                        $(this).find(".submenu").hide( 'fast');                                   })      })
    ����赽��϶������������Ƴ�����֮ǰ����stop()��ֹͣ��ǰ���������£�

    $(function(){      $(".menu li").hover(function(){          $(this).find(".submenu").stop().show( 'fast');                }, function(){                        $(this).find(".submenu").hide( 'fast');                                   })      })
    Ч�������ã���Ϊstop()ֻ��ֹͣ�˵�ǰ��һ���Ķ�����Ȼ���ֽ����˵ڶ����Ķ�������ʱstop()�Ĳ������������ó������������û��ִ�еĶ������ж���յ���

    $(function(){      $(".menu li").hover(function(){          $(this).find(".submenu").stop(true��true).show( 'fast');               }, function(){                        $(this).find(".submenu").hide( 'fast');                                   })      })    
    
      
����:http://www.i5good.com/2012042392.html