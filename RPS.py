# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    # Strategy for Quincy
    quincy_sequence = ["R", "R", "P", "P", "S", "S"]
    if len(opponent_history) > 0:
        quincy_index = (len(opponent_history) - 1) % len(quincy_sequence)
        predicted_move = quincy_sequence[quincy_index]
        if prev_play == quincy_sequence[quincy_index]:
            return {"R": "P", "P": "S", "S": "R"}[predicted_move]

    # Strategy for Abbey (assuming pattern recognition)
    if len(opponent_history) >= 3:
        last_three = "".join(opponent_history[-3:])
        prediction = {
            "RRR": "S", "RRP": "S", "RRS": "P",
            "RPR": "R", "RPP": "S", "RPS": "P",
            "RSR": "R", "RSP": "P", "RSS": "S",
            "PRR": "S", "PRP": "S", "PRS": "P",
            "PPR": "R", "PPP": "S", "PPS": "P",
            "PSR": "R", "PSP": "P", "PSS": "S",
            "SRR": "S", "SRP": "S", "SRS": "P",
            "SPR": "R", "SPP": "S", "SPS": "P",
            "SSR": "R", "SSP": "P", "SSS": "S",
        }
        predicted_move = prediction.get(last_three, "R")
        return {"R": "P", "P": "S", "S": "R"}[predicted_move]

    # Strategy for Kris (frequency analysis)
    move_count = {"R": 0, "P": 0, "S": 0}
    for move in opponent_history:
        if move in move_count:
            move_count[move] += 1
    most_common_move = max(move_count, key=move_count.get)
    counter_move = {"R": "P", "P": "S", "S": "R"}[most_common_move]
    return counter_move

    # Strategy for Mrugesh (pattern detection)
    if len(opponent_history) >= 2:
        pattern = "".join(opponent_history[-2:])
        prediction = {
            "RR": "P", "RP": "S", "RS": "R",
            "PR": "S", "PP": "R", "PS": "P",
            "SR": "R", "SP": "S", "SS": "P",
        }
        predicted_move = prediction.get(pattern, "R")
        return {"R": "P", "P": "S", "S": "R"}[predicted_move]

    # Default move
    return "R"
