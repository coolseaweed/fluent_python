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

# BEGIN CLIP_ANNOT


def clip(text: str, max_len: 'int > 0' = 80) -> str:  # <1>
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

# END CLIP_ANNOT


if __name__ == '__main__':
    from inspect import signature
    sig = signature(clip)
    print(sig)  # doctest: +ELLIPSIS
    print(str(sig))
    for name, param in sig.parameters.items():
        print(param.kind, ':', name, '=', param.default)
