TD算法他是再求解state_value，一个给定策略的state_value
TD算法是基于数据，而不是基于模型来实现强化学习。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241008110905.png)
在t时刻访问到的状态就是st，因为一个agent在环境中当它一个时刻只能访问一个状态。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241008111451.png)

![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241008111814.png)

### TDtarget
我们为什么把Vtbar叫做TDtarget。
应为这个算法就是要把V(st)朝着TDbar的方向去改进也就是下一时刻V(st)会朝着离Vtbar更近的地方移动。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241008112959.png)


### TD error
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241008114352.png)

![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241008114440.png)
