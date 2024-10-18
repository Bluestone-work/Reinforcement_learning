![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241012222600.png)
这个公式在实际当中是不能用的，因为他涉及到了一个expection，这里面就涉及到了状态的分布，如果我们直到所有信息的话，其实这个分布我们是能确定下来的，但是很可惜，比如说环境的模型等等我们是不知道的，那么这时候我们是无法计算这个expectation的，所以我们要用随机的梯度来代替这个真实的梯度。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241012222821.png)
但是这个式子我们也是不能用的，因为这个式子涉及到了qπ，这个qπ是真实的action value。
所以我们要采取一个方法来近似的对qπ进行采样。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241012223026.png)
怎么来近似或者采样呢？
第一种方法是基于蒙特卡洛的方法。我要估计qπ（s，a）那我就从s出发采取a来得到一个episode。然后计算这个episode的return。
第二种方法是基于TD算法。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241012223626.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241012233218.png)
在采样S的时候，实际当中我们不会这么做（运行很久之后等他到达平稳状态再进行采样）。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241012233433.png)
在采样A的时候，理论上要求这个A是服从这个π的。那所以我在st应该根据当前的这个π采这个a，所以policy gradient在这里他是on-policy的算法。因为他的behavior policy就是π(θt)，然后target policy也是这个，因为他在不断改进，也有off-policy的情况，但是需要额外的技巧。

![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241012235908.png)
aβt相乘作为一个新的步长。这个式子其实是在优化π（at|st），就假设我有一个目标函数f（θ），希望能够使他maximized。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241013000038.png)
这个算法实际上是通过改变θ去优化π(at|st)的值。当aβt这个步长不是很大的时候：
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241013000349.png)
这个式子和θt，θt+1的值没有任何关系。他成立是因为微分，当θt＋1 - θt趋于0的时候这个不等式就近似变成等式。当θt+1和θt越来越大的时候，这种近似也会越来越不明确。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241013000606.png)
微分。
这也是RM思想的体现，回顾一下怎么收敛到不动点的，以及参数的更新会影响g(w)，联系起来，也就豁然开朗了。

![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241013000941.png)
如果这个action之前他的action value是比较大的，那么我会给他更大的概率去选择这个action，这也是在做exploitation，充分利用。
这个实际上是因为SGD需要a独立同分布，会反过来影响到策略

![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241013001241.png)
如果之前我选择at的概率是比较小的，那么我会在下个时刻给他更大的概率去选择它，这是在做exploration，探索。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241013001313.png)
所以这个βt通过分子和分母两项就很好的平衡了探索和利用。

#### 具体算法：
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241013001423.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241013001439.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241013001503.png)

伪代码：
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241013001516.png)
为什么最后的θt更新成θt+1时，他没有立刻去产生数据呢？
是因为这个方法是基于蒙特卡洛的方法，蒙特卡洛是off-line是离线的，也就是你必须把所有episode都采集完毕之后再更新。