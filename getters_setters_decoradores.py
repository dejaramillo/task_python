
class CasillaVotacion:
    def __init__(self, id,  country):
        self.__id = id
        self.__country = country
        self.__region = None

    @property
    def region(self):
        return self.__region

    @region.setter
    def region(self, region):
        if region in self.__country:
            self.__region = region
        else:
            raise ValueError(f'La {region} no es valida en el {self.__country}')

if __name__ == '__main__':
    casilla = CasillaVotacion(123,['Ciudad de Mexico', 'Morelos'])
    print(casilla.region)
    casilla.region = 'Ciudad de Mexico'
    print(casilla.region)
