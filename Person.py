import random


class Person:
    def __init__(self, _gender=None, _name=None, _height=None, _weight=None, _eye_color=None, _hair_color=None,
                 _ethnicity=None):  # Why do I have to set the parameters to None?
        self._gender = _gender
        self._name = _name
        self._height = _height
        self._weight = _weight
        self._eye_color = _eye_color
        self._hair_color = _hair_color
        self._ethnicity = _ethnicity

    def gender(self):
        possible_genders = ['Male', 'Female']
        gender = random.choice(possible_genders)
        self._gender = gender

    def name(self):
        common_male_names = ['James', 'John', 'Robert', 'Michael', 'William', 'David', 'Richard', 'Joseph', 'Thomas',
                             'Charles']
        common_female_names = ['Mary', 'Patricia', 'Jennifer', 'Linda', 'Elizabeth', 'Barbara', 'Susan', 'Jessica',
                               'Sarah', 'Sarah', 'Karen']
        if self._gender == 'Male':
            name = random.choice(common_male_names)
            self._name = name
        else:
            name = random.choice(common_female_names)
            self._name = name

    def height(self):
        random_height = random.randrange(60, 84, 1)
        self._height = random_height

    def weight(self):
        possible_weight = random.randrange(115, 300, 1)
        self._weight = possible_weight

    def eye_color(self):
        possible_colors = ['amber', 'blue', 'brown', 'gray', 'green', 'hazel', 'red']
        color = random.choice(possible_colors)
        self._eye_color = color

    def hair_color(self):
        possible_colors = ['brown', 'blond', 'black', 'red', 'white']
        color = random.choice(possible_colors)
        self._hair_color = color

    def ethnicity(self):
        possible_ethnicities = ['African American', 'Native American', 'Pacific Islander', 'Asian', 'Native Hawaiian',
                                'White']
        ethnicity = random.choice(possible_ethnicities)
        self._ethnicity = ethnicity


person = Person()
person.gender()
person.name()
person.height()
person.weight()
person.eye_color()
person.hair_color()
person.ethnicity()
print(person._gender, person._name, person._height, person._weight, person._eye_color, person._hair_color, person._ethnicity)


class Emotion:
    def __init__(self, _mood, _intensity):
        self._mood = _mood
        self._intensity = _intensity

    def mood(self):
        possible_moods = ['happy', 'sad', 'angry', 'tired', 'annoyed', 'content', 'calm']
        current_mood = random.choice(possible_moods)
        self._mood = current_mood

    def intensity(self, factor):
        self._intensity = factor
