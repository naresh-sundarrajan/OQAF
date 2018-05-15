#!flask/bin/python
from flask import Flask, jsonify, make_response
import pandas as pd
import csv

my_csv = pd.read_csv('/Users/naresh/Documents/workspace/Environments/dqaf/acc_dat.csv')
column = my_csv.age
column_name = 'AGE'
count_total_records= 0
count_zero=0
count_greaterthan130=0
count_negatives=0
count_correct_records=0
for row in column:
    if row == 0:
        count_zero += 1
    if row < 0:
        count_negatives +=1
    if row >= 130:
        count_greaterthan130 +=1
    count_total_records +=1
#print(count_zero)
#print(count_negatives)
#print(count_greaterthan130)
#count_tot = count_zero+count_negatives+count_greaterthan130
#print("total:",count_tot)
count_incorrect_records=count_zero+count_negatives+count_greaterthan130
count_correct_records=count_total_records-count_incorrect_records
Accuracy1=count_correct_records/count_total_records
app = Flask(__name__)
#ADDED CHANGE ON DASHBOARD HERE

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Refer documentation for available services'}), 404)

app.config['JSON_SORT_KEYS'] = False

Acc1 = [
    {
        'dqa_concept': u'Accuracy',
        'dqa_model':u'NDQM',
        'dqa_description': u'The extent to which data are correct, reliable, and free of error',
        'dqa_measure': u'Accuracy1',
        'dqa_measure_description':u'syntactic accuracy',
        'dqa_total_records':count_total_records,
        'dqa_total_correct_records':count_correct_records,
        'dqa_measure_result':Accuracy1,
        'dqa_visualization_preferred_method': u'Distribution',
        'done': True
    },
    {
        'dqa_measure_id': 1,
        'dqa_concept': u'Accuracy',
        'dqa_description': u'The extent to which data are correct, reliable, and free of error',
        'dqa_measure_count_zero': count_zero,
        'dqa_data_element_name':column_name,
        'dqa_visualization_preferred_method': u'Distribution',
        'done': True
    },
    {
        'dqa_measure_id': 2,
        'dqa_concept': u'Accuracy',
        'dqa_description': u'The extent to which data are correct, reliable, and free of error',
        'dqa_measure_count_negatives': count_negatives,
        'dqa_data_element_name':column_name,
        'dqa_visualization_preferred_method': u'Distribution',
        'done': True
    },
    {
        'dqa_measures_id': 3,
        'dqa_concept': u'Accuracy',
        'dqa_description': u'The extent to which data are correct, reliable, and free of error',
        'dqa_measure_count_greaterthan130': count_greaterthan130,
        'dqa_data_element_name':column_name,
        'dqa_visualization_preferred_method': u'Distribution',
        'done': True
    }
]

Compl1 = [
    {
        'dqa_concept': u'Completeness1',
        'dqa_model':u'NDQM',
        'dqa_description': u'The extent to which data are of sufficient breadth, depth, and scope for the task at hand',
        'dqa_measure_description':
        [
            { 'dqa_measure': u'Completeness1',
             'dqa_measure_result':count_zero }
        ],
        'dqa_total_records':count_total_records,
        'dqa_total_correct_records':count_correct_records,
        'dqa_visualization_preferred_method': u'Distribution',
        'done': True
    }
]


@app.route('/dqa/api/v2.7/Accuracy1', methods=['GET'])
def get_Acc1():
    return jsonify({'Accuracy1': Acc1})

@app.route('/dqa/api/v2.7/Completeness1', methods=['GET'])
def get_Compl1():
    return jsonify({'Completeness1': Compl1})


if __name__ == '__main__':
    app.run(debug=True)
