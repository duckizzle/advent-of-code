# part one
# score = []

# def calc_score(your_move, opponent_move):
#     global score

#     # rock vs paper

#     if your_move == "X" and opponent_move == "B":
#         score.append(1)

#     # paper vs scissors

#     if your_move == "Y" and opponent_move == "C":
#         score.append(2)

#     # scissors vs rock

#     if your_move == "Z" and opponent_move == "A":
#         score.append(3)

#     # rock vs scissors

#     if your_move == "X" and opponent_move == "C":
#         score.append(6)
#         score.append(1)

#     # scissors vs paper

#     if your_move == "Z" and opponent_move == "B":
#         score.append(6)
#         score.append(3)

# # rock vs paper

#     if your_move == "Y" and opponent_move == "A":
#         score.append(6)
#         score.append(2)

#     if your_move == "X" and opponent_move == "A":
#         score.append(3)
#         score.append(1)


#     if your_move == "Y" and opponent_move == "B":
#         score.append(3)
#         score.append(2)

#     if your_move == "Z" and opponent_move == "C":
#         score.append(3)
#         score.append(3)

# with open("advent_day2/fileinput.txt") as file:
#     for line in file:
#         line.strip()
#         moves = line.split(" ")
#         calc_score(opponent_move = moves[0].strip(), your_move = moves[1].strip())



# print(score)
# final_score = sum(score)
# print(final_score)

# part two 
score = []

def calc_score(your_move, opponent_move):
    global score

    # lose to paper (rock)

    if your_move == "X" and opponent_move == "B":
        score.append(1)

    # draw with scissors (scissors)

    if your_move == "Y" and opponent_move == "C":
        score.append(3)
        score.append(3)

    # win against rock (paper)

    if your_move == "Z" and opponent_move == "A":
        score.append(6)
        score.append(2)

    # lose to scissors (paper)

    if your_move == "X" and opponent_move == "C":
        score.append(2)

    # win vs paper (scissors)

    if your_move == "Z" and opponent_move == "B":
        score.append(6)
        score.append(3)

# draw vs rock

    if your_move == "Y" and opponent_move == "A":
        score.append(3)
        score.append(1)

    #lose against rock (scissors)

    if your_move == "X" and opponent_move == "A":
        score.append(3)

    #draw against paper
    if your_move == "Y" and opponent_move == "B":
        score.append(2)
        score.append(3)

    #win against scissors (rock)
    if your_move == "Z" and opponent_move == "C":
        score.append(6)
        score.append(1)

with open("advent_day2/fileinput.txt") as file:
    for line in file:
        line.strip()
        moves = line.split(" ")
        calc_score(opponent_move = moves[0].strip(), your_move = moves[1].strip())



print(score)
final_score = sum(score)
print(final_score)
