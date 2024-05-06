public class Solution {
    private int[] bandage;
    private int health;
    private int[][] attacks;

    public int solution(int[] bandage, int health, int[][] attacks) {
        this.bandage = bandage;
        this.health = health;
        this.attacks = attacks;
        int answer = calc();
        return answer;
    }

    public int calc() {
        int casting = bandage[0];
        int hp1sec = bandage[1];
        int hpplus = bandage[2];
        int maxhp = health;

        int time = 1;

        for (int[] attack : attacks) {
            int attackTime = attack[0];
            int damage = attack[1];
            maxhp += (attackTime - time) * hp1sec;
            maxhp += (attackTime - time) / casting * hpplus;
            maxhp = Math.min(maxhp, health);
            maxhp -= damage;

            if (maxhp <= 0) {
                return -1;
            }
            time = attackTime + 1;
        }
        return maxhp;
    }
}
