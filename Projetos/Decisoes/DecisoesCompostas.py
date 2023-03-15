nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doenca_infectocontagiosa = input("Suspeita de doença infecto-contagiosa?").upper() #Converte toda a resposta em UPPER CASE.
if idade>=65 and doenca_infectocontagiosa == "SIM":
    print("O paciente será direcionado para a sala AMARELA - Com prioridade.")
elif idade < 65 and doenca_infectocontagiosa == "SIM": #Elif = else + if / "=" representa atribuição e "==" representa comparação.
    print("O paciente será direcionado para sala AMARELA - SEM prioridade")
elif idade >= 65 and doenca_infectocontagiosa == "NAO":
        print("O paciente será direcionado para sala BRANCA - COM prioridade")
elif idade < 65 and doenca_infectocontagiosa == "NAO":
        print("O paciente será direcionado para sala BRANCA - SEM prioridade")
else:
        print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO")