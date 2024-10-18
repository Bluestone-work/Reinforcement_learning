在一个集合X上有一个点x，有一个映射或是函数f，如果x满足f(x)=x，x就被称为不动点。

如果有一个函数，它被称为contrastion mapping
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006105709.png)

![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006105810.png)
如果f是一个contrastion mapping 有三个结论。
1.一定存在一个fixed point
2.这个fixed point一定是唯一的
3.一定可以求解出这个fixed point、

把这个理论应用到最优贝尔曼公式。
对于最优贝尔曼公式，v = f(v) = maxπ(rπ+γPπv)是存在一个solution v‘ 并且他的解是唯一的。这个解可以用迭代的方式解出
![image.png](https://cdn.jsdelivr.net/gh/Bluestone-work/image/image/20241006110341.png)
这个序列Vk最后会收敛到V’。