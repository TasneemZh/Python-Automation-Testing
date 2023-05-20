import os

import pyautogui
import allure

from utils.ManageFiles import ManageFiles


class ScreenShot:
    image_path = None
    image_extension = None

    def take_screenshot(self, image_name, image_extension="png"):
        manage_files = ManageFiles()
        config = manage_files.read_from_json("config")
        if config["run_command"]:
            relative_path = "./"
        else:
            relative_path = "../../"
        self.image_path = relative_path + "resources/screenshots/" + image_name + "." + image_extension
        self.image_extension = image_extension
        pyautogui.screenshot(os.path.abspath(self.image_path))

    def attach_image_to_allure(self):
        attachment_type = allure.attachment_type.PNG
        match self.image_extension:
            case "png":
                None
            case "jpg":
                attachment_type = allure.attachment_type.JPG
            case "bmp":
                attachment_type = allure.attachment_type.BMP
            case "gif":
                attachment_type = allure.attachment_type.GIF
            case _:
                raise Exception("'" + self.image_extension + "' is not supported for attachment to Allure!")
        allure.attach.file(self.image_path, attachment_type=attachment_type)
