class Prodavnica(object):
    def __init__(self,brasno,vino,rakija):
        print('brasno',brasno, 'vino ',vino,'rakija',rakija)
class Prodavnica1(Prodavnica): #povikuvanje na objketo roditel Prodavnica
     def __init__(self):
       super().__init__('tip 500','smederevka','raklija')
class Prodavnica2(Prodavnica):
     def __init__(self):
        super().__init__('tip 500','burgunddec','brendi')
pro1=Prodavnica1()
pro2=Prodavnica2()