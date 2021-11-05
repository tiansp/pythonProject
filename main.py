from telnetlib import Telnet
from jinja2 import Environment, FileSystemLoader
import csv


class TelnetClient:

    def __init__(self, ip, port, device_type):
        self.ip = ip
        self.port = port
        self.type = device_type
        self.template = None
        self.template = self.read_template()

    def read_template(self):
        if self.type == 'Switch':
            env = Environment(loader=FileSystemLoader('.'))
            return env.get_template('template_1.txt')

    def read_csv(self, path):
        tmp = ''
        with open(path, encoding='utf-8-sig') as f:
            csv_f = csv.DictReader(f)
            for i in csv_f:
                print(self.template.render(i))
                tmp += self.template.render(i)
        return tmp

    def telnetCil(self, data):
        tn = Telnet(self.ip, self.port, timeout=10)
        tn.write(data.encode('ascii'))


if __name__ == '__main__':
    cil = TelnetClient('192.168.68.129', '32769', 'Switch')
    print(cil.template)
    cil.telnetCil(cil.read_csv('./interface.csv'))
