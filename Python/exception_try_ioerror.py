try:
    open('myfile.txt')
except IOError as err:
    print("IOError")
    print(err)
except:
    print("catch all")
else:
    print("no exception")
finally:
    print("always runs")