## （并不）有趣的 Python 3 教程 - 1

第二节课了！小朋友们你们还在听还在看吗！

老规矩，我们看看这节课我们做了什么……

1. 数据类型

   Python 中的数据具有许多类型，但本质上来说，它们都是对象。具体而言，常见的类型包括：

   * 整数
   * 浮点数（实数）
   * 字符串
   * 布尔值（True or False!）
   * None
   * 数组
   * 字典
   * 自定义对象

   Python 是一个强类型、动态类型语言。

   * 强类型意味着几乎不允许**隐式（implicit）**类型转换。
   * 动态类型意味着类型错误是一个**运行时（runtime）**错误。
   * 可以参考数学概念上的解释。

2. 变量系统

   当我们在`a = 1`的时候，我们究竟在做什么？

   * Python 本身维护一张具有两列的表——一列可以理解为门牌号，另外一列才是实际的数值（右值，Right Value）。

   * 我们定义的符号永远只是一个门牌号。

   * 考虑一下下面的代码段，`print(a)`和`print(b)`会返回什么？

     ```python
     a = 1
     b = a
     a = 2
     print(a)
     print(b)
     ```

   * 考虑一下为什么？

   * 另一个例子：

     ```python
     a = {"Reading": 30,
          "Listening": 30,
          "Speaking": 30,
          "Writing": 30}
     b = a
     a['Speaking'] = 27
     print(a)
     print(b)
     ```

   * Again, why?

3. 自学内容

   * 复习[廖雪峰的 git 教程](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)……对我知道你们一定没有好好看！

4. 作业

   * [github地址](https://github.com/SHSTuringClub/pyTutorial)依然可用……然而并不建议在上面提交（比较慢）
   * 图灵社的自有 Git 系统成立啦！[项目地址](https://git.turing.pro/TuringClub/pyTutorial)，注意需要注册后才能访问。还是老规矩，fork 出去写完作业提一个 pull request。适应以后我就直接~~尾行~~跟踪你们的私有 repo 啦~