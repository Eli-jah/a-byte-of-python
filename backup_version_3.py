import os
import time


# set time zone to 'Asia/Shanghai'
os.environ['TZ'] = 'Asia/Shanghai'
if os.name != 'nt':
    time.tzset()  # Note: this function tzset() is only available on Unix & Unix-like OS
# time.altzone = -28800
# time.timezone = 'Asia/Shanghai'
print(time.altzone)  # -28800
print(time.timezone)  # -28800
print(time.tzname)  # ('CST', 'CST')

if os.name == 'nt':
    source = [r'D:\Documents']
    target_dir = r'E:\Backup'
else:
    source = ['/home/vagrant/Documents']
    target_dir = '/home/vagrant/Backup'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)
    print('Successfully created backup directory:', target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

# Take a comment(optional) from user
# to create the name of the zip archive.
comment = input('Enter your comment --->>>')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
             comment.strip(' ').replace(' ', '_') + '.zip'
print('Date-Time:', time.strftime('%Y-%m-%d %H:%M:%S'))

if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory:', today)

zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))
print(zip_command)
exit(0)

print('Zip Command:', zip_command)
print('Running ...')
if os.system(zip_command) == 0:
    print('Done! Target Backup File:', target)
else:
    print('Failed!')
