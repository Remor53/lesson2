class_list = [{'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
              {'school_class': '4b', 'scores': [2, 4, 3, 5]},
              {'school_class': '4c', 'scores': [5, 4, 4, 3, 3, 5]},
              {'school_class': '5a', 'scores': [5, 5, 3, 4, 5, 4, 3]},
              {'school_class': '5b', 'scores': [2, 4, 5]}]
score_sum = 0
student_number = 0
for class_index in class_list:
    score_sum += sum(class_index['scores'])
    student_number += len(class_index['scores'])
    print('В классе {0} средний балл - {1:.3g}'.
          format(class_index['school_class'],
                 sum(class_index['scores']) / len(class_index['scores'])))
print('Средний балл по школе - {0:.3g}'.format(score_sum / student_number))
