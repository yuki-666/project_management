
def change_time_format(data, column_name):
    if isinstance(data, list):
        for i in range(len(data)):
            if data[i][column_name] is None:
                data[i][column_name] = ''
            else:
                data[i][column_name] = data[i][column_name].strftime('%Y-%m-%d %H:%M:%S')
    else:
        assert isinstance(data, dict)
        if data[column_name] is None:
            data[column_name] = ''
        else:
            data[column_name] = data[column_name].strftime('%Y-%m-%d %H:%M:%S')
    
    return data
