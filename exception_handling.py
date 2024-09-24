try:
    name = 'arjun'
    a = 10
    total = 5 + 10
    # import asdf
    # k = int('as123')
    with open('asdf.txt', 'r') as brutal:
        content = brutal.read()
except TypeError:
    print('encountered type error')
except ImportError:
    print('facing problems while importing')
except IOError:
    print('IO error raised')
except:
    print('error happened')
else:
    print('there are no errors')
finally:
    print('i will execute no matter what')



