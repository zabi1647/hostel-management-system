# hostel-management-system
# Hostel Management System

This is a Python program that implements a simple Hostel Management System. It allows students and managers to perform various tasks related to hostel management such as student registration, fee submission, complaint management, and data analysis.

## Prerequisites

To run the program, make sure you have the following installed:

- Python: The program is written in Python, so you need to have Python installed on your system.
- `pyodbc`: This is a Python library used to connect to Microsoft Access database.

## Getting Started

1. Clone the repository or download the source code files to your local machine.

2. Open the command prompt or terminal and navigate to the project directory.

3. Install the required Python packages by running the following command:
   ```
   pip install pyodbc
   ```

4. Modify the connection string in the code (`con_string`) to point to your Microsoft Access database file (`.mdb` or `.accdb`) that contains the hostel data.

5. Run the program using the following command:
   ```
   python hostel_management_system.py
   ```

## Usage

Upon running the program, you will be presented with a menu where you can choose your role as a student or manager. Based on your selection, you will be prompted for further actions.

### Student

- New Student: If you are a new student, you can register by providing your details, selecting an available room, and paying the monthly rent.
- Hosteler: If you already live in the hostel, you can submit the monthly fee, change your information, or leave the hostel.
- Complain: If you have any complaints, you can submit them, and they will be recorded for further processing.

### Manager

- Servants Data: View the data of the hostel's servants.
- Student Data: View the data of students living in the hostel or students who have left.
- Calculate Fee and Expenditure: Calculate the total fee collected from students or the total expenditure of the hostel.

## Contributing

Contributions to the project are welcome. You can contribute by adding new features, fixing bugs, or improving the existing code. Please follow the standard GitHub workflow (fork, branch, commit, pull request) for making contributions.

## License

The project is licensed under the [MIT License](https://opensource.org/licenses/MIT). Feel free to modify and use the code according to your needs.

## Disclaimer

This program is intended for educational purposes and may not cover all possible scenarios or security measures required for a real-world hostel management system. Use it at your own risk.
