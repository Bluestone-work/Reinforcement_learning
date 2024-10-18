#### 访问数据
在MCbasic方法中我们用的策略是initial-visit，意思就是对于这个episode我只考虑（s1 ，a2），然后我用剩下的所得到的这个return来估计（s1 ，a2）的action value，所以我就来估计这个qπ（s1，v2），他的问题在于我们没有充分的利用这个episode，它里面还有很多数据被浪费了。

两个概念 every visit与first visit
 every visit的含义在于，我只要访问了某个状态动作集合，他后面的路径就可以代表是他的return。
 ![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007142844.png)
不管访问多少次都行
first visit的含义在于，我只对第一次访问的某个状态动作集合的路径作为return，后面再访问到我就不管了。![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007142940.png)

#### 更新策略
1.MCbasic 我们把所有的episode从一个state-action pair中出发的全部收集起来，收集到之后我们做一个average return，这样来估计action value，这样存在一个问题就是他需要等所有的episode全部得到了才行。
2.我得到了一个episode，我就用这个episode的return来立刻估计action value，下一个就直接开始改进策略。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007144837.png)
GPI框架

#### 过程
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007145022.png)

exploring start指的是无论我从哪一个(s,a)出发，我都要有一个return，这样我才能用后面生成的这些reward来估计return

start其实有两种方法
1.我从（s，a）开始一个episode就是一个start。
2.我从其他的（s，a）开始但是我也能够经过当前的这个（s，a），那么后面这些数据也能够估计。
但是目前来说这个visit是无法确保的，所以第二个方法无法用。

![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007145856.png)
