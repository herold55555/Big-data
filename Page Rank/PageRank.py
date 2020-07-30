#Sheina Lussato 336089891
#Herold Tahar 342611274
import random


def playerPageRank(listOfPairs):
    solution = dict()
    children = dict()
    count_dict_part1 = dict()
    count_dict_part2 = dict()
    all_the_url = list()
    input_length = len(listOfPairs)
    for link in listOfPairs:
        x = link[0]
        children[x] = []
        if x not in all_the_url:
            all_the_url.append(x)
    for link in listOfPairs:
        x = link[0]
        y = link[1]
        if y not in children[x]:
            children[x].append(y)
        if y not in all_the_url:
            all_the_url.append(y)
        count_dict_part1[x] = 0
        count_dict_part1[y] = 0
        count_dict_part2[x] = 0
        count_dict_part2[y] = 0
        start_url = random.choice(all_the_url)
    for i in range(200000):
        if start_url not in children:
            next_url = random.choice(all_the_url)
            if i < 100000:
                count_dict_part1[next_url] = count_dict_part1[next_url] + 1
            else:
                count_dict_part2[next_url] = count_dict_part2[next_url] + 1
            start_url = next_url
        else:
            rand_int = random.randint(1, 100)
            if rand_int < 86:
                next_url = random.choice(children[start_url])
                if i < 100000:
                    count_dict_part1[next_url] = count_dict_part1[next_url] + 1
                else:
                    count_dict_part2[next_url] = count_dict_part2[next_url] + 1
                start_url = next_url
            else:
                next_url = random.choice(all_the_url)
                if i < 100000:
                    count_dict_part1[next_url] = count_dict_part1[next_url] + 1
                else:
                    count_dict_part2[next_url] = count_dict_part2[next_url] + 1
                start_url = next_url

    for link in all_the_url:
        my_list = list()
        step1 = count_dict_part1[link] / 100000
        step2 = count_dict_part2[link] / 100000
        my_list.append(step1)
        my_list.append(step2)
        solution[link] = my_list
    return solution
