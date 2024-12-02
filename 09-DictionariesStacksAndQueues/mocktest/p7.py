import re
def f(array):
    counter=0
    pat=r'^(?=.*[a-z])(?=.*[\_])[a-z\d\_]{4,12}$'
    for name in array:
        if re.match(pat,name):
            counter+=1
    return counter


if __name__=='__main__':
    print(f(["uek","water_7_x","anna.may","a_b_c_d_e_f"]))