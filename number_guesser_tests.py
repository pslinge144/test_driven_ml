from number_guesser import NumberGuesser

def given_no_information_when_asked_to_guess_test():
    number_guesser = NumberGuesser()
    result = number_guesser.guess()
    assert result is None, "Then it should provide no result."

def given_one_datapoint_when_asked_to_guess_test():
    number_guesser = NumberGuesser()
    previously_chosen_number = 5
    number_guesser.number_was(previously_chosen_number)

    guessed_number = number_guesser.guess()

    assert type(guessed_number) is int, 'the answer should be a number'
    assert guessed_number == previously_chosen_number, 'the answer should be the previously chosen number.'