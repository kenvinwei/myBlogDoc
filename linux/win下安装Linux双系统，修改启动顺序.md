              
          
    一直是双系统，物理机上安装了win7，然后又删掉一块磁盘，用于安装centos6.2，启动的时候总是先启动centos6.2,然而用于玩的时间总是比学习的时间长，所以总是在开启的时候守候电脑，选择启动那个系统，嗯，很恼火，有时候打个电话，或者打个水，顺便启动电脑，回来本来想玩玩，然后发现启动的是linux,唉，废话少说了，记录一下修改启动项：

    首先找到centos6.2的引导文件：

    /boot/grub/grub.conf
    然后查看启动项：

    # grub.conf generated by anaconda## Note that you do not have to rerun grub after making changes to this file# NOTICE:  You have a /boot partition.  This means that#          all kernel and initrd paths are relative to /boot/, eg.#          root (hd0,2)#          kernel /vmlinuz-version ro root=/dev/mapper/vg_livecd-lv_root#          initrd /initrd-[generic-]version.img                                                                                             #boot=/dev/sdadefault=0timeout=5splashimage=(hd0,2)/grub/splash.xpm.gzhiddenmenutitle CentOS (2.6.32-220.7.1.el6.x86_64)    root (hd0,2)    kernel /vmlinuz-2.6.32-220.7.1.el6.x86_64 ro root=/dev/mapper/vg_livecd-lv_root rd_NO_LUKS rd_LVM_LV=vg_livecd/lv_swap rd_NO_MD quiet rd_LVM_LV=vg_livecd/lv_root rhgb crashkernel=auto LANG=zh_CN.UTF-8  KEYBOARDTYPE=pc KEYTABLE=us rd_NO_DM    initrd /initramfs-2.6.32-220.7.1.el6.x86_64.imgtitle CentOS (2.6.32-220.4.2.el6.x86_64)#   root (hd0,2)#   kernel /vmlinuz-2.6.32-220.4.2.el6.x86_64 ro root=/dev/mapper/vg_livecd-lv_root rd_NO_LUKS rd_LVM_LV=vg_livecd/lv_swap rd_NO_MD quiet rd_LVM_LV=vg_livecd/lv_root rhgb crashkernel=auto LANG=zh_CN.UTF-8  KEYBOARDTYPE=pc KEYTABLE=us rd_NO_DM#   initrd /initramfs-2.6.32-220.4.2.el6.x86_64.img#title CentOS (2.6.32-220.el6.x86_64)#   root (hd0,2)#   kernel /vmlinuz-2.6.32-220.el6.x86_64 ro root=/dev/mapper/vg_livecd-lv_root rd_NO_LUKS rd_LVM_LV=vg_livecd/lv_swap rd_NO_MD quiet rd_LVM_LV=vg_livecd/lv_root rhgb crashkernel=auto LANG=zh_CN.UTF-8  KEYBOARDTYPE=pc KEYTABLE=us rd_NO_DM#   initrd /initramfs-2.6.32-220.el6.x86_64.imgtitle Other    rootnoverify (hd0,0)    chainloader +1
    注释：

    default=0#默认开机，预设第一个title项目

    timeout=5#停留五秒，末动键盘选择黙认
splashimage=(hd0,2)/grub/splash.xpm.gz#背景图示所在档案

    hiddenmenu#预设隐藏完整的开机菜单

    root(hd0,0)#核心档案的分区

    所以，如果改成默认启动win7，只需要把default修改成1即可：

    # grub.conf generated by anaconda## Note that you do not have to rerun grub after making changes to this file# NOTICE:  You have a /boot partition.  This means that#          all kernel and initrd paths are relative to /boot/, eg.#          root (hd0,2)#          kernel /vmlinuz-version ro root=/dev/mapper/vg_livecd-lv_root#          initrd /initrd-[generic-]version.img#boot=/dev/sda                                                                                                                              default=1timeout=5splashimage=(hd0,2)/grub/splash.xpm.gzhiddenmenutitle CentOS (2.6.32-220.7.1.el6.x86_64)    root (hd0,2)    kernel /vmlinuz-2.6.32-220.7.1.el6.x86_64 ro root=/dev/mapper/vg_livecd-lv_root rd_NO_LUKS rd_LVM_LV=vg_livecd/lv_swap rd_NO_MD quiet rd_LVM_LV=vg_livecd/lv_root rhgb crashkernel=auto LANG=zh_CN.UTF-8  KEYBOARDTYPE=pc KEYTABLE=us rd_NO_DM    initrd /initramfs-2.6.32-220.7.1.el6.x86_64.imgtitle CentOS (2.6.32-220.4.2.el6.x86_64)#   root (hd0,2)#   kernel /vmlinuz-2.6.32-220.4.2.el6.x86_64 ro root=/dev/mapper/vg_livecd-lv_root rd_NO_LUKS rd_LVM_LV=vg_livecd/lv_swap rd_NO_MD quiet rd_LVM_LV=vg_livecd/lv_root rhgb crashkernel=auto LANG=zh_CN.UTF-8  KEYBOARDTYPE=pc KEYTABLE=us rd_NO_DM#   initrd /initramfs-2.6.32-220.4.2.el6.x86_64.img#title CentOS (2.6.32-220.el6.x86_64)#   root (hd0,2)#   kernel /vmlinuz-2.6.32-220.el6.x86_64 ro root=/dev/mapper/vg_livecd-lv_root rd_NO_LUKS rd_LVM_LV=vg_livecd/lv_swap rd_NO_MD quiet rd_LVM_LV=vg_livecd/lv_root rhgb crashkernel=auto LANG=zh_CN.UTF-8  KEYBOARDTYPE=pc KEYTABLE=us rd_NO_DM#   initrd /initramfs-2.6.32-220.el6.x86_64.imgtitle Other    rootnoverify (hd0,0)    chainloader +1
    很简单把！soeasy!!!
    
    
      
来自:http://www.i5good.com/2012050495.html