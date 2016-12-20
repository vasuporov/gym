import gevent
import random
import datetime


def foo():
    print ("Running foo...")
    gevent.sleep(0)
    print ("Exiting foo...")


def bar():
    print ("Running bar...")
    gevent.sleep(0)
    print ("Exiting bar...")


def main_foo_bar():
    threads = [gevent.spawn(foo), gevent.spawn(bar)]
    gevent.joinall(threads)


def task(pid):
    gevent.sleep(random.randint(0, 2) * 0.001)
    print ("Task %s done" % pid)


def log_timestamp(func):
    def wrap(*args, **kwargs):
        start_time = datetime.datetime.now()
        func(*args, **kwargs)
        print (datetime.datetime.now() - start_time)
    return wrap


@log_timestamp
def sync():
    for i in range(1, 10):
        task(pid=i)


@log_timestamp
def async():
    threads = [gevent.spawn(task, pid) for pid in range(1, 10)]
    gevent.joinall(threads)


def main_async_sync():
    sync()
    async()


if __name__ == '__main__':
    # main_foo_bar()
    main_async_sync()
