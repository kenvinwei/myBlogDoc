              
          
    对于像我这些没有独立域名的主机，用mail默认是不能给外部邮箱如163、sina等发送邮件的。但是我们可以通过修改mail配置文件做到这点。设置方法如下（这里以163为例）：打开/etc/nail.rc (/etc/mail.rc)，添加以下两行：set from=user@163.com smtp=smtp.163.comset smtp-auth-user=user smtp-auth-password=passwd smtp-auth=login其中user为网易邮箱用户名，passwd为你的邮箱密码。设置之后就可以给外部邮箱发送邮件了，可以测试一下：mail -s &quot;Hello&quot; user@sina.com </dev/null如果配置正确的话，user@sina.com这个邮箱就可以收到邮件，当然只有标题，没有正文，因为这里我们已经指定正文为空（/dev/null）。

    指定文件：

    mail -s &quot;Hello&quot; user@sina.com < files

    测试：

    成功发送到QQ邮箱！
    
    
      
来自:http://www.i5good.com/20130115157.html