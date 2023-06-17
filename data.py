        
class data:

    def __init__(self):

        self.test_cases = [{"PLACES": 
                                [{"Place":[{"actions":["klick", "input"]},
                                                 {"expected_result": 'text'},
                                                 {"elements_path": "//input[@name='ss']"}]},
                                {"Date":[{"actions":["klick", "input"]},
                                                 {"expected_result": ''},
                                                 {"elements_path": "//div[@class='b91c144835']"}]},
                                {"Persons":[{"actions":["klick"]},
                                                 {"expected_result": ''},
                                                 {"elements_path": "//button[@data-testid='occupancy-config']"}]},
                                {"Adults":[{"actions":["klick", "input"]},
                                                 {"expected_result": ''},
                                                 {"elements_path": "//button[@class='fc63351294 a822bdf511 e3c025e003 fa565176a8 f7db01295e c334e6f658 e1b7cfea84 d64a4ea64d']"}]},
                                # {"Chilren":[{"actions":["klick", "input"]},
                                #                  {"expected_result": ''}]},
                                # {"Rooms":[{"actions":["klick", "input"]},
                                #                  {"expected_result": 'text'}]},
                                {"Button_Search":[{"actions":["klick"]},
                                                 {"expected_result": ''},
                                                 {"elements_path": "//button[@type='submit']"}]}
                                ]},

                            {"AIRLINES": 
                                [{"Button_Flights":[{"actions":["klick"]},
                                                 {"expected_result": ""},
                                                 {"elements_path": ""}]},
                                {"Button_Round_trip":[{"actions":["klick"]},
                                                 {"expected_result": ""},
                                                 {"elements_path": ""}]},
                                {"Button_One_way":[{"actions":["klick"]},
                                                 {"expected_result": "text"},
                                                 {"elements_path": ""}]},
                                {"Button_Multi_city":[{"actions":["klick"]},
                                                 {"expected_result": ""},
                                                 {"elements_path": ""}]},
                                {"Place_start":[{"actions":["klick", "input"]},
                                                 {"expected_result": ""},
                                                 {"elements_path": ""}]},
                                {"Place_finish":[{"actions":["klick", "input"]},
                                                 {"expected_result": ""},
                                                 {"elements_path": ""}]},
                                {"Date":[{"actions":["klick", "input"]},
                                                 {"expected_result": ""},
                                                 {"elements_path": ""}]},
                                {"Button_Search":[{"actions":["klick"]},
                                                 {"expected_result": ""},
                                                 {"elements_path": ""}]}
                                ]},
                                
                            {"AUTO_RENT": 
                                [{"Button_Car_rentals":[{"actions":["klick"]},
                                                 {"expected_result": ""},
                                                 {"elements_path": ""}]},
                                {"Place":[{"actions":["klick", "input"]},
                                                 {"expected_result": ""},
                                                 {"elements_path": ""}]},
                                {"Date_start":[{"actions":["klick", "input"]},
                                                 {"expected_result": "text"},
                                                 {"elements_path": ""}]},
                                {"Time_start":[{"actions":["klick", "input"]},
                                                 {"expected_result": ""},
                                                 {"elements_path": ""}]},
                                {"Date_finish":[{"actions":["klick", "input"]},
                                                 {"expected_result": ""},
                                                 {"elements_path": ""}]},
                                {"Time_finish":[{"actions":["klick", "input"]},
                                                 {"expected_result": ""},
                                                 {"elements_path": ""}]},
                                {"Button_Search":[{"actions":["klick"]},
                                                 {"expected_result": ""},
                                                 {"elements_path": ""}]}
                                ]}
                            ]
          

    def get_list_to_str(self, elements):
        items = []
        for element in elements:
            for item in element:
               items.append(item)
        return items



    def get_test_objects(self):
        test_objects = []
        for objekts in self.test_cases:
            test_objects.append(objekts.keys())
        test_objects = data().get_list_to_str(test_objects)
        return test_objects


    def get_test_elements(self, test_object):
        elements = []
        for objekts in self.test_cases:
            if test_object in objekts.keys():
                for item in objekts.get(test_object):
                    
                    for element, values in item.items():
                        elements.append(element)
        return elements


    def get_data(self, test_object, element, data_elements):
        for objekts in self.test_cases:
            if test_object in objekts.keys():
                for item in objekts.get(test_object):
                    if element in item.keys():
                      for element, values in item.items():
                        for i in values:
                            if data_elements in i.keys():
                                for key, val in i.items():
                                   return val


    def get_test_actions(self, test_object, element):
        return self.get_data(test_object, element, "actions")
                        

    def get_test_expected_result(self, test_object, element):
        return self.get_data(test_object, element, "expected_result")


    def get_test_elements_path(self, test_object, element):
        return self.get_data(test_object, element, "elements_path")

if __name__ == "__main__":
    print(data().get_test_objects())
    print(data().get_test_actions("PLACES", "Persons"))