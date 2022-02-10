"""
    This file contains your final_strategy that will be submitted to the contest.

    You can only depend on "general-purpose" libraries - do not import or open any
    contest-specific files, like other Python or text files. All contest logic must
    be in this file.

    Remember to supply a unique PLAYER_NAME or your submission will not succeed.
"""

PLAYER_NAME = ''  # Change this line!


def final_strategy(score, opponent_score):
      def picky_piggy(score):
 
        digit = (142857//(10**(6-score%6)))%10
        if digit == 0:
            digit = 7
            return digit
        else:
            return digit
    
    def picky_piggy_strategy(score, opponent_score, cutoff=8, num_rolls=6):

        if picky_piggy(opponent_score) >= cutoff:
            return 0
        else:
            return num_rolls

        
    if score>=98:
        return 1
    elif score>=91:
        return 3
    elif picky_piggy_strategy(score,opponent_score) ==0:
        return 0
    else:
        return 5