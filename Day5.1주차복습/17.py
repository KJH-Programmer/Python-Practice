def check_duplicates(my_list):
    # 여기에 코드를 작성하세요
    a = set()
    b = set()
    for i in my_list:
        if i in a:
            b.add(i)
        else:
            a.add(i)
    print(f' Duplicates found: {b}')
                

duplicate_list = [1, 2, 2, 3, 4, 4, 4, 5]
check_duplicates(duplicate_list)
# 출력:
# Duplicates found: {2, 4}

