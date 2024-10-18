PPO全称是proximal policy optimization，相当于TRPO他就是把KL divergence去掉了。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241015112131.png)
直接在边缘处clip，给你一个最大值，再给你一个最小值，然后只要在这个范围内就可以了。不允许更新太多，比如说你想加1，但是clip的范围是0.2，就只能加0.2，在进行计算，如果还是大的话，就再加0.2。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241015112518.png)
