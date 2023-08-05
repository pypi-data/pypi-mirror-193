'''
使用argparse对参数进行解析，方便通过命令行与程序进行交互
'''

import argparse



def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def parse(config:dict):
    '''
    使用argparse解析字典中的项
    '''

    parser = argparse.ArgumentParser()
    # start to parse
    for name, value in config.items():
        if isinstance(value, list):
            parser.add_argument(f'--{name}', type=type(value[0]), nargs='*', default=value)
        elif isinstance(value, bool):
            parser.add_argument(f'--{name}', type=str2bool, default=value)
        else:
            parser.add_argument(f'--{name}', type=type(value), default=value)
    args = parser.parse_args()

    # update config
    config.update(vars(args).items())

    return config

