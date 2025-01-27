# representations of large or deeply nested objects

import reprlib

aRepr = reprlib.Repr()

example = [1, 'spam', {'a': 2, 'b': 'spam eggs', 'c': {3: 4.5, 6: []}}, 'ham']

print(aRepr.repr(example))