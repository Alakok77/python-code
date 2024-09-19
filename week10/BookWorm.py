"""mod doc"""
def main():
    """doc"""
    box = int(input())
    max_time = 0
    time_list = []
    book = 0
    time =  0
    cnt_book = 0
    result = []
    for _ in range(box):
        max_time = int(input())
        book = int(input())
        for _ in range(book):
            time = int(input())
            time_list.append(time)
        time_list.sort()
        while max_time >= 0 and len(time_list) > 0:
            if max_time - time_list[0] < 0:
                break
            max_time -= time_list[0]
            cnt_book += 1
            time_list.pop(0)
        time_list.clear()
        result.append(cnt_book)
        cnt_book = 0
    for i in result:
        print(i)
main()
