TD算法是在没有模型的情况下来求解贝尔曼公式。
根据TD算法的要求，我们要建立一个新的贝尔曼公式。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241008115057.png)
TD算法从本质来将他是来求解这一个贝尔曼公式的。

### 与RM算法联系
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241008115815.png)

![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241008115955.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241008120159.png)
不断迭代更新。

### 定理
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241008120253.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241008120419.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241008120425.png)
红框部分从本质上来说他的每一个状态s都应该被访问很多次。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241008120538.png)
我们希望很久之后得到的经验还是能派上用场，所以说不能设置为0.

### 与MC算法的对比
	TD算法是一个在线的，比如说我现在得到了一个reward+state我就立刻可以用这些信息来更新我当前的一些估计状态的值，
	MClearning是一个离线的，虽然我得到了一些采样，但是我不可能立刻用，我必须等到episode结束后，我才能计算从当前s到最后的return是多少。
	也正是因为TD是在线的，他才能处理continuing task，也能处理episode task。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241008121019.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241008121211.png)
因为TD是bootstraping的，一旦初始的策略估计有偏差，他会把这种偏差携带进迭代中去，当然随着越来越多的数据进来他会把这个bais给抵消掉，直到最后收敛到估计值。
MC 是无偏估计。

**无偏估计**的定义是：某个估计值的期望等于真实值，也就是没有系统性偏差。例如，在强化学习中，状态的真实价值是其未来累计回报的期望值。如果一个算法的估计值在多次采样后，期望能等于这个真实的期望值，那么该算法就是无偏的。

#### 蒙特卡罗算法的特点：

- 蒙特卡罗算法在一个完整的回合结束后，计算从某一状态到回合结束的**真实累计回报** Gt​（无论回合时间长短），然后将这个真实的回报用于更新该状态的价值估计。
    
- 蒙特卡罗直接使用这个真实的回报 Gt 来更新，而这个值不依赖于任何其他估计。因为它基于实际观察的数据，并且代表了从某个状态到结束的真实奖励总和，完全反映了环境的实际动态。

与蒙特卡罗不同，**时间差分算法（TD）** 在更新价值估计时并不等待整个回合的结束。相反，TD算法使用当前的奖励 Rt+1 和下一状态的估计价值 V(St+1) 来更新当前状态 St​ 的价值：
#### TD算法的偏差来源：

- TD算法的更新依赖于下一状态 St+1​ 的价值估计 V(St+1)，这个价值估计是基于我们当前的模型或策略的预测值，而不是基于实际的未来回报。这意味着 V(St+1) 本身可能是不准确的，因为它可能在训练的初期或策略尚未完全学到正确的值时存在误差。
    
- TD算法只看一步的奖励 Rt+1 和下一步的估计值，而不是整个回合的累计回报。因此，它的更新并不完全反映整个未来的真实情况，而是基于当前的估计进行“逐步修正”。这个逐步修正的过程会引入**偏差**，因为每一步更新都依赖于已经不完全正确的估计。

### 结合使用：TD(λ) 算法

TD算法和MC算法各有优缺点，因此有一种方法是结合这两种方法的优点，即**TD(λ)算法**。TD(λ)算法是一种基于**资格迹**（Eligibility Traces）的算法，它通过引入衰减系数 λ 来在TD和MC之间进行折中。当 λ=0 时，TD(λ) 就变为纯TD(0)算法；当 λ=1 时，它趋近于蒙特卡罗方法。
