print("Hola a todos :D")
print("Esto es una prueba")


 def resolver_ecuacion():
     print("Resuelve la siguiente ecuación simple: 5 + 3 = ?")
     
     respuesta = int(input("Tu respuesta: "))
     
     if respuesta == 5 + 3:
         print("¡Correcto! La respuesta es 8.")
     else:
         print(f"¡Incorrecto! La respuesta correcta es 8.")
 
 # Llamar a la función para resolver la ecuación
 resolver_ecuacion()
