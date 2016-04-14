class NumberGuesser:
    """Guesses numbers based on the history of your input."""
    def __init__(self):
        self._guessed_numbers = None
    def numbers_were(self, guessed_numbers):
        self._guessed_number = guessed_numbers[0]
    def number_was(self, guessed_number):
        self._guessed_number = guessed_number
    def guess(self):
        return self._guessed_number
