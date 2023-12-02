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
