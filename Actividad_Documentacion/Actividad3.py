from math import sqrt


class Calculos:
    """
    Calculos varios

    Atributos(Ecuación de segundo grado ax^2 + bx + c = 0)

    op1:
        primer operando(representado por a)
    op2:
        segundo operando(representado por b)
    op3:
        segundo tercer(representado por c)

    Atributos(Calculo de la gravedad)

    op1:
        masa del planeta
    op2:
        radio del planeta
    op3:
        valor vacio(0)

    Metodos

    ecu_2grado:
        Calcula la ecuación de segundo grado de los valores introducidos
        devolviendo dos resultados
    gravedad:
        Calcula la gravedad de un planeta

        Masas y radios de los planetas en el sistema solar:

        Mercurio:
            Radio(m): 2.34*10**(6)
            Masa(kg): 3.28*10**(23)
        Venus:
            Radio(m): 6.26*10**(6)
            Masa(kg): 4.83*10**(24)
        Tierra:
            Radio(m): 6.37*10**(6)
            Masa(kg): 5.98*10**(24)
        Marte:
            Radio(m): 3.32*10**(6)
            Masa(kg): 6.40*10**(23)
        Júpiter:
            Radio(m): 6.98*10**(7)
            Masa(kg): 1.90*10**(27)
        Saturno:
            Radio(m): 5.82*10**(7)
            Masa(kg): 5.98*10**(26)
        Urano:
            Radio(m): 2.37*10**(7)
            Masa(kg): 8.67*10**(25)
        Neptuno:
            Radio(m): 2.24*10**(7)
            Masa(kg): 1.05*10**(26)

        Ejemplo gravedad de la Tierra
        
        >>> G = G = 6.67384*10**(-11) "constante de la gravitación universal"
        >>> M = 6.37*10**(6)
        >>> r = 5.98*10**(24)
        >>> g = G*M/r**2
        >>> print(g)

    """
    def __init__(self, op1, op2, op3):
        self.op1 = op1
        self.op2 = op2
        self.op3 = op3

    def ecu_2grado(self):
        """
        Calcula la ecuaciónde segundo grado con los valores introducidos
        """
        if ((self.op2**2)-4*self.op1*self.op3) < 0:
            print("La solución de la ecuación es con numeros complejos")
        else:
            x1 = (-self.op2+sqrt(self.op2**2-(4*self.op1*self.op3)))/(2*self.op1)
            x2 = (-self.op2-sqrt(self.op2**2-(4*self.op1*self.op3)))/(2*self.op1)
            print("Las soluciones de la ecuación son:")
            print(x1)
            print(x2)

    def gravedad(self):
        """
        Calcula la gravedad de un planeta
        """
        G = 6.67384*10**(-11)

        g = G*self.op1/self.op2**2
        return g
