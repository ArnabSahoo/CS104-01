def average_score():
    total = 0
    count = int(input("How many test scores would you like to average? "))
    for i in range(count):
        score = int(input("Enter test score: "))
        total += score
    average = total / count
    print("The average for the test scores you entered is: ", average)

average_score()


