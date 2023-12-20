import os
import numpy as np
import pandas as pd
import re


def get_matrix(prompt):
    """
    Gets 3 lines of input from the user.
    For each line, it splits the input by spaces and adds the values into the array.
    After reading in 3 lines it returns the array.
    :param prompt: The message to print out with the input request
    :return: The string array containing the 3 lines of user input provided, as separated by a space
    """
    matrix_input = []
    matrix_input.append(input(prompt).split(" "))
    matrix_input.append(input("\t").split(" "))
    matrix_input.append(input("\t").split(" "))

    return matrix_input


def validate_matrix(matrix):
    """
    Determines if the input given by the user represents a valid 3x3 matrix.
    Note that we put everything in the same try block because either case of invalid input
    will throw the same exception.
    :param matrix: The array containing the user input in string form we want to validate
    :return: True, if the array given is a valid 3x3 matrix, False if not
    """
    try:
        # ensure it can properly be converted to a numpy array (this will automatically fail if
        # there are not the same number of elements in each row of the array, or there are values that are not floats)
        # However we also have to check the length and size afterward, because a 3x4 array could be given
        # (or a 3x Any number > 3)
        numpy_matrix = np.array(matrix).astype(np.float_)
        if len(numpy_matrix) > 3 or numpy_matrix.size != 9:
            return False
    except ValueError:
        return False
    return True


def validate_phone_number(phone_number):
    """
    Validates the phone number input by the user is in correct XXX-XXX-XXXX format. Returns True if valid, False if not.
    :param phone_number: The phone number (in string form) to verify
    :return: True, if the string contains a phone number in the format "XXX-XXX-XXXX"
    """
    # Regex that looks for 3 numbers followed by a dash, followed by 3 more numbers and a dash, and then 4 more numbers.
    pattern = re.compile(r"^[\d0-9]{3}-[\d0-9]{3}-[\d0-9]{4}$")
    if pattern.match(phone_number) is not None:
        return True
    else:
        return False


#
def validate_zip_code(zip_code):
    """
    Validates the zip code input by the user is in correct XXXXX-XXXX format.
    :param zip_code: The zip code (in string form) to validate
    :return: True if valid, False if not
    """
    pattern = re.compile(r"[\d0-9]{5}-[/d0-9]{4}$")
    if pattern.match(zip_code) is not None:
        return True
    else:
        return False


def print_matrix(matrix, prompt, is_2d=True, is_string_matrix=False):
    """
     Prints the specified prompt, if any, followed by the specified matrix out to the console
    :param matrix: The array containing the matrix to print out
    :param prompt: What message to print before the array, if any
    :param is_2d: whether the matrix is a one or two-dimensional array (defaults to true if not specified)
    :param is_string_matrix: whether the matrix contains strings or not. Defaults to false, used to determine how to
    format the values inside the matrix (will round floats but display the full string value)
    :return: Nothing
    """

    # if the matrix is 2d (multidimensional array), iterate over both rows and columns
    if is_2d:
        print(f"\t{prompt}")
        print()
        for row in matrix:
            print("", end="\t")
            for col in row:
                if is_string_matrix:
                    # if it's a string matrix, don't try to format the value
                    print(f"{col}", end=" ")
                else:
                    # otherwise cap it to 2 decimal places
                    print("{:.2f}".format(col), end=" ")
            print("\n", end="")
        print("")
    else:
        # otherwise it's a one-dimensional array, only iterate over a single row
        print(f"\t{prompt}", end=" ")
        for number in matrix:
            if is_string_matrix:
                # if it's a string matrix, don't try to format the value
                print(f"{number}", end=" ")
            else:
                # otherwise cap it to 2 decimal places
                print("{:.2f}".format(number), end=" ")

        print("")


def get_matrix_operation():
    """
    Gets the matrix operation selection from the user and returns it.
    :return : The selection input by the user
    """
    print("\tSelect a matrix operation from the list below:")
    print("\ta. Addition")
    print("\tb. Subtraction")
    print("\tc. Matrix Multiplication")
    print("\td. Element by element multiplication")
    print()
    selection = input("\t")
    return selection


def validate_matrix_operation_selection(selection):
    """
    Validates the operation selection from the list
    :param selection: The selection from user input
    :return :True if the selection is valid, false if not
    """
    return selection == 'a' or selection == 'b' or selection == 'c' or selection == 'd'


def add_matrices(first_matrix, second_matrix):
    """
    Adds two matrices, displays the result of the subtraction as well as the transpose and column and row means
    :param first_matrix: The first matrix to add, a numpy array
    :param second_matrix: The first matrix to add, a numpy array
    :return: Nothing
    """
    addition_result = np.add(first_matrix, second_matrix)
    result_transpose = np.transpose(addition_result)
    column_mean = np.mean(addition_result, axis=0)
    row_mean = np.mean(addition_result, axis=1)

    print_matrix(addition_result, "You selected addition. The results are:")
    print_matrix(result_transpose, "The Transpose is:")
    print("\tThe row and column mean values of the result are:")
    print_matrix(row_mean, "Row:", False)
    print_matrix(column_mean, "Column:", False)
    print()


def subtract_matrices(first_matrix, second_matrix):
    """
    Subtracts two matrices, displays the result of the subtraction as well as the transpose and column and row means
    :param first_matrix: The first matrix to add, a numpy array
    :param second_matrix: The first matrix to add, a numpy array
    :return: Nothing
    """

    subtraction_result = np.subtract(first_matrix, second_matrix)
    result_transpose = np.transpose(subtraction_result)
    column_mean = np.mean(subtraction_result, axis=0)
    row_mean = np.mean(subtraction_result, axis=1)

    print_matrix(subtraction_result, "You selected subtraction. The results are:")
    print_matrix(result_transpose, "The Transpose is:")
    print("\tThe row and column mean values of the result are:")
    print_matrix(row_mean, "Row:", False)
    print_matrix(column_mean, "Column:", False)
    print()


def multiply_matrices(first_matrix, second_matrix):
    """
    Multiplies two matrices, displays the result of the subtraction as well as the transpose and column and row means
    :param first_matrix: The first matrix to add, a numpy array
    :param second_matrix: The first matrix to add, a numpy array
    :return: Nothing
    """

    mult_result = np.subtract(first_matrix, second_matrix)
    result_transpose = np.transpose(mult_result)
    column_mean = np.mean(mult_result, axis=0)
    row_mean = np.mean(mult_result, axis=1)

    print_matrix(mult_result, "You selected multiplication. The results are:")
    print_matrix(result_transpose, "The Transpose is:")
    print("\tThe row and column mean values of the result are:")
    print_matrix(row_mean, "Row:", False)
    print_matrix(column_mean, "Column:", False)
    print()


def elt_by_elt_multiply_matrices(first_matrix, second_matrix):
    """
    Multiplies two matrices element-by-element, displays the result of the subtraction as well as the transpose and
    column and row means
    :param first_matrix: The first matrix to add, a numpy array
    :param second_matrix: The first matrix to add, a numpy array
    :return: Nothing
    """
    elt_by_elt_mult_result = np.multiply(first_matrix, second_matrix)
    result_transpose = np.transpose(elt_by_elt_mult_result)
    column_mean = np.mean(elt_by_elt_mult_result, axis=0)
    row_mean = np.mean(elt_by_elt_mult_result, axis=1)

    print_matrix(elt_by_elt_mult_result, "You selected element-by-element multiplication. The results are:")
    print_matrix(result_transpose, "The Transpose is:")
    print("\tThe row and column mean values of the result are:")
    print_matrix(row_mean, "Row:", False)
    print_matrix(column_mean, "Column:", False)
    print()


def main():
    # Enter main flow control loop for the game
    done = False
    while not done:
        print("***************** Welcome to the Python Matrix Application *****************")
        print("\tDo you want to play the Matrix Game?")
        user_choice = input("\tEnter Y for Yes or N for No\n\t")

        if user_choice == 'Y' or user_choice == 'y':
            phone_number = input("\tEnter your phone number (XXX-XXX-XXXX):\n\t")
            valid = validate_phone_number(phone_number)
            # If the initial phone number is not valid, if not, loop until the user enters a valid one
            while not valid:
                phone_number = input("\tYour phone number is not in correct format. Please renter:\n\t")
                valid = validate_phone_number(phone_number)

            zip_code = input("\tEnter your zip code + 4 (XXXXX-XXXX):\n\t")
            # And do the same for zip code
            valid = validate_zip_code(zip_code)
            while not valid:
                zip_code = input("\tYour zip code is not in correct format. Please renter:\n\t")
                valid = validate_zip_code(zip_code)

            # Gather first matrix
            first_matrix = get_matrix("\tEnter your first 3x3 Matrix:\n\t")
            valid = validate_matrix(first_matrix)
            # If validation fails, allow the user to enter it until it becomes valid
            while not valid:
                first_matrix = get_matrix("\tYour matrix was invalid, meaning it was not a 3x3 or contained "
                                          "something other than numbers. Enter your first 3x3 Matrix:\n\t")
                valid = validate_matrix(first_matrix)
            # Now that it has been confirmed valid, convert it to a numpy array as floats
            numpy_first_matrix = np.array(first_matrix).astype(np.float_)

            # Print the matrix back to the user
            print_matrix(first_matrix, "Your first 3x3 matrix is: ", is_string_matrix=True)

            # Now do the same for the second matrix
            second_matrix = get_matrix("\tEnter your second 3x3 Matrix:\n\t")
            valid = validate_matrix(second_matrix)
            # If validation fails, allow the user to enter it until it becomes valid
            while not valid:
                second_matrix = get_matrix("\tYour matrix was invalid, meaning it was not a 3x3 or contained "
                                           "something other than numbers. Enter your second 3x3 Matrix:\n\t")
                valid = validate_matrix(second_matrix)
            # Now that it has been confirmed valid, convert it to a numpy array as floats
            numpy_second_matrix = np.array(second_matrix).astype(np.float_)

            # Print the matrix back to the user
            print_matrix(second_matrix, "Your second 3x3 matrix is: ", is_string_matrix=True)

            # Select Matrix Operation
            selection = get_matrix_operation()
            valid = validate_matrix_operation_selection(selection)
            while not valid:
                print("\tInvalid operation selection. Please choose a valid matrix operation.")
                selection = get_matrix_operation()
                valid = validate_matrix_operation_selection(selection)

            # Do corresponding matrix operation
            if selection == 'a':
                add_matrices(numpy_first_matrix, numpy_second_matrix)
            elif selection == 'b':
                subtract_matrices(numpy_first_matrix, numpy_second_matrix)
            elif selection == 'c':
                multiply_matrices(numpy_first_matrix, numpy_second_matrix)
            else:
                # guaranteed this is the 'd' case since value was validated, and it was not a, b, or c
                elt_by_elt_multiply_matrices(numpy_first_matrix, numpy_second_matrix)
        elif user_choice == 'N' or user_choice == 'n':
            print("***************** Thanks for playing Python Numpy *****************")
            done = True
        else:
            print("Invalid input. Please enter Y for Yes, and N for No")


main()
