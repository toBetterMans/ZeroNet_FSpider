# -*- coding: utf-8 -*-

from config import redis_client,mysql_conn


def getUrlFromDB():
    try:

        cur = mysql_conn.cursor()
        cur.execute("SELECT url FROM webservice WHERE  type='zsite'")
        results = cur.fetchall()
        for domain in results:
            task_url = "http://47.56.197.215:43110/" + domain[0]
            print(task_url)
            redis_client.lpush("zeronet_whole", task_url)
        mysql_conn.commit()
        cur.close()
        mysql_conn.close()
    except Exception as e:
        print("Mysql Error %d:%s" % (e.args[0], e.args[1]))
        return None


if __name__ == '__main__':
    getUrlFromDB()


# urllist = ["zybbs.bit", "1PKDXAgCBR77JBwjir4cjjXt2hwSpw78bs", "1NCezLP8aXjABVreBB1CKGPub2tKTtyhWU/", "NewGFWTalk.bit","1Brez7NV7rmEuJ72yBBPxxZybcc4CQyNn6", "btsynchina.bit/"
#            , "1MpKFgUUAPd9ZxTQjhixCXkzqEGYuozq4y"]
# for result in urllist:
#     task_url = "http://47.56.197.215:43110/" + result
#     print(task_url)
#     redis_client.lpush("zeronet_whole", task_url)