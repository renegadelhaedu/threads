import threading

valor = 0

def quem_sou_eu(nome): #usa threads, uma thread por tarefa
    #tarefa custosa
    global valor

    if nome == 'pedro':
        print(f'{nome} voce é o maior namorador de Sousa')
    else:
        print(f'{nome} voce tem que aprender com pedro')
    valor += 1


nomes = ['rene','joao victor', 'gustavo','luiz','pedro','nicollas']

for nome in nomes:
    my_thr = threading.Thread(target=quem_sou_eu, args=(nome,))
    my_thr.start()

print(f'o valor final foi {valor}')

