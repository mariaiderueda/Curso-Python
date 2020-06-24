#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Introducción a Python


# In[41]:


# Python como calculadora
#Python es perfectamente adecuado para hacer cálculos básicos. Además de la suma, resta, multiplicación y división, también hay soporte para operaciones más avanzadas como:

#Exponentes: **. Este operador eleva el número a su izquierda a la potencia del número a su derecha. Por ejemplo 4 ** 2 dará 16.
#Residuos: %. Este operador devuelve el resto de la división del número a la izquierda por el número a su derecha. Por ejemplo, 18% 7 es igual a 4.

#Resuelve los siguientes ejemplos: 

# Imprime la suma de 7 mas 10:
print(7 + 10)

# Divide 5 entre 8
print(5 / 8)

# Suma 7 mas 10
print(7 + 10)

# Suma y resta 5 con 5
print(5 + 5)
print(5 - 5)

# Multiplicación, división, residuo, and exponente
print(3 * 5)
print(10 / 2)
print(18 % 7)
print(4 ** 2)

# Cuanto vale un billete de 100 pesos que puede invertir con un rendimiento de 10% cada año. ¿Cuánto tendrás en 7 años?
print(100 * 1.1 ** 7)


# In[2]:


# Creación de variables
#En Python, una variable le permite hacer referencia a un valor con un nombre. Para crear una variable use =, como este ejemplo:

#x = 5
#Ahora puede usar el nombre de esta variable, x, en lugar del valor real, 5.

#Recuerde, = en Python significa asignación, ¡no prueba la igualdad!

# Crea una variable "ahorros" igual a 100
ahorros = 100

#Crea una variable "mult_crec"
mult_crec = 1.1

# Crea una variable "resultado" con el resultado anterior
resultado = ahorros * mult_crec ** 7

# Imprime el resultado
print(resultado)


# In[21]:


# Tipos de variables

#En el ejercicio anterior, trabajó con dos tipos de datos de Python:

#int o entero: un número sin una parte fraccionaria. ahorros, con el valor 100, es un ejemplo de un entero.
#flotante: un número que tiene una parte entera y una fracción, separadas por un punto. mult_crec, con el valor 1.1, es un ejemplo de flotante.
#Junto a los tipos de datos numéricos, hay otros dos tipos de datos muy comunes:

#str o string: un tipo para representar texto. Puede usar comillas simples o dobles para construir una cadena.
#bool o boolean: un tipo para representar valores lógicos. Solo puede ser Verdadero o Falso (¡la capitalización es importante!).
#A continuación vas a crear tres variables: "edad" igual a tu edad, "estatura" igual a tu estatura (con decimales), "nombre" igual a tu nombre,y "log_bin" igual a True.
edad = 24
estatura = 1.64
nombre = 'María'
log_bin = True

#Ahora verifica el tipo de variable de cada una usando el comando type() e imprime los resultados
print(type(num))
print(type(dec))
print(type(letras))
print(type(log_bin))


# In[43]:


#Conversión de tipo de variables
#Usar el operador + para pegar dos cadenas puede ser muy útil en la creación de mensajes personalizados.

#Supongamos, por ejemplo, que ha calculado el rendimiento de su inversión y desea resumir los resultados en una cadena. Suponiendo que los ahorros enteros y el resultado flotante están definidos, puede intentar algo como esto:

#print ("Empecé con $" + ahorro + "y ahora tengo $" + resultado + ". ¡Impresionante!")
#Sin embargo, esto no funcionará, ya que no puede simplemente sumar cadenas/strings y enteros/flotantes.

#Para corregir el error, deberá convertir explícitamente los tipos de sus variables. Más específicamente, necesitará str (), para convertir un valor en una cadena. str(ahorros), por ejemplo, convertirá el ahorro entero en una cadena.

#Funciones similares como int (), float () y bool () te ayudarán a convertir los valores de Python en cualquier tipo:

#Imprime la frase "Me llamo (tu nombre), tengo (tu edad) años, y mido (tu estatura)" utilizando las variables nombre, edad y estatura y haciendo uso del comando str()

print("Me llamo " + nombre + ", tengo " + str(edad) + " años, y mido " + str(estatura))


# In[25]:


# LISTAS
#Una lista es un tipo de datos compuestos en los que puedes agrupar distintos valores:
#nombre = "Maria"
#apellido = "De Rueda"
#mi_lista = ["me", "llamo", a, b]
#Con daltos de la Encuesta Nacional de Ingresos y Gastos de los Hogares (ENIGH) se colectaron los datos de una familia mexicana para los siguientes ejercicios:
cereales = 437.13 #Cuanto destina la familia de su ingreso a comprar cereales
carnes =  1787.13 #Cuanto destina la familia de su ingreso a comprar carnes
leche = 2841.41 #Cuanto destina la familia de su ingreso a comprar leche y derivados
verduras = 861.38 #Cuanto destina la familia de su ingreso a comprar verduras
frutas = 244.27 #Cuanto destina la familia de su ingreso a comprar frutas

#Termina la lista adaptada a alimentos:
alimentos = ["Gasto en cereales", cereales, "Gasto en carnes", carnes, "Gasto en leche", leche, "Gasto en verduras", verduras, "Gasto en frutas", frutas]

# Imprime alimentos
print(alimentos)

#Como pudiste comprobar, las listas en Python pueden tener distintos tipos de variables, en este caso la lista tiene variables tipo String y Float.


# In[28]:


#LISTA DE LISTAS
#A menudo te tocará trbajar con muchos datos y tendrá sentido agrupar algunos de estos.
#En lugar de crear una lista plana que contenga strings y floats como el ejercicio pasado, puedes crear una lista de listas.
#Acompleta la lista de listas mostrada a continuación e imprime la nueva lista para que notes la diferencia, ¿Cuál hace más sentido?.
alimentos = [["Gasto en cereales", cereales],
         ["Gasto en carnes", carnes],
         ["Gasto en leche", leche],
         ["Gasto en verduras", verduras],
         ["Gasto en frutas", frutas]]
print(alimentos)

#Ahora descrubre que tipo de variables es alimentos para que continues familiarizandote con el tipo de variables en Python:
print(type(alimentos))


# In[29]:


# SUBCONJUNTOS DE LISTAS

#Para hacer una subconjunto de listas tomaremos como ejemplo el código a continuación
#x = ["a", "b", "c", "d"]
#x [1]
#x [-3] # mismo resultado!

#la lista x tiene 4 índices que comienzan con cero, es decir, "a" es el índice 0, "b" es el índice 1 y así sucesivamente. Con los corchetes después de la variable puedes llamar a cualquier parte de la lista.
#También lo puedes hacer usando índices negativos cuando la lista es muy larga, -1 corresponde al último valor de la lista que en este caso es "d"

#¿Recuerdas la lista de áreas de antes, que contiene cadenas y flotantes? Su definición ya está en el guión. ¿Puedes agregar el código correcto para hacer algunos subconjuntos de Python?
alimentos = ["Gasto en cereales", cereales, "Gasto en carnes", carnes, "Gasto en leche", leche, "Gasto en verduras", verduras, "Gasto en frutas", frutas]

#Imprime el segundo elemento de la lista:
print(alimentos[1])

#Imprime el último elemento de la lista:
print(alimentos[-1])

#Imprime cuánto gasta la familia del ejemplo en leche y derivados:
print(alimentos[5])


# In[30]:


#Subconjuntos y calculos

#Después de extraer los valores de una lista, puede usarlos para realizar cálculos adicionales. Tome este ejemplo, donde se extraen el segundo y cuarto elemento de una lista x. Las cadenas que resultan se pegan juntas usando el operador +:

#x = ["a", "b", "c", "d"]
#imprimir (x [1] + x [3])

#Utilizando la lista de alimentos, crea una variables que me diga cuanto gasta la familia en frutas y verduras e imprime el resultado:
frut_verd = alimentos[-1] + alimentos[-3]
print(frut_verd)


# In[37]:


#Subconjunto de multiples elementos de una lista

#Seleccionar valores individuales de una lista es solo una parte de la historia. También es posible dividir su lista, lo que significa seleccionar varios elementos de su lista. Use la siguiente sintaxis:

#mi_lista [inicio: fin]
#El índice inicial se incluirá, mientras que el índice final no.

#El siguiente ejemplo de código muestra un ejemplo. Una lista con "b" y "c", correspondiente a los índices 1 y 2, se seleccionan de una lista x:

#x = ["a", "b", "c", "d"]
#x [1: 3]
#Los elementos con índice 1 y 2 están incluidos, mientras que el elemento con índice 3 no lo está.

alimentos = ["Gasto en cereales", cereales, "Gasto en verduras", verduras, "Gasto en frutas", frutas, "Gasto en carnes", carnes, "Gasto en leche", leche]

#Crea una variable que contenga el gasto en alimentos de origen animal y de no origen animal e imprime el resultado
or_anim = alimentos[0:6]
no_or_anim = alimentos[6:10]

print(or_anim)
print(no_or_anim)


# In[38]:


# Subconjunto de multiples elementos de una lista
#Existe otra manera de hacer subconjuntos con sin especificar con índices. Si no especifica el índice de inicio, Python se da cuenta de que desea comenzar su segmento al comienzo de su lista. Si no especifica el índice final, el segmento irá hasta el último elemento de su lista. Ve el siguiente ejemplo:
#x = ["a", "b", "c", "d"]
#x [: 2]
#x [2:]
#X[:]

#Realiza de nuevo las variables pero con el nuevo sintaxis y agrega una variable "todo" con todos los elementos de la lista:
or_anim = alimentos[:6]
no_or_anim = alimentos[6:]
todo = alimentos[:]

print(or_anim)
print(no_or_anim)
print(todo)


# In[39]:


# Subconjunto de listas de listas

#Viste antes que una lista de Python puede contener prácticamente cualquier cosa; incluso otras listas! Para hacer un subconjunto de listas de listas, puede usar la misma técnica que antes: corchetes. Pruebe los comandos en el siguiente ejemplo de código:

# x = [["" "," b "," c "],
#     ["d", "e", "f"],
#     ["g", "h", "i"]]
#x[2][0] #Aquí le estarías pidiendo a Python que te de el primer elemento de la tercera lista, es decir, "g"
#x[2][: 2] #Aquí le estarías pidiendo a Python que te de los primeros tres elemento de la tercera lista, es decir, "g, h, i"
#x[2] da como resultado una lista, que puede subconjunto nuevamente agregando corchetes adicionales.

alimentos = [["Gasto en cereales", cereales],
         ["Gasto en carnes", carnes],
         ["Gasto en leche", leche],
         ["Gasto en verduras", verduras],
         ["Gasto en frutas", frutas]]

#Imprime el valor carnes de la lista alimentos:
print(alimentos[1][1])


# In[44]:


# Manipulando listas
#Reemplazar elementos de la lista es bastante fácil. Simplemente subconjunte la lista y asigne nuevos valores al subconjunto. Puede seleccionar elementos individuales o puede cambiar secciones enteras de la lista a la vez.

#Observa el código que se muestra a continuación. ¿Puedes decir qué está pasando y por qué?

#x = ["a", "b", "c", "d"]
#x [1] = "r" #le estoy pidiendo a python que cambie el valor "b" por "r"
#x [2:] = ["s", "t"] #le estoy pidiendo a python que cambie los valores "c y d" por "s y t"
#Para este y los siguientes ejercicios, continuará trabajando en la lista de áreas que contiene el gasto en alimentos de una familia mexicana.

alimentos = ["Gasto en cereales", 437.13, "Gasto en verduras", 861.38, "Gasto en frutas", 244.27, "Gasto en carnes", 1787.13, "Gasto en leche", 2841.41]

#redondea el gasto en verduras de 861.38 a 861.4

alimentos[3] = 861.4

#Cambia el texto "Gasto en leche" a "Gasto en leche y derivados"

alimentos[-2] = "Gasto en leche y derivados"

#Imprime alimentos y comprueba que se hicieron los cambios:
print(alimentos)


# In[45]:


# Ampliar una lista
#Si puede cambiar elementos en una lista, seguramente desea poder agregarle elementos, ¿verdad? Puedes usar el operador +:

#x = ["a", "b", "c", "d"]
#y = x + ["e", "f"] #la lista y tiene todos los elementos de la lista x mas los elementos "e y f"

#Agrega a la lista de alimentos que la familia gasta 308.57 pesos en huevos y llama a esa nueva lista alimentos_1:
alimentos_1 = alimentos + ["Gasto en huevos", 308.57]

#Agrega a la lista de alimentos_1 que la familia gasta 964.28 pesos en café y llamala alimentos_2:
alimentos_2 = alimentos_1 + ["Gasto en cafe", 964.28]

#Imprimer la variable alimentos_2 para comprobar que se hicieron tus cambios:
print(alimentos_2)


# In[47]:


# Eliminar elementos de la lista
#Finalmente, también puede eliminar elementos de su lista. Puede hacer esto con la declaración "del":

#x = ["a", "b", "c", "d"]
#del (x [1]) #Python me va a eliminar el elemento "b"
#Preste atención aquí: tan pronto como elimine un elemento de una lista, ¡los índices de los elementos que vienen después del elemento eliminado cambian todos!

#La versión actualizada y extendida de las áreas que ha creado en los ejercicios anteriores se codifica a continuación. 

alimentos = ['Gasto en cereales', 437.13, 'Gasto en verduras', 861.4, 'Gasto en frutas', 244.27, 'Gasto en carnes', 1787.13, 'Gasto en leche y derivados', 2841.41, 'Gasto en huevos', 308.57, 'Gasto en cafe', 964.28]

#Los ; El signo se utiliza para colocar comandos en la misma línea. Los siguientes dos fragmentos de código son equivalentes:

# Misma línea
#comando1; comando2

# Líneas separadas
#comando1
#comando2

#Elimina el gasto que hace la familia mexicana en café:

del(alimentos[-3:-1])
print(alimentos)


# In[48]:


#FUNCIONES

#Fuera de la caja, Python ofrece un montón de funciones integradas para facilitarle la vida como científico de datos. Ya conoce dos de estas funciones: print() y type(). También ha utilizado las funciones str(), int(), bool() y float() para cambiar entre los tipos de datos. Estas son funciones integradas también.

#Llamar a una función es fácil. Para obtener el tipo de 3.0 y almacenar el resultado como una nueva variable, resultado, puede usar lo siguiente:

#resultado = type(3.0)
#La receta general para llamar a funciones y guardar el resultado en una variable es así:

#salida = nombre_función(entrada)

#Tal vez ya conozca el nombre de una función de Python, pero aún tiene que descubrir cómo usarla. Irónicamente, tienes que pedir información sobre una función con otra función: ayuda (). En IPython específicamente, ¿también puedes usar? antes del nombre de la función.

#Para obtener ayuda sobre la función max(), por ejemplo, puede usar una de estas llamadas:

#help(max)
#? max
 
#Descubre como se usa la función max() usando la función help() y pide a python el máximo de la variable a
a = [1, 2, 3, 4, 5]
help(max)
max(a)


# In[ ]:




