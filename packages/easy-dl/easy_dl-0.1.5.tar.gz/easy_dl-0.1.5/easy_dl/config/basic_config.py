'''
基于munch实现基础的深度学习配置功能。
1. 能够格式化输出配置信息
2. 能够使用argparse解析参数，获取用户的输入

'''
import yaml
from munch import Munch

from .config_parse import parse


class Config(Munch):
    '''
    初始化配置，接受三种参数:
    1. 类
    2. json文件
    3. yaml文件
    '''

    def __init__(self, *args, **kwargs) -> None:
        # 添加一个默认项，方便选择配置
        super().__init__(*args, **kwargs)

    def load_yaml(self, f, config_name='default'):
        self['config_name'] = config_name

        args = yaml.safe_load(open(f, encoding='utf8'))[config_name]
        self.update(args)
        return self

    def parse(self):
        '''
        使用argparse解析，与用户进行交互
        '''
        parse(self)
        return self

    def __str__(self):
        '''
        打印配置信息
        '''
        table = '\n# ----------------------------parameters table--------------------------- #\n'
        for name, value in self.items():
            table += f'{name}: {value}\n'
        table += '# ------------------------------------------------------------------------ #'
        return table
