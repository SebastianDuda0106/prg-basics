ans=['o','o','o']
ans[0]=input('SURVEY Are you interested in computer science? (y/n): ')
ans[1]=input('Do you like playing computer games? (y/n): ')
ans[2]=input('Do you have an Instagram account? (y/n): ')
i=0
while i<3:
    if ans[i]=='y':
        ans[i]='Yes'
    elif ans[i]=='n':
        ans[i]='No'
    else:
        ans[i]='Invalid answer'
    i+=1

print(f'\nSURVEY RESULTS Interested in computer sciene: {ans[0]}')
print(f'Playing computer games: {ans[1]}')
print(f'Has an Instagram account: {ans[2]}')