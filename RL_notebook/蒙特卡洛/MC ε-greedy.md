如果我们从一个（s，a）出发，后面的episode特别长，因为他是探索性的，实际上我能够确保任何的一个s和a都能够被这个episode访问到，这样我就能够去掉explore start这个条件，我就不需要从每个s和a出发了，我只要从一个或几个出发就能够访问到他了，因此我们要使用soft policy。
那么这里面的soft policy我们要用什么呢？
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007151558.png)
	|A（s）|就是s所对应的a的个数。比如说我们在grid world这个example当中，每一个状态所对应的action应该就是5。如果我们选择ε，比如说ε = 0.2，这时候ε / |A（s）| = 0.04，也就是我们有4个概率的action，他们的概率是0.04剩下的哪个action他的概率就是1-0.16 = 0.84。通过这个我们可以得出，greedy-action是由最大的概率做选择，但是其他的action也有一定概率能访问到。

那么我们为什么要用ε-greedy呢？
因为它能够平衡exploitation和exploration。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007154304.png)
uniform distribution 均匀分布。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007155046.png)


#### 算法
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007155106.png)


#### 举例
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007160907.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007160919.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007162028.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007162109.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007162935.png)
为什么ε越大，区域内的负数的值越大呢？
因为ε越大，智能体在运作的过程中就越有可能跑进forbidden area内。![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241007164156.png)
