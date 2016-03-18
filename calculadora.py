

class Calculadora:

    def sumar(self, a, b):
        return a+b

    def restar(self, a, b):
        return a-b
        
    def multiplicar (self, a, b):
        return a*b

    def dividir (self, a, b):
        return a/b
        
    def dale(self):
        seguir=True
        
        while(seguir):
            cmd = input("Comando (SUMAR|RESTAR|MULTIPLICAR|DIVIDIR|SALIR) (PARAMETRO1 PARAMETRO2): ")
            args = cmd.split(" ")

            if(args[0]=="SALIR"):
                seguir=False
            elif(args[0]=="SUMAR" and len(args) == 3):
                print( self.sumar( float(args[1]), float(args[2]) ) )
            elif(args[0]=="RESTAR" and len(args) == 3):
                print( self.restar( float(args[1]), float(args[2]) ) )
            elif(args[0]=="MULTIPLICAR" and len(args) == 3):
                print( self.multiplicar( float(args[1]), float(args[2]) ) )
            elif(args[0]=="DIVIDIR" and len(args) == 3):
                print( self.dividir( float(args[1]), float(args[2]) ) )               
            else:
                print("Error, commando/parametros erroneos")
        

    def __init__(self):
        pass



def main():
    Calculadora().dale()


if __name__ == '__main__':
    main()
