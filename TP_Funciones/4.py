#Ejercicio 4: Manejo de aridad variable (*args y **kwargs) 
#Concepto: *ARGS / **KWARGS
def generar_auditoria_sistema(modulo:str,*mensajes:str,**metadatos)->str:
    lineas = [f"MÓDULO: {modulo.upper()}"]
    for i, mensaje in enumerate(mensajes, start=1):
        lineas.append(f"[{i}] {mensaje}")
    for clave, valor in metadatos.items():
        lineas.append(f"{clave.upper()}: {valor}")
    return "\n".join(lineas)

log = generar_auditoria_sistema("AUTH", "Intento fallido", "Bloqueo de IP", usuario="admin", ip="192.168.1.10")
print(log)
print()