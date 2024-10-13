from datetime import date
from slugify import slugify

a = '2016-12-12'
dates = date.fromisoformat(a)
print(dates.year)


b = 'True'
print(bool(b))

t = 'Samsung Galaxy Edge 2'
slug_text = slugify(text=t)
print(slug_text)
