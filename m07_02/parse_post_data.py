import urllib.parse

data = b'name=%D0%AE%D1%80%D1%96%D0%B9+%D0%92%D0%BE%D0%BB%D0%BE%D0%B4%D0%B8%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B8%D1%87+%D0%9A%D1%83%D1%87%D0%BC%D0%B0&email=krabatua%40gmail.com&text=%D0%94%D0%BE%D0%B1%D1%80%D0%B8%D0%B9+%D0%B2%D0%B5%D1%87%D1%96%D1%80%21+%D0%90+%D0%BD%D0%B0%D0%B2%D1%96%D1%89%D0%BE+%D0%92%D0%B0%D0%BC+windows+95%3F'

parse_data = urllib.parse.unquote_plus(data.decode(), encoding='utf-8')

# parse_data = parse_data.split('&')
# parse_data = [el.split('=') for el in parse_data]
# print(dict(parse_data))
# parse_data = {key: value for key, value in parse_data}
# print(parse_data)

result = dict([el.split('=') for el in parse_data.split('&')])
print(result)
