import random


def main():
    # Get the lists
    namelist = loadfile("names.txt")
    titlists = loadfile("titles.txt")

    # Generate 10 character names
    number_of_characters = 10
    characters = [''] * number_of_characters
    for count in range(10):
        characters[count] = generate_char(namelist, titlists)
        print(characters[count])

    # Write to a file
    dumpfile(characters)
    print('\nThe characters have been saved to characterName.txt.')


def loadfile(text_file):
    infile = open(text_file, 'r')
    array = infile.readlines()
    infile.close()
    for index in range(len(array)):
        array[index] = array[index].rstrip('\n')
    return array


def generate_char(names, ttls):
    char = ('{0} {1} {2}'.format(ttls[random.randrange(len(ttls))], names[random.randrange(len(names))], names[random.randrange(len(names))]))
    return char


def dumpfile(array):
    outfile = open('CharacterNames.txt', 'w')
    for item in array:
        outfile.write(item + '\n')
    outfile.close()


main()
