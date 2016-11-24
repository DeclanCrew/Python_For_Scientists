import csv

def read_valid_universities (file, removeEmpty):
    """
    This function will read the contents of the csv file 'uniData.csv' using
    the csv.DictReader generator, it will return a list of entries, if
    if removeEmpty is set to True, it will skip entries with no data on part
    time students.
    """
    output = []
    with open(file) as csvFile:
        for entry in csv.DictReader(csvFile):
            if removeEmpty and entry["Part time"] == "None":
                continue
            output.append(entry)
    return output

read_valid_universities("uniData.csv", False)
