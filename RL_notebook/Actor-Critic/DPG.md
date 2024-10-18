![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241014213544.png)
我们的问题是我们之前看的都是stochastic的策略，那我们能不能用deterministic的策略呢？
之前我们的策略是π，他的输入是s，他的输出是Π(a1|s,θ)一直到π(a5|s,θ),比如说有五个action的话。
它通过这个输出层，约束每一个输出全部都是严格大于0的并且他们的和是等于1的，这就是我们之前一直用的一种方式。

他的缺点是他对action的个数是有要求的，你只能是有限个，因为它是输出，他不可能输出无限个。
如果我在一个状态s有无限个action要怎么办呢？
这时候我们就可以用deterministic的一个情况，首先我们来做一个定义。
![7ceb55c0208b7deff504d961f29e6d9f_720.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/7ceb55c0208b7deff504d961f29e6d9f_720.png)
之前我们所有的策略全部都是用π(a|s,θ)来表示的，它是在状态s的时候take action a，他的概率是从0-1的一个数值，这就是stochastic策略。deterministic策略的概率等于1，现在我们要做一个变化，我们已经知道了要求他就是deterministic，就可以不用这种方法，可以直接携程a = μ(s,θ)，μ是一个函数，他的输入是s他的参数是θ输出是a。
注意这个μ他不是输出我在s采取的action a的概率是多少，他的输出直接是a，比如说他的索引是向上还是向下是直接告诉你的，所以μ是从状态空间到动作空间的一个映射，变成了一个回归问题（输入状态，输出动作），当状态空间确定的时候，动作空间的点也就确定下来了。
![68d74b8f160ea4b35a1929eba78bf7ee_720.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/68d74b8f160ea4b35a1929eba78bf7ee_720.png)
这时候就有两个问题：①梯度怎么计算②把梯度用到梯度上升的方法当中进行优化

之前我们所得到的那个梯度J(θ)，它是stochastic情况下的，和deterministic策略不一样。
![fc79eee69c0a91151d640c63fd22432a_720.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/fc79eee69c0a91151d640c63fd22432a_720.png)
首先我们要有一个目标函数J(θ),θ是这个μ策略的参数。我们希望去优化他，塔的定义为在所有状态上然后求和，这个权重是d0(s)乘以vμ(s)，vμ(s)就是在策略μ下面他们的state value，d0是一个概率分布，它每一个都大于等于0并且他的和是等于1的，这里的d0选取比较简单，他的选择和μ是没有关系的。

有两种重要而特殊的情况，第一种是我只关心某一个状态，比如说我有一个任务，我每次开始这个任务都会从这个状态出发，我只要去最大化从这个状态出发它的return就可以了，这时候我就给d0(s0) =1 d0(s≠s0)=0，目标函数就是vμ(s0)。
第二个情况就是d0是一个stationary distribution of a behavior policy，也就是我另外一个behavior policy比如说β，我在它下边，它的stationary distribution和off-policy是有关系的，我们就会发现deterministic policy gradient它是off-policy的天然的。我们就不需要用importance sampling把它转成off-policy。
![20537b2ac7e49dbd067784f483183f52_720.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20537b2ac7e49dbd067784f483183f52_720.png)

通过如下gradient可以看出来些蛛丝马迹。
![2cc432c36798fb527e4a195069f7a737_720.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/2cc432c36798fb527e4a195069f7a737_720.png)
![ccb027ba4651c1d0083927e4d1120cc9.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/ccb027ba4651c1d0083927e4d1120cc9.png)
![](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/ccb027ba4651c1d0083927e4d1120cc9.png)![8c3e5c8478a4838461f9af89ac20e6b8.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/8c3e5c8478a4838461f9af89ac20e6b8.png)


![38f46cb2d92e892645a7e926c9233113_720.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/38f46cb2d92e892645a7e926c9233113_720.png)
在这个discounted的情况下我求他的梯度就等于图中的公式，s是要服从一个ρμ的分布，第二行括号内的式子分为两项，第一项是μ对θ的梯度，第二项是qμ，qμ是在μ分布下的action value对a的梯度要qμ先对a进行求梯度然后再把里边所有的a全部替换为μ(s)。
为什么不能直接变呢？因为你如果直接变成μ(s)的话这里面就没有a了。

这个梯度和前面stochastic情况的梯度是非常不一样的，一是这里面没有涉及到a，这里面的a最后会被替换为μ(s)，自然也就没a的梯度，他的一个结果就是一个off-policy的算法，因为之后会对true gradient进行求stochastic gradient，也就是采样，在进行采样的时候，如果给定了一个s，然后我要求一个a，在得到rt+1，那这时候就不需要关系这个a究竟是哪个策略得到的，应为expectation没有要求我们必须按照哪一个策略得到，所以它可以是任意的。
这时候就可以用一个behavior policy其他的任何一个策略都可以，有了这个梯度之后，我们就可以应用到梯度上升的方法当中去进行优化。

![c32564dd7f088a1a04f99340f959939a_720.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/c32564dd7f088a1a04f99340f959939a_720.png)
梯度上升就是θt+1 = θt+αθ，还是老样子，这里面有expectation不容易求出来，我们就用stochastic gradient来进行替代。

#### 代码：
![c7d4e41acaf8cccf5a63d78e0c433d4d_720.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/c7d4e41acaf8cccf5a63d78e0c433d4d_720.png)
![d183307e3b62bbe9bfb7c0dc07190f63.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/d183307e3b62bbe9bfb7c0dc07190f63.png)
这里应该是action 函数，而不应该是value 函数

![a807abb68366e4e9c844c049ddbc683a_720.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/a807abb68366e4e9c844c049ddbc683a_720.png)
本质上来说它是一个off-policy的算法，所以它既可以用off又可以用on，μ+noise实际上和我们之前x-greedy的方法是非常类似的，但这边不能用是因为这里面他的action是连续的，所以不能在其他有限的action上面加上一些比较小的概率，另外一个问题就是这里面其实涉及到了q的计算，包括在梯度中q怎么选取呢？
一种方法是之前应用了非常广的包括在dpg论文中提出来的linear function，另一种则是用神经网络。

### DPG：
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241014220547.png)
策略网络是确定性的函数，输入是状态S，输出是具体状态A。