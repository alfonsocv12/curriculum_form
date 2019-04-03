class input_verifier():

    def __init__():
        '''
        Funcion constructora
        '''
    def check_if_string(self, msg):
        '''
        Funcion encargada de que el input sea un string
        '''
        while True:
            x = input('{}:'.format(msg))
            try:
                y = 1+int(x)
                print('Introduce letras')
            except:
                return x
                break

    def array_string(self, msg):
        '''
        Funcion encargada de verificar que el arrego
        sea de strings
        '''
        array_string = []
        while True:
            input = self.check_if_string(self,msg)
            if input == 'fin':
                break
            array_string.append(input)
            print()
        return array_string
