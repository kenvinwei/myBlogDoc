              
          
    ����PHP�Ĺ������ƣ�����û��һ��daemon�̣߳�����ʱ��ɨ��session��Ϣ���ж����Ƿ�ʧЧ����һ����Ч������ʱ��PHP�����ȫ�ֱ��� session.gc_probability/session.gc_divisor��ͬ������ͨ��php.ini����ini_set()�������޸ģ� ��ֵ���������Ƿ�����һ��GC��Garbage Collector����Ĭ������£�session.gc_probability �� 1��session.gc_divisor ��100��Ҳ����˵��1%�Ŀ����Ի�����GC��

    GC�Ĺ���������ɨ�����е�session��Ϣ�� �õ�ǰʱ���ȥsession������޸�ʱ�䣨modified date����ͬsession.gc_maxlifetime�������бȽϣ��������ʱ���Ѿ�����gc_maxlifetime���ͰѸ�sessionɾ ����

    ��Ϊʲô�ᷢ��gc_maxlifetime��Ч������أ�

    ��Ĭ������£�session��Ϣ�����ı��ļ�����ʽ����������ϵͳ ����ʱ�ļ�Ŀ¼�С���Linux�£���һ·��ͨ��Ϊtmp����Windows��ͨ��ΪC:WindowsTemp�������������ж��PHPӦ��ʱ�� ���ǻ���Լ���session�ļ���������ͬһ��Ŀ¼�С�ͬ���أ���ЩPHPӦ��Ҳ�ᰴһ����������GC��ɨ�����е�session�ļ���

    �� �����ڣ�GC�ڹ���ʱ�����������ֲ�ͬվ���session��������֮��վ��A��gc_maxlifetime����Ϊ2Сʱ��վ��B�� gc_maxlifetime����ΪĬ�ϵ�24���ӡ���վ��B��GC����ʱ������ɨ�蹫�õ���ʱ�ļ�Ŀ¼�������г���24���ӵ�session�ļ�ȫ��ɾ ����������������������վ��A��B��������վ��A��gc_maxlifetime���þ���ͬ�����ˡ�

    �ҵ��������ڣ���������ͺܼ��ˡ��޸�session.save_path����������ʹ��session_save_path()�������ѱ���session��Ŀ¼ָ��һ��ר�õ�Ŀ¼��gc_maxlifetime�������������ˡ�
����һ��������ǣ�gc_maxlifetimeֻ�ܱ�֤session��������ʱ�䣬�����ܹ������ڳ�����һʱ��֮��session��Ϣ������õ� ɾ������ΪGC�ǰ����������ģ�������ĳһ����ʱ���ڶ�û�б���������ô������session�ڳ���gc_maxlifetime�Ժ���Ȼ����Ч������� �������һ�������ǣ���session.gc_probability/session.gc_divisor�Ļ�����ߣ�����ᵽ100%���ͻ᳹�׽� ��������⣬����Ȼ�������������ص�Ӱ�졣��һ���������Լ��ڴ������жϵ�ǰsession������ʱ�䣬���������gc_maxlifetime������ �յ�ǰsession��    
    
      
����:http://www.i5good.com/20140414160.html