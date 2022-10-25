def calc_sum(**kwargs):
    ax=0
    for n in kwargs:
        ax=ax+n
    return ax

print(calc_sum(1,2,3,45,6))