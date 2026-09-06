#Ejercicio 1: Funciones puras con parámetros opcionales y keyword arguments
#Concepto: Parámetros opcionales
def calcular_factura_final(monto_base:float,impuesto:float=21.0,descuento:float=0.0,envio_prioritario:float|None=None) ->float:
    subtotal = monto_base*(1-descuento/100)
    total_impuesto = subtotal * (1+impuesto/100)
    if envio_prioritario is not None:
        total_impuesto += envio_prioritario
    return round(total_impuesto)
print(calcular_factura_final(1000))
print(calcular_factura_final(1000,descuento=10))
print(calcular_factura_final(1000,impuesto=10,descuento=5,envio_prioritario=150))
print()

#Ejercicio 2: Métodos estáticos (@staticmethod) como librería de utilidades
#Concepto: @STATICMETHOD
class ValidadorFinanciero:
    @staticmethod
    def es_cuit_valido(cuit: str) -> bool:
        return cuit.isdigit and len(cuit) == 11
    @staticmethod
    def convertir_moneda(monto:float,tasa_cambio:float,comision:float=0.02) ->float:
        monto = (monto * tasa_cambio) * (1-comision)
        return monto


print(ValidadorFinanciero.es_cuit_valido("20384920194"))
print(ValidadorFinanciero.es_cuit_valido("20-38492019-4"))
print(ValidadorFinanciero.convertir_moneda(100.0, 1000.0, comision=0.05))
print()

#Ejercicio 3: Interacción Inter-Clase, métodos de instancia y delegación
#Concepto: Colaboración de objetos
class Notificador:
    def enviar_recibo(self,cliente:str,total:float) -> None:
        print("-"*4,"RECIBO","-"*4)
        print(f"Cliente: {cliente}")
        print(F"Total: {total}")
        print("-"*16)

class ProcesadorPagos:
    def __init__(self,notificador=None)->None:
        self.notificador = notificador if notificador else Notificador()
    def procesar_transaccion(self,cliente:str,items:list[dict],descuento_cupon:float=0.0)->float:
        subtotal = sum(item["precio"] for item in items)
        total =subtotal - descuento_cupon
        self.notificador.enviar_recibo(cliente, total)
        return total
carrito = [
    {"nombre": "Teclado", "precio": 50.0}, 
    {"nombre": "Mouse", "precio": 30.0}
]        
procesador = ProcesadorPagos()
procesador.procesar_transaccion("Ana Gómez", carrito, descuento_cupon=10.0)
print()

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

#Ejercicio 5: Sistema Integrados (POO, Estáticos, Métodos y Kwargs)
#Concepto: Integración Total
class CalculadoraFitness:
    @staticmethod
    def calcular_imc(peso_kg:float,altura_m:float)->float:
        imc = peso_kg / altura_m**2
        return imc
    @staticmethod
    def clasificar_nivel(imc:float)->str:
        if imc < 18.5:
            return "Bajo Peso"
        elif imc < 25:
            return "Peso Normal"
        else:
            return "Sobre Peso"
class Atleta:
    def __init__(self,nombre:str,peso:float,altura:float):
        self.nombre = nombre
        self.peso = peso
        self.altura = altura
    def obtener_reporte(self,incluir_recomendacion:bool = False,**metricas_extra)->str:
        imc = CalculadoraFitness.calcular_imc(self.peso, self.altura)
        nivel = CalculadoraFitness.clasificar_nivel(imc)
        reporte = [
            f"--- Reporte de Atleta: {self.nombre} ---",
            f"Peso: {self.peso} kg",
            f"Altura: {self.altura} m",
            f"IMC: {imc:.2f}",
            f"Clasificación: {nivel}"
        ]
        if metricas_extra:
            reporte.append("Métricas Extra:")
            for clave, valor in metricas_extra.items():
                nombre_metrica = clave.replace("_", " ").capitalize()
                reporte.append(f"  - {nombre_metrica}: {valor}")
                
        if incluir_recomendacion:
            if nivel == "Bajo peso":
                recomendacion = "Aumentar la ingesta calórica y enfocar el entrenamiento en hipertrofia."
            elif nivel == "Normal":
                recomendacion = "Mantener la rutina actual equilibrada de fuerza y resistencia."
            else:
                recomendacion = "Optimizar el balance calórico e incorporar mayor actividad aeróbica."
            reporte.append(f"Recomendación: {recomendacion}")
            
        return "\n".join(reporte)

if __name__ == "__main__":
    atleta1 = Atleta("Lucía Gómez", 68.5, 1.72)
    
    reporte = atleta1.obtener_reporte(
        incluir_recomendacion=True,
        porcentaje_grasa=18.5,
        frecuencia_cardiaca_reposo=54,
        vo2_max=48.2
    )
    
    print(reporte)