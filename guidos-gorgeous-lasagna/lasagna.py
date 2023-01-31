"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

EXPECTED_BAKE_TIME=40

#       equal to the time it takes to prepare a single layer
PREPERATION_TIME=2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME-elapsed_bake_time
#       and consider using 'PREPARATION_TIME' here

def preparation_time_in_minutes(number_of_layers):
    """
    Return preparation time in minutes
    :param number_of_layers: int the number of layers in the lasagna
    :return:  int how many minutes you would spend for preparation
    """
    return number_of_layers*PREPERATION_TIME
def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):
    """
    This function takes two numbers representing the number of layers & the time already spent
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    :param number_of_layers: int the number of layers in the lasagna
    :param elapsed_bake_time: int elapsed cooking time
    :return:  int total time elapsed (in in minutes) preparing and cooking
    """
    return preparation_time_in_minutes(number_of_layers)+elapsed_bake_time
    