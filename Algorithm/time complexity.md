# Time complexity
1. Basic operation (O(1))
2. Order structure (+)
3. For structure (*)
4. If-else structure (max(if, else))
- worst-case time complexity

|Examples|Complexity|Comment|Rank|
|----|----|----|----|
|12|O(1)|常数阶|1|
|2n+3|O(n)|线性阶|3|
|3n^2+2n+1|O(n^2)|平方阶|5|
|5log2n+1|O(logn)|对数阶|2|
|2n+3nlog2n+1|O(nlogn)||4|
|6n^3+2n^2+3n+14|O(n^3)|立方阶|6|
|2^n|O(2^n)|指数阶|7|

O(1)<O(logn)<O(n)<O(nlogn)<O(n^2)<O(n^3)<O(2^n)<O(n!)<O(n^n)

## Functions complexity
python 内置类型性能分析： timeit
```class timeit.Timer(stmt='pass', setup='pass, timer=<timer function>)```
Timer是测量小段代码执行速度的类。
stmt参数是要测试的代码语句 (statment)
setup参数是运行代码时需要的设置;
timer参数是一个定时器函数，与平台有关。

```timeit.Timer.timeit(number=1000000)```
Timer类中测试语句执行速度的对象方法。number参数是测试代码时的测试次数，默认为1000000次。方法返回执行代码的平均耗时，一个float类型的秒数。

