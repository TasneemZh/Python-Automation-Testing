import csv


class ManageCsv:
    writer = None
    writer_name = None

    def read_from_csv(self, file_name):
        requests_array = []
        with open("../../resources/files/" + file_name, "rt") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                requests_array.append([row[1], row[2], row[3]])
            return requests_array

    def open_writer_csv(self, file_name):
        with open("../../resources/files/" + file_name, "w", newline='') as file:
            self.writer_name = file_name
            self.writer = csv.writer(file)
            self.writer.writerow(["hotel name", "address_link"])

    def write_to_csv(self, search_result):
        with open("../../resources/files/" + self.writer_name, "a", newline='') as file:
            self.writer = csv.writer(file)
            self.writer.writerow(search_result)
