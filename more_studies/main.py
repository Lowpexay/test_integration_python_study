class RoletaDeDados:
    def __init__(self, lados=6):
        self.lados = lados

    def rolar(self):
        import random
        return random.randint(1, self.lados)
    



# Exemplo de uso
if __name__ == "__main__":
    roleta = RoletaDeDados(6)
    resultado = roleta.rolar()
    print(f"Você rolou um dado de {roleta.lados} lados e obteve: {resultado}")
