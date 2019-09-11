from math import hypot


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        # The %s specifier converts the object using str(), and %r converts it using repr().
        # %r或者对象属性的字符串表达形式
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        # 默认情况下，自定义的类的实例对象总被认为是真的。除非这个类对 __bool__ 或者
        # __len__ 函数有自己的实现。bool(x) 的背后是调用 x.__bool__() 的结果；如果不存
        # 在 __bool__ 方法，那么 bool(x) 会尝试调用 x.__len__()。若返回 0，则 bool 会返回
        # False；否则返回 True。
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

# Python 对象的一个基本要求就是它得有合理的字符串表示形式，我们可以通过 __repr__
# 和 __str__ 来满足这个要求。前者方便我们调试和记录日志，后者则是给终端用户看
# 的。这就是数据模型中存在特殊方法 __repr__ 和 __str__ 的原因。

# 对象/数据模型 指的是对象的属性
