# encoding=utf-8
import sys


version = sys.version
version_info = sys.version_info
print('Python Version:', version)
print('Python Version info: major: {}; minor: {}; micro: {}; releaselevel: {}; serial: {}'.format(version_info.major, version_info.minor, version_info.micro, version_info.releaselevel, version_info.serial))
