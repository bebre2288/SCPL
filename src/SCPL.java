import java.util.Iterator;
import java.util.Scanner;

public class SCPL {
	
	char[] program = null;
	int counter=0;
	int iter = 0;
	Scanner input = new Scanner(System.in);
	Main(){
//		Scanner program_input = new Scanner(System.in);
//		program = program_input.next().toCharArray();
//		program_input.close();
		program = "(+++++)*(+++++*-)++++,".toCharArray();
		while(iter < program.length) {
			counter = operate(counter);
			iter++;
		}
		System.out.println("\nfinal: "+counter);
	}
	
	public int operate(int num) {
		char oper = program[iter];
		
		if(oper=='+') {
			num++;
		} else if (oper=='-') {
			num--;
		} else if (oper=='*') {
			iter++;
			num *= operate(num);
		} else if (oper=='/') {
			iter++;
			num /= operate(num);
		} else if (oper=='(') {
			int temp = 0;
			while(program[iter]!=')') {
				iter++;
				temp = operate(temp);
			}
			num = temp;
		} 
		
		
		else if (oper=='<') {
			iter++;
			int temp=0;
			int condition = 0;
			while(program[iter]!=';') {
				iter++;
				condition = operate(condition);
			}
			char tmp_oper = program[iter];
			iter++;
			while(program[iter]!='>') {
				iter++;
				temp = operate(temp);
			}
			while(condition!=0) {
				iter++;
				condition = operate(condition);
			}
			
		}
		
		
		else if (oper==',') {
			System.out.print((char)num);
			num=0;
		} else if (oper=='.') {
			num=input.nextInt();
		}
		
		return num;
	}
	
	public static void main(String[] args) {
			new SCPL();
		}
}
