# testlinkwrapper

Wrapper for test tool Testlink

## sample usage
```python
from testlinkwrapper import TestLinkWrapper

TESTLINK_URL = 'http://xxx'
TESTLINK_DEVKEY = 'xxx'
tlw = TestLinkWrapper(TESTLINK_URL, TESTLINK_DEVKEY)
for project in tlw.projects:
    print(project.name)
```
TESTLINK_URL and TESTLINK_DEVKEY as environment variables:
```python
tlw = TestLinkWrapper()
for project in tlw.projects:
    print(project.name)
```