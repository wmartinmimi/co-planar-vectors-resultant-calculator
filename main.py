import csv
import math
import os


class Vector:

    def __init__(self, magnitude, direction):
        # clear up args
        if magnitude < 0:
            magnitude = -magnitude
            direction += 180

        direction = direction % 360

        # store magnitude and direction of vector
        self.magnitude = magnitude
        self.direction = direction

        # calculate change in x and y using magnitude and direction
        self.x = magnitude * math.sin(math.radians(direction))
        self.y = magnitude * math.cos(math.radians(direction))

    def __str__(self):
        # print the vector object
        return f'magnitude: {self.magnitude}\ndirection: {self.direction}\nx: {self.x}\ny: {self.y}'


def get_vector_from_input():
    print('Enter vector details:')
    print('-' * 38)

    # get magnitude and direction of vector
    magnitude = float(input('magnitude: '))
    direction = float(input('direction (from the vertical): '))

    print()

    # create and return a vector using magnitude and direction
    return Vector(magnitude, direction)


def get_all_vectors_from_input():
    # array to store vectors in
    vectors = []

    while True:
        # add a new vector if answer 'y'
        print('Enter new co-planar vector?')
        ans = input('[Y/n]: ').upper()
        print()

        if ans == 'Y':
            vectors.append(get_vector_from_input())
        else:
            break

    # return the array of vectors
    return vectors


def get_all_vectors_from_csv():
    print("IMPORTANT: CSV format: [magnitude no unit], [direction in degrees no unit]")
    print("Enter path to csv file containing vectors:")
    path = input("> ")

    if not os.path.exists(path):
        print(f"Error: File {path} not found")
        exit(1)

    print()

    # array to store vectors in
    vectors = []

    # open and retrieve vectors from csv
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            # expected format: [magnitude no unit], [direction in degrees no unit]
            magnitude = float(row[0].strip())
            direction = float(row[1].strip())

            vectors.append(Vector(magnitude, direction))

    # return the array of vectors
    return vectors


def get_resultant_vector_from_vectors(vectors):
    # get the resultant change in x-axis and change in y-axis
    x = 0
    y = 0

    for vector in vectors:
        x += vector.x
        y += vector.y

    # get the magnitude and direction of the resultant vector
    magnitude = math.sqrt(x * x + y * y)
    direction = math.degrees(math.atan(x / y))

    # return the resultant vector
    return Vector(magnitude, direction)


def get_vectors():
    print('Choose input format:')
    print('  1. CSV')
    print('  2. Manual')
    print('Enter option number:')
    option = int(input('> ').strip())
    print()
    if option == 1:
        return get_all_vectors_from_csv()
    else:
        return get_all_vectors_from_input()


def main():
    print('Co-planar vectors resultant calculator')
    print('-' * 38 + '\n')

    vectors = get_vectors()

    resultant_vector = get_resultant_vector_from_vectors(vectors)

    print('resultant vector:')
    print('-' * 38)
    print(resultant_vector)


if __name__ == '__main__':
    main()
