class JuiceBox{
	enum JuiceBoxSize {SMALL, MEDIUM, LARGE}
	JuiceBoxSize size;
}

public class EnumTrial{
	public static void main (String[] args){
		JuiceBox jb = new JuiceBox();
		jb.size = JuiceBox.JuiceBoxSize.SMALL;
		System.out.println("Size: "+jb.size);
	}
}