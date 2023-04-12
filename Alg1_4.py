number_students = int(input())
variants = int(input())
number_line_Petya = int(input())
place_Petya = int(input())

if place_Petya == 1:
    number_place_Petya = number_line_Petya * 2 - place_Petya
    number_place_Vasya_after = number_place_Petya + variants
    number_place_Vasya_before = number_place_Petya - variants

else:
    number_place_Petya = number_line_Petya * 2
    number_place_Vasya_after = number_place_Petya + variants
    number_place_Vasya_before = number_place_Petya - variants


if number_place_Vasya_before > 0:
    if number_place_Vasya_before % 2 == 0:
        place_Vasya_before = 2
        number_line_Vasya_before = number_place_Vasya_before // 2

    else:
        place_Vasya_before = 1
        number_line_Vasya_before = number_place_Vasya_before // 2 + 1
    
    if number_place_Vasya_after <= number_students:
        if number_place_Vasya_after % 2 == 0:
            place_Vasya_after = 2
            number_line_Vasya_after = number_place_Vasya_after // 2
        else:
            place_Vasya_after = 1
            number_line_Vasya_after = number_place_Vasya_after // 2 + 1

        if (number_line_Petya - number_line_Vasya_before) < (number_line_Vasya_after - number_line_Petya):
            print(number_line_Vasya_before, place_Vasya_before)
        else:
            print(number_line_Vasya_after, place_Vasya_after)

    else:
        print(number_line_Vasya_before, place_Vasya_before)

    
else:
    if number_place_Vasya_after <= number_students:
        if number_place_Vasya_after % 2 == 0:
            place_Vasya = 2
            number_line_Vasya = number_place_Vasya_after // 2

        else:
            place_Vasya = 1
            number_line_Vasya = number_place_Vasya_after // 2 + 1

        print(number_line_Vasya, place_Vasya)

    else:
        print(-1)