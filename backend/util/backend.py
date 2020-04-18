
def change_time_format(data, column_name, only_day=False):
    if isinstance(data, list):
        for i in range(len(data)):
            if data[i][column_name] is None:
                data[i][column_name] = ''
            else:
                if data[i][column_name] == '0000-00-00':
                    data[i][column_name] = ''
                    continue
                if only_day:
                    data[i][column_name] = data[i][column_name].strftime('%Y-%m-%d')
                else:
                    data[i][column_name] = data[i][column_name].strftime('%Y-%m-%d %H:%M:%S')
    else:
        assert isinstance(data, dict)
        if data[column_name] is None:
            data[column_name] = ''
        else:
            if data[column_name] == '0000-00-00':
                data[column_name] = ''
            elif only_day:
                data[column_name] = data[column_name].strftime('%Y-%m-%d')
            else:
                data[column_name] = data[column_name].strftime('%Y-%m-%d %H:%M:%S')
    
    return data
