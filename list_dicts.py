def run():
    my_list = [1, "Hi", True, 3.5]
    my_dict = {"firstname": "Cristobal", "lastname": "Lopez"}

    super_list = [
        {"firstname": "Cristobal", "lastname": "Lopez"},
        {"firstname": "Tony", "lastname": "Montana"},
        {"firstname": "Sergio", "lastname": "Pérez"},
        {"firstname": "Carlos", "lastname": "Sainz"},
    ]

    super_dict = {
        "monoplaza": ["RB18", "F175", "W13", "MCL36"],
        "teams": ["RedBull", "Ferrari", "Mercedes", "Mclaren"],
        "drivers": ["Max Verstappen", "Sergio Perez", "Charles Leclerc", "Lewis Hamilton", "Lando Norris"],

    }

    for key, value in super_dict.items():
        print(key, ">", value) 

if __name__ == '__main___':
    run()



