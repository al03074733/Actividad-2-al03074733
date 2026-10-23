print("\n++++++++++++")
print("Ejercicio 5 realizado por Sofia")
print("Ejercicio 5: ¿Cuánto dura mi playlist?")

# Duración de cada canción en segundos
canción1 = 210
canción2 = 200
canción3 = 180
canción4 = 230
canción5 = 180

# Sumamos todo
total_segundos = canción1 + canción2 + canción3 + canción4 + canción5

# // división entera: cuántos minutos completos caben
minutos = total_segundos // 60

# % residuo: los segundos que sobran 
segundos = total_segundos % 60
print("\nResultados")
print(f"Total de segundos: {total_segundos}")
print(f"Total en segundos: {total_segundos}")
print(f"Tu playlist dura {minutos} minutos con {segundos} segundos")
print("\n++++++++++++")