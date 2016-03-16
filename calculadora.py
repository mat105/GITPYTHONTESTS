

class Calculadora:

    def sumar(self, a, b):
        return a+b

    def restar(self, a, b):
        return a-b

    def dale(self):
        seguir=True
        
        while(seguir):
            cmd = input("Comando (SUMAR|RESTAR|SALIR) (PARAMETRO1 PARAMETRO2)")

            args = cmd.split(" ")

            if(args[0]=="SALIR"):
                seguir=False
            elif(args[0]=="SUMAR" and len(args) == 3):
                print( self.sumar( int(args[1]), int(args[2]) ) )
            elif(args[0]=="RESTAR" and len(args) == 3):
                print( self.restar( int(args[1]), int(args[2]) ) )
            else:
                print("Error, commando erroneo")
        

    def __init__(self):
        pass



def main():
    Calculadora().dale()


if __name__ == '__main__':
    main()
