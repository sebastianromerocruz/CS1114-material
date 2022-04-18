"""
Author: Sebastián Romero Cruz
NYU Tandon School of Engineering
CS-UY 1114
Spring 2022
"""
from enum import Enum


class Direction(Enum):
    """
    Determines direction in Arpeggiator method play()
    """
    UP = 0
    DOWN = 1


class Arpeggiator:
    ROOTS = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
    NOTE_TYPES = ('b', '#', '')
    INVALID_NOTES = ("B#", "Cb", "E#", "Fb")
    _ROOT_IDX = 0
    _MIN_NOTE_LEN = 1
    _UP_DIRECTIONS = 'Uu'
    _DOWN_DIRECTIONS = 'Dd'

    @staticmethod
    def _is_valid_note(note):
        """
        Returns True if parameter note is any permutation of ROOTS and NOTE_TYPE (in that order i.e. "A", "Bb", "F#",
        etc.); False otherwise.

        :param note: A str representing a musical note
        :return: True or False
        """
        if type(note) != str:
            raise TypeError("Notes must be str types.")

        if len(note) < Arpeggiator._MIN_NOTE_LEN:
            return False

        root, note_type = note[Arpeggiator._ROOT_IDX], note[Arpeggiator._ROOT_IDX + 1:]

        return root in Arpeggiator.ROOTS and \
               note_type in Arpeggiator.NOTE_TYPES and \
               root + note_type not in Arpeggiator.INVALID_NOTES

    def __init__(self):
        """
        The Arpeggiator class initialiser.
        """
        self.possible_notes = [root + note_type for root in Arpeggiator.ROOTS for note_type in Arpeggiator.NOTE_TYPES]

        self._notes = []
        self._direction = Direction.UP

    def add_note(self, note):
        """
        Appends a user-inputted valid note (see: _is_valid_note()) to the Arpeggiator object.

        :param note: A string representing a musical note
        :return: None
        """
        if not self._is_valid_note(note):
            print("WARNING: '{}' is not a valid note.".format(note))
            print("VALID NOTES: {}".format(
                ", ".join(note for note in self.possible_notes if note not in Arpeggiator.INVALID_NOTES)
            ), end="\n\n")
            return

        self._notes.append(note)
        print("Note '{}' added!\n".format(note))

    def play(self, direction=Direction.UP):
        """
        Prints a simple visualisation of an arpeggiator being played. For example, if the notes stored in the
        arpeggiator are Bb, A#, D, Fb, and G the visualisation will look like:

        ~Bb
        ~~~A#
        ~~~~~D
        ~~~G
        ~D#

        The user may also choose if the arpeggiator is to be played up or down.

        :param direction: An enum of type Direction
        :return: None
        """
        if (direction == Direction.DOWN and self._direction == Direction.UP) or \
                (direction == Direction.UP and self._direction == Direction.DOWN):
            self._notes.reverse()

        mid = len(self._notes) // 2

        for index in range(mid):
            print('~' * ((index + 1) * 2 - 1) + self._notes[index])

        if len(self._notes) % 2 == 1:
            print('~' * ((mid + 1) * 2 - 1) + self._notes[mid])

        for index in range(mid, 0, -1):
            print('~' * (index * 2 - 1) + self._notes[len(self._notes) - index])

    def __str__(self):
        return "Arpeggiator (notes: {})".format(
            ", ".join(note for note in self._notes)
        )


if __name__ == '__main__':
    arp = Arpeggiator()
    arp.add_note('Bb')
    arp.add_note("A#")
    arp.add_note('D')
    arp.add_note('Fb')
    arp.add_note('G')
    arp.add_note('D#')
    arp.add_note("Done")

    print(arp)

    arp.play()
