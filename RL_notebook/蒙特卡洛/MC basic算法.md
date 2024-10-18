要理解这个算法的核心是，要怎么把policy iteration这个算法变成model free的。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006231409.png)
核心量就是Qπk
我们又两种方法求这个Q
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006231437.png)
基于MC的方法用的是第二种方法。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006231526.png)
#### 过程
1.首先我们从任意的一个s和a的一个组合出发，然后根据当前策略得到一个episode。
2.计算出来这个episode的discount return g(s , a)
3.g(s , a)就是Gt的一个样本
4.如果我们又很多个这样的采样，有一个这样的集合。我们就可以用这个采样求一个平均值来估计这个Gt的平均值。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006231841.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006231917.png)

到此为止这个算法已经逐渐清晰了。

首先我们从一个初始的策略出发，这个策略可能是不好的，我们会慢慢改进。
在第k个iteration它包含两个步骤。
第一个是policy evaluation，第二个是policy improvement。
在第一个步骤计算的是qπk(s , a)，对任意的所有的(s,a)都要得到qπk。方法就是从(s,a)出发得到很多的episode，然后对episode求平均。
第一个步骤我们得到了qπk，我们求新策略。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006232442.png)

MC basic是policy iteration的一个变形。他不实用，他的efficiency是比较低的。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006233108.png)
### 举例
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006233856.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006233938.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006234200.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006234329.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006234413.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006234420.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006234443.png)


那么在使用的过程中，episode的长度应该设置为多长合适呢？
采样的次数又是设置多少次合适呢？
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007000400.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007000908.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007000946.png)
