#!/usr/bin/env python3

with open('etc/VERSION.txt') as r:
  version = int(r.read()) + 1
with open('etc/VERSION.txt', 'w') as w:
  w.write(f'{version}\n')

with open('etc/setup.cfg') as r:
  with open('setup.cfg', 'w') as w:
    w.write(r.read().replace('{VERSION}', f'0.0.{version}'))

import os
os.system('rm dist/*')
os.system('python3 -m build')
os.system('python3 -m twine upload dist/*')
os.system('git add .')
os.system(f'git commit -m version-{version}')
os.system('git push')
