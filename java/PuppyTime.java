class Puppy{
	String name;
	int age;
	public Puppy(String name){
		this.name = name;
		this.age = 10;
	}

	public void growPuppy(int age){
		this.age += age;
	}

	public void dispName(){
		System.out.println("The puppy's name is: "+this.name);
	}

	public void dispAge(){
		System.out.println("The puppy's age is: "+this.age);
	}
}

public class PuppyTime{
	public static void main(String[] args) {
		Puppy p = new Puppy("Dash");
		p.dispName();
		System.out.println("[Before Growing]");
		p.dispAge();
		p.growPuppy(20);
		System.out.println("[After Growing]");
		p.dispAge();
	}
}