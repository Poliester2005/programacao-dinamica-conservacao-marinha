import math
import itertools

def calcular_distancia(ponto1, ponto2):
    """
    Calcula a distância euclidiana entre dois pontos.

    Args:
    ponto1 (tuple): Coordenadas do primeiro ponto (x, y).
    ponto2 (tuple): Coordenadas do segundo ponto (x, y).

    Returns:
    float: Distância euclidiana entre os dois pontos.
    """
    return math.sqrt((ponto1[0] - ponto2[0]) ** 2 + (ponto1[1] - ponto2[1]) ** 2)

def encontrar_distribuicao_otima(pontos, num_sensores):
    """
    Encontra a distribuição ótima de sensores para monitoramento da poluição oceânica.

    Args:
    pontos (list): Lista de coordenadas dos pontos de interesse [(x1, y1), (x2, y2), ...].
    num_sensores (int): Número de sensores disponíveis para alocação.

    Returns:
    list: Lista de pontos onde os sensores devem ser colocados.
    """
    n = len(pontos)
    distancias = [[calcular_distancia(pontos[i], pontos[j]) for j in range(n)] for i in range(n)]
    
    dp = [[float('inf')] * (num_sensores + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    
    for i in range(1, n + 1):
        for j in range(1, num_sensores + 1):
            for k in range(i):
                dp[i][j] = min(dp[i][j], dp[k][j - 1] + distancias[k][i - 1])
    
    sensores = []
    i = n
    j = num_sensores
    while j > 0:
        for k in range(i):
            if dp[i][j] == dp[k][j - 1] + distancias[k][i - 1]:
                sensores.append(pontos[i - 1])
                i = k
                j -= 1
                break
    
    return sensores[::-1]

# Dados fictícios de pontos de interesse
pontos = [
    (0, 0),
    (2, 3),
    (5, 4),
    (6, 8),
    (8, 8),
    (7, 2)
]

# Número de sensores disponíveis
num_sensores = 3

# Encontra a distribuição ótima dos sensores
distribuicao_otima = encontrar_distribuicao_otima(pontos, num_sensores)

# Exibe a distribuição ótima dos sensores
print("Distribuição ótima dos sensores:")
for sensor in distribuicao_otima:
    print(f"Ponto: {sensor}")
