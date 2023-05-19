
class DispositivoEntrada:

    def __init__(self, tipo_entrada, marca) -> None:
        self._tipo_entrada = tipo_entrada
        self._marca = marca

    def __str__(self) -> str:
        return f'MARCA: [{self._marca}] TIPO_ENTRADA:[{self._tipo_entrada}]'


if __name__=='__main__':
    entrada = DispositivoEntrada('USB','DELL')
    print(entrada)