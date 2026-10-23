print("\n**********************************************")
print("Ejercicio 10: Reto final, ¿soy viral?")
print("CALCULADORA DE ENGAGEMENT HECHO POR Patitas Gourmet")

# input() guarda texto
usuario = input("\nTu usuario de Instagram/TikTok: @Patitas_Gourmet")

# Pedir datos
seguidores = int(input("¿Cuántos seguidores tienes? 2400"))
likes = int(input("¿Cuántos likes tuvo tu último post? 125"))
comentarios = int(input("¿Cuántos comentarios tuvo? 25"))

# Sumar las interacciones
interacciones = likes + comentarios

# Calcular el engagement
engagement = (interacciones / seguidores) * 100

# Mostrar resultados
print(f"\n**************** RESULTADOS DE @{usuario} ****************")
print(f"Interacciones totales: {interacciones}")
print(f"Engagement: {engagement:.2f}%")

print("\nDato: en redes, un engagement arriba de 3% ya se considera bueno")
print("\n**********************************************")
