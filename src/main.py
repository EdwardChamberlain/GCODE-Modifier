import json


def read_config(path=r'src/config.json'):
    with open(path, 'r') as f:
        config = json.loads(f.read())
    return config


def find_replace(file, replace_terms):
    for k, v in replace_terms.items():
        file = [
            i if i.strip() != k else i + v + " ;ADDED BY GCODE EDITOR" + "\n"
            for i in file
        ]
    return file


def read_gcode(filepath):
    with open(filepath, 'r') as f:
        file = f.readlines()
    return file


if __name__ == '__main__':
    config = read_config()
    file = read_gcode(r'examples/PA-on-and-off-trial.gcode')

    replace_terms = config['find-append']
    file = find_replace(file, replace_terms)

    with open(r'examples/PA-on-and-off-trial_output.gcode', 'w') as f:
        f.writelines(file)
