import pandas
import requests
import json
from collections import defaultdict

def Post(caminho_arquivo):
    access_token = "CJs1PSyZYDQxjxK9B8mkFzn5pTf4a2eTs9umAB2WGC5oAHtq0ZJl3A0ld2jwVKV8R9j8TdMfWaabzCAkTjcCSiKvf9SyUCbtiajwSKoQj1xPAtH3sXs4qsOBNRbzl0Yh"

    my_headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-type': 'application/json',
        'Accept': 'application/json'
    }

    # criando data frame
    df_unificado = pandas.read_excel(caminho_arquivo)

    # atributo para mostrar o numero da linha
    row = 0
    qtd_linhas = len(df_unificado)
    print('criando json...')
    for data in df_unificado.iterrows():
        # valores
        emailInstitucional = str(data[1]['E-mail Institucional'])
        turmaAluno = str(data[1]['Turma Aluno'])
        cursoDisciplina = str(data[1]['Curso Disciplina'])
        turmaDisciplina = str(data[1]['Turma Disciplina'])
        divisao = str(data[1]['Divisão'])
        disciplina = str(data[1]['Disciplina'])
        diaSemana = str(data[1]['Dia da Semana'])
        horarioInicio = str(data[1]['Horário de inicio'])
        horarioTermino = str(data[1]['Horário de Término'])
        sala = str(data[1]['Sala'])
        professor = str(data[1]['Professor'])

        # criando dict
        dict_valores = {
            'emailInstitucional': emailInstitucional,'turmaAluno': turmaAluno,
            'cursoDisciplina': cursoDisciplina,
            'turmaDisciplina': turmaDisciplina,
            'divisao': divisao,
            'disciplina': disciplina,
            'diaSemana': diaSemana,
            'horarioInicio': horarioInicio,
            'horarioTermino': horarioTermino,
            'sala': sala,
            'professor': professor,
        }

        if row == 0:
            valores_json = f'[{json.dumps(dict_valores)},'
        elif row == qtd_linhas - 1:
            valores_json += f'{json.dumps(dict_valores)}]'
        else:
            valores_json += f'{json.dumps(dict_valores)},'

        row += 1

    #armazenando o valor da barra invertida
    #barra = r"'\'"

    #retirando a barra invertida
    #valores_json = valores_json.replace(barra, '')

    #salvando o arquivo
   # with open('data.json', 'w', encoding='utf-8') as f:
    #    json.dump(valores_json, f, ensure_ascii=False, indent=4)

    # links
    escolha = int(input('Insira 1 para homologação, ou 2 para produção: '))
    if escolha == 1:
        link = "https://magister-hom.pucpr.br/radix/v1/ensalamentoalunotemp/inserir"
    elif escolha == 2:
        link = "https://magister.pucpr.br/radix/v1/ensalamentoalunotemp/inserir"
    else:
        exit()

    print('enviando...')

    # enviando
    response = requests.post(link, headers=my_headers, data=valores_json)

    # retornando status
    print(response.headers)
    print(response.text)
    print(f'retornou codigo: 'f'{response.status_code} ({response.reason})')


if __name__ == '__main__':
    Post()
