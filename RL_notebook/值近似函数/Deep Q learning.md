![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241010200801.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241010201024.png)

我们要怎样计算梯度呢？
在deep Q learning中我们把整个假设为y然后y里面是包含了w的，假设y里面w是一个常数，那这个时候J（w）就只是后面的w的一个函数了，这个时候我再去求解他的梯度就会比较简单了。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241010201256.png)

为了做到这一点，deep Q learning中引入了两个net，第一个是main network，另一个是target network
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241010201828.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241010203008.png)
第一个技巧是他使用了一个网络，而不是两个网络。
