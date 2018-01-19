from parser import parse_file


# def generate_code_file(input_file, table_name, output_file):
#     """生成代码文件"""
#     with open(output_file, 'wb') as f:
#         rows = parse_file(input_file, table_name)
#         for row in rows:
#             generate_map(f, row)


def generate_code_file(input_file, table_name, output_file, start=0, end=0):
    """生成代码文件"""
    with open(output_file, 'wb') as f:
        rows = parse_file(input_file, table_name, start, end)
        for row in rows:
            generate_map(f, row)


def generate_map(file, row):
    """生成Map字段"""
    file.write(str("//" + row['condition'].strip() + "\n").encode('utf-8'))
    data = row['data']
    file.write("Map<String, String> map = new HashMap<>();\n".encode('utf-8'))
    for (k, v) in data.items():
        map_str = str("map.put(\"%s\", \"%s\")\n" % (k, v))
        file.write(map_str.encode('utf-8'))
    trace_args = (row['id'], row['label'])
    trace_str = ".getInstance().traceLogAndDa(\"%s\", \"%s\", map)\n\n" % trace_args
    file.write(trace_str.encode('utf-8'))


# generate_code_file('statistics.xlsx', 'Android', 'generate_code.txt')
generate_code_file('statistics.xlsx', 'Android', '课程页.txt', 34, 51)
generate_code_file('statistics.xlsx', 'Android', '学习页.txt', 59, 68)
