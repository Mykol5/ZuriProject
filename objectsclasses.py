class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
        
    def change_name(self, newname):
      	self.name = newname
      	print('My name is', self.name)

    def change_age(self, newage):
    	self.age = newage
    	print('And my age is', self.age)

    def add_track(self, tracks):
    	self.tracks.append(tracks)
    	print('I am offering tracks', self.tracks)

    def get_score(self):
    	print('The score I got is', self.score)
        
        

Bob = Student(name="Bob", age=26, tracks=["FE", "BE"], score=20.90)
Bola = Student(name="Bola", age=28, tracks=["FE", "BE"], score=25.92)
Bolu = Student(name="Bolu", age=22, tracks=["FE", "BE"], score=34.01)
Jide = Student(name="Bola", age=21, tracks=["FE", "BE"], score=32.44)
Mody = Student(name="Bola", age=29, tracks=["FE", "BE"], score=43.52)


Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()


Bola.change_name("John")
Bola.change_age(32)
Bola.add_track("Python")
Bola.get_score()

Bolu.change_name("Martins")
Bolu.change_age(37)
Bolu.add_track("JavaScript")
Bolu.get_score()

Jide.change_name("Jonah")
Jide.change_age(31)
Jide.add_track("Python")
Jide.get_score()

Mody.change_name("Dennis")
Mody.change_age(28)
Mody.add_track("Php")
Mody.get_score()
