import random
from random import randrange
# Exercise 1
# Create an emotions dict, where the keys are the names of different human emotions and the values are the degree to which the emotion is being felt on a scale from 1 to 3.

# Exercise 2
# Write a Person class with the following characteristics:

# name (string)
# emotions (dict)
# Initialize an instance of Person using your emotions dict from exercise 1.

# Exercise 3
# Add an instance method to your class that displays a message describing how the person is feeling. Substitute 
# the words "high", "medium", and "low" for the emotion levels 1, 2, and 3.

emotions={
    'happy':[1,2,3],
    'sad':[1,2,3],
    'angry':[1,2,3],
    'elated':[1,2,3],
    'malaise':[1,2,3],
    'depressed':[1,2,3],
    'upset':[1,2,3],
    'excited':[1,2,3]
}

class Person:
    def __init__(self,name, emotion):
        self.name = name 
        self.emotion = emotion
    def message(self):
        return(f'{self.name} is feeling {self.emotion_level()} {self.rand_emotion()} today')
    def emotion_level(self):
        x = randrange(3)
        if x == 0:
            return "a little"
        elif x==1:
            return "somewhat"
        elif x==2:
            return "very"
    def rand_emotion(self):
        return(random.choice(list(self.emotion.keys())))


adam = Person('Adam', emotions)
print(adam.message())