package Main;

import Service.JobFactory;

public class SakilaMain {

	public static void main(String[] args) {
	
		SakilaService service = new SakilaService(new JobFactory());
		service.doWork();
	
	}

}
