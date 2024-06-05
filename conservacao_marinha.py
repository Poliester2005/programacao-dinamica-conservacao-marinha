def calcular_valor_area(biodiversidade, vulnerabilidade, conectividade):
    """
    Calcula o valor de uma área marinha com base nos critérios fornecidos.
    
    Args:
    biodiversidade (float): Valor de biodiversidade da área.
    vulnerabilidade (float): Valor de vulnerabilidade da área.
    conectividade (float): Valor de conectividade da área.
    
    Returns:
    float: Valor calculado da área marinha.
    """
    return biodiversidade * 0.5 + vulnerabilidade * 0.3 + conectividade * 0.2

def otimizar_alocacao_recursos(areas, orcamento):
    """
    Otimiza a alocação de recursos limitados para maximizar o valor das áreas marinhas protegidas.
    
    Args:
    areas (list): Lista de áreas marinhas, cada uma representada por um dicionário com 'custo' e 'valor'.
    orcamento (int): Orçamento total disponível para alocação.
    
    Returns:
    list: Lista de áreas selecionadas para maximizar o valor dentro do orçamento.
    """
    n = len(areas)
    dp = [[0] * (orcamento + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(orcamento + 1):
            if areas[i - 1]['custo'] <= w:
                dp[i][w] = max(dp[i - 1][w],
                               dp[i - 1][w - areas[i - 1]['custo']] + areas[i - 1]['valor'])
            else:
                dp[i][w] = dp[i - 1][w]

    # Recupera as áreas selecionadas
    areas_selecionadas = []
    w = orcamento
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            areas_selecionadas.append(areas[i - 1])
            w -= areas[i - 1]['custo']

    return areas_selecionadas

# Dados fictícios de áreas marinhas
areas = [
    {'nome': 'Área 1', 'custo': 3, 'biodiversidade': 8, 'vulnerabilidade': 6, 'conectividade': 7},
    {'nome': 'Área 2', 'custo': 5, 'biodiversidade': 7, 'vulnerabilidade': 8, 'conectividade': 6},
    {'nome': 'Área 3', 'custo': 2, 'biodiversidade': 6, 'vulnerabilidade': 7, 'conectividade': 8},
    {'nome': 'Área 4', 'custo': 4, 'biodiversidade': 9, 'vulnerabilidade': 5, 'conectividade': 9},
    {'nome': 'Área 5', 'custo': 7, 'biodiversidade': 8, 'vulnerabilidade': 9, 'conectividade': 8}
]

# Calcula o valor de cada área
for area in areas:
    area['valor'] = calcular_valor_area(area['biodiversidade'], area['vulnerabilidade'], area['conectividade'])

# Define o orçamento disponível
orcamento = 10

# Otimiza a alocação de recursos
areas_selecionadas = otimizar_alocacao_recursos(areas, orcamento)

# Exibe as áreas selecionadas
print("Áreas selecionadas para conservação:")
for area in areas_selecionadas:
    print(f"{area['nome']} - Custo: {area['custo']} - Valor: {area['valor']:.2f}")
