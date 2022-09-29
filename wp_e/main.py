import csv
import json
import requests
import sys


csv_file=sys.argv[1]
output_csv_file_name=sys.argv[2]

def wpe_merge(csv_file, output_csv_file_name):
    # Time: O(n+m)
    # Space: O(n+m)
    

    h = {}
    data = []
    with open(csv_file, 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        header.append("Status")
        header.append("Status Set On")
        response = requests.get("http://interview.wpengine.io/v1/accounts/")
        items = json.loads(response.content)

        ## O(n)
        ## Loop over the results dictionaries and create a hash map of the account 
        # ID's as keys and the full account object as the value
        for i in items["results"]:
            h[i.get("account_id")] = i
        
        ## Because the data for the write function has to be a list of lists; we are 
        # adding status and status_set_on to the row by accessing the key of the account id
        # and returning the dictionary.
        # Followed by appending the whole row to the data list.
        ## O(m)
        for row in csvreader:
            obj_of_account_row = h.get(int(row[0]))
            status = obj_of_account_row.get("status")
            status_set_on = obj_of_account_row.get("created_on")
            row.append(status)
            row.append(status_set_on)
            data.append(row)

    ## Write to a new file - the data being inputed for this method to work is a list of lists,
    # where each inner list is a row of the file.
    with open(output_csv_file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        # write the header
        writer.writerow(header)
        # write all of the rows with the data
        writer.writerows(data)
    ## Return a print statement to display on the CLI that it ran successfully. 
    return print('Merge Complete')

x = wpe_merge(csv_file, output_csv_file_name)