def read_file(path):
    """
    (str) -> (list)
    Return list of lines from file (path to file)
    """
    lst = []
    f = open(path, "r", encoding='utf-8', errors='ignore')
    for i in range(14):
        f.readline()
    for line in f:
        lst.append(line.strip().split())
    f.close()
    return lst


def country_dict(lines_list, year):
    """
    (list) -> (dict)
    Return dict from list of lines with country as a key and name as value
    """
    dictionary = {}
    for item in lines_list:
        if "({})".format(year) in item:
            if item[-1] in dictionary.keys():
                dictionary[item[-1]].append(item[:-1])
            else:
                dictionary[item[-1]] = [item[:-1]]
    return dictionary


def country_num(dict_country):
    """
    (dict) -> (list)
    Return sorted list of tuple with country and number of films
    """
    lst = []
    for key, value in dict_country.items():
        lst.append((key, len(value)))
    lst.sort(key=lambda x: x[1], reverse=True)
    return lst


def write_films(film_list):
    """
    (list) -> Note
    Write country and number of films to file
    """
    with open("result.txt", "w") as f:
        for item in film_list:
            f.write("Country: {} | Number of films: {}".format(item[0], item[1]))
            f.write("\n")
    return None

def main(path, year):
    """
    (str, int) -> (None)
    Main function of the program. Contain calls of another functions
    """
    try:
        assert (type(year) is int)
        assert (year >= 0)
        f = read_file(path)
        dictionary = country_dict(f, year)
        lst = country_num(dictionary)
        write_films(lst)
    except AssertionError:
        print("Something went wrong. You caught an Error :D")


main("countries.list", 2007)
