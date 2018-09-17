# import tensorflow as tf
import requests
# w=tf.Variable(tf.random_normal(shape=[100000,100000]),dtype=tf.float32,name='W')
# b=tf.Variable(tf.random_normal(shape=[100000,100000]),dtype=tf.float32,name='b')
# y=tf.matmul(w,b)
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     for i in range(1):
#         sess.run(y)
#         requests.post('127.0.0.1:5000/post',json={"w":sess.run(w)[0][0],"b":sess.run(b)[0][0]})
import asyncio,aiohttp,logging
@asyncio.coroutine
async def getPage(url,jsons):
    async with aiohttp.ClientSession() as session:
        async with session.post(url,json=jsons) as resp:
                res=(await resp.text())
                print(jsons)
tasks=[getPage('http://127.0.0.1:5000/post', jsons={"w": i, "b": i}) for i in range(1000)]

loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))