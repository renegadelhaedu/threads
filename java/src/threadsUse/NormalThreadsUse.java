package threadsUse;

import taskThreads.Task;

import java.io.File;
import java.time.Duration;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class NormalThreadsUse {

    public static void main(String[] args) throws InterruptedException {

        long inicial = System.currentTimeMillis();
        //aqui sao criadas e designadas threads por tarefa
        try (ExecutorService executor = Executors.newFixedThreadPool(100)) {

            List<Task> tasks = new ArrayList<Task>();
            for (File arquivo : new File("images").listFiles()) {
                if (arquivo.isFile()) {
                    tasks.add(new Task(arquivo.getAbsolutePath()));

                }
            }

            List<Future<Double>> futures = (List<Future<Double>>) executor.invokeAll(tasks);

            long sum = 0;
            for (Future<Double> future : futures) {
                sum += future.get();
            }

            System.out.println("valor final foi: " + sum/futures.size());

        } catch (ExecutionException e) {
            e.printStackTrace();
        }

        System.out.println(Duration.ofMillis(System.currentTimeMillis() - inicial).toSeconds() + " segundos");
    }

}
