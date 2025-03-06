import threading

with open('NEWS.txt', 'r') as arquivo:
    conteudo = arquivo.read().upper()

def tarefa(nome):
    print(f"{nome} iniciando...")
    soma = conteudo.count(nome)
    print(f"{nome} possui {soma} ocorrencias")

threads = []
for nome in ['WINDOWS', 'LINUX','PYTHON','THREADS']:
    t = threading.Thread(target=tarefa, args=(nome,))
    threads.append(t)
    t.start()

for t in threads:
    t.join() #para cada thread iniciada, pause o prosseguimento (thread main) enquanto todas as threads nao terminarem


print('ACABOUUUUUUUUU')
