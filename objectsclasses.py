class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def show(self):
    	print('Name:', self.name, 'Age:', self.age, 'Tracks:', self.tracks, 'Score:', self.score)


print('First Student')
Bob = Student("Bob", 26, "UI/UX", 20.90)
Bob.show()

print('Second Student')
Bob = Student("Jessa", 24, "Python", 25)
Bob.show()

print('Third Student')
Bob = Student("Bolu", 27, "Python", 22.4)
Bob.show()

print('Fourth Student')
Bob = Student("Junior", 23, "Python", 28.8)
Bob.show()