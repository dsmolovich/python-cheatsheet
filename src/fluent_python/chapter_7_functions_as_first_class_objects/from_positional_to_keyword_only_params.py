
def tag(name, *content, class_ = None, **attrs):
    """
    >>> tag('br')
    '<br />'

    >>> tag('p', 'hello')
    '<p>hello</p>'

    >>> print(tag('p', 'hello', 'world'))
    <p>hello</p>
    <p>world</p>

    >>> print(tag('p', 'hello', 'world', class_='sidebar'))
    <p class="sidebar">hello</p>
    <p class="sidebar">world</p>

    >>> tag(content="testing", name="img")
    '<img content="testing" />'

    >>> my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
    ...           'src': 'sunset.jpg', 'class': 'framed'}
    >>> tag(**my_tag)
    '<img class="framed" src="sunset.jpg" title="Sunset Boulevard" />'
    """
    if class_ is not None:
        attrs['class'] = class_
    attr_pairs = (f' {attr}="{value}"' for attr, value in sorted(attrs.items()))
    attr_str = ''.join(attr_pairs)
    if content:
        elements = (f'<{name}{attr_str}>{c}</{name}>' for c in content)
        return "\n".join(elements)
    else:
        return f'<{name}{attr_str} />'
