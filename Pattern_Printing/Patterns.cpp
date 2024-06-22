#include <iostream>

using namespace std;

// Function prototype
void solid_rectangle();
void hollow_rectangle();
void half_pyramid_right();
void half_pyramid_right_numbers();
void inverted_half_pyramid();
void inverted_half_pyramid_Numbers();
void half_pyramid_left_after180degree();
void half_pyramid_right_print_row_numbers();
void inverted_half_pyramid_row_numbers();
void Floyds_Triangle();
void Butterfly_Pattern();



int main()
{
	// Calling the function

	//solid_rectangle();
	//hollow_rectangle();
	//half_pyramid_right();
	//inverted_half_pyramid();
	//half_pyramid_left_after180degree();
	//half_pyramid_right_numbers();
	//inverted_half_pyramid_Numbers();
	//half_pyramid_right_print_row_numbers();
	//inverted_half_pyramid_row_numbers();
	//Floyds_Triangle();
	 Butterfly_Pattern();
	

	// Pause the program before exiting
	system("pause");
	return 0;
}

// Function definition
void solid_rectangle()
{
	int row;
	int column;

	cout << "Enter number of rows: ";
	cin >> row;

	cout << "Enter number of columns: ";
	cin >> column;

	for (int i = 1; i <= row; i++)
	{
		for (int j = 1; j <= column; j++)
		{
			cout << "*";
		}
		cout << endl;
	}
}

void hollow_rectangle()
{
	int row;
	int column;

	cout << "Enter number of rows: ";
	cin >> row;

	cout << "Enter number of columns: ";
	cin >> column;

	for (int i = 1; i <= row; i++)
	{
		for (int j = 1; j <= column; j++)
		{
			if (i == 1 || i == row || j == 1 || j == column)
			{
				cout << "*";
			}
			else {
				cout << " ";
			}
			
		}
		cout << endl;
	}
}

void half_pyramid_right()
{
	int row;

	cout << "Enter number of rows: ";
	cin >> row;	

	for (int i = 1; i <= row; i++)
	{
		for (int j = 1; j <= i; j++)
		{
			cout << "*";
		}
		cout << endl;
	}
}

void half_pyramid_right_numbers()
{
	int row;

	cout << "Enter number of rows: ";
	cin >> row;

	for (int i = 1; i <= row; i++)
	{
		for (int j = 1; j <= i; j++)
		{
			cout << j;
		}
		cout << endl;
	}
}

void inverted_half_pyramid()
{
	int row;

	cout << "Enter number of rows: ";
	cin >> row;

	for (int i = row; i >=1 ; i--)
	{
		for (int j = 1; j <= i; j++)
		{
			cout << "*";
		}
		cout << endl;
	}
}

void inverted_half_pyramid_Numbers()
{
	int row;

	cout << "Enter number of rows: ";
	cin >> row;

	for (int i = row; i >= 1; i--)
	{
		for (int j = 1; j <= i; j++)
		{
			cout << j;
		}
		cout << endl;
	}
}

void half_pyramid_left_after180degree()
{
	int row;

	cout << "Enter number of rows: ";
	cin >> row;

	for (int i = 1; i <= row; i++)
	{
		for (int j = 1; j <= row; j++)
		{
			if (j <= row - i)
			{
				cout << " ";
			}
			else{
				cout << "*";
			}

		}
		cout << endl;
	}
}

void half_pyramid_right_print_row_numbers()
{
	int row;

	cout << "Enter number of rows: ";
	cin >> row;

	for (int i = 1; i <= row; i++)
	{
		for (int j = 1; j <= i; j++)
		{
			cout << i << " ";
		}
		cout << endl;
	}
}

void inverted_half_pyramid_row_numbers()
{
	int row;

	cout << "Enter number of rows: ";
	cin >> row;

	for (int i = row; i >= 1; i--)
	{
		for (int j = 1; j <= i; j++)
		{
			cout << i << " ";
		}
		cout << endl;
	}
}

void Floyds_Triangle()
{
	int row;

	cout << "Enter number of rows: ";
	cin >> row;

	int total=0;

	for (int i = 1; i <= row; i++)
	{
		for (int j = 1; j <= i; j++)
		{
			total++;
			cout << total << " ";
		}
		cout << endl;
	}
}

void Butterfly_Pattern()
{
	int row;

	cout << "Enter number : ";
	cin >> row;

	//For upper part
	for (int i = 1; i <= row; i++)
	{
		for (int j = 1; j <= i; j++)
		{			
			cout << "*";
		}

		int space = 2 * row - 2 * i;
		for (int j = 1; j <= space; j++){
			cout << " ";
		}

		for (int j = 1; j <= i; j++)
		{
			cout << "*";
		}
		cout << endl;
	}

	//For lower part
	for (int i = row; i >= 1; i--)
	{
		for (int j = 1; j <= i; j++)
		{
			cout << "*";
		}

		int space = 2 * row - 2 * i;
		for (int j = 1; j <= space; j++){
			cout << " ";
		}

		for (int j = 1; j <= i; j++)
		{
			cout << "*";
		}
		cout << endl;
	}
}