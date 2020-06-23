'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

example_list = [1, 2, 3, 4, 5, 6, 7]


# define the function here
def stats(list_of_number):
    for numb_ in list_of_number:
        # get the max number
        max_numb = max(list_of_number)
        print('the max number is: ', max_numb)
        # get the min munber
        min_numb = min(list_of_number)
        print('the min number is : ', min_numb)
        # get the sum
        sum_1 = sum(list_of_number)
        print("the sum is : ", sum_1)
        # get the average number
        average = sum_1 / len(list_of_number)
        print('the average is : ', average)


# call the function below here
stats(example_list)

