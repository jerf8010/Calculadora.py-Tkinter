from tkinter import *
import parser


class app:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        

        self.display = Entry(self.root)
        self.display.grid(row = 0, columnspan = 6, sticky = W + E)
        

        self.i = 0

        self.boton1 = Button(self.root, text = "1", command = lambda: self.get_numbers(1))
        self.boton1.grid(row = 1, column = 0, sticky = W + E)

        self.boton2 = Button(self.root, text = "2", command = lambda: self.get_numbers(2))
        self.boton2.grid(row = 1, column = 1, sticky = W + E)

        self.boton3 = Button(self.root, text = "3", command = lambda: self.get_numbers(3))
        self.boton3.grid(row = 1, column = 2, sticky = W + E)

        self.boton4 = Button(self.root, text = "4", command = lambda: self.get_numbers(4))
        self.boton4.grid(row = 2, column = 0, sticky = W + E)

        self.boton5 = Button(self.root, text = "5", command = lambda: self.get_numbers(5))
        self.boton5.grid(row = 2, column = 1, sticky = W + E)

        self.boton6 = Button(self.root, text = "6", command = lambda: self.get_numbers(6))
        self.boton6.grid(row = 2, column = 2, sticky = W + E)

        self.boton7 = Button(self.root, text = "7", command = lambda: self.get_numbers(7))
        self.boton7.grid(row = 3, column = 0, sticky = W + E)

        self.boton8 = Button(self.root, text = "8", command = lambda: self.get_numbers(8))
        self.boton8.grid(row = 3, column = 1, sticky = W + E)

        self.boton9 = Button(self.root, text = "9", command = lambda: self.get_numbers(9))
        self.boton9.grid(row = 3, column = 2, sticky = W + E)


        self.botonAC = Button(self.root, text = "AC", command = self.clearDisplay)
        self.botonAC.grid(row = 4, column = 0, sticky = W + E)

        self.boton0 = Button(self.root, text = "0", command = lambda: self.get_numbers(0))
        self.boton0.grid(row = 4, column = 1, sticky = W + E)

        self.botonPorc = Button(self.root, text = "%", command = lambda: self.get_operation("%"))
        self.botonPorc.grid(row = 4, column = 2, sticky = W + E)


        self.botonSum = Button(self.root, text = "+", command = lambda: self.get_operation("+"))
        self.botonSum.grid(row = 1, column = 3, sticky = W + E)

        self.botonRes = Button(self.root, text = "-", command = lambda: self.get_operation("-"))
        self.botonRes.grid(row = 2, column = 3, sticky = W + E)

        self.botonMul = Button(self.root, text = "x", command = lambda: self.get_operation("*"))
        self.botonMul.grid(row = 3, column = 3, sticky = W + E)

        self.botonDiv = Button(self.root, text = "/", command = lambda: self.get_operation("/"))
        self.botonDiv.grid(row = 4, column = 3, sticky = W + E)




        self.botonDel = Button(self.root, text = "←", command = self.undo)
        self.botonDel.grid(row = 1, column = 4, columnspan = 2, sticky = W + E)

        self.botonExp = Button(self.root, text = "exp", command = lambda: self.get_operation("**"))
        self.botonExp.grid(row = 2, column = 4, sticky = W + E)

        self.botonPow2 = Button(self.root, text = "^2", command = lambda: self.get_operation("**2"))
        self.botonPow2.grid(row = 2, column = 5, sticky = W + E)

        self.botonLeft = Button(self.root, text = "(", command = lambda: self.get_operation("("))
        self.botonLeft.grid(row = 3, column = 4, sticky = W + E)

        self.botonRight = Button(self.root, text = ")", command = lambda: self.get_operation(")"))
        self.botonRight.grid(row = 3, column = 5, sticky = W + E)

        self.botonEq = Button(self.root, text = "=", command = self.calculate)
        self.botonEq.grid(row = 4, column = 4, columnspan = 2, sticky = W + E)


    def get_numbers( self, n ):
        self.display.insert( self.i , n)
        self.i += 1
    
    def get_operation( self, operator ):
        operatorLen = len(operator) 
        self.display.insert( self.i, operator )
        self.i += operatorLen

    def clearDisplay(self):
        self.display.delete(0, END)

    def undo(self):
        displayState = self.display.get()
        if len(displayState):
            displayNewState = displayState[:-1]
            self.clearDisplay()
            self.display.insert(0, displayNewState)
        
        else:
            self.clearDisplay()
            self.display.insert(0, 'Error')

    def calculate( self ):
        displayState = self.display.get()

        try:
            mathExpression = parser.expr(displayState).compile()
            result = eval(mathExpression)
            self.clearDisplay()
            self.display.insert(0, result)
        except:
            self.clearDisplay()
            self.display.insert(0, "Error!!!!!")



if __name__ == '__main__':
    root = Tk()
    aplicacion = app(root)
    root.mainloop()