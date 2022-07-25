# write your code here
import random

operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y
        # '/':lambda x,y:x/y
    }
difficulty_description = {
    1:'simple operations with numbers 2-9',
    2:'integral squares of 11-29'
}
def get_difficutly():
    while True:
        difficulty_level= int(input('''Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29\n'''))
        if difficulty_level in [1,2]:
            return difficulty_level
        print('Incorrect format.')

def save(name, content):
    with open(name, 'a') as f:
        f.write(content)
def main():
    mark = 0
    difficulty = get_difficutly()

    if difficulty == 1:
        for i in range(5):
            a, sy, b = random.randint(2, 9), random.choice(list(operations.keys())), random.randint(2, 9)
            question = f'{a} {sy} {b}\n'
            while True:
                try:
                    answer = int(input(question))
                    break
                except:
                    print('Incorrect format.')
                    continue
            correct_answer = operations[sy](a, b)
            if correct_answer == answer:
                print('Right!')
                mark += 1
            else:
                print('Wrong!')


    else:
        for i in range(5):
            a = random.randint(11, 29)
            question = f'{a} \n'
            while True:
                try:
                    answer = int(input(question))
                    break
                except:
                    print('Incorrect format.')
                    continue
            correct_answer = a**2
            if correct_answer == answer:
                print('Right!')
                mark += 1
            else:
                print('Wrong!')
    #while True:
    save_results = input(f'Your mark is {mark}/5. Would you like to save the result? Enter yes or no.\n')
    #    if save_results in ['yes', 'YES', 'y', 'Yes', 'no', 'NO','n']:
    #        break
    if save_results[0].lower()=='y' and len(save_results)<=3:
        name = input("What is your name?\n")
        save('results.txt', f'{name}: {mark}/5 in level {difficulty} ({difficulty_description[difficulty]})\n')
        print('The results are saved in "results.txt"')




main()