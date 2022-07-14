package Main;

import java.util.Scanner;

import Service.DbTask;
import Service.JobFactory;

public class SakilaService {

	private Scanner scanner;
	private JobFactory factory;

	public SakilaService(JobFactory factory) {
		this.factory = factory;
	}

	public void doWork() {
		DbTask work = null;
		String inputString;
		scanner = new Scanner(System.in);

		while (true) {
			System.out.println("Select Menu");
			System.out.println("===================================");
			System.out.println("a. Films by genre");
			System.out.println("b. Titles by actor");
			System.out.println("c. Stores by title");
			System.out.println("q. Quit");
			System.out.print("> ");

			inputString = scanner.nextLine();

			work = factory.createJob(inputString, scanner);
			
			if (work != null) {
				work.getInfo();
				work = null;
			}

			System.out.println();
		}
	}

}
