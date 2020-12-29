# Brute Force
# read line by line
# first line: create number of lists based on N, so 2 5 => 2 lists
# can use 5 to define the loop for i in range(0, second number on first line)
#     ** notes: XOR in python is ^, so my formula is ((x ^ lastAnswer) % N)
# initialize lastAnswer
# start reading line by line
#     check the first element of the line
#         if it is a 1 --> put smth in the list
#             calculate ((x^lastAnswer)%N)
#                 if it is 0/1/2...
#                     put the third number of the list to the corresponding array
#         if it is a 2 --> change lastAnswer, print the lastAnswer
#             calculate ((x^lastAnswer) % N)
#                 if it is 0/1/2...
#                     take out the last number of the array --> assign it to lastAnswer --> print it out

# ** What is complexity of 2D array??
def dynamicArray(n, queries):
    lastAnswer = 0
    list = []
    result = []
    for i in range(0,n):
        list.append([]) # --> list = ( [], [], [], ...) = (S0, S1, S2, ...)

    for i in range(0, len(queries)):
        for j in range(0, len(queries[i])):
            if queries[i][0] == 1:
                seq = ((queries[i][1] ^ lastAnswer) % n)
                list[seq].append(queries[i][2])

            if queries[i][0] == 2:
                seq = ((queries[i][1] ^ lastAnswer) % n)
                number = list[seq][len(list)-1]
                lastAnswer =  number
                result.append(number)
    print(result)


queries = [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]
dynamicArray(2, queries)




