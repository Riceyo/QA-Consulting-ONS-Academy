try:
    open('myfile.txt')
except OSError as err:
    print("OSError")
    print(err)
except:
    print("catch all")
else:
    print("no exception")
finally:
    print("always runs")

