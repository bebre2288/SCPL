#include <iostream>
#include <fstream>
#include <conio.h>

using namespace std;

string program;
int counter=0;
int iter = 0;
int temp = 0;

int operate(int num) {
	char oper = program[iter];
	if(iter>program.length()){
		return num;
	}
	if ( oper=='+'){
		num++;
	} else if ( oper=='-'){
		num--;
	} else if ( oper=='*'){
		iter++;
		num *= operate(num);
	} else if ( oper=='/'){
		iter++;
		num /= operate(num);
	} else if ( oper=='|'){
		iter++;
		num += operate(num);
	} else if ( oper=='('){
		temp = 0;
		while(program[iter]!=')') {
			iter++;
			temp = operate(temp);
		}
		num = temp;
	} else if ( oper==','){
		cout << (char)num;
		num=0;
	} else if ( oper=='.'){
		cin >> num;
	}  else if ( oper==')'){
		//pass
	}  else {
		iter++;
		num=operate(num);
	}

	return num;
}

int main(int argc, char *argv[]) {
	string tempLine;
	string fileName = argv[1];
	ifstream file;
	file.open (fileName);
	while(!file.eof()){
		getline(file, tempLine);
		program += tempLine;
	}
	//cout << program << endl;
	file.close();

	while(iter < program.length()) {
		counter = operate(counter);
		iter++;
	
	}
	cout << endl;
	cout << "final: " << counter << endl;
	_getch();
	return 0;
}
