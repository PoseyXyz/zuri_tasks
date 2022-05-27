class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, new_name):
        self.name = new_name
        print(f"Student's name has been changed to {self.name}")

    def change_age(self, new_age):
        self.age = int(new_age)
        print(f"Student's age has been changed to {self.age}")

    def add_track(self, new_track):
        self.tracks.append(new_track)
        print(f"{new_track} has been appended as a new track")

    def get_score(self):
        print(f"{self.name}'s score is {self.score}")



Bob = Student(name="Bob", age=26, tracks=["FE", "BE"], score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
