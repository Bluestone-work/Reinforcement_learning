![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241010175214.png)

### 伪代码on policy
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241010175247.png)
如果当前的state不是target state 我们做如下的是：
1.收集sample，也就是在当前的状态st根据当前的策略πt得到一个action at，然后和环境去交互，观察rt+1和st+1。
然后做value updata和policy updata

### 例子
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241010175613.png)
