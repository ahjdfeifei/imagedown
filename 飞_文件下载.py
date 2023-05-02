
'''
导入 class 图文下载器  参数顺序
    1:默认文件存放路径 后缀需要带/
    2 headers 默认已有

下载列表类  → 列表链接下载(["列表链接"])  
单图片下载 →   单次下载(键,"值必须为字符串") 
list拼接下载('链接头 如 http://baidu.com/',['列表数据'])



'''
import requests
headers = {
    "user-agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
}


class 图文下载器:
    '''
    (存放路径="D:/",headers=headers)

     #文件存放路径最后一定要带/例如 →存放路径="D:/123/"


    '''

    def __init__(self, 存放路径="D:/", headers=headers):

        self.headers = headers
        self.keys = []
        self.values = []
        self.字典 = {}
        self.后缀 = ''
        self.文件数据 = b''
        self.文件路径 = ''
        self.变量名 = None
        self.网址拼接 = None
        self.存放路径 = 存放路径
        # self.存放路径 = 存放路径

    def 列表链接下载(self, 数据):
        '''
        列表数据的下载 转换成字典格式下载 例如
        ['https://example.com/image1.jpg', 'https://example.com/image2.jpg']
        '''
        for i in range(len(数据)):
            self.keys.append(i + 1)

        for i in 数据:
            self.values.append(i)

        self.字典 = dict(zip(self.keys, self.values))
        for 键, 值 in self.字典.items():
            self.后缀 = 值.split('.')[-1]
            self.文件数据 = requests.get(url=值, headers=self.headers).content
            self.文件路径 = self.存放路径 + str(键) + '.' + self.后缀
            with open(self.文件路径, 'wb') as self.变量名:
                self.变量名.write(self.文件数据)
        print("下载结束", "存放路径在:", self.存放路径)

    def 单次下载(self, 键, 值):
        '''
        ☆☆☆☆ 值 必须为字符串格式☆☆☆

        '''

        self.后缀 = 值.split('.')[-1]
        self.文件数据 = requests.get(url=值, headers=self.headers).content
        self.文件路径 = self.存放路径 + '0' + str(键) + '.' + self.后缀
        with open(self.文件路径, 'wb') as self.变量名:
            self.变量名.write(self.文件数据)
        print("下载结束", "存放路径在:", self.存放路径)

    def list拼接下载(self, 链接头, 列表):
        for i in range(len(列表)):
            self.keys.append(i + 1)

        for i in 列表:
            self.values.append(链接头+i)
            # print(链接头+i)

        self.字典 = dict(zip(self.keys, self.values))
        for 键, 值 in self.字典.items():
            self.后缀 = 值.split('.')[-1]
            self.文件数据 = requests.get(url=值, headers=self.headers).content
            self.文件路径 = self.存放路径 + str(键) + '.' + self.后缀
            with open(self.文件路径, 'wb') as self.变量名:
                self.变量名.write(self.文件数据)
        print("下载结束", "存放路径在:", self.存放路径)
