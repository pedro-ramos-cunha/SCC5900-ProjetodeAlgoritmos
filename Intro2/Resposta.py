

while True:
    number_students = input() ## Line 1
    if int(number_students) == 0:
        break
    
    group_subject_list = {}

    

    for student in range(0,int(number_students)):
        input_list = input()
        subject_list = input_list.split(' ')
        subject_list.sort()
        key = '-'.join(subject_list)


        if key in group_subject_list:
            group_subject_list[key]+=1
        else:
            group_subject_list[key]=1

        popular_combination =max([group_subject_list[x] for x in group_subject_list])

    if popular_combination>1:
        print(popular_combination)
    else:
        print(number_students)


