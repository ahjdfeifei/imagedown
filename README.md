# 下载器
使用了很多别人分享的库 新手 第一次分享前辈别见笑哈!


三种文件下载方式
===


+ 图(路径).list拼接下载(img, list2)

+ 图(路径).列表链接下载(['https://example.com/image1.jpg',
              'https://example.com/image2.jpg'])

+ 图(路径).单次下载("名称", "https://example.com/image2.pdf")

```python

from 飞_文件下载 import 图文下载器 as 图

list2 = ['20221031_double11/3088929375_14_524_374.jpg',
         '20210629/31313889_14.jpg']


路径 = r"F:/练习/"  # 路径格式后面一定要加/ 不传递路径 默认下载在D盘根目录下面

img = 'https://lupic.cdn.bcebos.com/'
```

```python
图(路径).list拼接下载(img, list2)

图(路径).列表链接下载(['https://example.com/image1.jpg',
              'https://example.com/image2.jpg'])

图(路径).单次下载("名称", "https://example.com/image2.pdf")
```
