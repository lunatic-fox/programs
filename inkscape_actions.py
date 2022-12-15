import re
from os import system

cmd = lambda act, i, o: system(';'.join([
  f'inkscape --actions="file-open:{i}',
  act,
  f'export-filename:{o}',
  'export-do"'
]))

actions, action, act_cmd = {}, lambda e: actions.setdefault(e.__name__, e), []

@action
def ungroup(*i):
  '''
    Ungroup all paths.
    `i`: `str` - Input path
  '''
  with open(i[0]) as gn:
    gn = gn.read()
    gn = len(re.findall(r'<g\s', gn))

  t_cmd = []
  for _ in range(gn):
    t_cmd.extend([
      'select-all: all',
      'selection-ungroup'
    ])

  act_cmd.extend(t_cmd)

@action
def unify(*_):
  '''
    Unify all paths.
  '''
  act_cmd.extend([
    'select-all: all',
    'selection-ungroup',
    'select-all: all',
    'path-union'
  ])

@action
def center(*_):
  '''
    Align to the all paths to the center of the page.
  '''
  act_cmd.extend([
    'select-all: all',
    'selection-group',
    'object-align: hcenter vcenter page',
    'selection-ungroup'
  ])

@action
def resize(*i):
  '''
    Resize all paths as a group to defined size.
    `i[0]`: `str` - Input path
    `i[1]`: `str | float` - Size
    `i[2]`: `0 | 1` - Defined axis.
  '''
  with open(i[0]) as file:
    file = file.read()

  def nlist(attrs: list):
    return list(map(lambda e: float(re.sub(r'.+="(.+)"', r'\g<1>', e)), attrs))

  x = nlist(re.findall(r'\sx=".+"', file))
  w = nlist(re.findall(r'\swidth=".+"', file))
  w = w[-len(x):]
  w = w[x.index(max(x))] + max(x) - min(x)

  y = nlist(re.findall(r'\sy=".+"', file))
  h = nlist(re.findall(r'\sheight=".+"', file))
  h = h[-len(y):]
  h = h[y.index(max(y))] + max(y) - min(y)

  try:
    id_size = i[2]
  except IndexError:
    id_size = -1

  dn = [w, h][id_size] if id_size > -1 else max(w, h)
  scale = float(i[1]) / dn

  act_cmd.extend([
    'select-all: all',
    'selection-group',
    f'transform-scale: {scale}',
    'selection-ungroup'
  ])

@action
def fitBox(*i):
  '''
    Resize all paths as a group to fit the page size.
    `i[0]`: `str` - Input path
  '''
  with open(i[0]) as file:
    file = file.read()

  f_str = file.replace('\n', '')
  f_res = re.findall(r'<svg\s.*?viewBox="(.*?)"', f_str)

  if len(f_res) == 1:
    f_res = list(filter(lambda e: e != '0', f_res[0].split(' ')))
    f_res = f_res[-2:]
  else:
    w = re.findall(r'<svg\s.*?width="(.*?)"', f_str)
    h = re.findall(r'<svg\s.*?height="(.*?)"', f_str)
    f_res = [w[0], h[0]]

  f_res = list(map(lambda e: float(e), f_res))

  actions['resize'](i[0], min(f_res), f_res.index(min(f_res)))
  actions['center']()
