def opendoor(N,n) :
    door_list = []
    for number in range(N) :
        door_list.append('closed')
    for number in range(1,n+1) : 
        for secnumber in range(number,N+1,number):
            if door_list[secnumber-1] == 'closed' :
                door_list[secnumber-1] = 'open'
                secnumber += number
            else :
                door_list[secnumber-1] = 'closed'
                secnumber += number
    return door_list.count('open')   


