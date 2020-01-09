# testlinkwrapper

Wrapper for test tool Testlink

## sample usage
```
from testlinkwrapper import TestLinkWrapper

SERVER_URL = 'http://xxx'
DEVKEY = 'xxx'

tl = TestLinkWrapper(SERVER_URL, DEVKEY)

for p in tl.projects:
    print(p.name)
```