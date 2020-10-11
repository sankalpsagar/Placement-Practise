class A{
	int i = 5;
	static int y = 7;
	public void someMethod(){
		System.out.println("This is class A.");
	}
	static void staticMethod(){
		System.out.println("Class A's static method");
	}
}

class B extends A{
	int i = 10;
	static int y = 10;
	public void someMethod(){
		System.out.println("This is class B.");
		super.someMethod();
	}

	public void someMethod2(){
		System.out.println("This is method2 from class B.");
	}

	static void staticMethod(){
		System.out.println("Class B's static method");
	}
}

public class InheritanceIsHard{

	public static void main(String[] args) {
		A a = new B();
		B b = new B();
		a.someMethod();
		b.someMethod();
		b.someMethod2();
		((B)a).someMethod2();
		a.staticMethod();
		b.staticMethod();
		System.out.println("i in A: " + a.i);
		System.out.println("i in B: " + b.i);
		System.out.println("Static y in A: " + a.y);
		System.out.println("Static y in B: " + b.y);
		System.out.println("Typecast i in A: " + ((B)a).i);
		System.out.println("Typecast y in A: " + ((B)a).y);
		System.out.println("End of program.");
		// calling somemethod2 from A variable gives compile time error
	}

}