class_list = [{'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
              {'school_class': '4b', 'scores': [2, 4, 3, 5]},
              {'school_class': '4c', 'scores': [5, 4, 4, 3, 3, 5]},
              {'school_class': '5a', 'scores': [5, 5, 3, 4, 5, 4, 3]},
              {'school_class': '5b', 'scores': [2, 4, 5]}]
score_sum = 0
student_number = 0
score_in_class_sum = 0
student_in_class_number = 0
for class_index in class_list:
    for score_index in class_index['scores']:
        score_in_class_summ += score_index
        student_in_class_number += 1
    score_sum += score_in_class_sum
    student_number += student_in_class_number
    print('В классе ' + class_index['school_class'] + ' средний балл - ' +
          str(float('{0:.2f}'.format(score_in_class_sum /
                                     student_in_class_number))))
    score_in_class_sum = 0
    student_in_class_number = 0
print('Средний балл по школе - ' + str(float('{0:.2f}'.format
                                             (score_sum / student_number))))
