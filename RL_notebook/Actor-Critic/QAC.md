actor-critic不是一个特别，完全不一样的方法。
他和我们上节课所学到的policy gradient的方法实际上是一种方法，但是他融入了基于value的方法，特别是value function approximation。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241013205741.png)

actor实际上是一个策略，他是用来更新策略的一个过程，他为什么会被称为actor呢？因为策略是用来take action采取行动的。
critic实际上是评论家或者批评家，在这里实际上是做policy evaluation的，也就是我有一个策略，我要去评估一下他到底好还是不好，那么怎么样去评估呢？实际上就是根据value estimation，去他的action value或者是state value。

#### 首先回顾一下policy gradient
policy gradient的基本思路是首先我们有一个目标函数。这个目标函数可以是vπbar也可以是rπbar。
有了这个目标函数我们就可以对其优化，用最简单的梯度上升法。
把这样一个包含expectation的算法转化成一个不含有expectation的方法。采样
通过如下的表达式我们就会知道哪些是actor，哪些是critic。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241013210141.png)
刚才这个qt怎么去计算呢？我们用第二种方法估计。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241013210229.png)

#### 代码
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241013210424.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241013210523.png)
这个算法本身就具有一定探索能力，我们就不需要把他转成greed这种形式了。![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241013210638.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241013210704.png)
