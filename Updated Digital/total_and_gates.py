                    # Total AND Gates #
import operator

count_dict = dict()
total_equations = []
elements = ['A','B','C','D','E','F','a','b','c','d','e','f']
sample_set = []

fin = open("EQUATION.txt")
for line in fin :
    equation = line.strip().split(',')
    total_equations.append(equation)

# Filling the Sample_Set
for i in range(len(elements)) :
    for j in range(i + 1 , len(elements)) :
        if j != i + 6 :
            sample_set.append(elements[i] + elements[j])
            sample_set.append(elements[j] + elements[i])
        else :
            continue

def update_dict(each_term) :
    global count_dict
    for i in range(len(each_term)) :
        for j in range(i + 1 , len(each_term)) :
            sample = each_term[i] + each_term[j]

            if sample not in count_dict and sample in sample_set :
                count_dict[sample] = 1
            else :
                count_dict[sample] = count_dict[sample] + 1


for each_equation in total_equations :
    for each_term in each_equation :
        update_dict(each_term)

sorted_dict = sorted(count_dict.items(), key = operator.itemgetter(1))

fout = open('output.txt','w')

for each in sorted_dict :
    output_string = each[0] + " = " + str(each[1]) + "\n"
    fout.write(output_string)

fout.close()
