无论是AC还是A2C他们都是on-policy的，如果之前有一些经验了，我们想用这些经验怎么办呢？
这要用到一个技术 importance sampling 重要性采样。来吧一个on-policy的算法，转化整一个off-policy 的算法。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241014141824.png)

首先考虑一个极端的例子，一个随机变量的集合只有两个元素{+1 ， -1}。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241014141940.png)

我们可以使用两种情况
一：
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241014142059.png)
二：
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241014143317.png)
问题就是我们有一个概率分布p1，我们在这个概率分布下产生了一些sample，想利用这些sample来估计在p0下的expectation。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241014143447.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241014143515.png)
我们要求的就是
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241014143631.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241014143759.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241014143818.png)

如果P0(xi)>P1(xi)说明我在P0概率分布下采到xi的概率是比较大的，在P1概率分布下采样到的概率是比较小的，所以这个权重大于1的话，就是想让他有比较大的概率被采样到，因为我们后面算的是
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241014144213.png)

![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241014144257.png)

![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241014144351.png)
因为我们有可能找不到p0的表达式，比如说神经网络。![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241014144420.png)

### 总结：
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241014144623.png)

![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241014144745.png)
dβ(s)是在策略β下的一个stationary distribution，Vπ（s）是在策略π下所对应的state value。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241014144907.png)
这里面仍然可以加上一个baseline，不改变他的梯度。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241014150527.png)

### 伪代码
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241014150700.png)
