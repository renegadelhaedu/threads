import asyncio
#na programação assíncrona,toda a ação acontece em uma única thread do sistema
#  um único núcleo da CPU (nada de multi threads)

with open('NEWS.txt', 'r') as arquivo:
    conteudo = arquivo.read().upper()  # Converte tudo para maiúsculas uma vez


async def tarefa(nome):
    print(f"{nome} iniciando...")
    soma = conteudo.count(nome)
    print(f"{nome} possui {soma} ocorrências.")


async def main():
    #tarefas = [tarefa(nome) for nome in ['WINDOWS', 'LINUX', 'PYTHON', 'THREADS']]
    #a instrucao acima é o mesmo que
    tarefas = []
    for nome in ['WINDOWS', 'LINUX', 'PYTHON', 'THREADS']:
        tarefas.append(tarefa(nome))

    await asyncio.gather(*tarefas)


asyncio.run(main())


#for t in threads:
#    t.join()  # Espera todas terminarem

print('terminei doidao')