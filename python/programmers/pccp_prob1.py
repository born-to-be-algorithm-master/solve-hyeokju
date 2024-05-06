def solution(bandage, health, attacks):
    casting = bandage[0]
    hp1sec = bandage[1]
    hpplus = bandage[2]
    maxhp = health

    time = 1

    for attackTime, damage in attacks:
        maxhp += (attackTime - time) * hp1sec
        maxhp += (attackTime - time) // casting * hpplus
        maxhp = health if maxhp > health else maxhp
        maxhp -= damage

        if maxhp <= 0:
            return -1
        
        time = attackTime + 1

    answer = maxhp
    
    return answer
