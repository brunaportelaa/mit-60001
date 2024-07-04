#Calculating what item is better to buy
scores = {}
def calculate_score(scores):
    done = False
    while not done:
        name = input('Qual é o nome do item?\n')
        vers = float(input('De zero dez, o quão versátil é o item?\n'))
        freq = float(input('De zero dez, com que frequência você acredita que vai usá-lo?\n'))
        tot = float(input('De zero dez, quantos dos itens inclusos acredita que valem a pena?\n'))
        subs = float(input('De zero dez, o quão substituível você acredita que ele é?\n'))
        check_exit = int(input('Envie 1 para obter resultado e 2 para avaliar novo item\n'))

        if check_exit == 1:
            done = True
        elif check_exit != 1 and check_exit !=2:
            print('Input inválido.')
            check_exit = input('Envie 1 para obter resultado e 2 para avaliar novo item')

        score = (vers + freq + tot)/3 - subs/4
        scores[name] = score
    max_value = max(scores.values())
    best = []
    for key, value in scores.items():
        print(f'{key} has a score of {value:.2f}')
        if value == max_value:
            best.append(key)
    print(f'The best itens to buy are: {best} with a maximum score of {max_value:.2f}')





calculate_score(scores)


