"""Functions to parse a file containing student data."""


def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:z
      - set[str]: a set of strings
    """
    #  TODO: replace this with your code

    houses = set()
    file = open(filename)
    # loop over each line in file
    for line in file:
        line = line.rstrip()  # remove extra characters
        line = line.split("|")  # split into a list

        a_house = line[2]  # assign variable to index

        if a_house == "":  # if there is no house, skip
            continue
        else:
            houses.add(a_house)  # add each house to houses

    return houses


def students_by_cohort(filename, cohort='All'):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """
    # grab file and open it
    # loop through the file line by line
    # rstrip file and split into list
    # make a full name var set to line[0] + line[1]
    # if line @ -1 will be set to var cohort
    # if cohort is == G or I , continue

    # if cohort is == 'Fall 2015' append name var to proper var
    # if cohort is == 'Spring 2016' append name var to proper var
    # if cohort is == 'Summer 2016' append name var to proper var
    # if cohort is == 'Winter 2016' append name var  to proper var
    # append all cohorts to students

    students = []
    file = open(filename)
    # loop over each line in file
    for line in file:
        first, last, _, _, cohort_name = line.rstrip().split("|")
        if cohort_name not in ("I", "G") and cohort in ("All", cohort_name):
            students.append(f"{first} {last}")

    return sorted(students)


def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """

    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []

    data = open(filename)

    # loop over each line in file
    for line in data:
        # assign variables to sections of the list
        first, last, house, _, cohort_name = line.rstrip().split(
            "|")  # strip extra charaters and split into list

        full_name = f"{first} {last}"

        if house:  # if person has a house then check for exact house name
            if house == "Dumbledore's Army":
                dumbledores_army.append(full_name)
            elif house == "Gryffindor":
                gryffindor.append(full_name)
            elif house == "Hufflepuff":
                hufflepuff.append(full_name)
            elif house == "Ravenclaw":
                ravenclaw.append(full_name)
            elif house == "Slytherin":
                slytherin.append(full_name)

        else:  # if person does not have a house, check if they are ghost or instructor
            if cohort_name == "G":
                ghosts.append(full_name)
            elif cohort_name == "I":
                instructors.append(full_name)
    # return a sorted list of each cohort
    return [sorted(dumbledores_army),
            sorted(gryffindor),
            sorted(hufflepuff),
            sorted(ravenclaw),
            sorted(slytherin),
            sorted(ghosts),
            sorted(instructors), ]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """
    # Input: filename
    # Output: a list of tuples. return all data in tuples

    all_data = []

    data = open(filename)

    for line in data:
        # create varaibles for line data
        first, last, house, advisor, cohort = line.rstrip().split("|")
        # create a tuple of profile information
        profile = (f"{first} {last}", house, advisor, cohort)
        # append profie information to list
        all_data.append(profile)

    return all_data


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Balloonicorn')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """

    # Given input of name and filesname
    # Return the person's cohort, return None if the person does not exist

    data = open(filename)

    for line in data:
        # create variables
        first, last, _, _, cohort = line.rstrip().split("|")
        # create fullname variable
        full_name = f"{first} {last}"
        # check to see that name entered matched name in list
        if name == full_name:
            return cohort
    # will return None if nothing is found
    return None

    # ALTERNATE SHORTER CODE
    # for full_name, _, _, cohort in all_data(filename):
    #     if full_name == name:
    #         return cohort


def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    # TODO: replace this with your code
    # input: filename
    # output: a set of strings containing last names of duplicates

    # create variable for dupe as a set
    # create variables for all_last_names in data
    # loop through the data
    # assign variables and split into list
    #  append last names to all_last_names
    # add all_last_names to set of dupes
    # return dupes

    dupes = set()
    seen = set()

    for full_name, _, _, _, in all_data(filename):
        last = full_name.split(" ")[-1]

        if last in seen:  # If we have seen the last name already
            dupes.add(last)  # add last to dupes

        seen.add(last)  # add all last to seen

    return dupes


def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """

    # TODO: replace this with your code


##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
