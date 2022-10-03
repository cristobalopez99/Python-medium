def run():

    the_third = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    print(the_third)



if __name__ == '__main__':
    run()



#    my_dict = {}
#
#    for i in range(1,101):
#        if i % 3 != 0:
#            my_dict[i] = i**3

#    print(my_dict)    