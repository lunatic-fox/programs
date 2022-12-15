import re, sys, os
from inkscape_actions import actions, cmd, act_cmd

entry = ' '.join(sys.argv[1:])
ipath = re.sub(r'^.*-i\s(.+?)(\n|\s.*|$)', r'\1', entry).replace('"', '')
opath = re.sub(r'^.*-o\s(.+?)(\n|\s.*|$)', r'\1', entry).replace('"', '')

try:
  open(ipath)
  if not re.match(r'.+\.svg$', ipath):
    print('\nInput path must be to a SVG file!')
  else:
    entry = re.sub(r'^(.*)-i\s(.+?)(\n|(\s.*)|$)', r'\g<1>\g<3>', entry)
    entry = re.sub(r'^(.*)-o\s(.+?)(\n|(\s.*)|$)', r'\g<1>\g<3>', entry)
    entry = re.sub(r'^\s*(.*?)\s*', r'\1', entry)

    if entry != '':
      entry = entry.split(' ')

    for e in entry:
      e_arg = ''
      if e.find('=') != -1:
        e, e_arg = e.split('=')

      if e in list(actions.keys()):
        actions[e](ipath, e_arg)

    cmd(';'.join(act_cmd), ipath, opath)
    os.system(f'echo All done! & echo File saved in "{opath}"!')

except FileNotFoundError:
  print('\nInput path does not exist!')
