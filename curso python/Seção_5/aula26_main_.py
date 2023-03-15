from log import LogFileMixin, LogPrintMixin
from eletronico import Smartphone

galaxy_s = Smartphone('Galaxy S')
iphone = Smartphone('iPhone')

galaxy_s.ligar()
iphone.desligar()