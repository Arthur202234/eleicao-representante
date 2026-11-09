# 1. Situação-problema
# Uma escola realizará uma eleição para escolher o representante de uma turma. Três alunos estão concorrendo, e a votação será realizada por meio de um programa em Python.

# Você deverá desenvolver um sistema que registre os votos, contabilize os resultados e identifique o candidato vencedor.

# 2. Menu do sistema
# O programa deverá apresentar o seguinte menu:

# ===== ELEIÇÃO DO REPRESENTANTE ===== 1 - Votar em Ana 2 - Votar em Bruno 3 - Votar em Carlos 4 - Votar em branco 5 - Consultar resultado parcial 6 - Encerrar votação Escolha uma opção:
# 3. Requisitos obrigatórios
# Utilizar while para manter o menu funcionando até o encerramento.

# Utilizar if, elif e else para verificar as opções selecionadas.

# Criar variáveis para armazenar os votos de cada candidato.

# Contabilizar os votos em branco separadamente.

# Exibir uma mensagem após cada voto registrado.

# Mostrar a quantidade de votos de cada candidato na opção 5.

# Calcular o total de votos registrados.

# Apresentar o resultado final ao encerrar a votação.

# Identificar qual candidato recebeu mais votos.

# Informar quando houver empate entre os candidatos mais votados.

# Exibir uma mensagem de erro caso seja selecionada uma opção inválida.

# Não encerrar o programa antes da escolha da opção 6.

# Observação: Utilize somente os conhecimentos de Python trabalhados até o momento. Não é necessário utilizar listas, funções ou banco de dados.

# 4. Exemplo de execução
# ===== ELEIÇÃO DO REPRESENTANTE ===== Escolha uma opção: 1 Voto em Ana registrado! Escolha uma opção: 2 Voto em Bruno registrado! Escolha uma opção: 1 Voto em Ana registrado! Escolha uma opção: 3 Voto em Carlos registrado! Escolha uma opção: 4 Voto em branco registrado! Escolha uma opção: 6 ===== RESULTADO FINAL ===== Ana: 2 votos Bruno: 1 voto Carlos: 1 voto Brancos: 1 voto Total de votos: 5 Candidato vencedor: Ana Votação encerrada!
# 5. Testes obrigatórios
# Antes de publicar o programa, realize os seguintes testes:

# Registre votos nos três candidatos.

# Registre pelo menos um voto em branco.

# Consulte o resultado parcial.

# Verifique se a soma dos votos está correta.

# Teste uma opção inexistente no menu.

# Teste uma eleição com empate.

# Encerre o programa e confira o relatório final.


votos_ana = 0
votos_bruno = 0
votos_carlos = 0
votos_branco = 0

opcao = 0
###########################################################

while opcao != 6:
    print("\n===== ELEIÇÃO DO REPRESENTANTE =====")
    print("1--- Votar em Ana")
    print("2--- Votar em Bruno")
    print("3--- Votar em Carlos")
    print("4--- Votar em branco")
    print("5--- Consultar resultado parcial")
    print("6--- Encerrar votação")
    ##################################
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        votos_ana += 1
        print("Voto registrado -- Ana")
    elif opcao == 2:
        votos_bruno += 1
        print("Voto registrado -- Bruno")
    elif opcao == 3:
        votos_carlos += 1
        print("Voto registrado -- Carlos ")
    elif opcao == 4:
        votos_branco += 1
        print("Voto registrado -- voto branco")
    elif opcao == 5:
        parcial = votos_ana + votos_bruno + votos_carlos + votos_branco
        print("\n--- RESULTADO PARCIAL ---")
        print(f"Ana: {votos_ana} votos")
        print(f"Bruno: {votos_bruno} votos")
        print(f"Carlos: {votos_carlos} votos")
        print(f"Brancos: {votos_branco} votos")
        print(f"Total de votos registrados: {parcial}")
    elif opcao == 6:
        print("\nEncerrando votação... ")
    else:
        print("Essa opção não é válida. Escolha um número de 1 a 6 ")

############################################################################################################
total_votos = votos_ana + votos_bruno + votos_carlos + votos_branco

print("\n===== RESULTADO FINAL =====")
print(f"Ana: {votos_ana} votos")
print(f"Bruno: {votos_bruno} votos")
print(f"Carlos: {votos_carlos} votos")
print(f"Brancos: {votos_branco} votos")
print(f"Total de votos: {total_votos}")

if total_votos == 0:
    print("Nenhum voto foi registrado.")
else:
    if votos_ana > votos_bruno and votos_ana > votos_carlos:
        print("Candidato vencedor: Ana")
    elif votos_bruno > votos_ana and votos_bruno > votos_carlos:
        print("Candidato vencedor: Bruno")
    elif votos_carlos > votos_ana and votos_carlos > votos_bruno:
        print("Candidato vencedor: Carlos")
    elif votos_ana == votos_bruno and votos_ana > votos_carlos:
        print("Empate entre Ana e Bruno")
    elif votos_ana == votos_carlos and votos_ana > votos_bruno:
        print("Empate entre Ana e Carlos")
    elif votos_bruno == votos_carlos and votos_bruno > votos_ana:
        print("Empate entre Bruno e Carlos")
    elif votos_ana == votos_bruno and votos_bruno == votos_carlos:
        print("Empate triplo entre Ana, Bruno e Carlos")
###########################
print("Fim da votação!!!")
