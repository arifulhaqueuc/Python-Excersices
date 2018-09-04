
# First you define the function
def test_arg_kwargs(arg1, arg2, arg3):
    print(arg1)
    print(arg2)
    print(arg3)


# play with *args
print("Playing with *args")
var_args1 = ("two", "DC", "Ohio")
print("Set of arguments1")
test_arg_kwargs(*var_args1)
var_args2 = ("Ramni", 2, "USA")
print("Set of arguments2")
test_arg_kwargs(*var_args2)


# play with **kwargs
print("\nPlaying with **kwargs")
kwargs = {"arg1": "Plainfield", "arg2": "Edison", "arg3": 8820}
test_arg_kwargs(**kwargs)
