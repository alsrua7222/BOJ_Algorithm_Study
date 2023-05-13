def solution(my_string, indices):
    my_string = list(my_string)
    for indice in indices:
        my_string[indice] = "0"
    my_string = "".join(my_string).replace("0", "")
    return my_string