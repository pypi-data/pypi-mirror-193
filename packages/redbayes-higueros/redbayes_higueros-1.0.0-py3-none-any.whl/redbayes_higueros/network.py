import itertools

class Nodo:
    def __init__(self, nombre, padres, p):
        self.nombre = nombre
        self.estados = []
        self.padres = padres
        self.p = p

class RedBayesiana:
    def __init__(self, nodos):
        self.nodos = nodos

    def calcular_probabilidad(self, evidencias):
        p = 1.0
        for nodo in self.nodos:
            valores_padres = tuple(evidencias[padre.nombre] for padre in nodo.padres)
            p *= nodo.p[valores_padres + (evidencias[nodo.nombre],)]
        return p

    def obtener_probabilidad_conjunta(self, evidencias):
        p = 1.0
        for nodo in self.nodos:
            valores_padres = tuple(evidencias[padre.nombre] for padre in nodo.padres)
            p *= nodo.p[valores_padres + (evidencias[nodo.nombre],)]
        return p
    
    def inferencia_elim_variables(self, variables_eliminar, evidencias):
        nodos_ordenados = self.orden_topologico()
        nodos_restantes = [nodo for nodo in nodos_ordenados if nodo not in variables_eliminar]
        factores = []
        for nodo in nodos_ordenados:
            if nodo in evidencias:
                factor = {nodo: {evidencias[nodo]: 1.0}}
            else:
                p = self.nodos[nodo].p
                padres = self.nodos[nodo].padres
                estados_padres = [self.nodos[padre].estados for padre in padres]
                estados_nodo = self.nodos[nodo].estados
                factor = {}
                for estado_nodo in estados_nodo:
                    for combinacion_estados_padres in itertools.product(*estados_padres):
                        valores = combinacion_estados_padres + (estado_nodo,)
                        factor[valores] = p[valores]
            factores.append(factor)
        for variable_eliminar in variables_eliminar:
            factores = self.eliminar_variable(factores, variable_eliminar)
        resultado = {}
        for factor in factores:
            for variable, valores in factor.items():
                if variable not in evidencias:
                    for valor, probabilidad in valores.items():
                        if valor in resultado:
                            resultado[valor] *= probabilidad
                        else:
                            resultado[valor] = probabilidad
        return resultado

    def obtener_probabilidad_marginal(self, nodo, evidencias):
        p = 0.0
        for x in [True, False]:
            evidencias_nodo = evidencias.copy()
            evidencias_nodo[nodo.nombre] = x
            p += self.obtener_probabilidad_conjunta(evidencias_nodo)
        return p

    def obtener_probabilidad_condicional(self, nodo, evidencias):
        p = {}
        for x in [True, False]:
            evidencias_nodo = evidencias.copy()
            evidencias_nodo[nodo.nombre] = x
            p[x] = self.obtener_probabilidad_conjunta(evidencias_nodo)
        normalizador = sum(p.values())
        for value in p.values():
            value /= normalizador
        return p

    def calcular_probabilidad_condicional(self, variable, evidencias):
        nodo_variable = next(
            (nodo for nodo in self.nodos if nodo.nombre == variable), None
        )
        if nodo_variable is None:
            raise ValueError(f"No se encontró la variable {variable}")

        p_variable = {}
        for valor_variable in nodo_variable.p.keys():
            evidencias_completas = evidencias.copy()
            evidencias_completas[variable] = valor_variable
            p_variable[valor_variable] = self.calcular_probabilidad(evidencias_completas)

        # Normalizar las probabilidades para que sumen 1
        p_suma = sum(p_variable.values())
        if p_suma == 0:
            raise ValueError("No se puede calcular la probabilidad condicional debido a la falta de información")
        for value in p_variable.values():
            value /= p_suma

        return p_variable


    def eliminar_variable(self, factores, variable_eliminar):
        factores_restantes = []
        for factor in factores:
            if variable_eliminar in factor:
                nuevos_factores = []
                for valor_variable_eliminar, probabilidad in factor[variable_eliminar].items():
                    nuevo_factor = {variable: {} for variable in factor if variable != variable_eliminar}
                    for combinacion_valores in itertools.product(*[factor[variable].items() for variable in nuevo_factor]):
                        valores = {variable: valor for variable, (valor, _) in zip(nuevo_factor, combinacion_valores)}
                        nuevo_factor |= valores
                        nuevo_factor[variable_eliminar][valor_variable_eliminar] = probabilidad
                    nuevos_factores.append(nuevo_factor)
                factor_restante = self.multiplicar_factores(nuevos_factores)
            else:
                factor_restante = factor
            factores_restantes.append(factor_restante)
        return factores_restantes

    def multiplicar_factores(self, factores):
            resultado = {}
            for factor in factores:
                for variable, valores in factor.items():
                    if variable in resultado:
                        for valor, probabilidad in valores.items():
                            resultado[variable][valor] *= probabilidad
                    else:
                        resultado[variable] = valores.copy()
            return resultado
