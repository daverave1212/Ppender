
def parse_config_file():
    with open('config.cfg', 'r') as f:  # Parse the config file
        text = f.read()
        lines = text.split('\n')
        pairs = [line.split('=') for line in lines if (not line.isspace() and not len(line) == 0)]
        config = {}
        for pair in pairs:
            config[pair[0].strip()] = pair[1].strip()
        setup_config(config)
        return config

def setup_config(config):
    print(config)
    if config['TEXT'] == 'None':
        print('Type in the phrase you want to paste with F3:')
        config['TEXT'] = input()
        print('Ok: ' + config['TEXT'])
    config['RENAME_PRESS_F2'] = to_bool(config['RENAME_PRESS_F2'])
    config['RENAME_PRESS_ENTER'] = to_bool(config['RENAME_PRESS_ENTER'])
    config['CUT_INSTEAD_OF_COPY'] = to_bool(config['CUT_INSTEAD_OF_COPY'])

def to_bool(string):
    return True if string in ['True', 'true', 'yes', '1'] else False

    