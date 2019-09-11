import collections

# namedtuple构建只有少数属性但是没有方法的对象,比如数据库条目
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    # 将具体实现代理给self._cards这个list
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

# 特殊方法的调用是隐式的，比如for i in x实际上会调用iter(x)->x.__iter__
# 另外通过内置的函数实现len iter str来使用特殊方法是最好的选择
