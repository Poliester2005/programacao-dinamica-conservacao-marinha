# Algoritmos para Otimização e Alocação de Recursos

Este repositório contém dois algoritmos desenvolvidos para otimizar a alocação de recursos em diferentes cenários:

## 1. Distribuição Ótima de Sensores para Monitoramento de Poluição Oceânica

O primeiro algoritmo visa encontrar a distribuição ótima de sensores para monitorar a poluição oceânica em uma determinada região. Ele utiliza o conceito de programação dinâmica para calcular a localização ideal dos sensores, maximizando a cobertura da área de interesse.

### Funcionalidades:
- **calcular_distancia(ponto1, ponto2)**: Calcula a distância euclidiana entre dois pontos.
- **encontrar_distribuicao_otima(pontos, num_sensores)**: Encontra a distribuição ótima de sensores para monitoramento da poluição oceânica.

## 2. Otimização da Alocação de Recursos em Áreas Marinhas Protegidas

O segundo algoritmo foca na otimização da alocação de recursos limitados para maximizar o valor das áreas marinhas protegidas. Ele considera diferentes critérios, como biodiversidade, vulnerabilidade e conectividade, para calcular o valor de cada área e selecionar as melhores opções dentro de um orçamento pré-definido.

### Funcionalidades:
- **calcular_valor_area(biodiversidade, vulnerabilidade, conectividade)**: Calcula o valor de uma área marinha com base nos critérios fornecidos.
- **otimizar_alocacao_recursos(areas, orcamento)**: Otimiza a alocação de recursos limitados para maximizar o valor das áreas marinhas protegidas.

## Utilização:

Os códigos são fornecidos como exemplos de implementação dos algoritmos. Eles podem ser adaptados e integrados a sistemas ou aplicativos de monitoramento ambiental e conservação marinha.

## Exemplo de Uso:

```python
# Exemplo de uso do algoritmo de distribuição ótima de sensores
pontos = [(0, 0), (2, 3), (5, 4), (6, 8), (8, 8), (7, 2)]
num_sensores = 3
distribuicao_otima = encontrar_distribuicao_otima(pontos, num_sensores)

# Exemplo de uso do algoritmo de otimização da alocação de recursos
areas = [
    {'nome': 'Área 1', 'custo': 3, 'biodiversidade': 8, 'vulnerabilidade': 6, 'conectividade': 7},
    {'nome': 'Área 2', 'custo': 5, 'biodiversidade': 7, 'vulnerabilidade': 8, 'conectividade': 6},
    {'nome': 'Área 3', 'custo': 2, 'biodiversidade': 6, 'vulnerabilidade': 7, 'conectividade': 8},
    {'nome': 'Área 4', 'custo': 4, 'biodiversidade': 9, 'vulnerabilidade': 5, 'conectividade': 9},
    {'nome': 'Área 5', 'custo': 7, 'biodiversidade': 8, 'vulnerabilidade': 9, 'conectividade': 8}
]
orcamento = 10
areas_selecionadas = otimizar_alocacao_recursos(areas, orcamento)
