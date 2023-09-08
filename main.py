import math


class Vector:
    def __init__(self, magnitude, direction):
        # store magnitude and direction of vector
        self.magnitude = magnitude
        self.direction = direction

        # calculate change in x and y using magnitude and direction
        self.x = magnitude * math.sin(math.radians(direction))
        self.y = magnitude * math.cos(math.radians(direction))

    def __str__(self):
        # print the vector object
        return f'vector[magnitude={self.magnitude}, direction={self.direction}, x={self.x}, y={self.y}]'


def get_vector_from_input():
    print('Enter vector:')

    # get magnitude and direction of vector
    magnitude = float(input('magnitude: '))
    direction = float(input('direction (from the vertical): '))

    # create and return a vector using magnitude and direction
    return Vector(magnitude, direction)


def get_all_vectors_from_input():
    # array to store vectors in
    vectors = []

    while True:
        # add a new vector if answer 'y'
        print('Enter new co-planar vector?')
        ans = input('[Y/n]: ').upper()
        if ans == 'Y':
            vectors.append(get_vector_from_input())
        else:
            break

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


def main():
    vectors = get_all_vectors_from_input()
    resultant_vector = get_resultant_vector_from_vectors(vectors)
    print()
    print(f'resultant vector: {resultant_vector}')


if __name__ == '__main__':
    main()
