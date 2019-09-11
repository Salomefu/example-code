# 列表推导、生成器表达式，以及同它们很相似的集合（set）推导和字典（dict）推
# 导，在 Python 3 中都有了自己的局部作用域，就像函数似的。表达式内部的变量和赋
# 值只在局部起作用，表达式的上下文里的同名变量还可以被正常引用，局部变量并不
# 会影响到它们。

# BEGIN BISECT_DEMO
import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'


def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)  # <1>
        offset = position * '  |'  # <2>
        print(ROW_FMT.format(needle, position, offset))  # <3>


if __name__ == '__main__':

    if sys.argv[-1] == 'left':  # <4>
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

    print('DEMO:', bisect_fn.__name__)  # <5>
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)

# END BISECT_DEMO
