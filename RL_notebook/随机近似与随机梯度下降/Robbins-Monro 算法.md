
首先随机近似(SA Stochastic approximation)是什么？
它代表了一大类的算法，随机的，迭代的算法，里面涉及到了对随机变量的采样。SA特指这些算法是要进行方程的求解或者是优化问题。
有很多算法可以进行方程的求解或者是优化问题，比如说梯度下降或是梯度上升。
那么SA的优势是什么？或者说特点是什么呢？
它不需要知道这个方程或是目标函数的表达式，那自然我们也不知道他的导数和梯度的这种表达式。

那么Robbins-Monro算法简称RM算法：
我们常用的随机梯度下降算法是RM算法的一种特殊情况。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007181711.png)

一个典型的例子就是做优化，我要去优化一个目标函数J（w）：
一般而言我都是求解一个方程![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007181831.png)
这个梯度=0是必要条件。
我们也有可能会遇到J(w)=c的情况，这时候我们可以把c移到左边，这样我们就得到了一个新的函数。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007181943.png)
仍然可以看作这样的一个形式。

![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007182202.png)

#### 正式介绍RM
我们的目标需要求解g(w) = 0,假设最优解是w star![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007182505.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007182627.png)
下面我们用RM算法求解这个问题。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007182635.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007182945.png)
不断逼近0点。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007183159.png)
RM算法如果这里面的一些条件满足了那么wk就会收敛到wstar。
凡是我们看强化学习的论文的时候，都会涉及到这么一个wp1.
因为这里面的wk不是一个普通的数，他是涉及到随机变量采样的这样一个数，所以他的收敛不是常规意义上的收敛，而是概率意义上的收敛。
下面来详细说明三个条件
1.关于梯度的要求：
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007183655.png)
单调递增且有界的。
如果不是有界的话，曲线随着w的增大，他可能在某一点就倾向于无穷，或者是他的值越来越大导致他的gradient也是趋近于无穷。这种情况出现的话，在算法收敛的时候，他可能会逐渐发散掉。
之前我们提过一个优化问题，加入说我们要minimize一个objective function的时候，我们的方法就是求解这个function，让他的gradient = 0，这样就转成一个求解g(w) = 0的方程问题。根据这里面这个条件，我再要求g(w)的gradient>c1的时候，意味着我们要对function求二阶导，他得到的实际上是一个Hessian matrix，Hessian matrix[黑塞矩阵](https://blog.csdn.net/qq_34886403/article/details/83589108)实际上是一个正的矩阵意味着这个函数是凸的(convex)所以这个性质实际上是对应着一种convexity，所以这个性质相对而言也是可以接受的。
2.关于系数ak的要求：
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007185313.png)
Ⅰ.ak的和应该等于无穷，意味着ak收敛的速度不要太快
Ⅱ.ak的平方和应该小于无穷，意味着ak最后一定会收敛到0
3.关于测量误差的要求：
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007185617.png)
常见的情况是他的η是一个iid的，从一个概率分布中去iid地进行采样，η不要求是高斯噪音
Ⅰ.他的η的mean应该是等于0
Ⅱ.他的variance应该是有界的
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007185747.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007185932.png)
什么样的ak能够满足这样的条件呢？
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007190018.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007190148.png)


#### 应用RM算法到mean estimation
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007190237.png)

![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007190355.png)
那么这个expectation实际上是我们所不知道的，但我们所知道的是我们可以对X进行采样，所以我们测量的就是G(w,x) = w - x,x就是对X的采样。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007190530.png)
相对应的RM算法如下：
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007190612.png)

#### 另一个定理
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007190722.png)
