
class Test101():
    def test1(self, x, *argv):
        print("First normal arg: ", x)

        for i in argv:
            print("Another", i)

    test1("Paypal", "Alibaba")
    test1("Tesla", "Volvo")
    test1("Yahoo", "Google", "Amazon", "Apple")
