

"""
# BEGIN TAG_DEMO
>>> tag('br')  # <1>
'<br />'
>>> tag('p', 'hello')  # <2>
'<p>hello</p>'
>>> print(tag('p', 'hello', 'world'))
<p>hello</p>
<p>world</p>
>>> tag('p', 'hello', id=33)  # <3>
'<p id="33">hello</p>'
>>> print(tag('p', 'hello', 'world', cls='sidebar'))  # <4>
<p class="sidebar">hello</p>
<p class="sidebar">world</p>
>>> tag(content='testing', name="img")  # <5>
'<img content="testing" />'
>>> my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
...           'src': 'sunset.jpg', 'cls': 'framed'}
>>> tag(**my_tag)  # <6>
'<img class="framed" src="sunset.jpg" title="Sunset Boulevard" />'

# END TAG_DEMO
"""


# BEGIN TAG_FUNC
def tag(name, *content, cls=None, **attrs):
    """Generate one or more HTML tags"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                           for attr, value
                           in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' %
                         (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)
# END TAG_FUNC


def test_f(a, *, b):

    print(f"a:{a}, b:{b}")


if __name__ == "__main__":
    new_tag = tag('br')  # <1>
    print(new_tag)
    new_tag = tag('p', 'hello')  # <2>
    print(new_tag)
    print(tag('p', 'hello', 'world'))
    tag('p', 'hello', id=33)  # <3>
    print(tag('p', 'hello', 'world', cls='sidebar'))  # <4>
    tag(content='testing', name="img")  # <5>
    my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
              'src': 'sunset.jpg', 'cls': 'framed'}
    tag(**my_tag)  # <6>

    print(test_f(3, b=2))
