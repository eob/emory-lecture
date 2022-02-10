import os
def on_each_file(fn, name: str = None, display: bool = False):
  ret = []
  files = os.listdir('./data')
  files.sort()
  for filename in files:
    if name is None or name in filename:
      with open(os.path.join("data", filename), 'r') as f:
        content = f.read()
        output = fn(content)
        if display:
          print(filename)
          print(output)
          print()
        ret.append(output)
  return ret
  