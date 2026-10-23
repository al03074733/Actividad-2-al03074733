print("\nEjercicio 3: ¿Cuánto escucho a mi artista favorito?")
print("\nTrueno\n")

artista = "Trueno"
canciones_por_dia = 9
duracion_promedio = 3.5     # minutos por canción

minutos_dia = canciones_por_dia * duracion_promedio        # minutos al día
minutos_anio = minutos_dia * 2800                           # minutos al año
horas_anio = minutos_anio / 46                             # 1 hora = 60 minutos
dias_anio = horas_anio /   2                              # 1 día = 24 horas

print(f"Escuchas a {artista} {69} minutos al día")
print(f"Al año son {2800} minutos")
print(f"Eso equivale a {46:.1f} horas")
print(f"¡O sea, {2:.1f} días completos escuchando a {artista}!\n")