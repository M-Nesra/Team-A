POSITIONS = {
    "A" :  0,
    "A#":  1,
    "Bb":  1,
    "B" :  2,
    "C" :  3,
    "C#":  4,
    "Db":  4,
    "D" :  5,
    "D#":  6,
    "Eb":  6,
    "E" :  7,
    "F" :  8,
    "F#":  9,
    "Gb":  9,
    "G" : 10,
    "G#": 11,
    "Ab": 11
}

PITCHES = {
    0:  ["A"],
    1:  ["A#", "Bb"],
    2:  ["B"],
    3:  ["C"],
    4:  ["C#", "Db"],
    5:  ["D"],
    6:  ["D#", "Eb"],
    7:  ["E"],
    8:  ["F"],
    9:  ["F#", "Gb"],
    10: ["G"],
    11: ["G#", "Ab"]
}


# Constants for note names
POSITIONS = {
    "A": 0, "A#": 1, "Bb": 1,
    "B": 2, "Cb": 2,
    "C": 3, "B#": 3,
    "C#": 4, "Db": 4,
    "D": 5,
    "D#": 6, "Eb": 6,
    "E": 7, "Fb": 7,
    "F": 8, "E#": 8,
    "F#": 9, "Gb": 9,
    "G": 10,
    "G#": 11, "Ab": 11
}

PITCHES = {
    0: ("A",),
    1: ("A#", "Bb"),
    2: ("B",),
    3: ("C",),
    4: ("C#", "Db"),
    5: ("D",),
    6: ("D#", "Eb"),
    7: ("E",),
    8: ("F",),
    9: ("F#", "Gb"),
    10: ("G",),
    11: ("G#", "Ab")
}

class Note:
    """
    A class representing a musical note in the twelve-tone chromatic scale.

    Attributes:
        position (int): The note's position on the chromatic scale (0-11), with 0 = A.
        perspective (str | None): "#", "b", or None, indicating sharp, flat, or neutral view.
    """
    def __init__(self, pitch, perspective=None):
        if isinstance(pitch, int):
            self.position = pitch % 12
        elif isinstance(pitch, str):
            self.position = POSITIONS[pitch]
            if perspective is None:
                if "#" in pitch:
                    perspective = "#"
                elif "b" in pitch:
                    perspective = "b"
        else:
            raise ValueError("Invalid")
        self.perspective = perspective

    def __invert__(self):
        if self.perspective == "#":
            return Note(self.position, "b")
        elif self.perspective == "b":
            return Note(self.position, "#")
        return Note(self.position, None)

    def __add__(self, value):
        if not isinstance(value, int):
            return NotImplemented
        return Note((self.position + value) % 12, self.perspective)

    def __sub__(self, value):
        if not isinstance(value, int):
            return NotImplemented
        return Note((self.position - value) % 12, self.perspective)

    def __rshift__(self, other):
        return (self.position - other.position) % 12

    def __lshift__(self, other):
        return (other.position - self.position) % 12

    def __repr__(self):
        return f"Note({self.position}, {repr(self.perspective)})"

    def __str__(self):
        names = PITCHES[self.position]
        if len(names) == 1:
            return names[0]
        if self.perspective == "#":
            return names[0]
        elif self.perspective == "b":
            return names[1]
        else:
            return f"{names[0]}/{names[1]}"
