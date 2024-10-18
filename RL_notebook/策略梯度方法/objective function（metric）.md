首先我们在读书，或是读论文的时候，我们经常会遇到两大类的metric
#### 1.average state value
它实际上就是state value 的一个加权平均，并且权重之和=1，d(s)也可以理解为，状态s被选中的概率。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241012202655.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241012202737.png)
那么我们怎么去选择这个d(s)呢？
	一、第一种情况是这个d是独立于π的。这种情况比较简单一点，因为后面求他的梯度的时候，这个d就不涉及任何梯度，所以我们只用求一个Vπ的梯度，如果d和π有关，那我求梯度的时候当然也要求这个d关于这个π的梯度。
	虽然说这个d和π没有关系，但我们要怎么选择这个d呢？
	1.均匀分布![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241012203209.png)
	2.我可能非常关心某个s，对某些状态有偏好
	![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241012203251.png)
	这种情况下，Vπbar也就变成了VπS0，我去最大化这个Vπbar其实也就是最大化我从s0出发，我最大能得到多少return。
	二、第二种情况d和π有关系：这个是一种非常常见的选择。这时候选择d为dπ，这时候dπ是叫stationary distribution。dπ他是依赖于π的一个distribution。
	![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241012203736.png)
	如果我们根据某一个策略来执行，肯定有的状态会访问多一点，有的会少一点，访问多的状态对应的状态概率dπs实际上会大一点，相对来说给他的权重会大一点。
#### 2.average reward或average one-step reward
从Vπ(S)变成Rπ(S),后者是从s出发得到的单步的，就是immediate reward的一个平均值。dπ(s)是s所对应的权重，它实际上是stationary distribution，他是依赖于这个策略π的，然后我把rπ(s)做一个加权平均。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241012210348.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241012210357.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241012210520.png)
当你跑了无穷多步之后，你最开始是从哪开始的就已经不重要了
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241012210634.png)
圈起来的式子在论文当中是经常看到的。这个式子就是Rπbar。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241012210723.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241012210906.png)

#### Basic idea：
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241012211252.png)
我们所说的这个mertic，如果我们深挖的话，还是会有比较麻烦的，他分两种情况，第一种是discounted case ，存在一个discounted rate γ，他是<1的一个数，还有一个undiscounted case，他是γ = 1的。到目前位置，我们只见过discounted case，为什么会出现undiscounted case？就是因为rπbar，这个metric它是对immediate reward他求一个平均。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241012211918.png)
Rπbar，Vπbar都是metric，那么他俩之间有什么关系呢？
实际上，这两个metric是等价的。这里的等价并不是说他们是相等的，而是说他们满足如下等式![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241012213614.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241012213835.png)

![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241012214039.png)
d(S)是加权的权重，可以取平均也可以取stationary distribution，不管是哪种都是求期望。
