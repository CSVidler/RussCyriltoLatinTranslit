# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 23:14:47 2021

@author: chris
"""

# Computational Linguistics Essay Program:
# A Basic Program for Transliterating (Russian) Cyrillic Characters
# to the Latin Alphabet


# A function is defined here at the start of the program that ensures
# the user can only enter "Y" (for yes) or "N" (for no) when prompted.
# The function's if condition ensures that only these letters
# can be entered to break the infinite while loop within the function
# and continue the program.  This is used to control program flow
# towards the end of the program and to allow the user to loop back
# to various steps, enabling them to test multiple inputs
# and/or transliteration systems in single run of the program.
def y_or_n_input(prompt):
    """Restrict user input to return either "Y" or "N"."""
    while True:
        y_or_n_answer = input(prompt).upper()
        if (y_or_n_answer != "Y" and y_or_n_answer != "N"):
            print("Error: Please enter either Y or N to proceed.")
            continue
        else:
            break
    return y_or_n_answer


# To begin, instructions are printed here that introduce the program
# and describe its functionality to the user.
print("""Welcome to the Russian text transliteration program!

This program allows the user to input a string of text containing
Russian letters, and have this string returned with the Cyrillic
characters romanised to Latin equivalents according to
a transliteration system selected by the user.

Please note that this program is only designed to convert
the 33 letters that appear in the Russian alphabet. Certain Cyrillic
characters that feature in other languages, such as Ukrainian "ї"
or Serbian "ђ", will not be converted by this program,
and the systems used to convert compatible letters will handle these
according to conventions used in transliterating Russian (i.e. "г"
will become "g", rather than "h" as it is commonly romanised
from Ukrainian and Belarusian.)

Although there is no commonly accepted standard for romanising Russian,
a few official systems exist for use in various applications such as
linguistics research, producing machine readable documents or
transliterating place names on road signs. The user can have
their string of text transliterated according to one of three systems:

- The International Scholarly System (also known as the scientific
  transliteration system), which has been used in linguistics
  publications since the 19th century

- The ISO 9 standard for transliterating Cyrillic characters into Latin
  equivalents, in its most recent version from 1995, which is notable
  for its use of one-to-one character mappings (which make use
  of letters with diacritics) that also allow for reliable reverse
  transliteration.

  The ISO 9 system has also been adopted into the GOST (ГОСТ) standards
  used by the countries of the CIS as GOST 7.79-2000,
  with an "A" subsystem that is identical to the ISO standard
  and retains the one Cyrillic character to one Latin character
  mapping system. A subsystem "B" also exists that features mappings
  from single Cyrillic characters to multiple Latin characters,
  although this version is not covered by this program.

- The system stipulated by the International Civil Aviation
  Organization (ICAO) for machine readable travel documents,
  which has been used in Russian passports since 2013
  according to Order No. 320 of Russia's Federal Migratory Service.

These transliteration systems are summarised in a table of character
mappings on Wikipedia, which can be found here:
https://en.wikipedia.org/wiki/Romanization_of_Russian

More information on the International Scholarly System can be found at:
https://en.wikipedia.org/wiki/Scientific_transliteration_of_Cyrillic

More information on ISO 9:1995 can be found at:
https://www.iso.org/standard/3589.html

More information on the ICAO system can be found at:
https://www.icao.int/publications/Documents/9303_p3_cons_en.pdf

This program comprises the following steps:
    - Input the string for transliteration
    - Input the code for the transliteration system to use

After the final step, you will have the option of entering a code
for a different transliteration system to use on the same string,
or to start from scratch by entering a new string for processing.
Alternatively, you will also be able to exit the program.
""")

# The program's main loop is initiated here using a while loop
# in conjunction with a sentry variable called loop_string_selection.
# If the user does not enter "N" as a value for this variable
# at the end when asked if they wish to end the program,
# the program flow reverts back here and repeats the steps,
# allowing them to enter a new string for conversion.
loop_string_selection = ""
while loop_string_selection != "N":

    # The user's first prompt is printed here, which asks them to enter
    # a string of text for transliteration.  This could be,
    # for example, the Russian pangram "Разъяренный чтец эгоистично
    # бьёт пятью жердями шустрого фехтовальщика."
    input_string = input("Please enter a string for processing: ")

    # Since strings are immutable objects in Python, the string
    # is converted into a mutable list format for ease of modification
    # and processing.  The list() function breaks the string down
    # into a list with its characters (including spaces and punctuation
    # marks) stored as individual items.  This list is then assigned
    # to the string_as_list variable.
    string_as_list = list(input_string)

    # A secondary loop is initiated here, this time using
    # a sentry variable called loop_dict_selection.
    # If the user does not enter "N" as a value for this variable
    # at the end when asked if they wish to enter a new string
    # for conversion or end the program, the program flow
    # reverts back here to repeat the last step,
    # allowing them to select a new transliteration system
    # for converting the string that was previously entered.
    loop_dict_selection = ""
    while loop_dict_selection != "N":

        # Mapping dictionaries for the various transliteration systems
        # are established here, along with the codes that are used
        # to refer to them and to select them.  The relevant dictionary
        # is accessed later in the program to return Latin character
        # sets (in the value entry) for each identified Cyrillic
        # character (in the key entry).
        #
        # This dictionary has been created for the International
        # Scholarly System.  Note that since double quotation marks
        # are used for the strings here, a backslash is required to
        # escape the double quotation mark used to represent
        # the hard sign "ъ" in this system.  Also note that
        # this system uses one-to-two character mappings
        # in a few cases.
        scholarly_code = "SCHOLARLY"
        scholarly_dict = {"А": "A", "а": "a",
                          "Б": "B", "б": "b",
                          "В": "V", "в": "v",
                          "Г": "G", "г": "g",
                          "Д": "D", "д": "d",
                          "Е": "E", "е": "e",
                          "Ё": "Ë", "ё": "ë",
                          "Ж": "Ž", "ж": "ž",
                          "З": "Z", "з": "z",
                          "И": "I", "и": "i",
                          "Й": "J", "й": "j",
                          "К": "K", "к": "k",
                          "Л": "L", "л": "l",
                          "М": "M", "м": "m",
                          "Н": "N", "н": "n",
                          "О": "O", "о": "o",
                          "П": "P", "п": "p",
                          "Р": "R", "р": "r",
                          "С": "S", "с": "s",
                          "Т": "T", "т": "t",
                          "У": "U", "у": "u",
                          "Ф": "F", "ф": "f",
                          "Х": "X", "х": "x",
                          "Ц": "C", "ц": "c",
                          "Ч": "Č", "ч": "č",
                          "Ш": "Š", "ш": "š",
                          "Щ": "Šč", "щ": "šč",
                          "Ъ": "\"", "ъ": "\"",
                          "Ы": "Y", "ы": "y",
                          "Ь": "'", "ь": "'",
                          "Э": "È", "э": "è",
                          "Ю": "Ju", "ю": "ju",
                          "Я": "Ja", "я": "ja"}

        # This dictionary has been created for the IS0 9:1995/
        # GOST 7.79-2000(A) system.  Note that since double quotation
        # marks are used for the strings here, a backslash is required
        # to escape the double quotation mark used to represent
        # the hard sign "ъ" in this system.  This system is notable
        # for consisting solely of one-to-one character mappings,
        # which would mean that text romanised with this system
        # would be quite easy to back-transliterate as well
        # using a similar method.
        ISO_9_code = "ISO9"
        ISO_9_dict = {"А": "A", "а": "a",
                      "Б": "B", "б": "b",
                      "В": "V", "в": "v",
                      "Г": "G", "г": "g",
                      "Д": "D", "д": "d",
                      "Е": "E", "е": "e",
                      "Ё": "Ë", "ё": "ë",
                      "Ж": "Ž", "ж": "ž",
                      "З": "Z", "з": "z",
                      "И": "I", "и": "i",
                      "Й": "J", "й": "j",
                      "К": "K", "к": "k",
                      "Л": "L", "л": "l",
                      "М": "M", "м": "m",
                      "Н": "N", "н": "n",
                      "О": "O", "о": "o",
                      "П": "P", "п": "p",
                      "Р": "R", "р": "r",
                      "С": "S", "с": "s",
                      "Т": "T", "т": "t",
                      "У": "U", "у": "u",
                      "Ф": "F", "ф": "f",
                      "Х": "H", "х": "h",
                      "Ц": "C", "ц": "c",
                      "Ч": "Č", "ч": "č",
                      "Ш": "Š", "ш": "š",
                      "Щ": "Ŝ", "щ": "ŝ",
                      "Ъ": "\"", "ъ": "\"",
                      "Ы": "Y", "ы": "y",
                      "Ь": "'", "ь": "'",
                      "Э": "È", "э": "è",
                      "Ю": "Û", "ю": "û",
                      "Я": "Â", "я": "â"}

        # This dictionary has been created for the ICAO system
        # for producing machine readable travel documents.
        # This system is notable for not using any diacritics,
        # so there is greater reliance on one-to-multiple character
        # mappings instead.  The hard sign "ъ" is transliterated
        # more unusually as "ie", while the soft sign "ь" is not
        # reflected in the transliteration at all in this case,
        # and so it returns an empty string (i.e. no character) here.
        ICAO_code = "ICAO"
        ICAO_dict = {"А": "A", "а": "a",
                     "Б": "B", "б": "b",
                     "В": "V", "в": "v",
                     "Г": "G", "г": "g",
                     "Д": "D", "д": "d",
                     "Е": "E", "е": "e",
                     "Ё": "E", "ё": "e",
                     "Ж": "Zh", "ж": "zh",
                     "З": "Z", "з": "z",
                     "И": "I", "и": "i",
                     "Й": "I", "й": "i",
                     "К": "K", "к": "k",
                     "Л": "L", "л": "l",
                     "М": "M", "м": "m",
                     "Н": "N", "н": "n",
                     "О": "O", "о": "o",
                     "П": "P", "п": "p",
                     "Р": "R", "р": "r",
                     "С": "S", "с": "s",
                     "Т": "T", "т": "t",
                     "У": "U", "у": "u",
                     "Ф": "F", "ф": "f",
                     "Х": "Kh", "х": "kh",
                     "Ц": "Ts", "ц": "ts",
                     "Ч": "Ch", "ч": "ch",
                     "Ш": "Sh", "ш": "sh",
                     "Щ": "Shch", "щ": "shch",
                     "Ъ": "Ie", "ъ": "ie",
                     "Ы": "Y", "ы": "y",
                     "Ь": "", "ь": "",
                     "Э": "E", "э": "e",
                     "Ю": "Iu", "ю": "iu",
                     "Я": "Ia", "я": "ia"}

        # The user's second prompt is printed here, with instructions
        # printed before the input prompt itself that ask the user
        # to enter the corresponding code for the transliteration
        # system to be used.  The variables that contain the strings
        # that will be matched against the user's input
        # are concatenated to the instruction string in this case.
        #
        # The input itself is framed within an infinite while loop
        # that restricts input in a similar way to the y_or_n_input()
        # function defined above: the user can only enter one
        # of the specified codes (with the upper() method applied,
        # to remove case sensitivity) to trigger the if condition
        # that will break out of the while loop and continue
        # the program.  If a non-matching string is entered,
        # the else condition will continue the loop until a valid
        # input is entered.
        while True:
            print("\nPlease enter the relevant code following the colon "
                  "for one of the transliteration systems below "
                  "for converting the text."
                  "\nInternational Scholarly System: "
                  + scholarly_code +
                  "\nISO 9:1995/GOST 7.79-2000(A): "
                  + ISO_9_code +
                  "\nICAO MRTD specification: "
                  + ICAO_code)
            input_code = input("Enter code: ")
            if (input_code.upper() == scholarly_code
               or input_code.upper() == ISO_9_code
               or input_code.upper() == ICAO_code):
                break
            else:
                print("The code entered was invalid. Please try again.")
                continue

        # With a valid input entered, a series of (el)if conditions
        # are defined that assign the relevant mapping dictionary
        # to the chosen_dict variable depending on the code
        # that was entered.
        if input_code.upper() == scholarly_code:
            chosen_dict = scholarly_dict
        elif input_code.upper() == ISO_9_code:
            chosen_dict = ISO_9_dict
        elif input_code.upper() == ICAO_code:
            chosen_dict = ICAO_dict

        # The crux of the program occurs here in the form of a list
        # comprehension expression that assigns the modified characters
        # of the string (along with any unchanged characters)
        # to a new variable named modified_list.  The expression itself
        # makes use of Python's get() method to access the chosen
        # dictionary and return the Latin equivalents
        # in this dictionary for any Russian Cyrillic characters
        # that appear.  The program does this by iterating
        # over each item in string_as_list, which in this
        # case is each character extracted from the original string.
        # Each item is assigned to a temporary variable, char,
        # for each iteration of the for loop.  By passing this char
        # variable as the first parameter for the get() method,
        # the method will return the value for any dictionary key
        # that matches the string contained in this variable
        # should this string be a Russian Cyrillic character, and add
        # this value to the new list.  The second parameter indicates
        # the value that should be returned if no dictionary key
        # is found, and in this case, the char variable is passed
        # again, meaning that the character will be simply be re-added
        # to the new list unmodified if no matching dictionary key
        # is found.  This creates a new list in the modified_list
        # variable with the same characters in the same order as the
        # string_as_list variable, but with only the Russian Cyrillic
        # characters changed.
        modified_list = [chosen_dict.get(char, char)
                         for char in string_as_list]

        # The items in modified_list are then combined back
        # into a single string using the join() method, with an empty
        # string as a separator to ensure that no spaces are inserted
        # between the characters.
        modified_string = "".join(modified_list)

        # Finally, the results of the program are printed:
        # The original string is printed for reference,
        # along with the modified string and the reference code
        # for the system that was used to transliterate it.
        print("\nOrginal string:\n" + input_string)
        print("Transliteration of string using the "
              + input_code.upper() + " system:\n"
              + modified_string)

        # With the final step of the program concluded, the user
        # is asked to enter "Y" or "N" according to the earlier
        # defined input function to determine whether they would
        # like to process the same string again with a different
        # system (i.e. revert to the beginning of the secondary
        # loop), or choose to enter a new string or exit the program
        # (i.e. exit the secondary loop and proceed to the end
        # of the main loop).
        loop_dict_selection = y_or_n_input("To process the same string again "
                                           "using a different "
                                           "transliteration system, "
                                           "please enter the letter Y."
                                           "\nTo process a different string "
                                           "or exit the program, "
                                           "please enter the letter N."
                                           "\nEnter Y/N: ")

    # Having entered "N" to exit the secondary loop above,
    # the user is asked to enter "Y" or "N" according to
    # the earlier defined input function to determine whether
    # they would like to enter a new string for processing
    # (i.e. revert to the beginning of the main loop) or exit
    # the program (i.e exit the main loop and proceed to the end
    # of the program).
    loop_string_selection = y_or_n_input("To enter a new string "
                                         "for processing, "
                                         "please enter the letter Y."
                                         "\nTo exit the program, "
                                         "please enter the letter N."
                                         "\nEnter Y/N: ")

# With the program's main loop ended, the user is simply prompted
# to press enter to end the program.
input("Thank you for trying out this program. "
      "Press enter to exit.")
