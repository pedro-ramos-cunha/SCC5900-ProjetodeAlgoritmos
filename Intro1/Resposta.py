total_answer = 0
numbers_count = {}

line1 = input() ## Line 1
line2 = input() ## Line 2
line1 = line1.split(' ')
line2 = line2.split(' ')

size = int(line1[0])
sum_compare = int(line1[1])



for number in line2:
    if number in numbers_count:
        numbers_count[number]+=1
    else:
        numbers_count[number]=1

for x in range(1,int(sum_compare/2)+1):
    comp_x = sum_compare-x
    if  str(x) in numbers_count and str(comp_x) in numbers_count:
        if x==comp_x:
            total_answer += int((numbers_count[str(x)]*(numbers_count[str(x)]-1))/2)
        else:
            total_answer += numbers_count[str(x)]*numbers_count[str(comp_x)]

print(total_answer)