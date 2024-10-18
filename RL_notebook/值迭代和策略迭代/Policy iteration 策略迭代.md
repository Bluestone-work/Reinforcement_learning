首先介绍一下算法
最开始有一个inital policy 我们用π0来表示，
每次迭代都分为两个步骤
#### step1.policy evaluation(PE)
我们给定一个策略，可以根据贝尔曼公式求解出它所对应的state value这样的一个过程就是PE
那么我已知这个πk，最开始是π0，然后求解出来Vπk。这个就是去evaluate这个策略。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006173026.png)
#### step2.policy improvement(PI)
刚才我们已经求出来了这个Vπk，我们接着求解一个这样的优化问题，得到一个新的策略πk+1，求解出来的πk+1会比原来的πk更好所以叫做PI。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006173235.png)

这样一个过程可以通过以下图片表示出来：
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006173259.png)

接下来回答几个问题
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006173336.png)

#### anwser1：
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006173509.png)
一个大的迭代算法其中的一步涉及到一个小的迭代算法。

![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006173341.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006173620.png)

![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006173347.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006173649.png)
对于policy iteration是收敛的这个结果，我们实际上是用到了value iteration算法是收敛的结果来证明的。

![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006173354.png)
policy iteration和value iteration实际上是两个极端。是一个更加general的，truncated policy iteration的算法的两个极端。

### 具体实现：
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006174039.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006174131.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006174224.png)
#### 文字说明：
首先在每个iteration，假设现在是第k个iteration，有两步policy evaluation和policy improvement。
在policy evaluation中我们的目的是求解Vπk，首先我们给他一个初始的猜测，可以是任意值。然后我们把猜测带入到这样的一个算法中。直到这个Vπj(j)第j次迭代的时候，能够收敛。
下一步policy improvement，我们首先遍历它所有的状态，再遍历他的每一个action，刚才我们已经求出来Vπk了，就可以通过式子求出qπk，我们从新的qπk中选出最大的action，计算出来这个πk+1之后再回到policy evaluation接下来算Vπk+1，这样不断地迭代循环下去。

#### 举例：
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006174756.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006174847.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006175124.png)

#### work
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006175334.png)
