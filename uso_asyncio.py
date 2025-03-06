import asyncio
#async é usada para definir uma função como assíncrona.
#Uma função assíncrona é diferente de uma função normal porque pode ser pausada e retomada.

#await: Essa palavra-chave é usada dentro de uma função assíncrona para pausar a execução até que
# outra função assíncrona seja concluída.


async def atividade_custosa(task_id): #usa corrotina, uma corrotina por tarefa
    print(f"tarefa {task_id} consultando banco por exemplo... sei la...")

    #coloquei o await aqui para a funçao ficar pausada aqui enquanto a instrução sleep nao terminar
    await asyncio.sleep(1) #nesse exato momento a PVM (asyncio) passa a execução para outra corrotina
    print(f"tarefa {task_id} finalizada!")



async def main():
    num_tarefas = 10

    tasks = [asyncio.create_task(atividade_custosa(i)) for i in range(1, num_tarefas + 1)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
