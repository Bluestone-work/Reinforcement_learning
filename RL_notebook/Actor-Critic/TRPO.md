之前的思路都是算出每一个state的V value，或者每个state，action pair的Qvalue，然后通过Vvalue或者Qvalue的最佳路径得到一个policyπ。

但是上述的Optimization很多时候非常困难，因为action和state都是离散的，导致DQN在训练的时候loss不平滑，优化效果不好。

(state,action)space通常来说非常大，而我们其实某种程度上只关心policy π，即当前情况下应该怎么做，所以通常只优化policy π说不定更有效。
![](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241015103524.png)

### 为什么policy optimization能解决DQN的问题？
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241015103629.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241015103726.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241015103756.png)
	τ和reward of τ是不会发生变化的，我们能做的就是调整θ，使得高reward的那个路径更经常出现，低reward的路径更少出现，这就是我们policy optimization的目标
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241015104507.png)

其实gradience某种程度上，他只给了一个方向。他其实并没有给大小，也没有给绝对的步长，传统的监督学习步长是根据learning rate。
但是在这个RL问题里面，因为你并没有全局信息，而且只能通过sample来获得新的点，有可能去了某个地方几次以后，我们得到类似gradient的海拔图，发现他非常的杂乱，如果在某个地方的步长没有选好，一下move的太远了，就永远没法顺着这个路径下去了，会掉入一个陷阱里。
所以说TR trusted region policy optimization主要解决的问题就是说我们怎么样能够，比如说做了一个action，我得到了一个reward，但是我多相信这个事情是整体的趋势，而不是偶然间的发现，这个是这个work主要解决的问题，那就是通过选步长来实现。

### 怎么样选一个比较好的步长呢？
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241015110719.png)
我们用一个新的loss，但最关键的是你现在的选择，你在这个方向上有好几个选择，你把这几个选择都算一遍，看他的reward是多少，但是呢你现在这个总体的policy跟以前的policy不能相差太远，这是他整体的一个思路。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241015111919.png)

![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241015112003.png)

