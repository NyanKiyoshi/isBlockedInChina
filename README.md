isBlockedInChina
================
Uses the service [blockedinchina.net](http://www.blockedinchina.net) to check if a given website is blocked in China or not.


## Usage Example

```python
>>> from isBlockedInChina import IsBlockedInChina
>>> is_blocked = IsBlockedInChina()
>>> servers = is_blocked.test('github.com')
>>> for server in servers:
...     print(server)

['Beijing', 'BLOCKED']
['Shenzhen', 'BLOCKED']
['Inner Mongolia', 'BLOCKED']
['Heilongjiang Province', 'BLOCKED']
['Yunnan Province', 'BLOCKED']
['No servers were able to reach your site.  This means that your site is most likely NOT accessible from within mainland China.']
```
