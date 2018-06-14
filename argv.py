


def test101(x, *argv):
    print("First normal arg: ", x)

    for i in argv:
        print("Another", i)

test101("Tesla", "Volvo")
test101("Yahoo", "Google", "Amazon", "Apple")

