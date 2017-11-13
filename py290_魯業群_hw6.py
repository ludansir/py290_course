file_old = open('stores_old.csv', 'r', encoding='big5')
file_new = open('stores_new.csv', 'w', encoding='big5')

for line in file_old.readlines():
    #print(line, end='')
    split_line_in_list = line.split(',')
    stores_new = split_line_in_list.pop(0)+','+split_line_in_list.pop(2)+','+split_line_in_list.pop(3)+','+split_line_in_list.pop(3)+'\n'
    print(line)
    file_new.write(stores_new)
    '''stores_new.insert(0,pop_collum_sid)
    stores_new.insert(1,pop_collum_name)
    stores_new.insert(2,pop_collum_tel)
    stores_new.insert(3,pop_collum_wifi)
    #print(stores_new)
    file = open('stores_new.txt', 'w', encoding = 'UTF-8')'''
       
    
file_old.close()
file_new.close()
