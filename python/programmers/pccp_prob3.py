def solution(h1, m1, s1, h2, m2, s2):
    answer = 0

    initial_time = h1 * 3600 + m1 * 60 + s1
    final_time = h2 * 3600 + m2 * 60 + s2  

    if initial_time == 0 * 3600 or initial_time == 12 * 3600:
        answer += 1

    while initial_time < final_time:
        current_hour_angle = initial_time / 120 % 360
        current_min_angle = initial_time / 10 % 360
        current_sec_angle = initial_time * 6 % 360

        if (initial_time + 1) / 120 % 360 == 0:
            next_hour_angle = 360
        else:
            next_hour_angle = (initial_time + 1) / 120 % 360

        if (initial_time + 1) / 10 % 360 == 0:
            next_min_angle = 360
        else:
            next_min_angle = (initial_time + 1) / 10 % 360

        if (initial_time + 1) * 6 % 360 == 0:
            next_sec_angle = 360
        else:
            next_sec_angle = (initial_time + 1) * 6 % 360

        if current_sec_angle < current_hour_angle and next_sec_angle >= next_hour_angle:
            answer += 1
        if current_sec_angle < current_min_angle and next_sec_angle >= next_min_angle:
            answer += 1
        if next_sec_angle == next_hour_angle and next_hour_angle == next_min_angle:
            answer -= 1

        initial_time += 1
    
    return answer
