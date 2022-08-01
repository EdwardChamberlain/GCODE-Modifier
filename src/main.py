import json


with open(r'src/config.json', 'r') as f:
    config = json.loads(f.read())

with open(r'examples/PA-on-and-off-trial.gcode', 'r') as f:
    file = f.readlines()

find_replace = config['find-append']
for k, v in find_replace.items():
    file = [
        i if i.strip() != k else i + v + " ;ADDED BY GCODE EDITOR" + "\n"
        for i in file
    ]

with open(r'examples/PA-on-and-off-trial_output.gcode', 'w') as f:
    f.writelines(file)
