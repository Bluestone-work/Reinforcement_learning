Sarsa及其变形所做的事都是给定一个策略，能够估计出来action value。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241008132449.png)
Sarsa估计出来action value之后，它实际上在做的也是policy evaluation。
我们需要把Sarsa policy evaluation和policy improvement结合起来。

第一部分：给一个策略，估计action value
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241008133855.png)
Sarsa算法是 State action reward State action这五个单词的首字母缩写。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241008134026.png)

#### 收敛性证明
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241008134145.png)
还是需要给定一个策略，然后估计出他的action value

#### 代码
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241008134341.png)

![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241008135808.png)

## example
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241008135844.png)
此例子与网格状态之前的例子不同，之前的例子是要找到每一个位置到达目的地的最佳策略，这个是单一位置。
在此例子中，这个特定状态是左上角的一个状态。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241008160811.png)
一开始的策略是比较不好的，所以他可能走了很久才碰到target area，所以刚开始的episode很长。
