inpuser_in = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
fl_list = []
def flatten(n):
    for i in n :
        if type(i) == list:
            flatten(i)
        else:
            fl_list.append(i)

flatten(user_in)
print(fl_list)
