# Abstração
# Herança - é um

# https://www.youtube.com/watch?v=T17BTNKBeJY
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'


class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log') 
        return msg
    def log_success(self, msg):
        return msg

class LogFileMixin(Log):
    def _log(self, msg):
        print(msg)
        msg_fomatada = f'{msg} ({self.__class__.__name__})'
        print('Salvando no log:', msg_fomatada)
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_fomatada)
            arquivo.write('\n')


class LogPrintMixin(Log):
    def _log(self, msg):
        return msg


    if __name__ == '__main__':
        l = LogPrintMixin()
        l.log_error('qualquer coisa')
        l.log_success('Que legal')
        lp = LogPrintMixin()
        lp.log_error('qualquer coisa')
        lp.log_success('Que legal')
        lf = LogFileMixin()
        lf.log_error('qualquer coisa')
        lf.log_success('Que legal')