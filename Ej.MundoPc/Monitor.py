
class Monitor:
    contador_monitor = 0
    @classmethod
    def Contador_Monitor(cls):
        cls.contador_monitor+=1
        return cls.contador_monitor
    
    def __init__(self, marca, tamaño) -> None:
        self._id_monitor =  Monitor.Contador_Monitor()
        self._marca = str(marca)
        self._tamaño = str(tamaño)
    
    @property
    def marca (self):
        return self._marca
    
    def __str__(self) -> str:
        return f'ID_MONITOR:[{self._id_monitor}] MARCA:[{self._marca} TAMAÑO:[{self._tamaño}]]'
    
if __name__=='__main__':
    monitor1 = Monitor('LG','900')
    print(monitor1)