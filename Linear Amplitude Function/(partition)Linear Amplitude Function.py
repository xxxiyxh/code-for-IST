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

def contains_only_elements(input_list, elements_to_check):
    # 使用集合操作判断列表是否只包含指定的元素
    unique_elements = set(input_list)
    return unique_elements.issubset(elements_to_check)

if __name__ == '__main__':
    csv_file = 'Linear Amplitude Function 4.csv'
    data = []

    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        
        # 跳过 CSV 文件的首行
        next(reader)
        
        # 遍历 CSV 文件中的每一行（从第二行开始）
        test_report = []
        for row in reader:
            
            # 将每个元素转换为双精度浮点数并添加到数据列表
            flag = []
            if float(row[0]) ==  3:
                flag = [0] + flag
            elif float(row[0]) < 3:
                flag = [1] + flag
            
            list_state = ast.literal_eval(row[1])       # str list '[]' to list []
            if_com = contains_only_elements(list_state, {0})
            if if_com:
                flag = [0] + flag
            elif not if_com:
                flag = [1] + flag
            
            # if float(row[2]) >= 0:
            #     flag = [0] + flag
            # elif float(row[2]) < 0:
            #     flag = [1] + flag

            # if float(row[3]) >= 0:
            #     flag = [0] + flag
            # elif float(row[3]) < 0:
            #     flag = [1] + flag

            test_report.append([flag, row[0], row[1], row[2], row[3], row[-1]])

    defect_counts(test_report)

    file_name = "LAF4.csv"

    # 打开文件以进行写入，newline='' 用于确保在 Windows 上正确处理换行符
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)

        # 写入表头（如果有的话）
        header = ['partition', 'n', 'initial_state', 'slope', 'offset', 'result']
        writer.writerow(header)

        for data in test_report:
            # 写入数据
            writer.writerow(data)
    print('done!')
        
