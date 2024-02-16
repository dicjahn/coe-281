#1817422
current_users=['danyboy','sindage','babali','seren','fercsd']

new_users=['fesr','sindage','heub','seren','henbd']
index= 0

for user in new_users:
    for current_user in current_users:
       if user == current_user:
        print('Enter a new name')
    else:
        print(f"The username '{user} is available")



