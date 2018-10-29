import math as mt

class Layer:

    def __init__(self, params):
        self.__refraction_index = params['refraction'] or 1
        self.__input_angle = params['input'] or 0
        self.__output_angle = params['output'] or 0
    
    def getInput(self):
        return self.__output_angle

    def getOutput(self):
        return self.__output_angle

    def proc(self, inc, inp_ref = 1, out_ref = 1):
        alpha_1 = self.__input_angle
        alpha_2 = self.__output_angle

        beta_1 = inc                        # Input angle horizontal
        theta_1 = beta_1 - alpha_1          # Input angle relative

        theta_1 = mt.radians(theta_1)      
        theta_2 = mt.degrees(mt.asin((inp_ref/self.__refraction_index)*mt.sin(theta_1)))        # Snell law

        beta_2 = theta_2 + alpha_1          # Internal angle horizontal

        gamma_1 = 90 - alpha_2
        gamma_2 = 180 - gamma_1
        gamma_3 = 180 - beta_2 - gamma_2

        theta_3 = 90 - gamma_3

        beta_3 = theta_3 - alpha_2

        theta_3 = mt.radians(theta_3)
        try:
            theta_4 = mt.degrees(mt.asin((self.__refraction_index/inp_ref)*mt.sin(theta_3)))        # Snell law
        except:
            theta_4 = 0
        beta_4 = theta_4 - alpha_2

        # print("t1 = {:.2f}\t t2 = {:.2f}\t t3 = {:.2f}\t t4 = {:.2f}".format(mt.degrees(theta_1), theta_2, mt.degrees(theta_3), theta_4))
        # print("b1 = {:.2f}\t b2 = {:.2f}\t b3 = {:.2f}\t b4 = {:.2f}".format(beta_1, beta_2, beta_3, beta_4))

        output = {
            'b1' : beta_1,
            'b2' : beta_2,
            'b3' : beta_3,
            'b4' : beta_4,
            't1' : theta_1,
            't2' : theta_2,
            't3' : theta_3,
            't4' : theta_4
        }

        return output

    def __add__(self, sl):
        return self.__input_angle + sl.__input_angle