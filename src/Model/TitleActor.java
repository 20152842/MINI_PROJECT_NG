package Model;

public class TitleActor {
	private String first_name;
	private String last_name;
	private String title;
	private double release_year;
	private double rental_rate;
	
	
	public String getFirst_name() {
		return first_name;
	}
	public void setFirst_name(String first_name) {
		this.first_name = first_name;
	}
	public String getLast_name() {
		return last_name;
	}
	public void setLast_name(String last_name) {
		this.last_name = last_name;
	}
	
	
	public void setRelease_year(double release_year) {
		this.release_year = release_year;
	}
	public void setRental_rate(double rental_rate) {
		this.rental_rate = rental_rate;
	}
	
	
	public String getTitle() {
		return title;
	}
	public void setTitle(String title) {
		this.title = title;
	}
	
	
	public double getRelease_year() {
		return release_year;
	}
	public double getRental_rate() {
		return rental_rate;
	}
	
	
	
	
}
