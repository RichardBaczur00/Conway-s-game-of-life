class IOhelper:
    def __init__(self, file_name, file_type):
        self.file_name = file_name
        self.file_type = file_type


    def interpret_txt(self, raw_data):
        print(raw_data)
        return (int(raw_data[0]), int(raw_data[1]))


    def read_txt(self, number_of_values):
        data = []
        
        with open(self.file_name, "r") as f:
            for i in range(number_of_values):
                raw_data = f.read()
                data.append(self.interpret_txt(raw_data))
                print(data)
        
        return data

