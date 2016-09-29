# Biconfigs
[![Build Status](https://img.shields.io/travis/antfu/biconfigs.svg?style=flat-square)](https://travis-ci.org/antfu/biconfigs)
[![Coverage](https://img.shields.io/codecov/c/github/antfu/biconfigs.svg?style=flat-square)](https://codecov.io/gh/antfu/biconfigs)
[![Python Version](https://img.shields.io/pypi/pyversions/biconfigs.svg?style=flat-square)](https://pypi.python.org/pypi/biconfigs)
[![PyPI](https://img.shields.io/pypi/v/biconfigs.svg?style=flat-square)](https://pypi.python.org/pypi/biconfigs)
[![License](https://img.shields.io/github/license/antfu/biconfigs.svg?style=flat-square)](https://github.com/antfu/biconfigs/blob/master/LICENSE)

📄⇄🛠 Two way configurations mapping helper for Python.

## Get Started
```python
from biconfigs import Biconfigs
configs = Biconfigs('configs.json')

# Simply change the dict, and it will automatically save the changes to file.
configs['options'] = {'debug': True,
                      'username': 'Anthony',
                      'list': [] }

# Access with simple 'x.y.z' style
configs.options.list.append('example')
```
Content of file `configs.json` after execution:
```json
{
  "options": {
    "debug": true,
    "list": [
      "example"
    ],
    "username": "Anthony"
  }
}
```

## Install
```sh
pip install biconfigs
```

## Dependencies
**No dependencies** required 🎉

Tested on Python `2.6`, `2.7`, `3.3`, `3.4`, `3.5`, `pypy`, `pypy3`

## Documentation

### High frequency update
Normally, Biconfigs will write the changes to file immediately. But sometime you
may want to update values frequently, which will result in a IO bottleneck. So you
can use **`with`** statement to prevent auto saving for a while.
```python
with configs:
  for i in range(1000):
    configs['some_key'] = i
# This statement will execute saving process only one time when exiting "with" scope
```

### When to save
- Saving when: *Item create, item delete, list reorder, value change, `get_set`, etc.*
```python
# All the following single statement will cause saving
configs['item'] = 'value'
configs['options'] = {}
configs.options['list'] = []
configs.options.list.append('example')
configs.options['list'] = []
configs.options.clear()
value2 = configs.get_set('item2', 45)
```

- Not saving when: *Item access, assignment but not changed, etc.*
```python
# All the following single statement will NOT cause saving
value = configs.item
configs['item'] = 'value' # The value of 'item' is not changed
value3 = configs.get('item_not_exists', 'default_value')
```

### Get or set
Biconfigs provides a special function `get_set` for dict.
The `get_set` acts just like `dict.get(key, default)`, but it will save the default value to dict if the key is not exists.

For example:
```python
# get_set will return the default value if the key is not exists
>>> self.config.get_set('item', 'value')
'value'
# get_set also set the default value to dict
>>> self.config.item
'value'
# get_set will just return the value of existing key
>>> self.config.get_set('item', 'new-value')
'value'
```

## License
MIT
