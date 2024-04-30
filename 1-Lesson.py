import pandas as pd

#dados para o primeiros exemplo
dados = {
'Nome': ['Claudia', 'José', 'Clara', 'Roberto', 'Harold', 'Marcia'],
'Idade': [25, 30, 22, 35, 27, 29],
'Cidade': ['São José Dos Campos', 'Rio Negrinho', 'Uberaba', 'Taubaté', 'Porto', 'Joinville'],
'Ocupação Profissional': ['Estudante', 'Programador', 'Atendente', 'Vendedor', 'Farmaceutico', 'Desempregado'],
'Salário': [850.50, 8652.78, 1500.45, 5000.10, 150]
}

#dataframe seria um quadro com as informaçoes organizadas

df= pd.DataFrame(dados)

#printar na tela o dataframe construidos com os dados fornecidos 

print(df)

################################################################################################

#a partir daqui iremos organizar o dataframe de acordo com metricas aleatorias disponiveis no pandas
#dataframe original 

print(df)
# ou uma impressão na tela mais bonita seria com o 
display(df)

#filtro 
#filtrar pessoas a partir do salario de 5000.00
df_filtrado_salario = df[df['Salário']> 5000.00]
print(df_filtrado_salario)

#ordenação de dataframe por idade decrescente e vice-versa

df_ordenado_idade = df.sort_values(by='Idade', ascending=False)

print(df_ordenado_idade)

# calcular media de idades dos usuarios

media_idade = df['Idade'].mean()
print(media_idade)

# calcular o salario das pessoas com idade de 30 pra cima 

media_salario_idade_30 = df[df['Idade']>30]['Salário'].mean()

# exibir todo o dataframe filtrado por salario, ordenado por idade e as medias de idade de slario 

print("\nDataframe filtrado por salario:")
print(df_filtrado_salario)
print("\nDataframe ordenado por idade:")
print("df_ordenado_idade")
print(f"\nMedia de idade: {media_idade}")
print(f"\nMedia de salario das pessoas com idade de 30 pra cima: {media_salario_idade_30}")

##############################################################
 #python para vida pessoal - notas rápidas

def add_note():
    note = input("Digite algo: ")

    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Annotation added with success")
def show_notes():
    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()
            if not notes:
                print("No notes found")
            else:
                print("Notes:")
                for note in notes:
                    print(note.strip())

    except FileNotFoundError:
        print("Notes file not found")


def menu():

    option = 0
    while option != 3:
        print("\n---MENU---")
        print("1. Add a note")
        print("2. Show notes")
        print("3. Out")
        try:
            option = int(input('Chose a option: '))
            if option == 1:
                add_note()
            elif option == 2:
                show_notes()
            elif option == 3:
                print("Bye bye!")
            else:
                print('Invalid option')
        except ValueError:
            print("not a option, error occured")
            
menu()

                
