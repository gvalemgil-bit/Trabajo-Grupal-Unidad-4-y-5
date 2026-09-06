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
