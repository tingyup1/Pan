#1

season=('spring','summer','autumn','winter')
month_number=int(input("choose a month(1-12):"))
if 12<=month_number<3:
    print(season[3])
elif 3<=month_number<6:
    print(season[0])
elif 6<=month_number<9:
    print(season[1])
elif 9<=month_number<12:
    print(season[2])
elif month_number==12:
    print(season[3])


#2
