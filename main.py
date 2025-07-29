def test_args_kwargs(*args, **kwargs):
    print("The positional parameters are: ",args)
    print("The keyword parameters are: ",kwargs)

test_args_kwargs(1, 2, 3, a=4, b=5)

    

