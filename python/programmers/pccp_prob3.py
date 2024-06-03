def solution(h1, m1, s1, h2, m2, s2):
    answer = 0

    initial_time = h1 * 3600 + m1 * 60 + s1
    final_time = h2 * 3600 + m2 * 60 + s2  

    if initial_time == 0 * 3600 or initial_time == 12 * 3600:
        answer += 1

    while initial_time < final_time:
        current_hour = initial_time / 120 % 360
        current_min = initial_time / 10 % 360
        current_sec = initial_time * 6 % 360

        if (initial_time + 1) / 120 % 360 == 0:
            next_hour = 360
        else:
            next_hour = (initial_time + 1) / 120 % 360

        if (initial_time + 1) / 10 % 360 == 0:
            next_min = 360
        else:
            next_min = (initial_time + 1) / 10 % 360

        if (initial_time + 1) * 6 % 360 == 0:
            next_sec = 360
        else:
            next_sec = (initial_time + 1) * 6 % 360

        if current_sec < current_hour and next_sec >= next_hour:
            answer += 1
        if current_sec < current_min and next_sec >= next_min:
            answer += 1
        if next_sec == next_hour and next_hour == next_min:
            answer -= 1

        initial_time += 1
    
    return answer
