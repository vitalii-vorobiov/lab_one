def read_file(path):
    """
    (str) -> (list)
    Return list of lines from file that starts with key symbols
    """
    with open(path) as f:
        lst = [line.strip()for line in f if line.startswith(("NOVL", "BOOK", "ADPT"))]
    return lst


def author_dict(lines_list):
    """
    (list) -> (dict)
    Return dict from list of lines with author name as key a
    """
    lst = [line[line.find(":")+1:line.find('.')].strip() for line in lines_list]
    dct = {i:lst.count(i) for i in set(lst)}
    return dct


def author_set(n, dict_author):
    """
    (int, dict) -> (set)
    Return set of n author with highest references
    """    
    lst = sorted(dict_author.values(),reverse = True)[:n]
    set1 = {num for num in dict_author if dict_author.get(num) in lst}
    return set1


def write_author(author_set):
    """
    (set) -> None
    Write authors and number references to file
    """    
    with open("file1.txt", "w") as f:
        for i in author_set:
            f.write(i+"\n")


def find_literature(n):
    """
    (int) -> None
    Receives number of authors and writes top n authors in the file
    """  
    write_author(author_set(n,author_dict(read_file("literature.list"))))


find_literature(14)
