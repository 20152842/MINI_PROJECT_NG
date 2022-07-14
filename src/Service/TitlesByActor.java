package Service;


import java.util.Scanner;

import DAO.SakilaDAO;


public class TitlesByActor implements DbTask{

	private Scanner sc;
	
	public TitlesByActor(Scanner sc) {
		// TODO Auto-generated constructor stub
		this.sc = sc;
	}
	
	@Override
	public void getInfo() {
		// TODO Auto-generated method stub
		SakilaDAO sa = SakilaDAO.getInstance();
		sa.getTitleByActor(sc);
	
	}
	

}
