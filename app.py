from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import sqlite3
from utils import create, insert, update, delete
import DB
import data

import time

from UI import UI
from Driver import Driver
from Actions import Actions


class App:

    @staticmethod
    def main(name_db):

        connection = sqlite3.connect(f"databases/{name_db}.db")
        manager = connection.cursor()

        DB.createDB(manager)
        

        objects = data.data().get_test_objects()

        for test_object in objects:
                        
            elements = data.data().get_test_elements(test_object)
            entries_data = UI().fill_enries(test_object, elements)

        for i in entries_data:
            for key, value in i.items():
                for k,v in value.items():
                    update.Update().update_by_condition(manager, key, 'Input', v, 'Test_element', k)

        connection.commit()
        print(entries_data)
        # chrome = Driver(webdriver.Chrome(
        #     ChromeDriverManager().install()))

        # time.sleep(1)

        # current_driver = chrome.get_driver()

        # Actions(current_driver).test_form(entries_data, objects)


if __name__ == "__main__":
    App().main("Tests")