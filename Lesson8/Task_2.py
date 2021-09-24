# Закодируйте любую строку из трех слов по алгоритму Хаффмана.

from collections import Counter, deque
words_str = 'mama papa brat'


class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def haff_tree(s):
    s_count = Counter(s)
    s_sorted = deque(sorted(s_count.items(), key=lambda item: item[1]))

    while len(s_sorted) > 1:
        weight = s_sorted[0][1] + s_sorted[1][1]
        node = Node(left=s_sorted.popleft()[0], right=s_sorted.popleft()[0])

        for i, item in enumerate(s_sorted):
            if weight > item[1]:
                continue
            else:
                s_sorted.insert(i, (node, weight))
                break
        else:
            s_sorted.append((node, weight))
    return s_sorted[0][0]


table = dict()


def haff_code(tree, path=''):
    if not isinstance(tree, Node):
        table[tree] = path
    else:
        haff_code(tree.left, path=f'{path}0')
        haff_code(tree.right, path=f'{path}1')


def form_table(t, st):
    for i in st:
        print(t[i], end=' ')


haff_code(haff_tree(words_str))
form_table(table, words_str)
