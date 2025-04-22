from ast import arg


def soma(x, y):
    return x + y


def multiplicacao(x, y):
    return x * y


def executar(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna


soma_cinco = executar(soma, 5)
multiplicacao_cinco = executar(multiplicacao, 10)
print(soma_cinco(10))
print(multiplicacao_cinco(10))
