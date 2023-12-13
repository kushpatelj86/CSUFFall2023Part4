from main import *
def homework_average(grades={70314: {'name': 'Anna Kendrick', 'homework': [77, 83, 100], 'laboratory': [85, 78]}, 90919: {'name': 'Rebel Wilson', 'homework': [51, 60, 96], 'laboratory': [92, 87]}, 72457: {'name': 'Brittany Snow', 'homework': [97, 81, 73], 'laboratory': [67, 100]}, 55331: {'name': 'Hailee Steinfeld', 'homework': [63, 67, 62], 'laboratory': [100, 98]}, 52392: {'name': 'Hana Mae Lee', 'homework': [95, 100, 73], 'laboratory': [97, 74]}, 65087: {'name': 'Skylar Astin', 'homework': [61, 89, 87], 'laboratory': [100, 97]}, 91523: {'name': 'Adam DeVine', 'homework': [99, 94, 89], 'laboratory': [69, 91]}}, student_id="70314"):
    if student_id in grades:
        sum = 0
        for i in grades[student_id]['homework']:
            sum = sum + i
        average = sum / len(grades[student_id]['homework'])
        return average
    else:
        return 0


def laboratory_average(grades={70314: {'name': 'Anna Kendrick', 'homework': [77, 83, 100], 'laboratory': [85, 78]}, 90919: {'name': 'Rebel Wilson', 'homework': [51, 60, 96], 'laboratory': [92, 87]}, 72457: {'name': 'Brittany Snow', 'homework': [97, 81, 73], 'laboratory': [67, 100]}, 55331: {'name': 'Hailee Steinfeld', 'homework': [63, 67, 62], 'laboratory': [100, 98]}, 52392: {'name': 'Hana Mae Lee', 'homework': [95, 100, 73], 'laboratory': [97, 74]}, 65087: {'name': 'Skylar Astin', 'homework': [61, 89, 87], 'laboratory': [100, 97]}, 91523: {'name': 'Adam DeVine', 'homework': [99, 94, 89], 'laboratory': [69, 91]}}, student_id="70314"):
    if student_id in grades:
        sum = 0
        for i in grades[student_id]['laboratory']:
            sum = sum + i
        average = sum / len(grades[student_id]['laboratory'])
        return average 
    else:
        return 0


def total_weighted_average (grades={70314: {'name': 'Anna Kendrick', 'homework': [77, 83, 100], 'laboratory': [85, 78]}, 90919: {'name': 'Rebel Wilson', 'homework': [51, 60, 96], 'laboratory': [92, 87]}, 72457: {'name': 'Brittany Snow', 'homework': [97, 81, 73], 'laboratory': [67, 100]}, 55331: {'name': 'Hailee Steinfeld', 'homework': [63, 67, 62], 'laboratory': [100, 98]}, 52392: {'name': 'Hana Mae Lee', 'homework': [95, 100, 73], 'laboratory': [97, 74]}, 65087: {'name': 'Skylar Astin', 'homework': [61, 89, 87], 'laboratory': [100, 97]}, 91523: {'name': 'Adam DeVine', 'homework': [99, 94, 89], 'laboratory': [69, 91]}}, student_id="70314"):
    if student_id in grades:
       hwgrade = homework_average(grades,student_id)
       labgrade = laboratory_average(grades,student_id)

       totalgrade =  (hwgrade * 0.25) + (labgrade * 0.75)
       return totalgrade
    
    else:
        return 0








