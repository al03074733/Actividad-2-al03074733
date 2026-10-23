print("\n****************************************************************")
print("Ejercicio 8: Mi tiempo de pantalla")
print("\n************************ TIEMPO DE PANTALLA ************************")

#Damos de alta la variable app y las horas que paso al día
app = "Youtube"
horas_diarias = 6

print(f"\nPaso {horas_diarias} horas diarias en {app}")

#Calculamos las horas al año
horas_anio = horas_diarias * 365
print(f"Al año son {horas_anio} horas")

#Convertimos las horas a días completos (1 día tiene 24 horas)
dias_anio = horas_anio / 24

#El :.1f muestra solo 1 decimal
print(f"¡Eso equivale a {dias_anio:.1f} días completos sin parar!")

#Calculamos cuántos meses son (un mes tiene aproximadamente 30 días)
meses = dias_anio / 30
print(f"\nO sea, casi {meses:.1f} meses de mi año se van en {app}\n")

print("****************************************************************")