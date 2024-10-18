
SGD算法想要解决的是，我有一个目标函数j这个目标函数是关于w的一个函数，这个w可以是一个参数或是一个变量，总而言之我要优化这个w使他的值达到最小![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007223348.png)
这和expectation实际上就是对X进行求的，所以我们的目标就是要找到最优的w使得这个目标函数能够达到最小。
求解这个问题实际上有多种方法。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007224021.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007224105.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007224203.png)


#### 举例使用
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007224355.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007225001.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007225233.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007225931.png)

#### 收敛性
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007230242.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007231943.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007232742.png)

SGD是吧过程中的true gradient用stochastic gradient来代替，但是sg是有随机性的，会不会造成sgd的收敛他的随机性也是比较大的，幸好他没有这个性质。
首先用![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007234359.png)
这个式子来定义true gradient和stochastic gradient之间的相对误差。这里面我假设所有的权都是标量。
	接下来我们会得到一个很有意思的结论，当wk离wstar非常远的时候实际上SGD所呈现的行为和GD是非常类似的，因为这个relative error是比较小的。
	当wk和wstar比较近的时候，在他附近的时候这时候SGD才会呈现出来比较大的随机性。这个是一种比较良好的性质。

![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241008001339.png)
首先我们注意到这个w是最优解，那这个expectation他的gradient expectation等于0，既然他是0那么我把它加到分母上就不会发生任何事。再用上中值定理，可证结论。
为什么要用上中值定理，因为我们想让wk - wstar这样的项出现。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241008001557.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241008001642.png)

#### 例子
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241008001853.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241008002021.png)

![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241008002307.png)
在之前的SGD公式中，他是涉及到随机变量和期望的。
但是我们在学习SGD的时候，一定会遇到另外一个problem formulation，其中是不包含任何的random variables。
这时候求解这个问题的gradient decent的方法肯定是可以得到的。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241008002411.png)
在实际当中有可能这样的一个xi的集合是比较大的。每次只能从这个集合之中拿到一个xi，那么这时候我们可以这样执行这个算法
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241008002509.png)
把前面这个求平均的直接用xk来代替，所以这个算法看起来是和SGD非常类似的，但是这个是不是SGD呢？
因为在这个描述中，没有涉及到任何的random variable。
另一个问题，我们应该怎样从xi这个集合中取数呢？
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241008002708.png)
首先我们回答这个问题的思路就是手动的去引入一个random variable，让刚才那个不涉及随机变量的问题，变成一个涉及随机变量的问题。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241008003204.png)
首先我们引入一个随机变量X，X是定义在随机变量xi上的，设这个xi取这个随机变量中的任何一个数的概率为1/n。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241008003223.png)
求解这个问题的算法就是SGD算法。
我们应该从集合中随机抽取。有可能有的数是被多次取到的。