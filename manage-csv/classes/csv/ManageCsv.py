import csv


class ManageCsv:
    @staticmethod
    def read_csv():
        with open('test.csv', 'rt') as file:
            reader = csv.reader(file)
            next(reader)
            print("Reading CSV File:-")
            for row in reader:
                print(row)

    @staticmethod
    def write_csv():
        with open('test.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows([
                ["rowNum", "fieldCol1", "fieldCol2"],
                ["row1", "field1", "field2"],
                ["row2", "field1", "field2"]
            ])


ManageCsv.write_csv()
ManageCsv.read_csv()
