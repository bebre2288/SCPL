#include <iostream>
#include <fstream>

using namespace std;

string program;
int counter=0;
int iter = 0;
int temp = 0;

int operate(int num) {
	char oper = program[iter];
	
	switch(oper){
		case '+':
			num++;
			break;
		case '-':
			num--;
			break;
		case '*':
			iter++;
			num *= operate(num);
			break;
		case '/':
			iter++;
			num /= operate(num);
			break;
		case '(':
			temp = 0;
			while(program[iter]!=')') {
				iter++;
				temp = operate(temp);
			}
			num = temp;
			break;
		case ',':
			cout << (char)num;
			num=0;
			break;
		case '.':
			cin >> num;
			break;
	}
	return num;
}

int main(int argc, char *argv[]) {
	
	string fileName = argv[1];
	ifstream file;
	file.open (fileName, ios::in);
	getline(file, program);
	file.close();
	cout << program << endl;
	while(iter < program.length()) {
		counter = operate(counter);
		iter++;
	}
	cout << "\nfinal: " << counter;
	cin.get();
	return 0;
}
