from Models.legislature import Legislature

def mapper(data_set)-> list:
    data = []

    for value in data_set['dados']:
        legislature = Legislature(
            id= value['id'],
            uri=value['uri'],
            dataInicio=value['dataInicio'],
            dataFim= value['dataFim']
        )
        data.append(legislature)
    
    return data