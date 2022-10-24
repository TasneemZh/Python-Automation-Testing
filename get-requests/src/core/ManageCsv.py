import csv


class ManageCsv:
    def get_read_csv(self, file_name):
        requests_array = []
        with open('./' + file_name, 'rt') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                requests_array.append(row)
                # print("row " + row[0] + ", " + row[1])
                # self.arrayOfRequests.extend([row[0], row[1]])

            return requests_array
