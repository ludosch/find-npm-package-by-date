import sys
import json
import dateutil.parser
import subprocess

if len(sys.argv) < 3:
    print('Please launch script with npm package like : find_date.py <date> <package1> <package2> ...')

arg_date = sys.argv[1]

for i in range(len(sys.argv)):
    if i < 2:
        continue

    package_name = sys.argv[i].strip()

    p = subprocess.Popen(['npm', 'view', package_name, 'time', '--json'],
                         shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    std_out, std_error = p.communicate()

    module_versions = json.loads(std_out.decode('utf-8'))

    target_date = dateutil.parser.parse(arg_date).date()
    last_version = 0

    last_date = None
    for v in module_versions:
        date_version = dateutil.parser.parse(module_versions[v]).date()
        if v != 'modified' and v != 'created' and (date_version < target_date or last_date is None):
            last_date = date_version
            last_version = v

    print(package_name, '@', last_version, sep='')
    
