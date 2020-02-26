import redis
redis_host = "localhost"
redis_port = 6379
redis_password = ""


def hello_redis():
        try:
                r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
                r.set(2, "Hello Redis!!!")
                msg = r.get(2)
                print(msg)
        except Exception as e:
                print(e)

r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)


def fibo(num, r):
        if num == 1 or num == 2:
                return 1
        else:
                r.get(num-1)
                if r.get(num-1) is not None and r.get(num-2) is not None:
                        return int(r.get(num-1)) + int(r.get(num-2))
                else:
                        f_per = fibo(num-1, r)
                        f_pper = fibo(num-2, r)
                        r.set(num-1, f_per)
                        r.set(num-2, f_pper)
                        return int(r.get(num-1)) + int(r.get(num-2))



# print(fibo(100,r))
# # r.flushdb()
