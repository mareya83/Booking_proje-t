
from utils import create, insert, update, delete
import data


def createDB(manager):
        

        for test_object in data.data().get_test_objects():

            create.CreateTable().create(manager,test_object)

            for test_elemets in data.data().get_test_elements(test_object):

                insert.Insert().insert(manager, test_object, test_elemets, 
                                       data.data().get_test_expected_result(test_object, test_elemets))

                actions = data.data().get_test_actions(test_object, test_elemets)

                if "input" not in actions:
                            update.Update().update_by_condition(manager, test_object, 'Input', '-','Test_element' , test_elemets)

