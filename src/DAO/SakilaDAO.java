package DAO;

import java.sql.CallableStatement;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

import Model.Film;
import Model.Store;
import Model.TitleActor;


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
public class SakilaDAO {

	
	
	private Connection con;
	private ResultSet rSet;
	private PreparedStatement pStmt;
	private CallableStatement cStmt;

	private final String url = "jdbc:mysql://localhost:3306/sakila?serverTimezone=UTC";
	private final String username = "lastcoder";
	private final String password = "1234";
	
	private static SakilaDAO Sakila = new SakilaDAO();
	//클래스 로더 시 SakilaDAO 객체 생성 후 static sakila에 주소 리턴
	
	private SakilaDAO() {
		
	}//외부에서 객체 생성 불가 (생성자를 private 선언)
	
	public static SakilaDAO getInstance() {
		return Sakila;
	}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	private void getConnection() {
		try {
			con = DriverManager.getConnection(url, username, password);
		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
	}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	private void closeConnection() {
		try {
			if (rSet != null) {
				rSet.close();
			}
			if (pStmt != null) {
				pStmt.close();
			}
			if (cStmt != null) {
				cStmt.close();
			}
			if (con != null) {
				con.close();
			}

		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}

	}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public List<Film> getFilms(Scanner sc) {
		List<Film> films = new ArrayList<>();
		System.out.println("장르를 입력하세요 : ");
		String genre = sc.nextLine();
		getConnection();

		StringBuffer sb = new StringBuffer();
		sb.append("select FL.film_id, FL.title, CG.name as genre");
		sb.append(", FL.release_year, LG.name as language ");
		sb.append("from film as FL join film_category as FC on FL.film_id = FC.film_id ");
		sb.append("join category as CG on FC.category_id = CG.category_id ");
		sb.append("join language as LG on FL.language_id = LG.language_id ");
		sb.append("where CG.name = ?");

		String sql = sb.toString();
		try {
			pStmt = con.prepareStatement(sql);
			pStmt.setString(1, genre);
			rSet = pStmt.executeQuery();

			Film film;

			while (rSet.next()) {
				film = new Film();
				film.setFilmId(rSet.getLong(1));
				film.setTitle(rSet.getString(2));
				film.setGenre(rSet.getString(3));
				film.setReleaseYear(rSet.getLong(4));
				film.setLanguage(rSet.getString(5));
				films.add(film);
			}
		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		} finally {
			closeConnection();

		}
		System.out
				.println("   Film ID               Title               	    Genre  	    Release Year        Language");
		System.out.println(
				"=================================================================================================");

		if (films.size() == 0) {
			System.out.println("NO DATA");

		} else {
			for (Film film : films) {
				System.out.printf("%5s    %30s     %15s       %5s        %15s\n", film.getFilmId(), film.getTitle(),
						film.getGenre(), film.getReleaseYear(), film.getLanguage());
			}

		}
		return films;

	}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public List<TitleActor> getTitleByActor(Scanner sc) {
		List<TitleActor> Actors = new ArrayList<>();
		System.out.println("배우의 First Name을 입력하세요 : ");
		String actor_F = sc.nextLine();
		System.out.println("배우의 Last Name을 입력하세요 : ");
		String actor_L = sc.nextLine();
 		getConnection();

		StringBuffer sb = new StringBuffer();
		sb.append("select AC.first_name, AC.last_name, FL.title, FL.release_year, FL.rental_rate ");
		sb.append("from actor AC join film_actor FA on AC.actor_id = FA.actor_id ");
		sb.append("join film FL on FA.film_id = FL.film_id ");
		sb.append("where AC.first_name = ? and AC.last_name = ? ");
		sb.append("order by FL.title");

		String sql = sb.toString();
		try {
			pStmt = con.prepareStatement(sql);
			pStmt.setString(1, actor_F);
			pStmt.setString(2, actor_L);
			rSet = pStmt.executeQuery();

			TitleActor TA;

			while (rSet.next()) {
				TA = new TitleActor();
				TA.setFirst_name(rSet.getString(1));
				TA.setLast_name(rSet.getString(2));
				TA.setTitle(rSet.getString(3));
				TA.setRelease_year(rSet.getDouble(4));
				TA.setRental_rate(rSet.getDouble(5));
				Actors.add(TA);
			}
		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		} finally {
			closeConnection();

		}

		System.out.println("First Name        Last Name        Title               Release Year         Rental rate");
		System.out.println("=======================================================================================");
		if (Actors.size() == 0) {
			System.out.println("NO DATA");

		} else {
			for (TitleActor actor : Actors) {
				System.out.printf("%10s    %10s     %20s       %5f                %.2f\n", actor.getFirst_name(), actor.getLast_name(), actor.getTitle(),
						actor.getRelease_year(), actor.getRental_rate());
			}

		}
		return Actors;

	}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public List<Store> getStoresByTitle(Scanner sc) {
		
		List<Store> Stores = new ArrayList<>();
		System.out.println("매장 정보를 출력합니다.");
		getConnection();

		StringBuffer sb = new StringBuffer();
		sb.append("call SP_GET_STORE(?)");
		
		String sql = sb.toString();
		try {
			pStmt = con.prepareStatement(sql);
			pStmt.setString(1, "AGENT TRUMAN");
			rSet = pStmt.executeQuery();

			Store st;
			
			while (rSet.next()) {
				st = new Store();
				st.setTitle(rSet.getString(1));
				st.setStore_id(rSet.getString(2));
				st.setFirst_name(rSet.getString(3));
				st.setLast_name(rSet.getString(4));
				st.setAd(rSet.getString(5));
				st.setStock(rSet.getDouble(6));
				Stores.add(st);
			}
		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		} finally {
			closeConnection();

		}
		
		
		System.out.println(
				"	Title            Store ID      First Name       Last Name                                Address                            Stock");
		System.out.println(
				"===========================================================================================================================================");

		if (Stores.size() == 0) {
			System.out.println("NO DATA");

		} else {
			for (Store store : Stores) {
				System.out.printf("%20s    %5s     %10s       %10s         %50s           %2f\n",
						store.getTitle(), store.getStore_id(), store.getFirst_name(), store.getLast_name(),
						store.getAd(), store.getStock());
			}

		}
		return Stores;
	}
		
	

}
