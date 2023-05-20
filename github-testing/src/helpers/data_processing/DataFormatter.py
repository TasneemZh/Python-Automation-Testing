from helpers.data_processing import Constants
from utils.ManageFiles import ManageFiles


class DataFormatter:
    @staticmethod
    def sort_list_by_stars(stars_list, user_id):
        max_stars = []
        manage_files = ManageFiles()
        file_name = Constants.SORTED_FILE_NAME + "-" + user_id
        for array in stars_list:
            thousands = array[2].find('k')
            if thousands > 0:
                stars_float = float(array[2][0:thousands:1]) * 1000
            else:
                stars_float = float(array[2])
            max_stars.append([stars_float, array[2]])
        max_stars.sort(reverse=True)
        manage_files.open_writer_csv(file_name, ["Repository Name", "Project Name", "Stars Count"])
        for star in max_stars:
            for array in stars_list:
                if star[1] == array[2]:
                    manage_files.write_to_csv([array[0], array[1], array[2]])
        return max_stars
