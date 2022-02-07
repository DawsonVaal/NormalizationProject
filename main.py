import csv
import math

myDict = {}

with open('auto-mpg.csv', mode='r') as read_obj:
    reader = csv.reader(read_obj)
    dataAsRows = list(reader)

def mainMenu():
    print(final_matrix[askUserInput()][askUserInput()])

def askUserInput():
    print("Please enter the index of the dataset you wish to compare (1-100): ")
    Index = int(input("Enter number : "))
    while True:
        if Index >= 1 and Index <= 100:
            return Index - 1
        else:
            print("That was an invalid number, please re-enter (1-100): ")
            Index = int(input("Enter number : "))

def normalize_data(data, min, max):
    normal_column = []
    for i in range(len(data)):
        new_value = round((data[i] - min) / (max - min), 2)
        normal_column.append(new_value)
    return normal_column

def compute_distance_numerical(new_data):
    distance_matrix = []
    for i in range(len(new_data)):
        temp = []
        for j in range(len(new_data)):
            distance = round(math.fabs(new_data[i] - new_data[j]),2)
            temp.append(distance)
        distance_matrix.append(temp)
    return distance_matrix

def compute_distance_categorical(data):
    distance_matrix = []
    for i in range(len(normalized_data[0])):
        temp = []
        for j in range(len(normalized_data[0])):
            if (data[i] != data[j]):
                distance = 1
            else:
                distance = 0
            temp.append(distance)
        distance_matrix.append(temp)
    return distance_matrix

def compute_distance_ordinal(data, ranking_order):
    distance_matrix = []
    for i in range(len(normalized_data[0])):
        temp = []
        for j in range(len(normalized_data[0])):
            rank_i = -1
            rank_j = -1
            for k in range(len(ranking_order)):
                if (data[i] == ranking_order[k]):
                    rank_i = k
                if (data[j] == ranking_order[k]):
                    rank_j = k
            difference = round(math.fabs(rank_i - rank_j)/(len(ranking_order)-1),2)
            temp.append(difference)
        distance_matrix.append(temp)
    return distance_matrix

def compute_distance_final(distance_numerical_1, distance_numerical_2, distance_nominal, distance_ordinal):
    distance_matrix = []
    for i in range(len(distance_numerical_1)):
        temp = []
        for j in range(len(distance_numerical_1)):
            sum = round((distance_numerical_1[i][j] + distance_numerical_2[i][j] + distance_nominal[i][j] + distance_ordinal[i][j]) * 1/4, 2)
            temp.append(sum)
        distance_matrix.append(temp)
    return distance_matrix

if __name__ == '__main__':
    open('auto-mpg.csv')

    normalized_data = []
    for j in range(0,4):
        columnList = []
        for i in range(1, len(dataAsRows)):
                columnList.append(int(dataAsRows[i][j]))
        normalized_data.append(normalize_data(columnList, min(columnList), max(columnList)))

    first_numerical_distance = compute_distance_numerical(normalized_data[0])
    second_numerical_distance = compute_distance_numerical(normalized_data[2])
    categorical_distance = compute_distance_categorical(normalized_data[3])
    ordinal_distance = compute_distance_ordinal(normalized_data[1],  [4,6,8])
    final_matrix = compute_distance_final(first_numerical_distance, second_numerical_distance, categorical_distance, ordinal_distance)

    mainMenu()

