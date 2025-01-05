import csv
import ast 

def defect_counts(test_report):
    partition = {}
    for test in test_report:
        str_part = str(test[0])
        str_res = str(test[-1])

        if str_part not in partition:
            partition[str_part] = [0, 0]      # test fault
        
        if str_res == 'fail':
            partition[str_part][1] += 1
        
        partition[str_part][0] += 1

    print(f"partitions \t # test cases \t # test failures \t fault ratio")
    for key, value in partition.items():
        ratio = '{:.3f}'.format(value[1] / value[0])
        print(f"{key} \t {value[0]} \t {value[1]} \t {ratio} ")
    return

if __name__ == '__main__':
    csv_file = 'Linear Pauli Rotations 4.csv'
    data = []

    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        
        next(reader)
        
        test_report = []
        for row in reader:
            flag = []
            if float(row[0]) == 3:
                flag = [0] + flag
            elif float(row[0]) < 3:
                flag = [1] + flag
            
            list_state = ast.literal_eval(row[1])       # str list '[]' to list []

            test_report.append([flag, row[0], row[1], row[2], row[3], row[4], row[-1]])

    defect_counts(test_report)

    file_name = "LPR4 2.csv"

    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)

        header = ['partition','n','initial_state','slop','offset','basis', 'result']
        writer.writerow(header)

        for data in test_report:
            writer.writerow(data)
    print('done!')
