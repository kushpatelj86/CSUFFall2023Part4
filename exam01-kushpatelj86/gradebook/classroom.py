from main import *


def homework_average  (grades={70314: {'name': 'Anna Kendrick', 'homework': [77, 83, 100], 'laboratory': [85, 78]}, 90919: {'name': 'Rebel Wilson', 'homework': [51, 60, 96], 'laboratory': [92, 87]}, 72457: {'name': 'Brittany Snow', 'homework': [97, 81, 73], 'laboratory': [67, 100]}, 55331: {'name': 'Hailee Steinfeld', 'homework': [63, 67, 62], 'laboratory': [100, 98]}, 52392: {'name': 'Hana Mae Lee', 'homework': [95, 100, 73], 'laboratory': [97, 74]}, 65087: {'name': 'Skylar Astin', 'homework': [61, 89, 87], 'laboratory': [100, 97]}, 91523: {'name': 'Adam DeVine', 'homework': [99, 94, 89], 'laboratory': [69, 91]}}, assignment_no=3):
    average = 0
    sum = 0
    
    average = 0
    sum = 0
    count = 0
    try:
         
        for i in grades:         
            for j in range(0,len(grades[i]['homework'])):
                if j == assignment_no and assignment_no >= 0 and  assignment_no < len(grades[i]['homework']):
                    sum = sum + grades[i]['homework'][j]
                    count = count + 1

        if count == 0:
            return 0
        else:
            average = sum / count
            return average 

    except Exception:
        return 0
    

def homework_average_average (grades={70314: {'name': 'Anna Kendrick', 'homework': [77, 83, 100], 'laboratory': [85, 78]}, 90919: {'name': 'Rebel Wilson', 'homework': [51, 60, 96], 'laboratory': [92, 87]}, 72457: {'name': 'Brittany Snow', 'homework': [97, 81, 73], 'laboratory': [67, 100]}, 55331: {'name': 'Hailee Steinfeld', 'homework': [63, 67, 62], 'laboratory': [100, 98]}, 52392: {'name': 'Hana Mae Lee', 'homework': [95, 100, 73], 'laboratory': [97, 74]}, 65087: {'name': 'Skylar Astin', 'homework': [61, 89, 87], 'laboratory': [100, 97]}, 91523: {'name': 'Adam DeVine', 'homework': [99, 94, 89], 'laboratory': [69, 91]}}):
    average = 0
    sum = 0
    count = 0
    try:
         
        for i in grades:         
            for j in grades[i]['homework']: 
                sum = sum + j
                count = count + 1

        if count == 0:
            return 0
        else:
            average = sum / count
            return average 

    except Exception:
        return 0





def laboratory_average  (grades={70314: {'name': 'Anna Kendrick', 'homework': [77, 83, 100], 'laboratory': [85, 78]}, 90919: {'name': 'Rebel Wilson', 'homework': [51, 60, 96], 'laboratory': [92, 87]}, 72457: {'name': 'Brittany Snow', 'homework': [97, 81, 73], 'laboratory': [67, 100]}, 55331: {'name': 'Hailee Steinfeld', 'homework': [63, 67, 62], 'laboratory': [100, 98]}, 52392: {'name': 'Hana Mae Lee', 'homework': [95, 100, 73], 'laboratory': [97, 74]}, 65087: {'name': 'Skylar Astin', 'homework': [61, 89, 87], 'laboratory': [100, 97]}, 91523: {'name': 'Adam DeVine', 'homework': [99, 94, 89], 'laboratory': [69, 91]}}, assignment_no=3):
    average = 0
    sum = 0
    
    average = 0
    sum = 0
    count = 0
    try:
         
        for i in grades:         
            for j in range(0,len(grades[i]['laboratory'])):
                if j == assignment_no and assignment_no >= 0 and  assignment_no < len(grades[i]['laboratory']):
                    sum = sum + grades[i]['laboratory'][j]
                    count = count + 1

        if count == 0:
            return 0
        else:
            average = sum / count
            return average 

    except Exception:
        return 0
    






def laboratory_average_average (grades={70314: {'name': 'Anna Kendrick', 'homework': [77, 83, 100], 'laboratory': [85, 78]}, 90919: {'name': 'Rebel Wilson', 'homework': [51, 60, 96], 'laboratory': [92, 87]}, 72457: {'name': 'Brittany Snow', 'homework': [97, 81, 73], 'laboratory': [67, 100]}, 55331: {'name': 'Hailee Steinfeld', 'homework': [63, 67, 62], 'laboratory': [100, 98]}, 52392: {'name': 'Hana Mae Lee', 'homework': [95, 100, 73], 'laboratory': [97, 74]}, 65087: {'name': 'Skylar Astin', 'homework': [61, 89, 87], 'laboratory': [100, 97]}, 91523: {'name': 'Adam DeVine', 'homework': [99, 94, 89], 'laboratory': [69, 91]}}):
    average = 0
    sum = 0
    count = 0
    for i in grades:         
        for j in grades[i]['laboratory']: 
            sum = sum + j
            count = count + 1

    if count == 0:
         return 0
    else:
         average = sum / count
         return average 






def total_weighted_average_average  (grades={70314: {'name': 'Anna Kendrick', 'homework': [77, 83, 100], 'laboratory': [85, 78]}, 90919: {'name': 'Rebel Wilson', 'homework': [51, 60, 96], 'laboratory': [92, 87]}, 72457: {'name': 'Brittany Snow', 'homework': [97, 81, 73], 'laboratory': [67, 100]}, 55331: {'name': 'Hailee Steinfeld', 'homework': [63, 67, 62], 'laboratory': [100, 98]}, 52392: {'name': 'Hana Mae Lee', 'homework': [95, 100, 73], 'laboratory': [97, 74]}, 65087: {'name': 'Skylar Astin', 'homework': [61, 89, 87], 'laboratory': [100, 97]}, 91523: {'name': 'Adam DeVine', 'homework': [99, 94, 89], 'laboratory': [69, 91]}}):
    average = 0
    sum = 0
    count = 0
    hwaverage = homework_average_average(grades)
    labaverage = laboratory_average_average(grades)



    average = (hwaverage * 0.25 ) + (labaverage *0.75)
    return average




