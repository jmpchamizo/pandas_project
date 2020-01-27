import re


#Devuelve una lista de con booleanos: True si no se encuentran los strings que introducimos como parámetros
def is_not_this(*args, lst= []):
    result = [None]* len(lst)
    for i, _ in enumerate(lst):
        for e in args:
            result[i] = result[i] or (e == lst[i])
    return [not e for e in result]

#Devuelve una lista de con booleanos: True si se encuentran los strings que introducimos como parámetros
def is_this(*args, lst= []):
    result = [None]* len(lst)
    for i, _ in enumerate(lst):
        for e in args:
            result[i] = result[i] or (e == lst[i])
    return result


#Devuelve una lista de con booleanos: True si no se encuentran los strings que introducimos como parámetros en sus
#respectivas listas
#Ambas listas deben tener la misma longitud
def is_not_this_in_two_list(values1 = [], lst1= [], values2 = [], lst2 = []):
    r1 = is_not_this(*values1, lst=lst1)
    r2 = is_not_this(*values2, lst=lst2)
    return [(r1[i] and r2[i]) for i, _ in enumerate(r1)]

#Devuelve una lista de con booleanos: True si se encuentran los strings que introducimos como parámetros en sus
#respectivas listas
#Ambas listas deben tener la misma longitud
def is_this_in_two_list(values1 = [], lst1= [], values2 = [], lst2 = []):
    r1 = is_this(*values1, lst=lst1)
    r2 = is_this(*values2, lst=lst2)
    return [(r1[i] or r2[i]) for i, _ in enumerate(r1)]


#Devuelve una función que recibe como parámetro un string(texto) y si se encuentra exactamente el primer string(st1) en
#el texto lo intercambia por el segundo (st2)
def swap(st1, st2):
    return lambda x: st2 if (st1.lower() == x or st1.upper() == x or \
        " "+st1.lower() == x or " "+st1.upper() == x or \
        st1.lower()+" " == x or st1.upper()+" " == x) else x


def get_month(dat):
    res=re.findall(r"-\w{3}-", dat)
    if res:
        return res[0][1:-1]
    elif re.findall(r"-\w{4}-", dat) and re.findall(r"-\w{4}-", dat)[0][1:-1] == "Sept":
        return "Sep"
    elif re.findall(r"\w{3}-", dat):
        return re.findall(r"\w{3}-", dat)[0][:-1]
    elif re.findall(r"-\w{2}-", dat) and re.findall(r"-\w{2}-", dat)[0][1:-1] == "Ap":
        return "Apr"
    elif re.findall(r"\w{3}\s\d{4}", dat):
        return re.findall(r"\w{3}\s\d{4}", dat)[0][:-5]
    else:
        return dat


def get_month_from_case(case):
    months = [None,"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    res=re.findall(r"\.\d{2}\.\d{2}", case)
    if res:
        return months[int(res[0][1:-3])]
    elif re.findall(r"\d{4}\.\d{2}", case):
        return months[int(re.findall(r"\d{4}\.\d{2}", case)[0][5:])]
    else:
        return case



def get_season(dat):
    res=re.search(r"^Summer", dat)
    if res:
        return res[0]
    else:
        return dat


def mean_attacks(month_number, fatal):
    n = month_number.value_counts().count()
    result = [0]*n
    for i,_ in enumerate(month_number):
        for j in range(n):
            if j+1 == month_number[i]:
                result[j] += fatal[i]
    return result


def combine_list(lst1, lst2):
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Summer"]
    return [lst2[i] if lst1[i] != lst2[i] and \
            lst1[i] not in months and \
            lst2[i] in months \
            else lst1[i] for i,_ in enumerate(lst1)]

def mean_attacks_hemisphere(season, fatal):
    n = season.value_counts().count()
    result = [0]*n
    for i,e in enumerate(season):
        if "Fall" == season[i]:
            result[0] += fatal[i]
        elif "Spring" == season[i]:
            result[1] += fatal[i]
        elif "Summer" == season[i]:
            result[2] += fatal[i]
        elif "Winter" == season[i]:
            result[3] += fatal[i]
    return result