from difflib import SequenceMatcher
from itertools import islice


def intersection(l1, l2):
    """
    returns a list of elements that exists in both lists
    """
    return list(set(l1).intersection(l2))


def tabulate(groups):
    """
    prints a list of lists in a tabular way, like:
    > 1 2 3
    > 3 4 5
    > 5 6 7
    > 7 8 9
    > 9 10 1
    """
    print('\n'.join(' '.join(map(str, row)) for row in groups))
    print('\n')


def list_by_group(l, grp, step=-1):
    """
    group items of a list with a step size
    l = [1 2 3 4 5 6 7 8 9 10]
    grp = 3; step = 2
    > 1 2 3
    > 3 4 5
    > 5 6 7
    > 7 8 9
    > 9 10 1
    grp= 4; step = 2
    > 1 2 3 4
    > 3 4 5 6
    > 5 6 7 8
    > 7 8 9 10
    """
    if step <= 0:
        step = grp
    starts = range(0, len(l), step)
    stops = [x + grp for x in starts]
    groups = [(l * 2)[start:stop] for start, stop in zip(starts, stops)]
    return groups


def rolling_window(seq, n=2):
    """
    Returns a rolling window (of width n) over data from the iterable
    s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...
    """
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result


def first_numeric(raw: str):
    for i in raw:
        if i.isnumeric():
            return i
    return ''


# Extract template variables from a text as integers.
# For example template: "toggle %,% through %,%"
#                 text: "toggle 239,400 through 100,199"
# Then to recover 239, 400, 100 and 199 as variables write the following code:
#
# w, x, y, z = extract("toggle %,% through %,%", "toggle 239,400 through 100,199")
def extract_int(template, text):
    seq = SequenceMatcher(None, template, text, True)
    return [int(text[c:d]) for tag, a, b, c, d in seq.get_opcodes() if tag == 'replace']


# Same as above but the resulting variables are strings.
def extract_string(template, text):
    seq = SequenceMatcher(None, template, text, True)
    return [text[c:d] for tag, a, b, c, d in seq.get_opcodes() if tag == 'replace']


def positional_squared_graph(heigh: int, width: int = None):
    """
    returns a graph dict of valid node addresses with neighbours for a squared node matrix
    """
    if not width:
        width = heigh
    g = {}
    for x in range(heigh):
        for y in range(width):
            """
            a(x-1,y-1), b(x-1,y), c(x-1,y+1)
            d(x  ,y-1),           e(x  ,y+1)
            f(x+1,y-1), g(x+1,y), h(x+1,y+1)
            """
            g[(x, y)] = []
            if x > 0 and y > 0:
                g[(x, y)].append((x - 1, y - 1))  # a
            if x > 0:
                g[(x, y)].append((x - 1, y))  # b
            if x > 0 and y < width - 1:
                g[(x, y)].append((x - 1, y + 1))  # c
            if y > 0:
                g[(x, y)].append((x, y - 1))  # d
            if y < width - 1:
                g[(x, y)].append((x, y + 1))  # e
            if x < heigh - 1 and y > 0:
                g[(x, y)].append((x + 1, y - 1))  # f
            if x < heigh - 1:
                g[(x, y)].append((x + 1, y))  # g
            if x < heigh - 1 and y < width - 1:
                g[(x, y)].append((x + 1, y + 1))  # h
    return g


def to_coord(text: str, sep=None):
    """
    usage:
    m1 = to_coord("a b c\nd e f", " ")
    m2 = to_coord("abc\ndef")
    returns a dict with a coord of each elem
    """
    matrix = {}
    for x, line in enumerate(text.splitlines()):
        if sep:
            cols = line.split(sep)
        else:
            cols = [i for i in line]
        for y, col in enumerate(cols):
            matrix[(x, y)] = col
    return matrix


def text_to_matrix(text: str, sep=None):
    """turns a pure text into a matrix (list of lists), provide separator to split elements."""
    matrix = []
    for x, line in enumerate(text.splitlines()):
        if sep:
            cols = line.split(sep)
        else:
            cols = [i for i in line]
        matrix.append(cols)
    return matrix


def rotate_matrix_clockwise(m):
    """rotate matrix (list of lists) to the right"""
    rotation = list(zip(*reversed(m)))
    return [list(elem) for elem in rotation]


def rotate_matrix_anticlockwise(m):
    """rotate matrix (list of lists) to the left"""
    rotation = list(zip(*reversed(m)))
    return [list(elem)[::-1] for elem in rotation][::-1]


def sum_tuples(a, b):
    return tuple([sum(x) for x in zip(a, b)])
