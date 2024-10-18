Q-learning是直接估计optimal action value
他不需要去做policy evaluation和policy improvement这两个来回切换。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241009203507.png)
当前时刻如果不是哪个trajectory访问到的st或者at的话那么他的qπ(s,a)是不变的。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241009203536.png)

那么Q-learning在数学上解决什么问题呢？
他已经不是在求解一个贝尔曼方程了。他是再求解一个贝尔曼最优方程也就是这样一个式子。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241009203711.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241009204553.png)
行为策略，从环境中收集。
目标策略，用于更新。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241009204627.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241009204833.png)
target policy可能是greedy或者是ε-greedy的他的探索性比较弱，我可能很难去探索到所有的s和a，很难正确评估所有。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241009210321.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241009210437.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241009210933.png)


#### 伪代码
Q-learning有两个版本
1.On-policy
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241009211010.png)
2.Off-policy
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241009211151.png)
用ε-greedy的原因是，我一会要用这个策略去生成数据，要让他具有探索性。但是off-policy不需要探索性，探索环境不是他的职责，所以只需要直接greedy就好。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241009211725.png)
#### 例子
首先我们生成一个behavier policy，然后用这个policy去生成很多的数据
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241009211740.png)
初始的behavior policy最好是探索性比较强的，如果他的探索性不强，可能会发生如下情况
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241009212002.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241009212050.png)
