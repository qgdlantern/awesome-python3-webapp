import orm
import asyncio
import hashlib
from models import User, Blog, Comment

async def test(loop):                      
    # *** 注意此处的密码填自己设的密码 ***
    await orm.create_pool(loop=loop, user='qgdlantern', password='zyt20041129', db='awesome')
    # *** 注意此处的密码填自己设的密码 ***
    u = User(name='qgdlantrn', email='freehappy@gmail.com', passwd=hashlib.md5('12345678'.encode('utf-8')).hexdigest(), image='about:blank')
    await u.save()
    ## 网友指出添加到数据库后需要关闭连接池，否则会报错 RuntimeError: Event loop is closed
    orm.__pool.close()
    await orm.__pool.wait_closed()
    
if __name__ == '__main__':
    print('test.py')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.close()