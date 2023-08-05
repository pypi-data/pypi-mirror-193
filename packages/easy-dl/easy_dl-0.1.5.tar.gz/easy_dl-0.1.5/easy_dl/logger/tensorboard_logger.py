from .basic_logger import Logger
from torch.utils.tensorboard import SummaryWriter

class TensorboardLogger(Logger):
    def __init__(self, base_root, runname=None, time_suffix=True):
        '''

        :param base_root: 存放多次实验结果的目录
        :param runname: 实验名，如果为None则以时间作为名称
        :param time_suffix: 为实验名加上时间后缀
        :param mode:

        example:
            logger = TensorboardLogger('./results', 'test', time_suffix=False)
            logger.log('Hello world!')

            image = torch.randn([3, 256, 256])
            logger.log_image(image, '00000.png')
        '''
        super().__init__(base_root, runname, time_suffix)

    def log_metric(self, name, value, global_step):
        '''
        log loss.

        example:
            for step in range(1000):
                loss = i + 1
                logger.log_metric('loss', loss, step)
        '''
        if self.writer is None:
            self.writer = SummaryWriter(self.res_dir)
        self.writer.add_scalar(name, value, global_step=global_step)

    def log_metrics(self, loss_dict: dict, global_step):
        if self.writer is None:
            self.writer = SummaryWriter(self.res_dir)
        for key, value in loss_dict.items():
            self.writer.add_scalar(key, value, global_step=global_step)

