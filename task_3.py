from pprint import pprint

def process_files(file_list):
    result = []
    for file_name in file_list:
        with open(file_name, 'r',) as file:
            lines = [line.strip().split('\n') for line in file]
            count = len(lines)
            result.append({'line_count': count, 'file_name': file_name, 'lines': lines})
    return result


file_list = ['1.txt', '2.txt', '3.txt']
result_data = process_files(file_list)
sorted_result = sorted(result_data, key=lambda x: x['line_count'])
pprint(sorted_result)

def get_result(sorted_result):
    with open('result.txt', 'w+') as result:
        for value in sorted_result:
            result.write(f'{value['file_name']}\n{value['line_count']}\n')
            for index, string in enumerate(value['lines']):
                result.write(f'Строка номер {index + 1} файла номер {value["file_name"][0]} '
                             f'{''.join(string)}\n')

get_result(sorted_result)