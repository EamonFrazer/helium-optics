import math as mt

class Layer:

    def __init__(self, params):
        self.__refraction_index = params['refraction'] or 1
        self.__input_angle = params['input'] or 0
    
    def getInputAngle(self):
        return self.__input_angle

    def getIndex(self):
        return self.__refraction_index

def snell(incidence, input_layer, output_layer):
    index_1 = input_layer.getIndex()
    index_2 = output_layer.getIndex()

    alpha = output_layer.getInputAngle()
    
    beta_1 = incidence
    theta_1 = beta_1 - alpha
    theta_1 = mt.radians(theta_1)
    try:      
        theta_2 = mt.degrees(mt.asin((index_1/index_2)*mt.sin(theta_1)))
    except:
        theta_2 = 0

    beta_2 = theta_2 + alpha

    return [beta_2, theta_2]