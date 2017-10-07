#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


print "number of data points: ", len(enron_data)

print "number of features per person: ", len(enron_data["SKILLING JEFFREY K"])

print "number of poi: ", sum( x["poi"] == 1 for x in enron_data.values() )

print enron_data["PRENTICE JAMES"]["total_stock_value"]

print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

print enron_data["SKILLING JEFFREY K"]["total_payments"]
print enron_data["LAY KENNETH L"]["total_payments"]
print enron_data["FASTOW ANDREW S"]["total_payments"]

print "number of point with salary: ", sum( x["salary"] != "NaN" for x in enron_data.values() )

print "number of point with email_address: ", sum( x["email_address"] != "NaN" for x in enron_data.values() )

print "number of point without total_payments: ", sum( x["total_payments"] == "NaN" for x in enron_data.values() )

print "number of poi without total_payments: ", sum( x["total_payments"] == "NaN" and x["poi"] == 1 for x in enron_data.values() )