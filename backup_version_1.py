# encoding=utf-8
import os
import time


# 1. The files and directories to be backed up
# are specified in the list.
# Example on Windows:
# source = ['"C:\\My Documents"']
# Example on Mac OS X and Linux:
# source = ['/home/elijah/Documents']

# Notice here that we have to use double quotes inside a string
# for names with spaces in it:
# source = ['"C:\\My Documents"']
# We can also use the raw string this way:
# source = [r'C:\My Documents']

# os.name
# The following names have currently been registered: 'posix', 'nt', 'java'.
if os.name == 'nt':
    source = ['D:\\Documents']
else:  # for Linux: posix
    source = ['/home/vagrant/Documents']

# 2. The backup must be store
# in a main backup directory.
# Example on Windows:
# target_dir = 'E:\\Backup'
# Example on Mac OS X and Linux:
# target_dir = '/home/elijah/Backup'

if os.name == 'nt':
    target_dir = 'E:\\Backup'
else:  # for Linux: posix
    target_dir = '/home/vagrant/Backup'

# 3. The files are backed up into a zip file.
# 4. The name of this zip archive is current date-time string.

target = target_dir + os.sep + \
    time.strftime('%Y%m%d%H%M%S') + '.zip'

# Create the target directory if it is not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # make the directory

# 5. We use the zip command to put the files into a zip archive
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))
print(zip_command)
exit(0)

# 6. Run the backup
print('Zip command is:')
print(zip_command)
print('Running ...')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED.')


