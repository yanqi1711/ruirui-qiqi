class Solution:
    def judgeCircle(self, moves: str) -> bool:
        array = [moves.count("U"),moves.count("D"),moves.count("L"),moves.count("R")]
        return not bool((array[0] - array[1]) or (array[2] - array[3]))