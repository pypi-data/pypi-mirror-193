'''
自定义一个logger类
能够生成一个目录(可以指定目录名,也可以自动根据时间来生成目录), 保存日志信息，生成图片，模型参数等
能够在终端输出日志信息，同时保存到txt文件
'''

import os
import time
import logging


import torch
from torchvision.utils import save_image
from torchvision.transforms.functional import to_pil_image

def makedir_if_not_exists(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def loadLogger(work_dir, save_name='log.txt'):
    if work_dir in logging.Logger.manager.loggerDict:
        return logging.getLogger(work_dir)
    # setup logger
    logger = logging.getLogger(work_dir) # 以工作目录区分多个logger对象
    # set level
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(fmt="[ %(asctime)s ] %(message)s", datefmt="%a %b %d %H:%M:%S %Y")
    # output to stdout
    sHandler = logging.StreamHandler()
    sHandler.setFormatter(formatter)
    logger.addHandler(sHandler)
    # output to file
    fHandler = logging.FileHandler(os.path.join(work_dir, save_name), mode='w')
    fHandler.setFormatter(formatter)
    logger.addHandler(fHandler)
    # sys.stdout = fHandler.stream # 设置 print 打印到logger 日志中。
    return logger


class Logger():
    def __init__(self, base_root, runname=None, time_suffix=True):
        '''

        :param base_root: 存放多次实验结果的目录
        :param runname: 实验名，如果为None则以时间作为名称
        :param time_suffix: 为实验名加上时间后缀
        :param mode:

        example:
            logger = Logger('./results', 'test', time_suffix=False)
            logger.log('Hello world!')
        '''
        # create the dir of results
        self.base_root = base_root
        time_stamp = time.strftime("%Y%m%d%H%M%S", time.localtime())
        if runname is None:
            self.runname = time_stamp
        else:
            self.runname = f'{runname}_{time_stamp}' if time_suffix else runname
        self.res_dir = os.path.join(self.base_root, self.runname)
        makedir_if_not_exists(self.res_dir)
        print(f'The results is in:{os.path.abspath(self.res_dir)}.')
        # setup logger
        self.logger = None

    # log info
    def log(self, msg):
        if self.logger is None:
            self.logger = loadLogger(self.res_dir, save_name=f'log.txt')
        self.logger.info(msg)

    # log tensor image
    def log_image(self, tensor, f):
        save_path = os.path.join(self.res_dir, f)
        makedir_if_not_exists(os.path.dirname(save_path))
        image = to_pil_image(tensor)
        image.save(save_path)

    # log tensor images
    def log_images(self, tensor, f, nrow=4):
        save_path = os.path.join(self.res_dir, f)
        makedir_if_not_exists(os.path.dirname(save_path))
        save_image(tensor, save_path, nrow=nrow)

    def log_state_dict(self, state_dict, f):
        save_path = os.path.join(self.res_dir, f)
        makedir_if_not_exists(os.path.dirname(save_path))
        torch.save(state_dict, save_path)
        self.log(f'save weight successfully!')

    def log_figure(self, figure, save_path):
        pass