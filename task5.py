def read_file(path):
    """
    (str) -> (set)
    Return set of lines from file
    """
    lst = set()
    f = open(path,'r')
    for one_line in f.readlines()[1:]:
        lst.add((one_line.split()[0],
                 float(one_line.split()[1]),
                 int(one_line.split()[2])))
    f.close()
    return lst
 
def votes_dict(lines_set,num_v):
    """
    (set) -> (dict)
    Return dict from set of lines
    if number of votes > num_v
    """
    dict_votes = {}
    for one_film in lines_set:
        if one_film[2] > num_v:
            if one_film[1] in dict_votes:
                dict_votes[one_film[1]].append(one_film[0])
            else:
                dict_votes[one_film[1]] = [one_film[0]]
    return dict_votes
def films_id(n,dict_votes):
    """
    (int,dict) -> (set)
    Return set of n films id with highest rating
    """
    chosen = 0
    chosen_list = set()
    while chosen <= n:
        max_rating = max(dict_votes)
        if len(dict_votes[max_rating]) >= n - chosen:
            print(len(dict_votes[max_rating]))
            chosen_list.update(set(dict_votes[max_rating][0:n - chosen]))
            break
        else:
            chosen += len(dict_votes[max_rating])
            chosen_list.update(set(dict_votes[max_rating]))
            dict_votes.pop(max_rating)
    return chosen_list
def write_films_id(set_films_id):
    """
    (set) -> None
    Write films_id to file
    """
    f = open('result.txt','w')
    for one_film in set_films_id:
        f.write(one_film + '\n')
    f.close()

def find_films_id(n,num_v):
    """
    (int,int) -> None
    """
    path = input("Enter path to file and its name ")
    write_films_id(films_id(n,votes_dict(read_file(path),num_v)))

