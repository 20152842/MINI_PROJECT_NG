package Service;

import java.util.Scanner;
import DAO.SakilaDAO;


public class FilmsByGenre implements DbTask{

	private Scanner sc;
	
	
	public FilmsByGenre(Scanner sc) {
//		super();
		this.sc = sc;
	}


	@Override
	public void getInfo() {
		// TODO Auto-generated method stub
		SakilaDAO sa = SakilaDAO.getInstance();

		sa.getFilms(sc);
		
		
	}

	
}
