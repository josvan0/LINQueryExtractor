import re


def extract_linq_query(linq):
    # extract original SQL query
    match = re.search("sp_executesql N'(.+)',N", linq)
    query = match.group(1) if match else ''
    if query == '':
        return ''

    # extract parameters
    match = re.search("',\s?(@p__linq__\d+=.+)", linq)
    p_linq_list = match.group(1) if match else ''

    # replace param values
    params = p_linq_list.split(',')
    for param in params[::-1]:
        tmp = param.split('=')
        if len(tmp) == 2:
            query = query.replace(tmp[0], tmp[1])

    # replace double qouted values
    double_quotes = re.findall("''\S+''", query)
    for dq in double_quotes:
        query = query.replace(dq, dq[1:-1])

    return query


def get_linq_query(filename):
    with open(filename, 'r') as f:
        sql = ''.join(f.readlines()).replace('\n', ' ')
    if not sql or sql == '':
        return

    query = extract_linq_query(sql)
    if query == '':
        print('LINQ query not found!')
        return

    output = filename.replace('.sql', '_original.sql')
    with open(output, 'w') as f:
        f.write(query)
    print('LINQ extracted successfully!')


if __name__ == '__main__':
    print('*' * 30, 'LINQ parser', '*' * 30)
    user_input = input('Enter LINQ file path: ')
    get_linq_query(user_input)
