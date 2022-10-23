class Ipv4:
    def __init__(self, ipv4):
        self.ipv4 = ipv4
        self.mask = []

    def mascara_rede(self):
        mask0 = 32 - int(self.ipv4[4])
        mask1 = '1' * int(self.ipv4[4]) + '0' * mask0
        lista = [mask1[:8], mask1[8:16], mask1[16:24], mask1[24:32]]
        mascara = []
        for x in lista:
            y = int(x, 2)
            mascara.append(str(y))

        self.mask = lista
        mask2 = '.'.join(mascara)
        print(f'Máscara de sub-rede:    {mask2}')
        return self.mask

    def first(self):
        self.ipv4[3] = str(1)
        ipv4firsthost = '.'.join(self.ipv4[:4])
        print(f'Primeiro Host:          {ipv4firsthost}')

    def last(self):
        if int(self.mask[2], 2) != 255:
            self.ipv4[2] = str(int(self.ipv4[2]) +
                               (255 - int(self.mask[2], 2)))
            self.ipv4[3] = str(254)
            ipv4finalhost = '.'.join(self.ipv4[:4])
            print(f'Último Host:            {ipv4finalhost}')

        self.ipv4[3] = str((255 - int(self.mask[3], 2)) - 1)
        ipv4finalhost = '.'.join(self.ipv4[:4])
        print(f'Último Host:            {ipv4finalhost}')

    def broadhost(self):
        if int(self.mask[2], 2) != 255:
            self.ipv4[2] = str(int(self.ipv4[2]) +
                               (255 - int(self.mask[2], 2)))
            self.ipv4[3] = str(255)
            ipv4broad = '.'.join(self.ipv4[:4])
            print(f'Broadcast da rede:      {ipv4broad}')

        self.ipv4[3] = str(255 - int(self.mask[3], 2))
        ipv4broad = '.'.join(self.ipv4[:4])
        print(f'Broadcast da rede:      {ipv4broad}')


def formatipv4(ipv4):
    print(f'Seu endereço/rede:      {ipv4}')
    ipv4 = ipv4.replace('/', '.')
    ipv4 = ipv4.split('.')
    return ipv4


ipv4 = formatipv4('192.168.0.12/26')

ip = Ipv4(ipv4)
ip.mascara_rede()
ip.first()
ip.last()
ip.broadhost()
