class UserData:
    dictionary = {}

    def set_data(self, test_case_id, repository_name, repository_description, list_name,
                 list_description, new_list_name, search_term):
        temp_dictionary = {
            "test_case_id": test_case_id,
            "user_name": self.dictionary["user_name"],
            "repository_name": repository_name,
            "repository_description": repository_description,
            "list_name": list_name,
            "list_description": list_description,
            "new_list_name": new_list_name,
            "search_term": search_term,
        }
        self.dictionary = temp_dictionary

    def get_value(self, key):
        return self.dictionary[key]

    def set_value(self, key, new_value):
        self.dictionary[key] = new_value
