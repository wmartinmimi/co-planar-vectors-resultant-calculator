import main


def test():
    vectors = [main.Vector(28, 90), main.Vector(17, 24)]
    resultant_vector = main.get_resultant_vector_from_vectors(vectors)
    if int(resultant_vector.magnitude) == 38 and int(resultant_vector.direction) == 66:
        print('Test passed')
    else:
        print('Test failed')


test()
