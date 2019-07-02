def hello(fn):
    def wrapper():
        print("hello, %s" % fn.__name__)
        fn()
        print("goodby, %s" % fn.__name__)
    return wrapper

@hello
def foo():
    print("i am foo")
# foo()


#网页编程的实例
# def makeHtmlTag(tag, *args, **kwds):
#     def deco(fn):
#         def wrapped():
#             return "<" + tag + " class = "+kwds["css_class"] + ">" + fn() + "</" + tag + ">"
#         return wrapped
#     return deco
#
# @makeHtmlTag(tag="b", css_class="bold_css")
# @makeHtmlTag(tag="i", css_class="italic_css")
# def hello():
#     return "hello"


# print(hello())

#用类来实现装饰器
# class myDecorator(object):
#     def __init__(self,fn):
#         print("inside myDecorator.__init__()")
#         self.fn = fn
#
#     def __call__(self):
#         self.fn()
#         print("inside myDecorator.__call__()")
#
#
# @myDecorator
# def aFunction():
#     print("inside aFunction()")
#
# aFunction()

#用类装饰器改造之前的例子
# class makeHtmlTagClass:
#     def __init__(self,tag,css_class=""):
#         self._tag = tag
#         self._css_class = " class={0}".format(css_class) if css_class!="" else ""
#
#     def __call__(self, fn):
#         def wrapper(*args,**kwargs):
#             return "<" + self._tag +self._css_class+">"+fn()+ "</" + self._tag + ">"
#         return wrapper
#
# @makeHtmlTagClass(tag="b", css_class="bold_css")
# @makeHtmlTagClass(tag="i", css_class="italic_css")
# def test():
#     return "hello bitch"
#
# print(test())



#这是正常的斐波拉契方法
#比如：我们要计算fib(5)，于是其分解成fib(4) + fib(3)，而fib(4)分解成fib(3)+fib(2)，fib(3)又分解成fib(2)+fib(1)…… 你可看到，基本上来说，fib(3), fib(2), fib(1)在整个递归过程中被调用了两次。
# def fib(n):
#     if n<2:
#         return n
#     return fib(n-1)+fib(n-2)

#用装饰器写斐波拉契函数  装饰器的目的是给函数装饰缓存，不要重复计算之前已经计算过的
def demo(fn):
    cache={}
    miss = object()
    def wrapper(args):
        result = cache.get(args,miss)

        if result is miss: #没有取到缓存，那么就开始计算
            # print("not get " + str(args) + " from cache" + str(result) + "\n")
            result = fn(args)
            # print("calcu:"+str(result))
            cache[args] = result
        else:
            print("get " + str(args) + " from cache" + str(result) + "\n")
        return result
    return wrapper


@demo
def fib(n):
    if n<2:
        return n
    return fib(n-1)+fib(n-2)

print(fib(5))




