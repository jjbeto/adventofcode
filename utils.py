def first_numeric(raw: str):
    for i in raw:
        if i.isnumeric():
            return i
    return ''

