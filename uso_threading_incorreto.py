import threading

#Cada thread abre o arquivo NEWS.txt de forma independente, mas sem sincronização
#Múltiplas threads acessando o mesmo arquivo ao mesmo tempo pode dar problema.
#Se o arquivo for muito grande, pode haver inconsistências.

def tarefa(nome):
    print(f"{nome} iniciando...")
    arquivo = open('NEWS.txt', 'r') #agradecer a PVM em tempo de execução gerenciou o acesso ao file
    soma = 0 #soma é uma variável local (não compartilha espaço de mem ram entre as threads)
    for linha in arquivo:
        soma += linha.upper().count(nome)
    print(f"{nome} possui {soma} ocorrencias")



threads = []
for nome in ['WINDOWS', 'LINUX','PYTHON','THREADS']:
    t = threading.Thread(target=tarefa, args=(nome,))
    threads.append(t)
    t.start()

#for t in threads:
#    t.join()  # Espera todas terminarem
