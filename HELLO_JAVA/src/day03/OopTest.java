package day03;

public class OopTest {
	public static void main(String[] args) {
		Human hum = new Human();
		System.out.println("age : " + hum.age);
		System.out.println("flagLang:" +hum.flagLang);
		hum.oneYear();
		System.out.println("age : " +hum.age);
		hum.momstouch();
		System.out.println("flagLang:" +hum.flagLang);
	
	}
}
