import csv
import json


class ManageFiles:
    writer = None
    writer_name = None
    relative_path = None

    def __init__(self):
        config = self.read_from_json("config")
        if config["run_command"]:
            self.relative_path = "./"
        else:
            self.relative_path = "../../"

    def read_from_json(self, file_name):
        count = 2
        while count > 0:
            if self.relative_path is None:
                self.relative_path = "./"
            try:
                config_file = open(self.relative_path + file_name + ".json")
                return json.load(config_file)
            except FileNotFoundError:
                count -= 1
                self.relative_path = "../../"

    def read_from_csv(self, file_name, storage_type):
        input_list = []
        with open(self.relative_path + "resources/files/" + file_name + ".csv", "rt") as file:
            reader = csv.reader(file)
            next(reader)
            match storage_type:
                case "unpack":
                    for row in reader:
                        input_list.append([row[0], row[1], row[2], row[3], row[4], row[5], row[6]])
                case "list":
                    for row in reader:
                        input_list.append([row[0], row[1], row[2]])
                case _:
                    raise Exception("Unsupported storage type!")
            return input_list

    def open_writer_csv(self, file_name, headers_name):
        with open(self.relative_path + "resources/files/" + file_name + ".csv", "w", newline='') as file:
            self.writer_name = file_name
            self.writer = csv.writer(file)
            self.writer.writerow(headers_name)

    def write_to_csv(self, csv_data):
        with open(self.relative_path + "resources/files/" + self.writer_name + ".csv", "a", newline='') as file:
            self.writer = csv.writer(file)
            self.writer.writerow(csv_data)
