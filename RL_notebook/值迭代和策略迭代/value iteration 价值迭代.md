实际上价值迭代和策略迭代是Truncated policy iteration的两个极端情况

首先思考一下，我们应该怎么样求解贝尔曼最优公式呢？
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006131820.png)
首先可以考虑迭代算法。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006131832.png)
实际上这个迭代算法是有自己名字的，它叫做value iteration。

这个算法首先我会给定vk，求解嵌套在这个式子中的一个优化问题，我要求解出来π。当这个π求解出来之后，再去求解出来这个vk+1.
这个就对应了两个步骤：
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006145552.png)
这里的vk并不是一个state value，他就是一个向量，就是一个值。
那么我们怎么样编程实现呢？
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006145800.png)

#### step1. Policy updata
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006145908.png)
#### step2.Value update
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006145944.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006150023.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006150242.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006150436.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006150521.png)

```
new_policy = np.eye(action_space_size)[best_action]
```
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006190229.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006190239.png)
