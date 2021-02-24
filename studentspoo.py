
class Student:
    # constructor de la clase
    def __init__(self):
        self.data = [
        {"id": "202100", "name": "zayda",   "age": 20, "gender": "female", "score": 9.8},
        {"id": "202101", "name": "laura",   "age": 20, "gender": "female", "score": 9.4},
        {"id": "202102", "name": "oana",    "age": 21, "gender": "female", "score": 8.9},
        {"id": "202103", "name": "marco",   "age": 22, "gender": "male",   "score": 9.1},
        {"id": "202104", "name": "monica",  "age": 21, "gender": "female", "score": 9.5},
        {"id": "202105", "name": "jose",    "age": 21, "gender": "male",   "score": 9.5},
        {"id": "202104", "name": "monica",  "age": 21, "gender": "female", "score": 9.5},
        {"id": "202105", "name": "jose",    "age": 21, "gender": "male",   "score": 9.5}
        ]
    # load_data
    def load_data(self):
        print("Diccionario sin modificaciones\n", self.data,"-"*84)
    # remove_duplicates
    def remove_duplicates(self):
        self.new_data = []
        ids = {}
        print("Diccionario sin duplicados")
        for student in self.data:
            key = student["id"] 
            if key in ids:
                ids[key] += 1
            else:
                ids[key] = 1                 
                self.new_data.append(student)     
                print(student)
        print("-" * 84)
    # summary
    def summary(self):
        for student in self.new_data:
            print("%-9s %-10s %-4d %-10s %.2f" % (student["id"], student["name"].capitalize(), student["age"], student["gender"].capitalize(), student["score"]))
        print("-" * 84)
    # short_summary
    def short_summary(self, cols):
        for student in self.new_data:
            line = ""
            for col in cols:   # ('age', 'score')
                line += "%-4s" % (student[col])
            print(line)
    # save
    def save(self, filename):
        with open(filename, "w") as fh:
            for student in self.new_data:
                line = "%-10s %-10s %-4d %-10s %.2f\n" % (student["id"], student["name"].capitalize(), student["age"],student["gender"].capitalize(), student["score"])
                fh.write(line)
    # print_mean
    def print_mean(self, key):
        self.values=[]
        for student in self.new_data:
            score = student[key]
            self.values.append(score)

        mean = sum(self.values) / len(self.values)

        print("Mean (%s): %.2f" % (key,mean))
    # print_gender_info
    def print_gender_info(self):
        female = 0
        male = 0

        for student in self.new_data:
            if student["gender"]=="female":
                female+=1
            if student["gender"]=="male":
                male+=1
        print("Female: ",female)
        print("Male: ",male)

if __name__ == "__main__":

    student = Student()
    student.load_data()
    student.remove_duplicates()
    student.summary()
    student.short_summary(["age","score"])
    student.save("StudentsPOO.txt")
    student.print_mean("age")
    student.print_mean("score")
    student.print_gender_info()