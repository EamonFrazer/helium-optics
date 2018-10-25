class Layer:

    def __init__(self, params):
        self.__refraction_index = params['refraction']
        self.__input_angle = params['input'] or None
        self.__output_angle = params['output'] or None
    
    def getInput(self):
        return self.__output_angle

    def getOutput(self):
        return self.__output_angle