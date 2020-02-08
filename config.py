phrase_to_paste = ''
press_f2_on_ctrl1 = False
does_press_enter = False
cut_instead_of_copy = False
exit_on_f5 = False
config = {}

def parse_config_file():
    with open('config.cfg', 'r') as f:  # Parse the config file
        text = f.read()
        lines = text.split('\n')
        pairs = [line.split('=') for line in lines if (not line.isspace() and not len(line) == 0)]
        config = {}
        for pair in pairs:
            config[pair[0].strip()] = pair[1].strip()
        return config

def configure():
    global config
    global phrase_to_paste, press_f2_on_ctrl1, does_press_enter, exit_on_f5
    config = parse_config_file()
    if config['TEXT'] == 'None':
        print('Type in the phrase you want to paste with F3:')
        phrase_to_paste = input()
        print('Ok: ' + phrase_to_paste)
    else:
        phrase_to_paste = config['TEXT']
    if config['PRESS_F2_ON_CTRL1'] == 'True':
        press_f2_on_ctrl1 = True
    if config['PRESS_ENTER'] == 'True':
        does_press_enter = True
    if config['CUT_INSTEAD_OF_COPY'] == 'True':
        cut_instead_of_copy = True
    if config['EXIT_ON_F5'] == 'True':
        exit_on_f5 = True