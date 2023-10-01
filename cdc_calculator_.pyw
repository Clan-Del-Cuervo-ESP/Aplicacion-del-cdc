from tkinter import *

__root__=Tk()
__root__.title("CDC")
__root__.iconbitmap("img/clan.ico")


__Frame__=Frame(__root__)

__Frame__.pack()

operacion=""

reset_pantalla=False

resultado=0
#------personalizacion----------------------------------------
__Frame__.config(background="#CEDEBD")

__root__.resizable(0,0)

__root__.title("calculadora-CDC")

#-------------------------------------------------------------

#-------------pantalla---------------------------------------

numeroPantalla=StringVar()


pantalla=Entry(__Frame__, textvariable=numeroPantalla)

pantalla.grid(
	row=1, 

	column=1,

	padx=10,

	pady=10,

	columnspan=4)

pantalla.config(

	background="black", 

	fg="#03f943", 
	
	justify="right"
)


#-------------------pulsaciones teclado--------------------------

def numeroPulsado(num):

	global operacion

	global reset_pantalla

	if reset_pantalla!=False:

		numeroPantalla.set(num)

		reset_pantalla=False

	else:
	
		numeroPantalla.set(numeroPantalla.get() + num)


#----------------funcion suma----------------------------------

def suma(num):

	global operacion

	global resultado

	global reset_pantalla

	resultado+=int(num) #resultado=resultado+int(num)

	operacion="suma"

	reset_pantalla=True

	numeroPantalla.set(resultado)



#---------------funcion resta------------------------------
num1=0

contador_resta=0

def resta(num):

	global operacion

	global resultado

	global num1

	global contador_resta

	global reset_pantalla

	if contador_resta==0:

		num1=int(num)

		resultado=num1

	else:

		if contador_resta==1:

			resultado=num1-int(num)

		else:

			resultado=int(resultado)-int(num)	

		numeroPantalla.set(resultado)

		resultado=numeroPantalla.get()


	contador_resta=contador_resta+1

	operacion="resta"

	reset_pantalla=True


#-------------funcion multiplicacion---------------------
contador_multi=0

def multiplica(num):

	global operacion

	global resultado

	global num1

	global contador_multi

	global reset_pantalla
	
	if contador_multi==0:

		num1=int(num)
		
		resultado=num1

	else:

		if contador_multi==1:

			resultado=num1*int(num)

		else:

			resultado=int(resultado)*int(num)	

		numeroPantalla.set(resultado)
		
		resultado=numeroPantalla.get()


	contador_multi=contador_multi+1

	operacion="multiplicacion"

	reset_pantalla=True

#-----------------funcion division---------------------

contador_divi=0

def divide(num):

	global operacion

	global resultado

	global num1

	global contador_divi

	global reset_pantalla
	
	if contador_divi==0:

		num1=float(num)
		
		resultado=num1

	else:

		if contador_divi==1:

			resultado=num1/float(num)

		else:

			resultado=float(resultado)/float(num)	

		numeroPantalla.set(resultado)
		
		resultado=numeroPantalla.get()


	contador_divi=contador_divi+1

	operacion="division"

	reset_pantalla=True



#----------------funcion el_resultado----------------

def el_resultado():

	global resultado

	global operacion

	global contador_resta

	global contador_multi

	global contador_divi
	

	if operacion=="suma":

		numeroPantalla.set(resultado+int(numeroPantalla.get()))

		resultado=0

	elif operacion=="resta":

		numeroPantalla.set(int(resultado)-int(numeroPantalla.get()))

		resultado=0

		contador_resta=0

	elif operacion=="multiplicacion":

		numeroPantalla.set(int(resultado)*int(numeroPantalla.get()))

		resultado=0

		contador_multi=0

	elif operacion=="division":

		numeroPantalla.set(int(resultado)/int(numeroPantalla.get()))

		resultado=0

		contador_divi=0

	




#-------------fila 1---------------------------------------------

boton7=Button(__Frame__,
			  
			    text="7",

			    width=3, 

				command=lambda:numeroPulsado("7"))

boton7.grid(row=2, column=1)

#------------------------------------------------------------------




# ------------------------------------------------------------------

boton8=Button(__Frame__,
			  
			    text="8",

				width=3,

				command=lambda:numeroPulsado("8"))

boton8.grid(row=2, column=2)

#---------------------------------------------------------------------------

boton9=Button(__Frame__,
			    text="9",

				width=3,

			    command=lambda:numeroPulsado("9"))

boton9.grid(row=2, column=3)
# -----------------------------------------------------------------------



botonDiv=Button(__Frame__,
				text="÷",

				width=3,

				command=lambda:divide(numeroPantalla.get()))

botonDiv.grid(row=2,
			column=4)
# --------------------------------------------------------------


#-------------fila 2---------------------------------------------

boton4=Button(__Frame__,
			    text="4",

				width=3,

				command=lambda:numeroPulsado("4"))

boton4.grid(row=3,
			
		 column=1)
# -------------------------------------------------------------------









#------------------------------------------------

boton5=Button(__Frame__,
			  
			    text="5",

				width=3,

				command=lambda:numeroPulsado("5"))

boton5.grid(row=3,
			
			column=2)
#---------------------------------------------------------


boton6=Button(__Frame__,
			    text="6",

				width=3,

				command=lambda:numeroPulsado("6"))

boton6.grid(row=3, column=3)

# ---------------------------------------------------------







# ---------------------------------------------

botonMult=Button(__Frame__,
				 
				text="x",

				width=3,

				command=lambda:multiplica(numeroPantalla.get()))

botonMult.grid(row=3,
			   
			    column=4)
# --------------------------------------------------------------



#-------------fila 3---------------------------------------------

boton1=Button(__Frame__,
			  
			    text="1",

				width=3,

				command=lambda:numeroPulsado("1"))

boton1.grid(row=4, column=1)
# -----------------------------------------------------------------








boton2=Button(__Frame__,
			   text="2",
				 width=3,
				   command=lambda:numeroPulsado("2"))

boton2.grid(row=4,
			 column=2)







boton3=Button(__Frame__,
			   text="3",
				 width=3,
				   command=lambda:numeroPulsado("3"))

boton3.grid(row=4, column=3)







botonRest=Button(__Frame__,
				  text="-",
				    width=3,
					  command=lambda:resta(numeroPantalla.get()))

botonRest.grid(row=4, column=4)


#-------------fila 4---------------------------------------------

boton0=Button(__Frame__,
			   text="0",
				 width=3,
				   command=lambda:numeroPulsado("0"))
boton0.grid(row=5, column=1)




botonComa=Button(__Frame__,
				  text=",",
				    width=3,
					  command=lambda:numeroPulsado("."))
botonComa.grid(row=5, column=2)



botonIgual=Button(__Frame__,
				   text="=",
				   width=3,
					command=lambda:el_resultado())

botonIgual.grid(row=5, column=3)

botonSum=Button(__Frame__,
				 text="+",
				   width=3,
					 command=lambda:suma(numeroPantalla.get()))
botonSum.grid(row=5, column=4)








__root__.mainloop()