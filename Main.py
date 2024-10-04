import pandas as pd
# Carregar o dataset
df = pd.read_csv('netflix_titles.csv')
# Quais colunas estão presentes
print("As colunas presentes são:")
print(df.columns)
# Diferenciar filmes de TV shows
num_filmes = df[df['type'] == 'Movie'].shape[0]
print(f"O número de filmes disponíveis na Netflix é: {num_filmes}")
# Quais os diretores com mais filmes e séries na plataforma
if 'director' in df.columns:
    # Remover entradas nulas na coluna 'director'
    df_diretor = df[df['director'].notnull()]  
    # Contar a quantidade de filmes/séries por diretor
    top_5_diretor = df_diretor['director'].value_counts().head(5)
    print("Os 5 diretores com mais filmes e séries na Netflix são:")
    print(top_5_diretor)
else:
    print("A coluna 'director' não foi encontrada no dataset.")
# Quais diretores atuaram em suas próprias obras
if 'cast' in df.columns and 'director' in df.columns:
    # Remover entradas onde 'director' é nulo
    df_diretor_ator = df[df['director'].notnull()]
    # Substituir valores NaN na coluna 'cast' por strings vazias
    df_diretor_ator['cast'] = df_diretor_ator['cast'].fillna('')
    # Função para verificar se o diretor está na lista de atores
    def diretor_ator(row):
        # Verificar se o diretor está no elenco
        if isinstance(row['cast'], str):
            return row['director'] in row['cast'].split(', ')
        return False
    # Aplicar a função em cada linha do DataFrame
    df_diretores_atores = df_diretor_ator[df_diretor_ator.apply(diretor_ator, axis=1)]
    # Listar diretores que atuaram como atores
    diretores_atores_lista = df_diretores_atores['director'].unique()
    print("Diretores que atuaram como atores em suas próprias produções:")
    print(diretores_atores_lista)
else:
    print("As colunas 'cast' ou 'director' não foram encontradas no dataset.")
#Número de séries adicionadas por ano[meu Insight :) ]
num_series_por_ano = df[df['type'] == 'TV Show'].groupby('release_year').size()
print("Número de séries adicionadas por ano:")
print(num_series_por_ano)
