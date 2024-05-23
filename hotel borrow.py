def solution(book_time):
    max = 1
    book_time = sorted(book_time, key=lambda x: x[0])
    progress = []
    finish = []

    for i in range(len(book_time)):
        hours, minutes = map(int, book_time[i][1].split(':'))
        minutes += 10
        if minutes >= 60:
            hours += 1
            minutes -= 60
        book_time[i][1] = f'{hours:02}:{minutes:02}'

    # print(book_time)

    while book_time:
        now_book_time = book_time.pop(0)
        # print("---------------------")
        # print("sdfsdf:", now_book_time)
        
        if not progress:
            progress.append(now_book_time)
            continue

        for i in range(len(progress)):
            # print(progress[i])
            if progress[i][1] <= now_book_time[0]:
                # print("마 끝내줘라")
                finish.append(i)
        
        finish.sort(reverse=True)
        for i in finish:
            progress.pop(i)
        finish.clear()

        progress.append(now_book_time)

        if len(progress) > max:
            max = len(progress)

    return max