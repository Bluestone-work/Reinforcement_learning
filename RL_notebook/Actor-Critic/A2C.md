A2C实际上是QAC的一个推广，他基本的思想是在QAC中引入一个新的baseline去减少他的方差。
首先我们要来介绍一个性质
我们所推导的policy gradient这个梯度，他对于引入一个新的偏置是不会发生变化的。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241014104700.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241014104714.png)
为什么引入一个新的b不会发生变化？
为什么我要关心这个b函数？
S的分布是![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241014104850.png)
A的分布是![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241014104859.png)

第一个问题：
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241014105030.png)
为什么等于1呢，因为对所有的概率求和是等于1的，然后对常数的偏导是等于0的。
第二个问题：
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241014105426.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241014105550.png)
如果采样的时候方差很小，那么采集的样本的值就很有可能贴近真实的均值，反之如果方差很大，那么采集的值就偏差很大。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241014105656.png)


最好的baseline如下
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241014105746.png)
虽然是最优的但同时也太复杂了，我们为了简化baseline，一般会把他的权重给去掉，直接去用q的一个expectation，他也是Vπ(s)。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241014105948.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241014110031.png)
Vπ可以看做是qπ在某个状态下的一个平均值。
$$
\delta_\pi(S, A) \doteq {{q_\pi}}(S, A)-{{v_\pi}}(S)
$$
$$
	{{v_\pi}}(S)  = \sum_a \pi(a \mid s) q \pi
$$
他的随机形式版本为：
$$
\begin{aligned}
\theta_{t+1} & =\theta_t+\alpha \nabla_\theta \ln \pi\left(a_t \mid s_t, \theta_t\right)\left[q_t\left(s_t, a_t\right)-v_t\left(s_t\right)\right] \\
& =\theta_t+\alpha \nabla_\theta \ln \pi\left(a_t \mid s_t, \theta_t\right) \delta_t\left(s_t, a_t\right)
\end{aligned}
$$
这个算法可以被重新表示为：
$$
\begin{aligned}
\theta_{t+1} & =\theta_t+\alpha \nabla_\theta \ln \pi\left(a_t \mid s_t, \theta_t\right) \delta_t\left(s_t, a_t\right) \\
& =\theta_t+\alpha \frac{\nabla_\theta \pi\left(a_t \mid s_t, \theta_t\right)}{\pi\left(a_t \mid s_t, \theta_t\right)} \delta_t\left(s_t, a_t\right) \\
& =\theta_t+\alpha \underbrace{\left(\frac{\delta_t\left(s_t, a_t\right)}{\pi\left(a_t \mid s_t, \theta_t\right)}\right)}_{\text {step size }} \nabla_\theta \pi\left(a_t \mid s_t, \theta_t\right)
\end{aligned}
$$
那么究竟是之前的qt比较好呢还是现在转化成的detat比较好呢？
显然是detat，因为我们在乎的不是action value的绝对值，而是在乎他的相对值。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241014121347.png)

更多的是：
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241014121424.png)

这么做的好处是，如果我需要用到qt的话，那么我需要用到一个函数，一个神经网络来近似，需要另外一个神经网络来近似Vt，转化之后我只需要一个神经网络Vt就行。

#### 算法：
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241014121601.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241014121607.png)
- **αw\alpha_wαw​ (Critic的学习率)**：Critic负责学习价值函数。通常选择一个较小的值，比如0.001到0.01之间，确保Critic的估计较为稳定。
    
- **αθ\alpha_\thetaαθ​ (Actor的学习率)**：Actor负责学习策略参数。相对于Critic，Actor的学习率可以稍微大一些，比如0.01到0.1之间，不过仍需要根据任务调整，以防止更新过大导致策略发散。
π是stochastic的，所以我们也不需要用greedy。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241014152846.png)
