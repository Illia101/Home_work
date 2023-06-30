

def clean_folder(path):

    def write_employees_to_file(employee_list, path):
        file = open(path, 'w')
        for department in employee_list:
            for employee in department:
                file.write(employee + '\n')
        file.close()

    def read_employees_from_file(path):
        file = open(path, 'r')
        data = file.readlines()
        file.close()
        employees = [line.rstrip('\n') for line in data]
        return employees

def main():
    folder_path = input("Enter the path of the folder to clean: ")
    clean_folder(folder_path)

if __name__ == "__main__":
    main()


