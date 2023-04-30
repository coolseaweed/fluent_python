"""
    >>> clip('banana ', 6)
    'banana'
    >>> clip('banana ', 7)
    'banana'
    >>> clip('banana ', 5)
    'banana'
    >>> clip('banana split', 6)
    'banana'
    >>> clip('banana split', 7)
    'banana'
    >>> clip('banana split', 10)
    'banana'
    >>> clip('banana split', 11)
    'banana'
    >>> clip('banana split', 12)
    'banana split'
"""

# BEGIN CLIP


def clip(text, max_len=80):
    """Return text clipped at the last space before or after max_len
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:  # no spaces were found
        end = len(text)
    return text[:end].rstrip()

# END CLIP


if __name__ == "__main__":
    inputs = [
        ('banana ', 6),
        ('banana ', 7),
        ('banana ', 5),
        ('banana split', 6),
        ('banana split', 7),
        ('banana split', 10),
        ('banana split', 11),
        ('banana split', 12)
    ]
    for input in inputs:
        res = clip(*input)
        print(f"input: {input}, output: {res}")
