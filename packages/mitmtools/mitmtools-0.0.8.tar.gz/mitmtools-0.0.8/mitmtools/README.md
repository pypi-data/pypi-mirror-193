# 介绍

mitmtools 是根据 mitmproxy 封装的工具库

具备如下功能

- 替换响应文件
- 修改部分响应内容
- 移除部分响应内容
- hook 注入

安装

```
pip install mitmtools
```

# 替换响应文件

- ReplaceByFile：通过正则匹配 url，使用文件替换整个响应
- ReplaceByStr：通过正则匹配 url，使用字典替换部分字段

```
ReplaceByFile(pattern='', filepath='', max_times=0)  # 注意 max_time 为可选参数，代表匹配次数
ReplaceByStr(pattern='', replace_dict={'':''})
```

# 移除部分响应内容

- RemoveContent：通过正则匹配 url，并去除部分响应内容

```
RemoveContent(pattern='', remove_list=['x']), max_times=0)
```

# hook 注入

- HookHtml：通过正则匹配 url，通过 html 进行插入 script 标签进行注入
- HookJs：通过正则匹配 url，通过 js 进行注入

```
HookHtml(pattern='', filepath='', content='')
HookJs(pattern='', filepath='', content='')
```

## 注意

html 注入属于 xss 攻击，部分会有 csp 防护导致 script 不会执行，从而 hook 失败

友情提醒：任何注入都可能被检测！

# 查看

如果只是想查看请求过程的话，直接使用 Show

```
Show()
```

# 执行

将需要执行的方法单独放一个 .py 文件，并放在 addons 列表中，如下：

```
"""
    这只是一个配置的例子
    
    注意：
        启动之后，文件是动态的，随时修改随时生效
        启动程序要和该程序在同一目录，不然可能找不到文件路径
        使用中要注意缓存的影响，停用缓存或清除缓存再尝试
"""
from mitmtools import Show
from mitmtools.remove import RemoveContent
from mitmtools.hook import HookJs, HookHtml
from mitmtools.replace import ReplaceByStr, ReplaceByFile

addons = [
    Show(),  # 输出请求、响应

    # replace
    # ReplaceByStr(pattern='https://www.baidu.com/', replace_dict={'百度一下，你就知道': '百度一下，你也不知道'})
    # ReplaceByFile(pattern='^https://www.baidu.com.?$', filepath="./mitmtools/static/index.html")

    # hook
    # HookHtml(pattern='https://www.baidu.com/', filepath='./mitmtools/static/hookCookie.js'),
    # HookHtml(pattern='https://www.baidu.com/', content='''
    #     (function () {
    #         var gkDocument = document;
    #         var gkPrint = console.log;
    #         Object.defineProperty(document, "cookie", {
    #             set: function (val) {
    #                 gkPrint("正在设置 Cookie：", val)
    #                 debugger;
    #                 cookieTemp = val;
    #                 return val
    #             },
    #             get: function () {
    #                 return gkDocument.cookie
    #             }
    #         })
    #     })()
    # '''),
    HookJs(
        pattern="san_b247717.js",
        filepath='./mitmtools/static/hookCookie.js'
    ),

    # remove
    # RemoveContent(pattern='https://www.baidu.com/', remove_list=['就知道'])
]
```

随后调用如下代码，或者自己通过 mitmproxy 命令行命令自行启动

```
from mitmtools.start import execute, execute_web

execute(filepath='xxx.py', port=8866) # 有其它命令都可以通过 args 传
execute_web(port=8866, args={'-s':filepath})    # 有其它命令都可以通过 args 传
```

# 常用启动参数
```
--ssl-insecure
```