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
            generate_data(f, row)
        for row in rows:
            generate_map(f, row)


def generate_map(file, row):
    """生成Map字段"""
    file.write(str("//" + row['condition'].strip() + "\n").encode('utf-8'))
    data = row['data']
    file.write("Map<String, String> map = new HashMap<>();\n".encode('utf-8'))
    for (k, v) in data.items():
        k = exchange_key(k.upper())
        map_str = str("map.put(StatisticsAttributesKeyConstant.%s, \"%s\");\n" % (k, v))
        file.write(map_str.encode('utf-8'))
    trace_args = (int(row['id']), row['label'])
    trace_str = "CourseDetailStatistics.getInstance().traceLogAndDa(%d, \"%s\", map);\n\n" % trace_args
    file.write(trace_str.encode('utf-8'))


def exchange_key(origin):
    """转换key值"""
    if origin == "pagename".upper():
        return "PAGE_NAME"
    elif origin == "Scenes".upper():
        return "SCENE"
    elif origin == "itemtype".upper():
        return "ITEM_TYPE"
    elif origin == "itemid".upper():
        return "ITEM_ID"
    elif origin == "itemname".upper():
        return "ITEM_NAME"
    elif origin == "itemurl".upper():
        return "ITEM_URL"
    elif origin == "position".upper():
        return "POSITION"
    elif origin == "pre_tab".upper():
        return "PRE_TAB"
    elif origin == "curr_tab".upper():
        return "CURR_TAB"
    else:
        return origin


def generate_data(file, row):
    """生成Data字段"""
    args = (int(row['id']), row['condition'], row['eventId'], row['actionId'])
    item_str = str("    StatItem item = new StatItem(%d, \"%s\", \"%s\", \"%s\")\n" % args)
    file.write("{\n".encode('utf-8'))
    file.write(item_str.encode('utf-8'))
    file.write("    array.append(item.getId(), item);\n".encode('utf-8'))
    file.write("}\n\n\n".encode('utf-8'))


# generate_code_file('statistics.xlsx', 'Android', 'generate_code.txt')
generate_code_file('statistics.xlsx', 'Android', '课程页.txt', 34, 51)
generate_code_file('statistics.xlsx', 'Android', '学习页.txt', 59, 68)
