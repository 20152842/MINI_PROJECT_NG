package Service;

import java.util.Scanner;

import DAO.SakilaDAO;

public class StoresByTitle implements DbTask{

	
	private Scanner sc;

	public StoresByTitle(Scanner sc) {
		super();
		this.sc = sc;
	}

	@Override
	public void getInfo(){
		// TODO Auto-generated method stub
		SakilaDAO sa = SakilaDAO.getInstance();
		sa.getStoresByTitle(sc);
	}
}

