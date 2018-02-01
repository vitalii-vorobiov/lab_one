def read_file(path):
    """
    (str) -> (set)
    Return set of lines from file
    """
    lst = set()
    f = open(path,'r')
    for one_line in f.readlines()[1:]:
        lst.add((one_line.split()[0],
                 one_line.split()[1],
                 one_line.split()[2]))
    f.close()
    return lst

def write_films_id(set_films_id):
    """
    (set) -> None
    Write films_id to file
    """
    f = open('result1.txt','w')
    for one_film in set_films_id:
        f.write(one_film + '\n')
    f.close()
def directors_dict(lines_set,flag):
    """
    (set,string) -> (dict)
    Return dict from set of lines with film id as key
    and list of directors or writers as value
    """
    dict_persons = {}
    if flag == 'directors':
        for one_film in lines_set:
            if one_film[1] != '\\N':
                dict_persons[one_film[0]] = one_film[1].split(',')
    else:
        for one_film in lines_set:
            if one_film[1] != '\\N':
                dict_persons[one_film[0]] = one_film[2].split(',')
    return (dict_persons)
def directors_max(dict_persons):
    """
    (dict) -> (list)
    Return list of films with highest number of persons
    """
    max_persons = 0
    out_lst = set()
    for one_film_name in dict_persons:
        if len(dict_persons[one_film_name]) >= max_persons:
            max_persons = len(dict_persons[one_film_name])
    for one_film_name in dict_persons:
        if len(dict_persons[one_film_name]) == max_persons:
            out_lst.add((one_film_name +':'+' '.join(dict_persons[one_film_name])))
    return out_lst
def find_directors_id(flag = 'directors'):
    """
    (string) -> None
    """
    path = input("Enter path to file and its name ")
    lines_set = read_file(path)
    dict_persons = directors_dict(lines_set,flag)
    out_set = directors_max(dict_persons)
    write_films_id(out_set)
        
