              
          
    1��const�������Ա�������壬һ�������Ҳ��ܸı���ֵ��define����ȫ�ֳ��������κεط������Է��ʡ�2��define���������ж����const���ԡ�3��const��������������ж��峣��if (...) {   const FOO = &#39;BAR&#39;;  // invalid } but if (...) {   define(&#39;FOO&#39;, &#39;BAR&#39;); // valid } 4��const����һ����ͨ�ĳ������ƣ�define���Բ��ñ��ʽ��Ϊ���ơ�const FOO = &#39;BAR&#39;; for ($i = 0; $i < 32; ++$i) {   define(&#39;BIT_&#39; . $i, 1 << $i); } 5��constֻ�ܽ��ܾ�̬�ı�������define���Բ����κα��ʽ��const BIT_5 = 1 << 5;  // invalid but define(&#39;BIT_5&#39;, 1 << 5); // valid 6��const ���Ǵ�Сд���У�Ȼ��define()����ͨ�������������������Сд�����еĳ���define(&#39;FOO&#39;, &#39;BAR&#39;, true); echo FOO; // BAR echo foo; // BAR �ܽ᣺ʹ��const���׶�����������һ�����Խṹ����define��һ����������const�����ڱ���ʱ��define��ܶࡣ
    
    
      
����:http://www.i5good.com/20121112137.html