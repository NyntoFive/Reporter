import csv

def write_csv(filename, header, data):
    """Write the provided data to the CSV file.
    :param str filename: the name of the file \
        to which the data should be written.
    :param list header: The header for the \
        columns in the csv file.
    :param list data: The list of list mapping \
        the values to the columns.
    """
    try:
        with open(filename, 'w') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(header)
            csv_writer.writerows(data)
    except (IOError, OSError) as csv_file_error:
        print(
            "Unable to write the contents to a csv file. Exception: {}"
            .format(csv_file_error)
        )

def new_write_csv(filename, header, data):
    """DictReader implementation
    :param str filename: name of the file to be read.
    :param list header: The header of the data
    :param list data: The list of dicts mapping \
        the values to columns
    """
    
    try:
        with open(filename, 'w') as csv_file:

            csv_writer = csv.DictWriter(csv_file, fieldnames=header)
            csv_writer.writeheader()
            csv_writer.writerows(data)


    except (IOError, OSError) as csv_file_error:
        print(
            "Unable to write the contents to csv file. Exception: {}"
            .format(csv_file_error)
        )
        
if __name__ == '__main__':

    header = ['name', 'age', 'gender']
    
    data = [['Richard', 32, 'M'],
            ['Mumzil', 21, 'F'],
            ['Abby', 27, 'F'],
            ['Mike', 39, 'M']]

    data2 = [
        {'name': 'Richard', 'age': 32, 'gender': 'M'},
        {'name': 'Mumzil', 'age': 21, 'gender':'F'},
        {'name': 'Melinda', 'age': 25, 'gender': 'F'}
    ]
    filename = 'sample_csv.csv'

    new_write_csv(filename, header, data2)
