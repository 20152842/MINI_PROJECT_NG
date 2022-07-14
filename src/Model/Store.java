package Model;

public class Store {

	private String title;
	private String store_id;
	private String first_name;
	private String last_name;
	private String address;
	private String district;
	private String city;
	private double stock;
	private String country;
	private String Ad;
	
	public String getAd() {
		return Ad;
	}
	public void setAd(String ad) {
		Ad = ad;
	}
	public double getStock() {
		return stock;
	}
	public void setStock(double stock) {
		this.stock = stock;
	}

	
	public String getTitle() {
		return title;
	}
	public void setTitle(String title) {
		this.title = title;
	}
	public String getStore_id() {
		return store_id;
	}
	public void setStore_id(String store_id) {
		this.store_id = store_id;
	}
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
	public String getAddress() {
		return address;
	}
	public void setAddress(String address) {
		this.address = address;
	}
	public String getDistrict() {
		return district;
	}
	public void setDistrict(String district) {
		this.district = district;
	}
	public String getCity() {
		return city;
	}
	public void setCity(String city) {
		this.city = city;
	}
	public String getCountry() {
		return country;
	}
	public void setCountry(String country) {
		this.country = country;
	}
	
	
	
}
