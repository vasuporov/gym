import time

"""
Coroutines - These are basically the consumers of data while
             generators are producer of data.

"""


def search_pattern(pattern):
    print ("searching pattern : " + str(pattern))

    while True:
        line = (yield)

        if pattern in line:
            print ("'" + str(pattern) + "' in '" + line + "'")
        else:
            print ("Pattern not found in '" + line + "'")


def coroutine(func):

    def wrap(*args, **kwargs):
        cr = func(*args, **kwargs)
        cr.next()
        return cr

    return wrap


@coroutine
def check_odd_even():
    print ("Checking number if odd or even")

    try:
        while True:
            number = (yield)

            if number % 2 == 0:
                print ("Number is even")
            else:
                print ("Number is odd")
    except GeneratorExit:
        print ("Coroutine is exiting, garbage collected.")


@coroutine
def printer():
    print ("printer initialized")
    while True:
        line = (yield)
        print (line)


def tail_minus_f(file, target):
    file.seek(0, 2)
    print ("tail -f")

    while True:
        line = file.readline()
        if not line:
            time.sleep(0.1)
            continue

        target.send(line)


def main_search_pattern():
    sp = search_pattern(pattern='hello')
    sp.next()    #
    sp.send("you you")
    sp.send("hell hell")
    sp.send("hello world")
    sp.close()


def main_check_odd_even():
    coe = check_odd_even()
    coe.send(4)
    coe.send(20)
    coe.send(3)
    coe.close()


def main_tail_minus_f():
    file = open("dummy-log")
    tail_minus_f(file, printer())


if __name__ == '__main__':
    main_search_pattern()
    # main_check_odd_even()
    # main_tail_minus_f()
