#include <iostream>
#include <fstream>

using namespace std;

string program;
int counter=0;
int iter = 0;

int operate(int num) {
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
		cout << (char)num;
		num=0;
	} else if (oper=='.') {
		cin >> num;
	}

	return num;
}

int main(int argc, char *argv[]) {
	
	string fileName = argv[1];
	ifstream file;
	file.open (fileName);
	getline(file, program);
	
	cout << program << endl;
	while(iter < program.length()) {
		counter = operate(counter);
		iter++;
	}
	cout << "\nfinal: " << counter;
	cin.get();
	return 0;
}