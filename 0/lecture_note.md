## （并不）有趣的 Python 3 教程 - 0

让我们来回顾一下我们这节课做了什么吧！

1. 为什么要学 Python

   * 因为编程能装[beep]！
   * 因为别的语言很辣鸡！
   * 因为 Python 很好用！
   * ~~因为学好 Python 能够 py 交易！~~
   * 忘了这些吧，你都来上课了是不是……

2. 怎么写 Python

   * 首先，你要装个 Python。
   * [Python 下载地址，注意选择当前最新版本。本文成时为3.5.2](https://www.python.org)
   * 其次，你要有个文本编辑器。
   * 不要用记事本。不要用记事本。不要用记事本。重要的话要说三遍。
   * 好的文本编辑器包括`Atom`, `Visual Studio Code`, `Sublime Text`, `Vim`等等。`Vim`并不建议在 Windows 下食用。
   * 初学者建议不要使用功能复杂的IDE，入门后可考虑`PyCharm`~~PY的魅力~~，向 JetBrains 上传学生证可以免费使用学生版，也有免费的 Community 版啦~

3. 我们的第一批代码

   代码的详解在此略去了，听过课应该都明白……了吧？

   ```python
   import random

   def 人种鉴定():
       if random.randint(0, 99) < 1:
           print('朕是欧皇!')
       else:
           print('非酋还不跪下?')

   人种鉴定()
   ```

   初始版本的人种鉴定。

   ```python
   import random

   def 人种鉴定():
       画符 = hash(input())
       机票 = (random.randint(0, 99) + 画符) % 100
       if 机票 < 1:
           print('朕是欧皇!')
       else:
           print('非酋还不跪下?')

   人种鉴定()
   ```

   加强版的人种鉴定。

   > **注意，这里使用中文作为变量/函数名称仅为了演示用途。实际代码编写中非常不建议使用中文或拼音。请使用英文以与全世界的代码编写者沟通交流~~PY交易~~**

4. 补药忘了我们的自学内容

   * [廖雪峰的 git 教程](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)
   * [廖雪峰的 python 教程](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000) 读到 Python 基础一章即可。
   * 以上内容应该不会占用太多时间……吧……QAQ

5. 补药忘了我们的作业

   * 作业会放在一个 [github repository](https://github.com/SHSTuringClub/pyTutorial) 里面。里面同时还有每节课的 keynote 和你正在阅读的这份笔记。BTW，笔记是用 Markdown 写的。虽然这不是教学内容，然而 Markdown 还是挺有用的……
   * 里面有详细的说明，只要你有基本的英文能力，并理解了 git 教程，肯定能理解的啦~
   * 实际的作业内容不过三四行代码而已……不过需要先读完自学内容。
   * 尽早交啦……（凝视）