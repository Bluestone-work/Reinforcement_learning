他是前两者的一般化推广
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006204115.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006204531.png)

接下来我们对比一下pi和vi
1.pi是给出一个初始策略，vi没开始
2.pi通过给出的π0求出Vπ0，vi给定一个初始值v0，为了让两个算法能比较，我们用V0=Vπ0
3.pi通过求出的Vπ0，求出一个新策略π1，vi刚开始有一个v0，通过v0求出π1
4.pi我有了π1要根据贝尔曼公式求出vπ1，vi我们已经有了一个π1也有了v0，通过求解得到v1.
这个时候V1和Vπ1就不在相同了。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006205028.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006205250.png)
policy iteration这个算法只在理论当中存在，在实际中是不存在的，我们经常做的就是去判断，Vπ1j-Vπ1j-1是不是已经小于阈值，即使是这样，也是计算了有限步。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006205701.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006210043.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006210119.png)
