def search():
    i=int(input('get me the id of employee:\t'))
    for n in range(len(emp)):
        if emp[n]==i: 
            print('employee found')
    else:
            print('no such id exist') 

emp=[101,102,103,104,105,106,107,108,109]
search()