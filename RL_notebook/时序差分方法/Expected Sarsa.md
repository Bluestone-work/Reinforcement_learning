与通常的Sarsa不一样的是![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241008185403.png)
括号内的γ * q(st+1,at+1)变成了期望的形式
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241008185616.png)
由于我们不需要对at+1进行采样了，所以他涉及的随机性也就减少了。
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241008185753.png)

#### n-step Sarsa
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241009194423.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241009194600.png)
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241009195158.png)
