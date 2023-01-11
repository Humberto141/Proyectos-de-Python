# LANE FINAL PARA PROFE
#####################################################################################
######################### PROGRAMA ALGORITMO DE KENNETH LANE ########################
#####################################################################################

##############################################
############ LIBRERIAS REQUERIDAS ############
##############################################

import pandas as pd 
import math as mt 
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from sklearn.linear_model import LinearRegression 
from sklearn.preprocessing import PolynomialFeatures
from scipy.optimize import curve_fit
from tkinter import *

################################################################################
############## LINEAS DE CODIGO PARA EJECUTAR LA INTERFAZ GRAFICA ##############
################################################################################
########################## INGRESO DE BASE DE DATOS ############################
######################### Y DE PARAMETROS ECONOMICOS ###########################
################################################################################

def agrega_ley_minima():
    if entrada_ley_minima.get() != (''):
        lstley_minima.insert(END, entrada_ley_minima.get())
        entrada_ley_minima.set('')

def quita_ley_minima():
    lstley_minima.delete(END, entrada_ley_minima.set(''))

def agrega_ley_maxima():
    if entrada_ley_maxima.get() != (''):
        lstley_maxima.insert(END, entrada_ley_maxima.get())
        entrada_ley_maxima.set('')

def quita_ley_maxima():
    lstley_maxima.delete(END, entrada_ley_maxima.set(''))

def agrega_tonelaje():
    if entrada_toneladas.get() != (''):
        lst_toneladas.insert(END, entrada_toneladas.get())
        entrada_toneladas.set('')

def quita_tonelaje():
    lst_toneladas.delete(END, entrada_toneladas.set(''))

def funcionsuma():
    global m
    m = float(txt1.get())
    global c
    c = float(txt2.get())
    global r
    r = float(txt3.get())
    global precio_cobre
    precio_cobre = float(txt4.get())
    global d
    d = float(txt5.get())
    global f     
    f = float(txt6.get())
    global h_reha
    h_reha = float(txt7.get())
    global CAPACIDAD_PLANTA
    CAPACIDAD_PLANTA = float(txt8.get())
    global R 
    R = float(txt9.get())
    global y 
    y = float(txt10.get())
    global ley_conc
    ley_conc = float(txt11.get())
    global perdida_metalurgica
    perdida_metalurgica = float(txt12.get())
    global TC 
    TC = float(txt13.get())
    global rc 
    rc = float(txt14.get())
    global respuesta
    respuesta = str(txt15.get())  ############# OJO 
    global e 
    e = float(txt16.get())
    global datos_ley_minima_2
    datos_ley_minima_2 = lstley_minima.get(first=0, last=100)
    global datos_ley_maxima
    datos_ley_maxima = lstley_maxima.get(first=0, last=100)
    global datos_toneladas
    datos_toneladas = lst_toneladas.get(first=0, last=100)
    ventana.destroy()

ventana = Tk()
ventana.title("INGRESO DE DATOS ALGORITMO DE LANE")
ventana.geometry("1080x800")
ventana.config(bg="papaya whip")

lbl0 = Label(ventana, text= "INGRESO DE PARAMETROS ECONÓMICOS")
lbl0.place(x=20, y= 10, width = 400, height = 30)
lbl0.config(font=("Cambria Math", "10", "bold"))

lbl1 = Label(ventana, text = "Costo Mina en usd/ton")
lbl1.place(x=20, y=50, width = 200, height = 30)
txt1 = Entry(ventana, bg="pink")
txt1.place(x=260, y = 50, width=100, height=30)
txt1.config(font=("Calibri", "12"))

lbl2 = Label(ventana, text = "Costo Planta en usd/ton")
lbl2.place(x=20, y=90, width = 200, height = 30)
txt2 = Entry(ventana, bg="pink")
txt2.place(x=260, y = 90, width=100, height=30)
txt2.config(font=("Calibri", "12"))

lbl3 = Label(ventana, text = "Costo de venta" "\n""en usd/ton de cobre fino")
lbl3.place(x=20, y=130, width = 200, height = 30)
txt3 = Entry(ventana, bg="pink")
txt3.place(x=260, y = 130, width=100, height=30)
txt3.config(font=("Calibri", "12"))

lbl4 = Label(ventana, text = "Precio del Cobre en cusd/lb")
lbl4.place(x=20, y=170, width = 200, height = 30)
txt4 = Entry(ventana, bg="pink")
txt4.place(x=260, y = 170, width=100, height=30)
txt4.config(font=("Calibri", "12"))

lbl5 = Label(ventana, text = "Tasa de Descuento en %")
lbl5.place(x=20, y=210, width = 200, height = 30)
txt5 = Entry(ventana, bg="pink")
txt5.place(x=260, y = 210, width=100, height=30)
txt5.config(font=("Calibri", "12"))

lbl6 = Label(ventana, text = "Costo Fijo Anual en usd")
lbl6.place(x=20, y=250, width = 200, height = 30)
txt6 = Entry(ventana, bg="pink")
txt6.place(x=260, y = 250, width=100, height=30)
txt6.config(font=("Calibri", "12"))

lbl7 = Label(ventana, text = "Costo de Rehabilitación del Botadero" "\n" "usd/ton de esteril")
lbl7.place(x=20, y=290, width = 200, height = 30)
txt7 = Entry(ventana, bg="pink")
txt7.place(x=260, y = 290, width=100, height=30)
txt7.config(font=("Calibri", "12"))


lbl8 = Label(ventana, text = "Capacidad de la Planta Concentradora" "\n" "en Toneladas")
lbl8.place(x=20, y=330, width = 200, height = 30)
txt8 = Entry(ventana, bg="pink")
txt8.place(x=260, y = 330, width=100, height=30)
txt8.config(font=("Calibri", "12"))

lbl9 = Label(ventana, text = "Capacidad de producción de " "\n" "la Refinería en Toneladas")
lbl9.place(x=20, y=370, width = 200, height = 30)
txt9 = Entry(ventana, bg="pink")
txt9.place(x=260, y = 370, width=100, height=30)
txt9.config(font=("Calibri", "12"))

lbl10 = Label(ventana, text = "Recuperación de la Planta " "\n" "Concentradora en %")
lbl10.place(x=20, y=410, width = 200, height = 30)
txt10 = Entry(ventana, bg="pink")
txt10.place(x=260, y = 410, width=100, height=30)
txt10.config(font=("Calibri", "12"))

lbl11 = Label(ventana, text = "Ley del Concentrado de Cobre " "\n" " en %")
lbl11.place(x=20, y=450, width = 200, height = 30)
txt11 = Entry(ventana, bg="pink")
txt11.place(x=260, y = 450, width=100, height=30)
txt11.config(font=("Calibri", "12"))

lbl12 = Label(ventana, text = "Perdida Metalúrgica de la " "\n" "Fundición y Refinería en %")
lbl12.place(x=20, y=490, width = 200, height = 30)
txt12 = Entry(ventana, bg="pink")
txt12.place(x=260, y = 490, width=100, height=30)
txt12.config(font=("Calibri", "12"))

lbl13 = Label(ventana, text = "Cargo TC en usd/TMS de concentrado")
lbl13.place(x=20, y=530, width = 200, height = 30)
txt13 = Entry(ventana, bg="pink")
txt13.place(x=260, y = 530, width=100, height=30)
txt13.config(font=("Calibri", "12"))

lbl14 = Label(ventana, text = "Cargo RC en cusd/lb " "\n" " ")
lbl14.place(x=20, y=570, width = 200, height = 30)
txt14 = Entry(ventana, bg="pink")
txt14.place(x=260, y = 570, width=100, height=30)
txt14.config(font=("Calibri", "12"))

lbl15 = Label(ventana, text = "¿Quieres incluir Economias de Escalas?" "\n" "ESCRIBE SOLO LA PALABRA SI O NO")
lbl15.place(x=0, y=610, width = 250, height = 30)
txt15 = Entry(ventana, bg="yellow")
txt15.place(x=260, y = 610, width=100, height=30)
txt15.config(font=("Calibri", "12"))

lbl16 = Label(ventana, text = "Costo de extracción del esteril en" "\n" "usd/ton (SI NO QUIERE Economias de Escalas" "\n" "DEBE INGRESAR SOLO EL NUMERO 0)")
lbl16.place(x=0, y=650, width = 250, height = 40)
txt16 = Entry(ventana, bg="yellow")
txt16.place(x=260, y = 657, width=100, height=30)
txt16.config(font=("Calibri", "12"))
################################################################################
#################### CONSTRUCCION DE TABLAS PARA INGRESO #######################
####################### DE LA DISTRIBUCION DE LEYES ############################
################################################################################

lblx = Label(ventana, text= "INGRESO DE LA DISTRIBUCIÓN DE LEYES")
lblx.place(x=530, y= 10, width = 400, height = 30)
lblx.config(font=("Cambria Math", "10", "bold"))

lbl_ley_minima = Label(ventana, text="Ingrese la Ley Mínima en %").place(x=470, y=50)
lstley_minima = Listbox(ventana)

lstley_minima.place(x=470, y=170, width=150, height=500)
entrada_ley_minima = StringVar()
txt_ley_minima = Entry(ventana, textvariable=entrada_ley_minima, width=18,font=("Calibri", "12")).place(x=470, y =80)

btn_agregar_ley_minima = Button(ventana, text="Agregar Dato", height=1, width=20, command=agrega_ley_minima, fg="white", bg="green", cursor="hand2").place(x=470, y = 110)
btn_cancelar_ley_minima = Button(ventana, text="Cancelar Dato", height=1, width=20, command=quita_ley_minima, bg="red", cursor="hand2").place(x=470, y=140)

############################################################################################################
lbl_ley_maxima = Label(ventana, text="Ingrese la Ley Maxima en %").place(x=630, y=50)
lstley_maxima = Listbox(ventana)

lstley_maxima.place(x=630, y=170, width=150, height=500)
entrada_ley_maxima = StringVar()
txt_ley_maxima = Entry(ventana, textvariable=entrada_ley_maxima, width=18, font=("Calibri", "12")).place(x=630, y =80)

btn_agregar_ley_maxima = Button(ventana, text="Agregar Dato", height=1, width=20, command=agrega_ley_maxima, fg="white", bg="green", cursor="hand2").place(x=630, y = 110)
btn_cancelar_ley_maxima = Button(ventana, text="Cancelar Dato", height=1, width=20, command=quita_ley_maxima, bg="red", cursor="hand2").place(x=630, y=140)

############################################################################################################
lbl_toneladas = Label(ventana, text="Ingrese el Tonelaje en Millones de Toneladas").place(x=790, y=50)
lst_toneladas = Listbox(ventana)

lst_toneladas.place(x=790, y=170, width=150, height=500)
entrada_toneladas = StringVar()
txt_toneladas = Entry(ventana, textvariable=entrada_toneladas, width=18, font=("Calibri", "12")).place(x=790, y =80)

################# CONFIGURACION DE LISTBOXS ##################
barra_leyminima = Scrollbar(ventana, command=lstley_minima.yview)
barra_leyminima.place(x=620, y=170, width=15, height=500)

barra_leymaxima = Scrollbar(ventana, command=lstley_maxima.yview)
barra_leymaxima.place(x=780, y=170, width=20, height=500)

barra_tonelaje = Scrollbar(ventana, command=lst_toneladas.yview)
barra_tonelaje.place(x=940, y=170, width=20, height=500)

lstley_minima.config(borderwidth=3, justify='center', yscrollcommand=barra_leyminima,font=("Calibri", "12"))
lstley_maxima.config(borderwidth=3, justify='center', yscrollcommand=barra_leymaxima,font=("Calibri", "12"))
lst_toneladas.config(borderwidth=3, justify='center', yscrollcommand=barra_tonelaje,font=("Calibri", "12"))

btn_agregar_toneladas = Button(ventana, text="Agregar Dato", height=1, width=20, command=agrega_tonelaje, fg="white", bg="green", cursor="hand2").place(x=790, y = 110)
btn_cancelar_toneladas = Button(ventana, text="Cancelar Dato", height=1, width=20, command=quita_tonelaje, bg="red", cursor="hand2").place(x=790, y=140)

lbl_titulo_1 = Label(ventana, text="ALGORITMO DE LANE", font=("Cambia Math", "20", "bold")).place(x=1080, y=70)
lbl_titulo_2 = Label(ventana, text="Consideraciones sobre el Ingreso de Datos:", font=("Cambia Math", "14", "bold")).place(x=1030, y=120)
lbl_titulo_3 = Label(ventana, text="Todos los datos ingresados no deben llevar espacios, es decir," "\n" "solo ingrese el numero considerando en todo momento" "\n" 
"el separador decimal como el punto y NO como la coma." "\n"
"Para el ingreso de la ley del concentrado, recuperación"  "\n" 
"metalúrgica, recuperación de la planta concentradora"  "\n" 
"y tasa de descuento debe ingresarlas en porcentaje %" "\n"
"si cada uno de estos parámetros valen, por ejemplo"  "\n" 
"un 30%, 3.65%, 88% y 10%, respectivamente debe ingresar" "\n"
"los numeros 30, 3.65, 88 y 10 respectivamente sin el simbolo" "\n"
"de porcentaje, es decir, solo ingresar el numero.", justify ="center", font=("Cambia Math", "11", "bold")).place(x=1010, y=150)

#################################################################################
###################### BOTON FINAL PARA ACEPTAR LOS DATOS #######################

btn1 = Button(ventana, text="INGRESAR DATOS", command=funcionsuma, cursor="hand2", bg="cyan")
btn1.place(x=450, y = 700, width=150, height=30)
btn1.config(font=("Arial", "10", "bold"))

ventana.mainloop()

print("despues de la ventana de inicio")
print("el costo mina ingresado es: ", m)
print("el costo planta ingresado es: ", c)
print("el costo de venta ingresado es: ", r)
print("el precio del cobre ingresado es de : ", precio_cobre, "cusd/lb")
print("la tasa de descuento ingresada es de: ", d)
print("El costo fijo ingresado es de: ", f)
print("el costo de rehabilitación ingresado es de: ", h_reha, "usd/ton de esteril")

############################# CONVERSION DE PARAMETROS ###########################
d = d/100
ley_conc = ley_conc/100
y = y/100
perdida_metalurgica = perdida_metalurgica/100

leymin = []
for i in datos_ley_minima_2: 
    print("cada dato de la tupla es: ", i)
    numero = float(i)/100
    print("cada valor de la tupla transformado a numero es: ", numero)
    leymin.append(numero)

print("los datos de entrada de ley minima son")
print(leymin)

leymax = []
for i in datos_ley_maxima:
    print("cada dato de la tupla es: ", i)
    numero = float(i)/100
    print("cada valor de la tupla transformado a numero es: ", numero)
    leymax.append(numero) 

print("los datos de entrada de la ley maxima son: ")
print(leymax)

mineral = []
for i in datos_toneladas:
    print("cada dato de la tupla es: ", i)
    numero = float(i)*1000000
    print("cada valor de la tupla transformado a numero es: ", numero)
    mineral.append(numero)  

print("los datos de entrada de las toneladas son: ")
print(mineral)

################################################################################
###################### FINALIZACION DEL INGRESO DE DATOS #######################
################################################################################

base_de_datos = {"leymin":leymin, "leymax":leymax, "mineral": mineral}
leyes = pd.DataFrame(data = base_de_datos)
print(leyes)

paso_algortimo = 1
ultimo_valor_ro = 1

s = precio_cobre*(2205/100)
M = 30000000
FURE = 1-perdida_metalurgica
RC = rc*(2205/100)*ley_conc*(1-perdida_metalurgica) 
ibruto = s*ley_conc
valor_perdida = ibruto*perdida_metalurgica
descuentos = TC + RC + valor_perdida 
pconc = ibruto - descuentos
####################################################
###$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$####
####################################################

########################################################################### ## ### # # ################# #### ##### ###############
######################################################################## ## ### #### #### ########### ####### ######## ############
#################### DEFINICION DE ECUACIONES ESPECIALES #################### ## ### ### ### ############# ###### ####### #############
########################################################################## ## ### ## ## ############### ##### ###### ##############
########################################################################### ## ### # # ################# #### ##### ###############

def minaconcentradora(gmh,gm,gh):
  if gmh <= gm:
    return gm

  if gmh >= gh:
    return gh

  else:
    return gmh

def minarefineria(gm,gk,gkm):
  if gkm<=gm:
    return gm
  
  if gkm >=gk:
    return gk
  
  else: 
    return gkm

def concentradorarefineria(gk,gh,ghk):
  if ghk<=gk:
    return gk
  if ghk>=gh:
    return gh
  else: 
    return ghk

def seleccion_Qc(vv):
  i = 0
  for i in range(0,len(leyes)):
    if vv > leyes.iloc[i,0] and vv <leyes.iloc[i,1]:
      vv = razon.iloc[i+1,2]
  return vv

#########################################################################
#########################################################################
def aproxabajo_leymedia(vv):
  i = 0
  for i in range(0,len(leyes)):
    if vv > leyes.iloc[i,3] and vv <leyes.iloc[i+1,3]:
      vv = leyes.iloc[i,3]

  return vv
 
def aproxarriba_leymedia(vv):
  i = 0
  for i in range(0,len(leyes)):
    if vv > leyes.iloc[i,3] and vv <leyes.iloc[i+1,3]:
      vv = leyes.iloc[i+1,3]

  return vv

########################################################################
########################################################################
def truncarleymedia(vv): 
  i = 0 
  for i in range(0,len(leyes)):
    if vv > leyes.iloc[i,0] and vv < leyes.iloc[i,1]:
      vv = leyes.iloc[i,4]
  return vv 

#########################################################################
#########################################################################
################## LEY MEDIA REGRESION POLINOMICA #######################

def regresionpolinomica_leymedia(vv): 
  return coeficiente_leymedia_1*(vv) + coeficiente_leymedia_2*(vv)**2 + coeficiente_leymedia_3*(vv)**3 + coeficiente_leymedia_4*(vv)**4 + coeficiente_leymedia_5*(vv)**5 + coeficiente_leymedia_6*(vv)**6 + intercepto_leymedia_polinomica

##########################################################################
##########################################################################
######### LEY MEDIA REGRESION LINEAL MAS ALLA DE LA ULTIMA LEY DE CORTE  ###########

def regresionlineal_mas_alla_de_la_ultima_ley_de_corte(vv): 
  return pendiente_leymedia_mas_alla*vv + intercepto_leymedia_mas_alla


##########################################################################
##########################################################################

def aproxabajo(vv):
  i = 0
  for i in range(0,len(leyes)):
    if vv > leyes.iloc[i,0] and vv <leyes.iloc[i,1]:
      vv = leyes.iloc[i,0]

  return vv
 
def aproxarriba(vv):
  i = 0
  for i in range(0,len(leyes)):
    if vv > leyes.iloc[i,0] and vv <leyes.iloc[i,1]:
      vv = leyes.iloc[i,1]

  return vv

##################################################################
##################################################################

def aproxanios(anios):
  if anios >0 and anios <1:
    anios = 1
  if anios >1 and anios <2:
    anios = 2
  if anios >2 and anios <3:
    anios = 3
  if anios >3 and anios <4:
    anios = 4
  if anios >4 and anios <5:
    anios = 5
  if anios >5 and anios <6:
    anios = 6
  if anios >6 and anios <7:
    anios = 7
  if anios >7 and anios <8:
    anios = 8
  if anios >8 and anios <9:
    anios = 9
  if anios >9 and anios <10:
    anios = 10
  if anios >10 and anios <11:
    anios = 11
  if anios >11 and anios <12:
    anios = 12
  if anios >12 and anios <13:
    anios = 13
  if anios >13 and anios <14:
    anios = 14
  if anios >14 and anios <15:
    anios = 15
  if anios >15 and anios <16:
    anios = 16
  else: 
    anios = anios 
  return anios 

def tomaraños(año):
  decimal = año - int(año)
  if decimal >=0.4:
    return int(año)+1
  else:
    return int(año)

def factortonelaje(Gopt):
  delta = aproxarriba(Gopt)-aproxabajo(Gopt)
  alpha = Gopt - aproxabajo(Gopt)
  F = (100 * alpha)/delta
  F = F/100
  F = abs(1-F)
  return F

def regresion_potencial(x): 
  return a_regresion_potencial*(x**b_regresion_potencial)

def regresion_logaritmica(x):
  return a_regresion_logaritmica*np.log(x)+b_regresion_logaritmica 

def regresion_leymedia(x):
  return pendiente_leymedia*x+intercepto_leymedia

def regresion_mineral(x):
  return pendiente_mineral*x+intercepto_mineral

def regresion_esteril_mineral(x):
  return pendiente_esteril_mineral1*Goptimo + (pendiente_esteril_mineral2*(Goptimo**2)) + (pendiente_esteril_mineral3*(Goptimo**3)) + (pendiente_esteril_mineral4*(Goptimo**4)) + (pendiente_esteril_mineral5*(Goptimo**5)) + (pendiente_esteril_mineral6*(Goptimo**6)) + intercepto_esteril_mineral

######################################################################## ## ### #### #### ########### ####### ######## ############
################ FIN DE DEFINICION DE LAS ECUACIONES ESPECIALES ######## ## ### ### ### ############# ###### ####### #############
########################################################################## ## ### ## ## ############### ##### ###### ##############
########################################################################### ## ### # # ################# #### ##### ###############

mc = (leyes["leymin"]+leyes["leymax"])/2
mc 

leyes = leyes.assign(mc=mc)
leyes

#linea especial de codigo para crear la primera tabla y mas importante que es la leymedia 
i= 0 
l= []
while i<=(len(leyes)-1):
  aa = leyes.iloc[i:len(leyes),:]
  cx = aa["mineral"]*aa["mc"]
  dx = cx.sum()
  bx= aa["mineral"].sum()
  ex = dx/bx
  l.append(ex)
  #print(l)
  i = i + 1

leyes = leyes.assign(leymedia=l) 
print(leyes)  #ACA ESTA LISTA LA TABLA LEYES


##########################################################################
##########################################################################
######################## MODELOS DE REGRESIONES ##########################
##########################################################################
##########################################################################

##########################################################################
#################### REGRESION POTENCIAL LEY MEDIA #######################
##########################################################################
x = np.array(leyes["mc"])
y_pote = np.array(leyes["leymedia"])

def func_potencial(x, a, b):
    return a*x**b


popt, pcov = curve_fit(func_potencial, x, y_pote)

a_regresion_potencial = popt[0]
b_regresion_potencial = popt[1]

##########################################################################
#################### REGRESION LOGARITMICA LEY MEDIA #####################
##########################################################################
import numpy as np
from sympy import *

x = np.array(leyes["mc"])
y_log = np.array(leyes["leymedia"])
valores_regresion_logaritmica = np.polyfit(np.log(x), y_log, 1)

a_regresion_logaritmica = valores_regresion_logaritmica[0]
b_regresion_logaritmica = valores_regresion_logaritmica[1]

#print(a,b)  # a acompaña a (log(x) y b es el intercepto)

##########################################################################
########## REGRESION POLINOMICA PARA LA LEY MEDIA ########################
##########################################################################

xleymediapolinomica = np.array(leyes["mc"])
yleymediapolinomica = np.array(leyes["leymedia"])

pf = PolynomialFeatures(degree = 6)    # usaremos polinomios de grado 6
X = pf.fit_transform(xleymediapolinomica.reshape(-1,1))  # transformamos la entrada en polinómica
regresion_polinomica_leymedia = LinearRegression() # creamos una instancia de LinearRegression

regresion_polinomica_leymedia.fit(X, yleymediapolinomica) 

print('w = ' + str(regresion_polinomica_leymedia.coef_) + ', b = ' + str(regresion_polinomica_leymedia.intercept_))

coeficiente_leymedia_1 = regresion_polinomica_leymedia.coef_[1]
coeficiente_leymedia_2 = regresion_polinomica_leymedia.coef_[2]
coeficiente_leymedia_3 = regresion_polinomica_leymedia.coef_[3]
coeficiente_leymedia_4 = regresion_polinomica_leymedia.coef_[4]
coeficiente_leymedia_5 = regresion_polinomica_leymedia.coef_[5]
coeficiente_leymedia_6 = regresion_polinomica_leymedia.coef_[6]
intercepto_leymedia_polinomica = regresion_polinomica_leymedia.intercept_

x = np.linspace(0,xleymediapolinomica.max(),len(leyes))
plt.plot(x,coeficiente_leymedia_1*(x) + coeficiente_leymedia_2*(x)**2 + coeficiente_leymedia_3*(x)**3 + coeficiente_leymedia_4*(x)**4 + coeficiente_leymedia_5*(x)**5 + coeficiente_leymedia_6*(x)**6 + intercepto_leymedia_polinomica,label="regresion Polinomica")
plt.plot(xleymediapolinomica,yleymediapolinomica, "o",label="curva de datos reales")
plt.legend(loc=2)
plt.xlabel("ley de corte MC")
plt.ylabel("ley media")
plt.grid()
#plt.show()


###########################################################################
######## REGRESION LINEAL LEY MEDIA MAS ALLA DEL ULTIMO INTERVALO #########
###########################################################################

LISTAX = [leyes.iloc[3,-2], leyes.iloc[3,-1]]
LISTAY = [leyes.iloc[4,-2], leyes.iloc[4,-1]]
xleymedia_mas_alla = np.array(LISTAX)
yleymedia_mas_alla = np.array(LISTAY)

pf = PolynomialFeatures(degree = 1)
X = pf.fit_transform(xleymedia_mas_alla.reshape(-1,1))
regresion_lineal_leymedia_mas_alla = LinearRegression()

regresion_lineal_leymedia_mas_alla.fit(X, yleymedia_mas_alla) 

print('w = ' + str(regresion_lineal_leymedia_mas_alla.coef_) + ', b = ' + str(regresion_lineal_leymedia_mas_alla.intercept_))

pendiente_leymedia_mas_alla = regresion_lineal_leymedia_mas_alla.coef_
intercepto_leymedia_mas_alla = regresion_lineal_leymedia_mas_alla.intercept_

###########################################################################
######## REGRESION LINEAL LEY MEDIA DENTRO DEL INTERVALO DE LEYES #########
###########################################################################

#REGRESION LINEAL PARA LEY MEDIA#
xleymedia = np.array(leyes["mc"])
yleymedia = np.array(leyes["leymedia"])


pf = PolynomialFeatures(degree = 1)    # usaremos polinomios de grado 1
X = pf.fit_transform(xleymedia.reshape(-1,1))  # transformamos la entrada en polinómica
regresion_lineal_leymedia = LinearRegression() # creamos una instancia de LinearRegression

# instruimos a la regresión lineal que aprenda de los datos (ahora polinómicos) (X,y)

regresion_lineal_leymedia.fit(X, yleymedia) 

# vemos los parámetros que ha estimado la regresión lineal

print('w = ' + str(regresion_lineal_leymedia.coef_) + ', b = ' + str(regresion_lineal_leymedia.intercept_))

pendiente_leymedia = regresion_lineal_leymedia.coef_[1]
intercepto_leymedia = regresion_lineal_leymedia.intercept_
print("EL VALOR DE A ES:", pendiente_leymedia)
print("EL VALOR DE B ES:", intercepto_leymedia)
#####################################################
x = np.linspace(0,xleymedia.max(),len(leyes))
plt.plot(x,x*pendiente_leymedia+intercepto_leymedia,label="regresion lineal")
plt.plot(xleymedia,yleymedia, "o",label="curva de datos reales")
plt.legend(loc=2)
plt.xlabel("ley de corte min")
plt.ylabel("ley media")
plt.grid()
#plt.show()

#####REGRESION LINEAL ##########################################################



###################################################################################################
######## LISTAS VACIAS QUE ALMACENAN Y GUARDAN LA INFORMACION QUE RESULTA DE CADA PROCESO #########
###################################################################################################

anio = 1 
listaanios = []
listavanes = []
listaro = []
listaGoptimo = []
listatm = []
listatc = []
listatr = []
listaley_media = []
listabeneficio = []
listaconcentrado = []

lista_años_RO_CERO = []
listavan_RO_CERO = []
listabeneficios_RO_CERO = []
listaleyes_COG_RO_CERO = []
listaro_RO_CERO = []
lista_qm_RO_CERO = []
lista_qc_RO_CERO = []
lista_qr_RO_CERO = []
lista_ley_media_RO_CERO = []
listaconcentrado_RO_CERO = []

lista_años_FASE2 = []
listavanFASE2 = []
listabeneficiosFASE2 = []
listaleyes_COG_FASE2 = []
listaroFASE2 = []
lista_qm_FASE2 = []
lista_qc_FASE2 = []
lista_qr_FASE2 = []
lista_ley_media_FASE2 = []
lista_concentrado_FASE2 = []


archivador_lista = []
archivador = pd.DataFrame(data = archivador_lista)

archivador_unico_2 = []
archivador_unico_2 = pd.DataFrame(data = archivador_unico_2)

###################################################################################################
###################################################################################################

RO = 0   #### VALOR DE COMIENZO PARA RO, NO CAMBIAR ESTE VALOR, SIEMPRE PARA LANE FIJARLO EN 0
tonqueda = 100  ### VALOR PARA QUE PUEDA COMENZAR EL CICLO WHILE DE MAS ABAJO
C = CAPACIDAD_PLANTA

while RO <= ultimo_valor_ro :    
  while leyes["mineral"].sum()>0 and tonqueda>0: 
    print("################################################################")  
    print("el año es: ",anio)
    print("################################################################") 
    i = 0 
    to = []
    while i<=(len(leyes)-1):
      ee = leyes.iloc[i:len(leyes),:]
      cr = ee["mineral"]
      tr = float(cr.sum())
      to.append(tr)
      i = i + 1 
    print(to)
    tw = leyes["mineral"].sum()-to
    print(tw)
    sr = tw/to
    print(sr)
    cueme = to*(1+sr)
    print(cueme)
    leymed = leyes["leymedia"]*y
    cuere = to*leymed
    print(cuere)
    razon = {"ley de corte":leyes["leymin"], "Qm":cueme, "Qc": to, "Qr": cuere, "SR":sr}
    razon = pd.DataFrame(razon)
    print(razon)
    
    #******************************************
    #### REGRESION LINEAL Qc (MINERAL)   ###################################
    xmineral = np.array(leyes["leymin"])
    ymineral = np.array(razon["Qc"])


    pf = PolynomialFeatures(degree = 1)    # usaremos polinomios de grado 3
    X = pf.fit_transform(xmineral.reshape(-1,1))  # transformamos la entrada en polinómica
    regresion_lineal_mineral = LinearRegression() # creamos una instancia de LinearRegression

    # instruimos a la regresión lineal que aprenda de los datos (ahora polinómicos) (X,y)

    regresion_lineal_mineral.fit(X, ymineral) 

    # vemos los parámetros que ha estimado la regresión lineal

    print('w = ' + str(regresion_lineal_mineral.coef_) + ', b = ' + str(regresion_lineal_mineral.intercept_))

    pendiente_mineral = regresion_lineal_mineral.coef_[1]
    intercepto_mineral = regresion_lineal_mineral.intercept_
    print("EL VALOR DE M ES:", pendiente_mineral)
    print("EL VALOR DE N ES:", intercepto_mineral)



    #0000000000000000000000000000000000000000000000000

    #REGRESION POLINOMICA PARA E/M######################
    xesteril_mineral = np.array(razon["ley de corte"])
    yesteril_mineral = np.array(razon["SR"])


    pf = PolynomialFeatures(degree = 6)    # usaremos polinomios de grado 3
    X = pf.fit_transform(xesteril_mineral.reshape(-1,1))  # transformamos la entrada en polinómica
    regresion_lineal_esteril_mineral = LinearRegression() # creamos una instancia de LinearRegression

    # instruimos a la regresión lineal que aprenda de los datos (ahora polinómicos) (X,y)

    regresion_lineal_esteril_mineral.fit(X, yesteril_mineral) 

    # vemos los parámetros que ha estimado la regresión lineal

    print('w = ' + str(regresion_lineal_esteril_mineral.coef_) + ', b = ' + str(regresion_lineal_esteril_mineral.intercept_))

    pendiente_esteril_mineral1 = regresion_lineal_esteril_mineral.coef_[1] #acompaña a X^1
    pendiente_esteril_mineral2 = regresion_lineal_esteril_mineral.coef_[2] #acompaña a X^2
    pendiente_esteril_mineral3 = regresion_lineal_esteril_mineral.coef_[3] #acompaña a X^3
    pendiente_esteril_mineral4 = regresion_lineal_esteril_mineral.coef_[4] #acompaña a X^4
    pendiente_esteril_mineral5 = regresion_lineal_esteril_mineral.coef_[5] #acompaña a X^5
    pendiente_esteril_mineral6 = regresion_lineal_esteril_mineral.coef_[6] #acompaña a X^6
    intercepto_esteril_mineral = regresion_lineal_esteril_mineral.intercept_

    print("pendiente regresion multiple", pendiente_esteril_mineral1) #acompaña a X^1
    print(pendiente_esteril_mineral2) #acompaña a X^2
    print(pendiente_esteril_mineral3)  #acompaña a X^3
    print(pendiente_esteril_mineral4)  #acompaña a X^4
    print(pendiente_esteril_mineral5)  #acompaña a X^5
    print(pendiente_esteril_mineral6)  #acompaña a X^6
    print(intercepto_esteril_mineral) 

    

    VAN_0 = 0  ### SE COMIENZA CON ESTA SOLUCION INICIAL PARA EL ALGORITMO DE LANE
    error = 10000000 ### DE DEFINE UN ERROR MAYOR QUE EL ACEPTABLE, PARA QUE PUEDA ENTRAR AL CICLO WHILE
    iii = 1  ### ESTE ES EL CONTADOR DE LAS ITERACIONES QUE REALIZA EL ALGORITMO DE LANE
    while error>0.01 and iii<=160:        #ACA VA EL WHILE 
      print("\n")
      gm = (c-h_reha+RO)/((s-r)*y) #ley de corte mina 
      if respuesta == "SI" or respuesta == "si": 
        gh = (c+m-e+RO-h_reha+((f+(VAN_0*d))/C))/((s-r)*y)  ### CON ECONOMIAS DE ESCALAS
      if respuesta == "NO" or respuesta == "no":
        gh = (c+RO-h_reha+((f+(VAN_0*d))/C))/((s-r)*y)  ### SIN ECONOMIAS DE ESCALAS 

      gk = (c)/(((s-r)-((f+(VAN_0*d))/R))*y)       #ley de corte de la refineria 
      gmh = 1 - (C/M)
      ghk = (2*R/C)-1
      gkm = pow((1-((2*R)/M)),0.5)

      print("el valor de gm es: ", gm)
      print("el valor de gh es: ", gh)
      print("el valor de gk es: ", gk)
      print("el valor de gmh es: ", gmh)
      print("el valor de gkm es: ", gkm)
      print("el valor de ghk es: ", ghk)
      print("000000000000000000000000000000000000")
      print("el valor de Gmh es: ", minaconcentradora(gmh,gm,gh))
      print("el valor de Gmk es: ", minarefineria(gm,gk,gkm))
      print("el valor de Ghk es: ", concentradorarefineria(gk,gh,ghk))
      leyesxx = {"leyes": [minaconcentradora(gmh,gm,gh),minarefineria(gm,gk,gkm),concentradorarefineria(gk,gh,ghk)]}
      #### LINEAS QUE ESTABLECEN LA LEY DE CORTE OPTIMA IGUAL A LA LEY DE CORTE DIFINIDA POR LA CONCENTRADORA
      leyesxxx = pd.DataFrame(data=leyesxx)
      leyesxxx
      leyesorden=leyesxxx.sort_values(by="leyes")
      leyesorden
      Goptimo = float(gh)
      print("EL VALOR DE GOPTIMO ES:",Goptimo)

      ############### LINEA PARA DETERMINAR SI LA LEY DE CORTE OPTIMA ES EXACTAMENTE IGUAL A LA LEY DE CORTE DEFINIDA ##############
      ########################### EN LA DISTRIBUCION DE LEYES INGRESA EN LOS DATOS DE ENTRADA AL PROGRAMA ##########################

      i7 = 0 
      beta = []
      betadataframe = pd.DataFrame(data = beta)
      while i7 <= (len(leyes)-1): 
        if leyes.iloc[i7,0] == Goptimo: 
          valor1 = 1
          beta1 = beta.append(valor1)
        else: 
          valor2 = 0 
          beta1 = beta.append(valor2)
        i7 = i7 + 1
      print(beta)
     
      ########################################################################################
      #### SI EL BETA ES 1 SIGNIFICA QUE LA LEY DE CORTE OBTENIDA ANTERIORMENTE ES IGUAL  ####
      #### A UNA DEL DE CORTE INGRESADA EN LA DISTRIBUCION DE LEYES ORIGINALES, SOLO PARA ####
      #### CASOS DONDE LA DISTRIBUCION DEL TONELAJE SEGUN SU LEY DE CORTE, ES UNA         ####
      #### CONSTANTE ES DECIR, PARA CASOS MUY ESPECIFICOS Y ALEJADOS DE LA REALIDAD, DONDE ###
      #### DONDE LA DISTRIBUCION  DEL TONELAJE ES UNA DISTRIBUCION DEL TIPO LOGARITMICO   ####
      #### INVERSO, ES DECIR, DECRECIENTE A MEDIDA DE QUE AUMENTA LA LEY DE CORTE         ####
      ########################################################################################
      if 1 in beta: 
        razon_1= razon.loc[razon['ley de corte'] == Goptimo]
        Qm = leyes["mineral"].sum()
        Qc = float(razon_1.iloc[0,2])
        ley_media_razon_2 = leyes.loc[leyes['leymin'] == Goptimo]
        ley_media = float(ley_media_razon_2.iloc[0,4])
        print("el valor de Qm es:", Qm, "el de Qc es: ", Qc)
        tm = Qm/M 
        tc = Qc/C 
        print("los años mina sin aproximar son: ", tm)
        print("los años de la planta sin aproximar son: ", tc)
        print("los años de la refineria sin aproximar son: ", tr)
        lll= [tc]
        ##############################################################################################
        #### SE DEFINE EL TIEMPO COMO AQUEL DEFINIDO SOLO POR LA PLANTA CONCENTRADORA, YA QUE SOLO  #####
        #### ESTE SISTEMA ES EL QUE LIMITA TODA LA OPERACION MINERA, LA REFINERIA NO ES UNA         #####
        #### LIMITANTE, YA QUE SE DECIDE QUE EL CONCENTRADO QUE NO PUEDA SER PROCESADO POR LA       #####
        #### FUNDICION Y REFINERIA, SEA VENDIDO COMO CONCENTRADO EN UN MERCADO INTERMEDIO POR LO    #####
        #### QUE PUEDE EXISTIR EL CASO QUE EL FLUJO DE CONCENTRADO QUE INGRESA A LA REFINERIA SEA   #####
        #### MAYOR A LA CAPACIDAD DE ESTA, EN ESE CASO, SE DICE QUE SE VENDE CONCENTRADO, POR LO    #####
        #### QUE NO PODEMOS LIMITAR EL TIEMPO SEGUN LA CAPACIDAD DE LA REFINERIA, YA QUE NO ES UNA  #####
        #### LIMITANTE DE MI SISTEMA, Y LA MINA SE DEFINE COMO ILIMITADA, POR LO QUE TAMPOCO ES UNA ##### 
        #### LIMITANTE A MI SISTEMA                                                                 #####
        #################################################################################################
        años = float(tc)
        decimal = años - int(años)
        print("los años maximos aproximados son:", años)
        añosentero = int(años)


        if años >=1: 
          qm = Qm/años 
          qc = Qc/años 
          qr = qc*y*ley_media 
          if qr>R: 
            qdelta = qr-R 
            qconc = (qdelta)/(ley_conc*FURE)
            qr = R 
            print("LA CANTIDAD DE CONCENTRADO ES: ", qconc)
            print("el valor final de qm es",qm, "el de qc es:",qc,"y el de qr es", qr)
            if respuesta == "SI" or respuesta == "si":
              b_lane = ((s-r)*qr)+(pconc*qconc)-(c+m-e-h_reha)*qc-(e+h_reha)*qm-(f*(qc/C))  ### CON ECONOMIAS DE ESCALAS
            if respuesta == "NO" or respuesta == "no":
              b_lane = ((s-r)*qr)-c*qc-m*qm-(f*(qc/C))-(h_reha*(qm-qc))+(pconc*qconc)  ### SIN ECONOMIAS DE ESCALAS 
        
            print("el valor del BENEFICIO DE LANE ES: ", b_lane)
            print("ESTAMOS EN LA ITERACION: ", iii)
            print("EL VALOR DE RO ES:", RO)
          else: 
            qconc = 0
            print("EL TONELAJE DE CONCENTRADO ES: ",qconc)
            print("el valor final de qm es",qm, "el de qc es:",qc,"y el de qr es", qr) 
            if respuesta == "SI" or respuesta == "si":
              b_lane = ((s-r)*qr)+(pconc*qconc)-(c+m-e-h_reha)*qc-(e+h_reha)*qm-(f*(qc/C))  ### CON ECONOMIAS DE ESCALAS
            if respuesta == "NO" or respuesta == "no":
              b_lane = ((s-r)*qr)-c*qc-m*qm-(f*(qc/C))-(h_reha*(qm-qc))+(pconc*qconc)  ### SIN ECONOMIAS DE ESCALAS 
            print("el valor del BENEFICIO DE LANE ES: ", b_lane)
            print("ESTAMOS EN LA ITERACION: ", iii)
            print("EL VALOR DE RO ES:", RO)

          años1 = round(años,0)
          contadoraños = 0 
          VAN = 0


          while contadoraños<=(años-1): 
            van = b_lane/((1+d)**contadoraños)
            VAN = van + VAN
            print("el valor del beneficio actualizado en el año ", contadoraños, "es", van)
            print("el valor del beneficio acutalizado acumulado en el año ", contadoraños, "es", VAN)
            contadoraños = contadoraños + 1 

          print("el valor del VAN DESPUES DEL CICLO WHILE es", VAN)

          decimal = años - int(años)
          print(decimal)
          años_redondeo_superior = int(años)
          print(años_redondeo_superior)
          beneficio_año_extra = b_lane/((1+d)**años_redondeo_superior)
          print("el beneficio en el año extra es",beneficio_año_extra )
          beneficio_año_extra_conchito = beneficio_año_extra*decimal
          print("el beneficio conchito del ultimo año es", beneficio_año_extra_conchito)
          VAN = VAN + beneficio_año_extra_conchito
          print("el van mas el conchito es", VAN)

          print("EL VALOR DEL VAN FINAL ES:", VAN)
            
        if años<1: 
          qm = Qm 
          qc = Qc 
          qr = qc*y*ley_media
          print("el flujo de material anual que mueve la mina es:", qm, ", el que mueve la planta concentradora es: ", qc,"y el flujo anual que mueve la refineria es", qr)
          if qr>R: 
            qdelta = qr-R 
            qconc = (qdelta)/(ley_conc*FURE)
            qr = R 
            print("LA CANTIDAD DE CONCENTRADO ES: ", qconc)
            print("el valor final de qm es",qm, "el de qc es:",qc,"y el de qr es", qr)
            if respuesta == "SI" or respuesta == "si":
              b_lane = ((s-r)*qr)+(pconc*qconc)-(c+m-e-h_reha)*qc-(e+h_reha)*qm-(f*(qc/C))  ### CON ECONOMIAS DE ESCALAS
            if respuesta == "NO" or respuesta == "no":
              b_lane = ((s-r)*qr)-c*qc-m*qm-(f*(qc/C))-(h_reha*(qm-qc))+(pconc*qconc)  ### SIN ECONOMIAS DE ESCALAS 
            print("el valor del BENEFICIO DE LANE ES: ", b_lane)
            print("ESTAMOS EN LA ITERACION: ", iii)
            print("EL VALOR DE RO ES:", RO)
          else: 
            qconc = 0
            print("EL TONELAJE DE CONCENTRAOD ES: ", qconc)
            print("el valor final de qm es",qm, "el de qc es:",qc,"y el de qr es", qr)
            if respuesta == "SI" or respuesta == "si":
              b_lane = ((s-r)*qr)+(pconc*qconc)-(c+m-e-h_reha)*qc-(e+h_reha)*qm-(f*(qc/C))  ### CON ECONOMIAS DE ESCALAS
            if respuesta == "NO" or respuesta == "no":
              b_lane = ((s-r)*qr)-c*qc-m*qm-(f*(qc/C))-(h_reha*(qm-qc))+(pconc*qconc)  ### SIN ECONOMIAS DE ESCALAS  
            print("el valor del BENEFICIO DE LANE ES: ", b_lane)
            print("ESTAMOS EN LA ITERACION: ", iii)
            print("EL VALOR DE RO ES:", RO)

######################################################
          if años < 1: 
            años = 1
          else: 
            años = años 
######################################################

          años1 = round(años,0)
          contadoraños = 0 
          VAN = 0
######################################################

          while contadoraños<=(años-1): 
            van = b_lane/((1+d)**contadoraños)
            VAN = van + VAN
            print("el valor del beneficio actualizado en el año ", contadoraños, "es", van)
            print("el valor del beneficio acutalizado acumulado en el año ", contadoraños, "es", VAN)
            contadoraños = contadoraños + 1 

          print("el valor del VAN DESPUES DEL CICLO WHILE es", VAN)

          decimal = años - int(años)
          print(decimal)
          años_redondeo_superior = int(años)
          print(años_redondeo_superior)
          beneficio_año_extra = b_lane/((1+d)**años_redondeo_superior)
          print("el beneficio en el año extra es",beneficio_año_extra )
          beneficio_año_extra_conchito = beneficio_año_extra*decimal
          print("el beneficio conchito del ultimo año es", beneficio_año_extra_conchito)
          VAN = VAN + beneficio_año_extra_conchito
          print("el van mas el conchito es", VAN)


          print("EL VALOR DEL VAN FINAL ES:", VAN)

      ######################################################################################
      ### CASO EN LOS CUALES NO HAY UN 1 EN BETA, SIGNIFICA QUE LA LEY DE CORTE OBTENIDA ###
      ### NO ES IGUAL A NINGUNA LEY DE CORTE INGRESADA ORIGINALMENTE AL SISTEMA COMO LA  ###
      ### DISTRIBUCION DEL TONELAJE SEGUN SU LEY DE CORTE, Y QUE ADEMAS REPRESENTA QUE   ###
      ### AQUELLA DISTRIBUCION ES DECRECIENTE Y NO CONSTANTE, POR LO CUAL, EN LA GRAN    ###
      ### MAYORIA DE LOS CASOS SE ACTIVARAN LAS LINEAS DE CODIGO QUE ESTAN DEBAJO        ###
      ######################################################################################
      else:  
        if Goptimo > leyes.iloc[-1,0]:                           ######## LINEAS DE CODIGO POR SI LA LEY DE CORTE ENCONTRADA 
          delta_ultimo = leyes.iloc[-1,1]-leyes.iloc[-1,0]       ######## EN UNA DETERMINADA ITERACION Y AÑO, ES MAYOR QUE LA 
          alpha_ultimo =  leyes.iloc[-1,1] - Goptimo             ######## LA MARCA DE CLASE MAS GRANDE DEFINIDA EN LA TABLA 
          F_ultimo = (alpha_ultimo)/delta_ultimo                 ######## INICIAL LLAMADA LEYES, POR LO QUE CUANDO SUCEDE ESTO, 
          Qc = F_ultimo*leyes.iloc[-1,2]                         ######## SE HACE UNA REGRESION LINEAL PARA LA LEY MEDIA, TOMANDO 
          Qm = leyes["mineral"].sum()                            ######## LOS ULTIMOS DOS DATOS DE LA DISTRIBUCION ORIGINAL INGRESADA 
          ley_media_ultima = regresion_leymedia(Goptimo)         ######## Y SE CALCULA LA LEY MEDIA A TRAVES DE UNA REGRESION LINEAL 
          print("el valor de la ley media, calculada a traves de la regresion lineal es: ", ley_media_ultima)
          ley_media_logaritmica = regresion_logaritmica(Goptimo)
          print("el valor de la ley media, calculada a traves de la regresion logaritmica es: ", ley_media_logaritmica)
          ley_media_potencial = regresion_potencial(Goptimo)
          print("el valor de la ley media, calculada a traves de la regresion potencial es: ", ley_media_potencial)
          ley_media_regresion_mas_alla = regresionlineal_mas_alla_de_la_ultima_ley_de_corte(Goptimo)
          print("el valor de la ley media, calculada a traves de la regresion lineal mas alla es", ley_media_regresion_mas_alla)
          Qr = Qc*y*ley_media_regresion_mas_alla
          print("el valor de Qm es ", Qm, ", el valor de Qc es ", Qc, "y el de Qr es ", Qr)


        else: 
          if Goptimo < leyes.iloc[0,3]:                                            ### LINEAS DE CODIGO CUANDO LA LEY DE CORTE HALLADO ES MENOR
            leyes_inf_paraQm = leyes.loc[leyes["leymin"] == aproxabajo(Goptimo)]   ### QUE LA ULTIMA MARCA DE CLASE DE LA LET DE CORTE EN LA 
            razon_sup = razon.loc[razon["ley de corte"] == aproxarriba(Goptimo)]   ### DISTRIBUCION ORIGINAL, POR LO QUE LA LEY MEDIA SE CALCULARA
            razon_inf = razon.loc[razon["ley de corte"] == aproxabajo(Goptimo)]    ### PARA CUALQUIER PUNTO DE LEY DE CORTE COMO LA INTERPOLACION
            print("El FACTOR TONELAJE ES: ", factortonelaje(Goptimo))              ### LINEAL ENTRE LA LEY MEDIA SUPERIOR E INFERIOR CONOCIDA 
            leymedia_MAS_BAJA  = regresionpolinomica_leymedia(Goptimo)             ### SEGUN LA TABLA "leyes" A PARTIR DE UNA LEY DE CORTE ESPECIFICA
            Qc = razon_sup.iloc[0,2]+(factortonelaje(Goptimo)*leyes_inf_paraQm.iloc[0,2]) ### TAMBIEN SE AGREGA EL FACTOR "F" EL CUAL, TOMA EN CUENTA
            Qr = Qc*y*leymedia_MAS_BAJA                                                   ### EL TONELAJE REAL SEGUN UNA LEY DE CORTE CUALQUIERA
            Qm = leyes["mineral"].sum()

          else: 
            razon_sup = razon.loc[razon["ley de corte"] == aproxarriba(Goptimo)]
            razon_inf = razon.loc[razon["ley de corte"] == aproxabajo(Goptimo)]
            print(razon_inf)
            print(razon_sup)
            FACTOR_SR = ((razon_sup.iloc[0,4]-razon_inf.iloc[0,4])/(razon_sup.iloc[0,0]-razon_inf.iloc[0,0])*(Goptimo-razon_inf.iloc[0,0]))+ razon_inf.iloc[0,4]
            print("LA RAZON E/M ES:", FACTOR_SR)
            ley_media_razon_2_sup = leyes.loc[leyes['mc'] == aproxarriba_leymedia(Goptimo)]
            ley_media_razon_2_inf = leyes.loc[leyes['mc'] == aproxabajo_leymedia(Goptimo)]
            print(ley_media_razon_2_sup)
            print(ley_media_razon_2_inf)
            #### la ley_media es el promedio de los dos puntos mas cercanos a una determinada ley media buscada ###
            ley_media = (ley_media_razon_2_sup.iloc[0,4]+ley_media_razon_2_inf.iloc[0,4])/2 #valor promedio 
            print("el valor de la ley media usando el promedio es:", ley_media)
            ##### la ley_media2 es la ley media en cualquier punto, usando la interpolacion lineal de sus dos puntos mas cercanos #####
            ley_media2 = ((ley_media_razon_2_sup.iloc[0,4]-ley_media_razon_2_inf.iloc[0,4])/(ley_media_razon_2_sup.iloc[0,3]-ley_media_razon_2_inf.iloc[0,3]))*(Goptimo-ley_media_razon_2_inf.iloc[0,3])+ley_media_razon_2_inf.iloc[0,4]
            print("el valor de la ley media calculada a traves de interpolacion es:", ley_media2)
            ley_media_bruta = ley_media_razon_2_inf.iloc[0,4]
            print("la ley media bruta es:", ley_media_bruta)
            #### la ley_media_polinomica es la obtenida usando la regresion polinomica #####
            ley_media_polinomica = regresionpolinomica_leymedia(Goptimo)
            print("EL VALOR DE LA LEY MEDIA CALCULADA A PARTIR DE LA REGRESION POLINOMICA ES :", ley_media_polinomica)
            ley_media_truncada = truncarleymedia(Goptimo)
            print("LA LEY MEDIA A PARTIR A LO SALVAJE ES", truncarleymedia(Goptimo))
            leyes_inf_paraQm = leyes.loc[leyes["leymin"] == aproxabajo(Goptimo)]
            ##### el factor tonelaje corresponde al factor F, el cual representa el tonelaje verdadero que se toma dentro de la ####
            ##### distribucion original de tonelaje, cuando la ley de corte obtenida se encuentra dentro de un intervalo definido ####
            print("El FACTOR TONELAJE ES: ", factortonelaje(Goptimo))
            Qc = razon_sup.iloc[0,2]+(factortonelaje(Goptimo)*leyes_inf_paraQm.iloc[0,2])
            print("el valor del FACTOR TONELAJE ES: ", factortonelaje(Goptimo))
            leymedia = round(pendiente_leymedia,4)*Goptimo+round(intercepto_leymedia,4)
            print("el valor de la ley media usando la regresion lineal es:", leymedia)
            #### aca de decide emplear el metodo de la interpolacion lineal, para encontra la ley media dentro de un intervalo de leyes de corte ####
            Qr = Qc*y*ley_media2
            #### SE DEFINE Qm COMO LA SUMA DE TODO EL MATERIAL EN UN AÑO ESPECIFICO ####
            Qm = leyes["mineral"].sum()
            print("EL VALOR DE Qm ES:",Qm)
            print("la ley media a partir del valor de Qr y de Qc es:", Qr/(Qc*y))
            print("Qm es: ",Qm, "el de Qc es:",Qc,"y el de Qr es:",Qr)
        ### se definen los tiempos para cada sistema dentro de la mina ####
        tm = Qm/M 
        tc = Qc/C 
        tr = Qr/R 
        print("los años mina sin aproximar son: ", tm)
        print("los años de la planta sin aproximar son: ", tc)
        print("los años de la refineria sin aproximar son: ", tr)
        lll= [tc, tm]   ##### CONSIDERANDO LA MINA Y LA CONCENTRADORA 
        lll = pd.DataFrame(data = lll)
        ##############################################################################################
        #### SE DEFINE EL TIEMPO COMO AQUEL DEFINIDO SOLO POR LA PLANTA CONCENTRADORA, YA QUE SOLO  #####
        #### ESTE SISTEMA ES EL QUE LIMITA TODA LA OPERACION MINERA, LA REFINERIA NO ES UNA         #####
        #### LIMITANTE, YA QUE SE DECIDE QUE EL CONCENTRADO QUE NO PUEDA SER PROCESADO POR LA       #####
        #### FUNDICION Y REFINERIA, SEA VENDIDO COMO CONCENTRADO EN UN MERCADO INTERMEDIO POR LO    #####
        #### QUE PUEDE EXISTIR EL CASO QUE EL FLUJO DE CONCENTRADO QUE INGRESA A LA REFINERIA SEA   #####
        #### MAYOR A LA CAPACIDAD DE ESTA, EN ESE CASO, SE DICE QUE SE VENDE CONCENTRADO, POR LO    #####
        #### QUE NO PODEMOS LIMITAR EL TIEMPO SEGUN LA CAPACIDAD DE LA REFINERIA, YA QUE NO ES UNA  #####
        #### LIMITANTE DE MI SISTEMA, Y LA MINA SE DEFINE COMO ILIMITADA, POR LO QUE TAMPOCO ES UNA ##### 
        #### LIMITANTE A MI SISTEMA                                                                 #####
        #################################################################################################
        años = float(tc)
        decimal = años - int(años)
        añosaprox = round(años,1)
        print("los años maximos son:", años)
        añosentero = int(años)
        print("EL VALOR DE  Goptimo ES:", Goptimo)


        if años >1:
          años1 = round(años,0) 
          qm = Qm/años
          qc = Qc/años
          print("los valores iniciales de qm es", qm, "y el de qc es", qc)
          qr = Qr/años 
          if qr>R: ##### EXISTE CONCENTRADO QUE PUEDE VENDERSE 
            qdelta = qr-R 
            qconc = (qdelta)/(ley_conc*FURE)
            qr = R 
            print("LA CANTIDAD DE CONCENTRADO ES: ", qconc)
            print("el valor final de qm es",qm, "el de qc es:",qc,"y el de qr es", qr)
            if respuesta == "SI" or respuesta == "si":
              b_lane = ((s-r)*qr)+(pconc*qconc)-(c+m-e-h_reha)*qc-(e+h_reha)*qm-(f*(qc/C))  ### CON ECONOMIAS DE ESCALAS
            if respuesta == "NO" or respuesta == "no":
              b_lane = ((s-r)*qr)-c*qc-m*qm-(f*(qc/C))-(h_reha*(qm-qc))+(pconc*qconc)  ### SIN ECONOMIAS DE ESCALAS 
        
            print("el valor del BENEFICIO DE LANE ES: ", b_lane)
            print("ESTAMOS EN LA ITERACION: ", iii)
            print("EL VALOR DE RO ES:", RO)
          else: #### NO EXISTE CONCENTRADO QUE PUEDA VENDERSE 
            qconc = 0
            print("EL TONELAJE DE CONCENTRADO ES: ",qconc)
            print("el valor final de qm es",qm, "el de qc es:",qc,"y el de qr es", qr) 
            if respuesta == "SI" or respuesta == "si":
              b_lane = ((s-r)*qr)+(pconc*qconc)-(c+m-e-h_reha)*qc-(e+h_reha)*qm-(f*(qc/C))  ### CON ECONOMIAS DE ESCALAS
            if respuesta == "NO" or respuesta == "no":
              b_lane = ((s-r)*qr)-c*qc-m*qm-(f*(qc/C))-(h_reha*(qm-qc))+(pconc*qconc)  ### SIN ECONOMIAS DE ESCALAS 
            print("el valor del BENEFICIO DE LANE ES: ", b_lane)
            print("ESTAMOS EN LA ITERACION: ", iii)
            print("EL VALOR DE RO ES:", RO)
          años1 = round(años,0)
          contadoraños = 0 
          VAN = 0

          while contadoraños<=(años-1): 
            van = b_lane/((1+d)**contadoraños)
            VAN = van + VAN
            print("el valor del beneficio actualizado en el año ", contadoraños, "es", van)
            print("el valor del beneficio acutalizado acumulado en el año ", contadoraños, "es", VAN)
            contadoraños = contadoraños + 1 

          print("el valor del VAN DESPUES DEL CICLO WHILE es", VAN)

          decimal = años - int(años)
          print(decimal)
          años_redondeo_superior = int(años)
          print(años_redondeo_superior)
          beneficio_año_extra = b_lane/((1+d)**años_redondeo_superior)
          print("el beneficio en el año extra es",beneficio_año_extra )
          beneficio_año_extra_conchito = beneficio_año_extra*decimal
          print("el beneficio conchito del ultimo año es", beneficio_año_extra_conchito)
          VAN = VAN + beneficio_año_extra_conchito
          print("el van mas el conchito es", VAN)
          print("EL VALOR DEL VAN FINAL ES:", VAN)


        if años <=1:
          Qm = leyes["mineral"].sum()
          print("el valor de Qm para años MENORES a 1 es",Qm)
          qm = Qm/1 
          qc = Qc/1
          if qc >C: 
            qc = C 
          else: 
            qc = qc 
          qr = Qr/1
          if qr>R: 
            qdelta = qr-R 
            qconc = (qdelta)/(ley_conc*FURE)
            qr = R 
            print("LA CANTIDAD DE CONCENTRADO ES: ", qconc)
            print("el valor final de qm es",qm, "el de qc es:",qc,"y el de qr es", qr)
            if respuesta == "SI" or respuesta == "si":
              b_lane = ((s-r)*qr)+(pconc*qconc)-(c+m-e-h_reha)*qc-(e+h_reha)*qm-(f*(qc/C))  ### CON ECONOMIAS DE ESCALAS
            if respuesta == "NO" or respuesta == "no":
              b_lane = ((s-r)*qr)-c*qc-m*qm-(f*(qc/C))-(h_reha*(qm-qc))+(pconc*qconc)  ### SIN ECONOMIAS DE ESCALAS 
            print("el valor del BENEFICIO DE LANE ES: ", b_lane)
            print("ESTAMOS EN LA ITERACION: ", iii)
            print("EL VALOR DE RO ES:", RO)
          else: 
            qconc = 0
            print("EL TONELAJE DE CONCENTRAOD ES: ", qconc)
            print("el valor final de qm es",qm, "el de qc es:",qc,"y el de qr es", qr)
            if respuesta == "SI" or respuesta == "si":
              b_lane = ((s-r)*qr)+(pconc*qconc)-(c+m-e-h_reha)*qc-(e+h_reha)*qm-(f*(qc/C))  ### CON ECONOMIAS DE ESCALAS
            if respuesta == "NO" or respuesta == "no":
              b_lane = ((s-r)*qr)-c*qc-m*qm-(f*(qc/C))-(h_reha*(qm-qc))+(pconc*qconc)  ### SIN ECONOMIAS DE ESCALAS  
            print("el valor del BENEFICIO DE LANE ES: ", b_lane)
            print("ESTAMOS EN LA ITERACION: ", iii)
            print("EL VALOR DE RO ES:", RO)

######################################################
          if años < 1: 
            años = 1
          else: 
            años = años 
######################################################

          años1 = round(años,0)
          contadoraños = 0 
          VAN = 0

          while contadoraños<=(años-1): 
            van = b_lane/((1+d)**contadoraños)
            VAN = van + VAN
            print("el valor del beneficio actualizado en el año ", contadoraños, "es", van)
            print("el valor del beneficio acutalizado acumulado en el año ", contadoraños, "es", VAN)
            contadoraños = contadoraños + 1 

          print("el valor del VAN DESPUES DEL CICLO WHILE es", VAN)

          decimal = años - int(años)
          print(decimal)
          años_redondeo_superior = int(años)
          print(años_redondeo_superior)
          beneficio_año_extra = b_lane/((1+d)**años_redondeo_superior)
          print("el beneficio en el año extra es",beneficio_año_extra )
          beneficio_año_extra_conchito = beneficio_año_extra*decimal
          print("el beneficio conchito del ultimo año es", beneficio_año_extra_conchito)
          VAN = VAN + beneficio_año_extra_conchito
          print("el van mas el conchito es", VAN)
          print("el valor del VAN es", VAN)
        
      error = abs(VAN-VAN_0)
      iii = iii + 1 
      VAN_0 = VAN

    print("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
    print("el valor del VAN ES:", VAN_0, "para el año:", anio)
    print("el valor del beneficio anual ES:", b_lane, "para el año:", anio)
    print("el TONELAJE DE MATERIAL ES:", qm, "para el año:", anio)
    print("EL VALOR DEL FACTOR RO ES:", RO)
    print("el valor del Goptimo es:", Goptimo, "para el año:", anio)

    listaanios.append(anio) 
    listavanes.append(VAN_0)
    listaro.append(RO)
    listatm.append(qm)
    listatc.append(qc)
    listatr.append(qr)
    listaGoptimo.append(Goptimo*100)
    listaley_media.append(ley_media2*100)
    listabeneficio.append(b_lane)
    listaconcentrado.append(qconc)
    print(listaanios)
    print(listavanes)
    print(listatm)
    print(listatc)
    print(listatr)
    print(listaGoptimo)

    datossalida1 = {"Años":listaanios,"ro": listaro, "VAN": listavanes , "Ley de Corte en %": listaGoptimo , "beneficio anual": listabeneficio,  "ley media en %": listaley_media, "Ton de Material": listatm , "Ton de Mineral": listatc , "Ton de Producto": listatr, "Ton de Concentrado": listaconcentrado} 
    datosultra1 = pd.DataFrame(data = datossalida1)
    print(datosultra1)


  ###################################################################
  ####################### DATOS DE LANE #############################
  ###################################################################


    print("#############################################################################")
    print("###################### DATOS DE FASE 2 OPTMIZANTE #############################")
    print("#############################################################################")

  ##########################################################################
  #################### DATOS DE FASE 2 OPTIMIZANTE #########################
  ##########################################################################

    max_van = datosultra1["VAN"].max()
    fila_max_van = datosultra1.loc[datosultra1["VAN"] == max_van]
    año_max = fila_max_van.iloc[0,0]
    ro_max = fila_max_van.iloc[0,1]
    van_max = fila_max_van.iloc[0,2]
    cog_max = fila_max_van.iloc[0,3]
    beneficio_max = fila_max_van.iloc[0,4]
    leymedia_max = fila_max_van.iloc[0,5]
    qm_max = fila_max_van.iloc[0,6]
    qc_max = fila_max_van.iloc[0,7]
    qr_max = fila_max_van.iloc[0,8]
    qconc_max = fila_max_van.iloc[0,9]

    print("EL VALOR DE RO OPTIMO ES: ",ro_max, "EN EL AÑO ", año_max)
    print("EL VALOR DEL VAN OPTIMO ES:", van_max, "EN EL AÑO ", año_max)
    print("EL VALOR DEL COG OPTIMO ES:", cog_max, "EN EL AÑO ", año_max)
    print("EL VALOR DEL BENEFICIO OPTIMO ES:", beneficio_max, "EN EL AÑO ", año_max)
    print("EL VALOR DE LA LEY MEDIA % ES:", leymedia_max, "EN EL AÑO ", año_max)
    print("EL VALOR DEL qm es:", qm_max, "EN EL AÑO ", año_max)
    print("EL VALOR DEL qc es:", qc_max, "EN EL AÑO ", año_max)
    print("EL VALOR DEL qr es:", qr_max, "EN EL AÑO ", año_max)
    print("EL VALOR DEL qr es:", qconc_max, "EN EL AÑO ", año_max)
    lista_años_FASE2.append(anio)
    listavanFASE2.append(van_max)
    listabeneficiosFASE2.append(beneficio_max)
    listaleyes_COG_FASE2.append(cog_max)
    listaroFASE2.append(ro_max)
    lista_qm_FASE2.append(qm_max)
    lista_qc_FASE2.append(qc_max)
    lista_qr_FASE2.append(qr_max)
    lista_ley_media_FASE2.append(leymedia_max)
    lista_concentrado_FASE2.append(qconc_max)


    datos_finales_XXX = {"Años":lista_años_FASE2,"ro optimos": listaroFASE2, "VAN optimo": listavanFASE2 , "Ley de Corte en %": listaleyes_COG_FASE2 , "beneficio anual": listabeneficiosFASE2,  "ley media en %": lista_ley_media_FASE2, "Ton de Material": lista_qm_FASE2 , "Ton de Mineral": lista_qc_FASE2 , "Ton de Producto": lista_qr_FASE2, "Ton de concentrado": lista_concentrado_FASE2} 
    datos_finales_XXX_dataframe = pd.DataFrame(data = datos_finales_XXX)
    archivador_unico = archivador.append(datos_finales_XXX_dataframe, ignore_index= True)
    print("EL ARCHIVADOR UNICO ES:")
    print(archivador_unico)

    if RO ==1:
      datossalida_final_fase_2_RO_1 = {"Años":lista_años_FASE2,"ro optimos": listaroFASE2, "VAN optimo": listavanFASE2 , "Ley de Corte en %": listaleyes_COG_FASE2 , "beneficio anual": listabeneficiosFASE2,  "ley media en %": lista_ley_media_FASE2, "Ton de Material": lista_qm_FASE2 , "Ton de Mineral": lista_qc_FASE2 , "Ton de Producto": lista_qr_FASE2} 
      datos_ultra_fase_2_final_RO_1 = pd.DataFrame(data=datossalida_final_fase_2_RO_1)
      print("LOS DATOS ULTRA FASE 2 FINAL RO 1 ES:")
      print(datos_ultra_fase_2_final_RO_1)

    if RO ==2:
      datossalida_final_fase_2_RO_2 = {"Años":lista_años_FASE2,"ro optimos": listaroFASE2, "VAN optimo": listavanFASE2 , "Ley de Corte en %": listaleyes_COG_FASE2 , "beneficio anual": listabeneficiosFASE2,  "ley media en %": lista_ley_media_FASE2, "Ton de Material": lista_qm_FASE2 , "Ton de Mineral": lista_qc_FASE2 , "Ton de Producto": lista_qr_FASE2} 
      datos_ultra_fase_2_final_RO_2 = pd.DataFrame(data=datossalida_final_fase_2_RO_2)
      print(datos_ultra_fase_2_final_RO_2)

    if RO ==3:
      datossalida_final_fase_2_RO_3 = {"Años":lista_años_FASE2,"ro optimos": listaroFASE2, "VAN optimo": listavanFASE2 , "Ley de Corte en %": listaleyes_COG_FASE2 , "beneficio anual": listabeneficiosFASE2,  "ley media en %": lista_ley_media_FASE2, "Ton de Material": lista_qm_FASE2 , "Ton de Mineral": lista_qc_FASE2 , "Ton de Producto": lista_qr_FASE2} 
      datos_ultra_fase_2_final_RO_3 = pd.DataFrame(data=datossalida_final_fase_2_RO_3)
      print(datos_ultra_fase_2_final_RO_3)

    if RO ==4:
      datossalida_final_fase_2_RO_4 = {"Años":lista_años_FASE2,"ro optimos": listaroFASE2, "VAN optimo": listavanFASE2 , "Ley de Corte en %": listaleyes_COG_FASE2 , "beneficio anual": listabeneficiosFASE2,  "ley media en %": lista_ley_media_FASE2, "Ton de Material": lista_qm_FASE2 , "Ton de Mineral": lista_qc_FASE2 , "Ton de Producto": lista_qr_FASE2} 
      datos_ultra_fase_2_final_RO_4 = pd.DataFrame(data=datossalida_final_fase_2_RO_4)
      print(datos_ultra_fase_2_final_RO_4)

    if RO ==4:
      datossalida_final_fase_2_RO_4 = {"Años":lista_años_FASE2,"ro optimos": listaroFASE2, "VAN optimo": listavanFASE2 , "Ley de Corte en %": listaleyes_COG_FASE2 , "beneficio anual": listabeneficiosFASE2,  "ley media en %": lista_ley_media_FASE2, "Ton de Material": lista_qm_FASE2 , "Ton de Mineral": lista_qc_FASE2 , "Ton de Producto": lista_qr_FASE2} 
      datos_ultra_fase_2_final_RO_4 = pd.DataFrame(data=datossalida_final_fase_2_RO_4)
      print(datos_ultra_fase_2_final_RO_4)

    if RO ==5:
      datossalida_final_fase_2_RO_5 = {"Años":lista_años_FASE2,"ro optimos": listaroFASE2, "VAN optimo": listavanFASE2 , "Ley de Corte en %": listaleyes_COG_FASE2 , "beneficio anual": listabeneficiosFASE2,  "ley media en %": lista_ley_media_FASE2, "Ton de Material": lista_qm_FASE2 , "Ton de Mineral": lista_qc_FASE2 , "Ton de Producto": lista_qr_FASE2} 
      datos_ultra_fase_2_final_RO_5 = pd.DataFrame(data=datossalida_final_fase_2_RO_5)
      print(datos_ultra_fase_2_final_RO_5)

    if RO ==6:
      datossalida_final_fase_2_RO_6 = {"Años":lista_años_FASE2,"ro optimos": listaroFASE2, "VAN optimo": listavanFASE2 , "Ley de Corte en %": listaleyes_COG_FASE2 , "beneficio anual": listabeneficiosFASE2,  "ley media en %": lista_ley_media_FASE2, "Ton de Material": lista_qm_FASE2 , "Ton de Mineral": lista_qc_FASE2 , "Ton de Producto": lista_qr_FASE2} 
      datos_ultra_fase_2_final_RO_6 = pd.DataFrame(data=datossalida_final_fase_2_RO_6)
      print(datos_ultra_fase_2_final_RO_6)


    listaanios = [] 
    listavanes = []
    listaro = []
    listatm = []
    listatc = []
    listatr = []
    listaGoptimo = []
    listaley_media = []
    listabeneficio = []
    listaconcentrado = []

    print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")
    print("###########################################################################")
    print("###########################################################################")
    print("###########################################################################")


    sumaton = leyes["mineral"].sum()
    print("el valor de la suma del tonelaje de mineral para el año", anio, "es: ", sumaton)

    mine = leyes["mineral"]

    sumton = mine.sum()
    print(sumton)
    tonqueda = sumton-qm_max ######OJOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
    print("el tonelaje restante es: ", tonqueda)
    px = mine/sumton
    print("la columna con los pesos es: ", px)
    qmpx = px*qm_max ######OJOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
    print(qmpx)

    tonrem = mine-qmpx
    print(tonrem)

    leyes["mineral"]=tonrem

    
    print(leyes)


    anio = anio + 1  #### ACA SE PASA AL SIGUIENTE AÑO #####

############################################################################################
############################# PASO AL PRIMER CICLO WHILE ###################################
############################################################################################
############################################################################################

  archivador_unico_2 = archivador_unico_2.append(archivador_unico, ignore_index= True)
  print("EL ARCHIVADOR UNICO 2 ES: ")
  print(archivador_unico_2)
  RO = RO + paso_algortimo 
  anio = 1 
  ##############################################################################################
  ################## LINEAS ESPECIALES SI SE EJECUTA EN PYTHON O COLAB #########################
  ##############################################################################################

  leyes = pd.DataFrame(data = base_de_datos) #### DESACTIVAR SI ES COLAB DE GOOGLE

  #leyes = pd.read_csv("/content/HOMOGENEOS.csv",sep=";") ### ACTIVAR SI ES COLAB DE GOOGLE
  leyes
  ##############################################################################################
  ##############################################################################################
  ##############################################################################################

  mc = (leyes["leymin"]+leyes["leymax"])/2
  mc 
  leyes = leyes.assign(mc=mc)
  leyes
  #linea especial de codigo para crear la primera tabla y mas importante que es la leymedia 
  i= 0 
  l= []
  while i<=(len(leyes)-1):
    aa = leyes.iloc[i:len(leyes),:]
    cx = aa["mineral"]*aa["mc"]
    dx = cx.sum()
    bx= aa["mineral"].sum()
    ex = dx/bx
    l.append(ex)
    #print(l)
    i = i + 1
  leyes = leyes.assign(leymedia=l) 
  print(leyes)  #ACA ESTA LISTA LA TABLA LEYES
  tonqueda = leyes["mineral"].sum() 

  listaanios = [] 
  listavanes = []
  listaro = []
  listatm = []
  listatc = []
  listatr = []
  listaGoptimo = []
  listaley_media = []
  listabeneficio = []
  listaconcentrado = []

  lista_años_FASE2 = []
  listavanFASE2 = []
  listabeneficiosFASE2 = []
  listaleyes_COG_FASE2 = []
  listaroFASE2 = []
  lista_qm_FASE2 = []
  lista_qc_FASE2 = []
  lista_qr_FASE2 = []
  lista_ley_media_FASE2 = []
  lista_concentrado_FASE2 = []



VAN_ULTRAMAXIMO = archivador_unico_2["VAN optimo"].max()
print("EL VALOR DEL VAN MAXIMO FINAL ES: ", VAN_ULTRAMAXIMO)
fila_VAN_ULTRAMAXIMO = archivador_unico_2.loc[archivador_unico_2["VAN optimo"] == VAN_ULTRAMAXIMO]
print(fila_VAN_ULTRAMAXIMO)
RO_ULTRAOPTIMO = fila_VAN_ULTRAMAXIMO.iloc[0,1]
print("EL VALOR DEL RO OPTIMO ES:", RO_ULTRAOPTIMO)

ARCHIVADOR_MAXIMO = archivador_unico_2["ro optimos"] == RO_ULTRAOPTIMO
filtrado_archivador_maximo = archivador_unico_2[ARCHIVADOR_MAXIMO]
print("LOS DATOS OPTIMIZANTES MAXIMOS SON:")
print(filtrado_archivador_maximo)

#archivador_unico_2.to_excel("RESULTADO DE LANE ESMERALDA.xlsx")

ARCHIVADOR_SELECCION = archivador_unico_2["ro optimos"] == 0
ARCHIVADOR_SELECCION_2 = archivador_unico_2[ARCHIVADOR_SELECCION]
print("EL RESULTADO DEL ALGORITMO DE LANE ES:", ARCHIVADOR_SELECCION_2)

ARCHIVADOR_SELECCION_2.insert(5, "beneficio actualizado", (ARCHIVADOR_SELECCION_2["beneficio anual"]/((1+d)**(ARCHIVADOR_SELECCION_2["Años"]-1))), allow_duplicates=False)
print(ARCHIVADOR_SELECCION_2)

i = 0 
to = []
while i<=(len(ARCHIVADOR_SELECCION_2)-1):
  ee = ARCHIVADOR_SELECCION_2.iloc[i:len(ARCHIVADOR_SELECCION_2),:]
  cr = ee["beneficio actualizado"]
  tr = float(cr.sum())
  to.append(tr)
  i = i + 1 
print(to)

ARCHIVADOR_SELECCION_2.insert(6, "VAN verdadero", to, allow_duplicates=False)

print("###########################################################################################  #######################")
print("##########################################################################################    ######################")
print("#########################################################################################      #####################")
print("#################################################################################         LANE         #############")
print("####################################################################################                ################")
print("############# RESULTADOS FINALES DEL ALGORITMO DE LANE ###############################            ##################")
print("##################### SEPARADOR DECIMAL ES EL PUNTO #################################      ##      #################")
print("#####################################################################################   ########   #################")
print("####################################################################################  ############  ################")


lista_1 = {"Año": np.array(ARCHIVADOR_SELECCION_2["Años"]), "VAN en MUSD": np.array(ARCHIVADOR_SELECCION_2["VAN verdadero"]/1000000), "Beneficio anual en MUSD": np.array(ARCHIVADOR_SELECCION_2["beneficio anual"]/1000000) , "Ley de Corte en %": np.array(ARCHIVADOR_SELECCION_2["Ley de Corte en %"]) , "ley media en %": np.array(ARCHIVADOR_SELECCION_2["ley media en %"])}
lista_a = pd.DataFrame(data = lista_1)
print(lista_a)
lista_3 = {"Año": np.array(ARCHIVADOR_SELECCION_2["Años"]), "Material Extraido en MTon": np.array(ARCHIVADOR_SELECCION_2["Ton de Material"]/1000000), "Mineral enviado a Planta en MTon": np.array(ARCHIVADOR_SELECCION_2["Ton de Mineral"]/1000000), "Cobre Fino en Toneladas": np.array(ARCHIVADOR_SELECCION_2["Ton de Producto"]), "Concentrado Vendido en Toneladas": np.array(ARCHIVADOR_SELECCION_2["Ton de concentrado"])}
lista_c = pd.DataFrame(data = lista_3)
print(lista_c)

print("#########################################################################")
print("#########################################################################")
print("#########################################################################")

#################################################################
#################### ARCHIVO EXCEL DE SALIDA ####################
#################################################################
#ARCHIVADOR_SELECCION_2.to_excel(titulo)   ######## LINEA QUE DEBE IR EN COLAB DE GOOGLE #######
#################################################################
#################################################################

##########################################################################################
#################################### GRAFICOS FINALES ####################################
##########################################################################################

fig = plt.figure(figsize=(15,20), dpi = 70)
fig.tight_layout()
ax1 = fig.add_subplot(2,3,1)
ax2 = fig.add_subplot(2,3,2)
ax3 = fig.add_subplot(2,3,3)
ax4 = fig.add_subplot(2,3,4)
ax5 = fig.add_subplot(2,3,5)
ax6 = fig.add_subplot(2,3,6)
ax1.bar(ARCHIVADOR_SELECCION_2["Años"],  height = ARCHIVADOR_SELECCION_2["VAN verdadero"], width = 0.5)
ax2.plot(ARCHIVADOR_SELECCION_2["Años"],  ARCHIVADOR_SELECCION_2["Ley de Corte en %"], color='red', marker='o', label = "X", linestyle='dashed',linewidth=1, markersize=10)
ax3.bar(ARCHIVADOR_SELECCION_2["Años"],  height = ARCHIVADOR_SELECCION_2["Ton de Material"], width = 0.5, color = "orange")
ax4.bar(ARCHIVADOR_SELECCION_2["Años"],  height = ARCHIVADOR_SELECCION_2["Ton de Mineral"], width = 0.5, color = "green")
ax5.bar(ARCHIVADOR_SELECCION_2["Años"],  height = ARCHIVADOR_SELECCION_2["Ton de Producto"], width = 0.5, color = "red")
ax6.bar(ARCHIVADOR_SELECCION_2["Años"],  height = ARCHIVADOR_SELECCION_2["Ton de concentrado"], width = 0.5, color = "magenta")
ax1.set_xlabel("años")
ax1.set_ylabel("MUSD")
ax2.set_xlabel("años")
ax2.set_ylabel("Ley de Corte %")
ax3.set_xlabel("años")
ax3.set_ylabel("Millones de Toneladas")
ax4.set_xlabel("años")
ax4.set_ylabel("Millones de Toneladas")
ax5.set_xlabel("años")
ax5.set_ylabel("Toneladas")
ax6.set_xlabel("años")
ax6.set_ylabel("Toneladas")
ax2.grid()
ax1.set_title("Valor Presente Neto")
ax2.set_title("Ley de Corte")
ax3.set_title("Material Movido por Mina")
ax4.set_title("Mineral Enviado a Planta")
ax5.set_title("Cobre Fino Vendido")
ax6.set_title("Concentrado de Cobre vendido")
ticks_van = ticker.FuncFormatter(lambda x, pos:'${: 0.2f}'.format(x/1000000))
ticks_Mton = ticker.FuncFormatter(lambda x, pos:'{: 0.2f}'.format(x/1000000))
ax1.yaxis.set_major_formatter(ticks_van)
ax3.yaxis.set_major_formatter(ticks_Mton)
ax4.yaxis.set_major_formatter(ticks_Mton)
plt.show()

##########################################################################################
##########################################################################################