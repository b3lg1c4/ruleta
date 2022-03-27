from random import randint

class Ruleta:

    def __girar_ruleta(self):
        return self.TABLERO[randint(0,36)]

    def __pleno(self,apuesta, resultado):
        
        if type(apuesta) == int and 0 <= apuesta <= 36:
            return apuesta == resultado["numero"]
        else:
            raise Exception("apuesta para PLENO debe recibir 'int' entre 0 y 36")

    def __semipleno(self,apuesta,resultado):


        numeros_en_el_intervalo = 1 <= apuesta[0] <= 36 and 1 <= apuesta[1] <= 36
        segundo_numero_valido = apuesta[1] == apuesta[0] - 1 or apuesta[1] == apuesta[0] + 3
       
        if type(apuesta) == list and numeros_en_el_intervalo and segundo_numero_valido:
            return resultado["numero"] in apuesta
        else:
            raise Exception("apuesta para SEMI-PLENO debe recibir 'list' con [n, n-1|n+3]")
    
    def __color(self,apuesta,resultado):
        
        if apuesta in ["R","N"]:
            return resultado["color"] == apuesta
        else:
            raise Exception("apuesta para COLOR debe ser 'R' o 'N'")
   
    
    def __par_impar(self,apuesta,resultado):
        
        if apuesta in ["PAR", "IMPAR"]:
            resultado_es_par = resultado["numero"] % 2 == 0 and resultado["numero"] != 0
            return apuesta == "PAR" and resultado_es_par

        else:
            raise Exception("apuesta para PAR-IMPAR debe ser 'PAR' o 'IMPAR'")

    def __docena(self,apuesta,resultado):
        
        if 1 <= apuesta <= 3:
            

            INTERVALOS = {
                1: [1,12],
                2: [13,24],
                3: [25,36]
            }

            return INTERVALOS[apuesta][0] <= resultado["numero"] <= INTERVALOS[apuesta][1]

        else:
            raise Exception("apuesta para DOCENA debe ser 'int' entre 1 y 3")

    def __columna(self,apuesta,resultado):
        
        if 1 <= apuesta <= 3:
            columna = resultado["numero"] % 3
            
            columna = 3 if columna == 0 else columna

            return columna == apuesta

        else:
            raise Exception("apuesta para COLUMNA debe ser 'int' entre 1 y 3")

    def __mitad(self,apuesta,resultado):
        
        if apuesta == 1 or apuesta == 2:

            INTERVALOS = {
                1: [1,18],
                2: [19,36]
            }

            return INTERVALOS[apuesta][0] <= resultado["numero"] <= INTERVALOS[apuesta][1]
        else:
            raise Exception("apuesta para MITAD debe ser 'int' siendo 1 o 2")

    def __calle(self,apuesta,resultado):

        if 1 <= apuesta <= 12:

            if resultado["numero"] == 0: 
                return False
            
            resto = resultado["numero"] % 3

            POSIBLES_CALLES = {
                0: [resultado["numero"], resultado["numero"] - 1, resultado["numero"] - 2],
                1: [resultado["numero"], resultado["numero"] + 1, resultado["numero"] + 2],
                2: [resultado["numero"] - 1, resultado["numero"], resultado["numero"] + 1]
            }


            return apuesta * 3 in POSIBLES_CALLES[resto]

        else:
            raise Exception("apuesta para CALLE debe ser 'int' entre 1 y 12")

    def __cuadro(self,apuesta,resultado):
        numeros_arriba = apuesta[0]
        numeros_abajo = apuesta[1]
        
        primera_diferencia_valida = numeros_arriba[1] - numeros_arriba[0] == 3 and numeros_abajo[1] - numeros_abajo[0] == 3
        segunda_diferencia_valida = numeros_arriba[0] - numeros_abajo[0] == 1 and numeros_arriba[1] - numeros_abajo[1] == 1
        numeros_dentro_del_intervalo = True

        cuadro_plano = [item for sublist in apuesta for item in sublist]

        for num in cuadro_plano:
            if not 1 <= num <= 36:
                numeros_dentro_del_intervalo = False
                break

        if type(apuesta) == list and primera_diferencia_valida and segunda_diferencia_valida and numeros_dentro_del_intervalo:
            return resultado["numero"] in cuadro_plano
        
        else:
            raise Exception("apuesta para CUADRO debe ser 'list' de un cuadro de la ruleta válido [[n,n+3],[n-1,n+2]]")

    
    def __linea(self,apuesta,resultado):
        
        primer_numero_linea = 3
        lineas = {}

        for i in range(1,12):

            numeros_en_linea = []
            actual = primer_numero_linea

            for j in range(0,3):
                numeros_en_linea.append(actual)
                numeros_en_linea.append(actual + 3)
                actual -= 1
            lineas[i] = numeros_en_linea
            primer_numero_linea += 3

        return resultado["numero"] in lineas[apuesta]

    def __0_1_2_3(self,apuesta,resultado):
        return resultado["numero"] in [0,1,2,3]

    TABLERO = [
                {3:"R"},{6:"N"},{9:"R"},{12:"R"},{15:"N"},{18:"R"},{21:"R"},{24:"N"},{27:"R"},{30:"R"},{33:"N"},{36:"R"},
      {0:"V"}  ,{2:"N"},{5:"R"},{8:"N"},{11:"N"},{14:"R"},{17:"N"},{20:"N"},{23:"R"},{26:"N"},{29:"N"},{32:"R"},{35:"N"},
                {1:"R"},{4:"N"},{7:"R"},{10:"N"},{13:"N"},{16:"R"},{19:"R"},{22:"N"},{25:"R"},{28:"N"},{31:"N"},{34:"R"}
    ]


    JUGADAS = {
        "PLENO": {
            "multiplicador":35,
            "accion": __pleno

        },
        "SEMI-PLENO": {
            "multiplicador": 17,
            "accion": __semipleno
        },

        "CALLE": {
            "multiplicador": 11,
            "accion": __calle
        },

        "CUADRO": {
            "multiplicador": 8,
            "accion": __cuadro
        },

        "0-1-2-3": {
            "multiplicador": 8,
            "accion": __0_1_2_3
        },

        "LINEA": {
            "multiplicador": 5,
            "accion": __linea
        },

        "DOCENA":{
            "multiplicador": 2,
            "accion": __docena
        },

        "COLUMNA":{
            "multiplicador": 2,
            "accion": __columna
        },

        "COLOR": {
            "multiplicador": 1,
            "accion": __color
        },
        "PAR-IMPAR":{
            "multiplicador": 1,
            "accion": __par_impar
        },


        "MITAD": {
            "multiplicador": 1,
            "accion": __mitad
        },

        
    }

    
    def tirar(self,informacion_apuesta):

        if not (type(informacion_apuesta["dinero"]) == int and informacion_apuesta["dinero"] > 0):
            raise Exception("El dinero debe ser entero mayor a 0")
        
        if informacion_apuesta["jugada"] in self.JUGADAS:

            resultado = {
                "victoria": None,
                "ruleta": None,
                "ganancia": -informacion_apuesta["dinero"]
            }

            tirada = self.__girar_ruleta()

            tirada = {
                "numero": list(tirada.keys())[0],
                "color": list(tirada.values())[0]
            }

            resultado["ruleta"] = tirada

            es_victoria = self.JUGADAS[informacion_apuesta["jugada"]]["accion"](self, informacion_apuesta["apuesta"], tirada)

            resultado["victoria"] = es_victoria 

            if es_victoria:
                resultado["ganancia"] = informacion_apuesta["dinero"] * self.JUGADAS[informacion_apuesta["jugada"]]["multiplicador"]

            return resultado
        else:
            raise Exception(informacion_apuesta["jugada"] +  " no es un tipo de jugada válido")



    @classmethod
    def generador(cls,dinero = None, jugada = None):

        if dinero != None:
            if not (type(dinero) == int and dinero > 0):
                raise Exception("dinero debe ser 'int' mayor a 0") 



        POSIBLES_JUGADAS = list(cls.JUGADAS.keys())
        
        if jugada != None:
            if not jugada in POSIBLES_JUGADAS:
                raise Exception("jugada debe ser una de las posibles, ver JUGADAS")



        parametros = {
            "dinero": dinero if dinero != None else randint(1,1000),
            "jugada": jugada if jugada != None else POSIBLES_JUGADAS[randint(0, len(POSIBLES_JUGADAS) - 1)],
            "apuesta": None
        }

        if parametros["jugada"] == "PLENO":
            parametros["apuesta"] = randint(0,36)
        
        elif parametros["jugada"] == "SEMI-PLENO":
            n = randint(2,33)
            direccion = randint(0,1) #0-ABAJO 1-DERECHA
            parametros["apuesta"] = [n,n-1 if direccion == 0 else n+3]

        elif parametros["jugada"] == "CALLE":
            parametros["apuesta"] = randint(1,12)
        
        elif parametros["jugada"] == "COLOR":
            color = randint(0,1)
            parametros["apuesta"] = "R" if color == 0 else "N"

        elif parametros["jugada"] == "PAR-IMPAR":
            paridad = randint(0,1)
            parametros["apuesta"] = "PAR" if paridad == 0 else "IMPAR"
        
        elif parametros["jugada"] in ["DOCENA","COLUMNA"]: 
            parametros["apuesta"] = randint(1,3)

        elif parametros["jugada"] == "MITAD":
            parametros["apuesta"] = randint(1,2)

        elif parametros["jugada"] == "LINEA":
            parametros["apuesta"] = randint(1,11)
        
        elif parametros["jugada"] == "CUADRO":
            n = randint(2,33)
            parametros["apuesta"] = [[n,n+3],[n-1,n+2]]

        return parametros

        


ruleta = Ruleta()

tirada1 = ruleta.tirar({"dinero": 350, "jugada": "LINEA", "apuesta": 2}) # <-- MANUAL
tirada2 = ruleta.tirar(Ruleta.generador()) # <-- AUTOMÁTICO CON DINERO Y JUGADA VARIABLES
tirada3 = ruleta.tirar(Ruleta.generador(350,"CUADRO")) # <-- AUTOMÁTICO CON DINERO Y JUGADA FIJOS

"""

    INSTRUCCIONES
    -------------

    ruleta = Ruleta() --> se crea la instancia
    jugada = Ruleta.generador() --> se genera la jugada aleatoria, también se pueden ingresar jugadas manuales sin el generador

    ruleta.tirar(jugada) --> se realiza una tirada con la jugada cargada previamente

    Ruleta.generador(300,"PLENO") --> el generador también permite setear el dinero y la jugada de manera fija

    POSIBLES JUGADAS
    ----------------

    ruleta = Ruleta()

    PLENO --> ruleta.tirar({"jugada": "PLENO", "dinero": n, "apuesta": n})
    SEMI-PLENO --> ruleta.tirar({"jugada": "SEMI-PLENO", "dinero": n, "apuesta": [n,n-1|n+3]})
    CALLE --> ruleta.tirar({"jugada": "SEMI-PLENO", "dinero": n, "apuesta": n})
    COLOR --> ruleta.tirar({"jugada": "COLOR", "dinero": n, "apuesta": "R"})  o también ..."apuesta": "N"
    PAR-IMPAR --> ruleta.tirar({"jugada": "PAR-IMPAR", "dinero": n, "apuesta": "PAR"})  o también ..."apuesta": "IMPAR"
    DOCENA --> ruleta.tirar({"jugada": "DOCENA", "dinero": n, "apuesta": n})
    COLUMNA --> ruleta.tirar({"jugada": "COLUMNA", "dinero": n, "apuesta": n})
    MITAD --> ruleta.tirar({"jugada": "MITAD", "dinero": n, "apuesta": n})
    LINEA --> ruleta.tirar({"jugada": "LINEA", "dinero": n, "apuesta": n})
    CUADRO --> ruleta.tirar({"jugada": "CUADRO", "dinero": n, "apuesta": [[n,n + 3],[n - 1, n+2]]}) 
    0-1-2-3 --> ruleta.tirar({"jugada": "0-1-2-3", "dinero": n, "apuesta": None}) 




                    DISPOSICION DEL TABLERO CON LAS JUGADAS

                                11 LINEAS(1 - 11)

    ********************************************************************
    *     *                  *                   *                     *
    *     *   3   6   9   12 * 15   18   21   24 * 27   30   33   36   *    < COLUMNA: 3
    *     *                  *                   *                     *
    *  0  *   2   5   8   11 * 14   17   20   23 * 26   29   32   35   *    < COLUMNA: 2
    *     *                  *                   *                     *
    *     *   1   4   7   10 * 13   16   19   22 * 25   28   31   34   *    < COLUMNA: 1
    *     *                  *                   *                     *
    ********************************************************************
            
    CALLES    ^   ^   ^   ^    ^    ^    ^    ^    ^    ^    ^    ^
              1   2   3   4    5    6    7    8    9   10   11   12

                    ^                  ^                  ^
                DOCENA: 1           DOCENA: 2         DOCENA: 3            

                       ^                           ^
                    MITAD: 1                    MITAD: 2

                        
"""