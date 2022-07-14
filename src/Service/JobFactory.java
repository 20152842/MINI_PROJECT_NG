package Service;

import java.util.Scanner;

public class JobFactory {

	public DbTask createJob(String job, Scanner scanner) {
		DbTask work = null;
		
		if(job.equals("a")) {
			work = new FilmsByGenre(scanner);
		}else if(job.equals("b")) {
			work = new TitlesByActor(scanner);
		}else if(job.equals("c")) {
			work = new StoresByTitle(scanner);
		}else if(job.equals("q")) {
			System.out.println();
			System.out.println("Program Terminated!!");
			scanner.close();
			System.exit(0);
		}else {
			System.out.println("Wrong selection!!");
		}
		return work;
	}
}
