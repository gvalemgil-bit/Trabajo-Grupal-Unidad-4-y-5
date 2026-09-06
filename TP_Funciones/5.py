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