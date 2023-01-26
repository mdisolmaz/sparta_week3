import csv

file_name='user_details.csv'

def open_file(file_name):
    with open(file_name,'r') as user_detail:
        csv_reader = csv.reader(user_detail,delimiter=',')
        data = []
        for line in csv_reader:
            data.append(line)
        return data

data = open_file(file_name)


def transform_file(data):
    new_data = []
    for row in data:
        name = row[1] 
        lastname = row[2]
        email = row[-1]
        username = email.split("@")[0]
        new_data.append([name, lastname,username])
    return new_data

transformed_data = transform_file(data)

def write_to_file(data, file_name):
    new_file_name = 'transformed_' + file_name
    with open(new_file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Name", "Last Name", "Username"])
        for row in data:
            writer.writerow(row)

write_to_file(transformed_data, file_name)
