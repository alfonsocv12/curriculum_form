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

    def array_string(self, msg, unique=False):
        '''
        Funcion encargada de verificar que el arrego
        sea de strings
        '''
        array_string = []
        while True:
            input = self.check_if_string(self,msg)
            input = self.format(self, input)
            if input == 'fin':
                break
            if unique:
                self.check_if_unique(self, input, array_string)
            else:
                array_string.append(input)
            print()
        return array_string

    def check_if_unique(self, input, array):
        '''
        Funcion encargada de revisar si el
        valor ya fue introducido en el
        arreglo
        '''
        if input in array:
            print('Valor ya introducido')
        else:
            return array.append(input)

    def format(self, input):
        '''
        Funcion dedicated to standarise
        the string to a format of lowercase
        no space
        '''
        output = input.lower().replace(' ','-')
        return output
