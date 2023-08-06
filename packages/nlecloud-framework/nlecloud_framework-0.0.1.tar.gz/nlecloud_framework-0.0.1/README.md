01、Installation
-----

```bash
pip install AioFastGet
```



## 02、Notice

> 后期如何使用？
>  1：默认redis 库是 aioredis==1.3.1 要安装这个版本的异步redis
>  2：
>      （1）继承这个类，
>      （2）然后将url通过_addurl 添加进来
>      （3）写一个接受返回结果的async函数
>      （4）启动crawl_main方法
>  3：可以更改参数
>      指定redis_key/redis_db/_max_workers/_poptype = 'FIFO'  ##先进先出



## 03、Eexmple

```python
from AioFastGet import RedisUrlPool
import asyncio

class GetFast(RedisUrlPool):
    def __init__(self):
        super(GetFast,self).__init__()
        self._redisKey = "BaiduList"   ##指定网络池的key
        self._max_workers = 2          ##开始多少个任务

    async def load_url(self):
        """加载url"""
        url_item = {"url":"https://www.baidu.com","backfunc":"parse_baidu"}
        await self._addurl(url_item)


    async def parse_baidu(self,r):
        """解析对应的回调函数"""
        print(r.keys())
        print("收到html长度：",len(r['html']))

    async def run(self):
        await self.load_url()     ##加载url
        await self.crawl_main()   ##启动爬虫程序


if __name__ == '__main__':
    baidu = GetFast()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(baidu.run())
```

