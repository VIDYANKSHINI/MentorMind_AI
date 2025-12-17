def aggregate(scores):
    avg = {k: sum(d[k] for d in scores)/len(scores) for k in scores[0]}
    avg["overall"] = round(
        0.25*avg["clarity"] +
        0.2*avg["engagement"] +
        0.15*avg["pace"] +
        0.15*avg["filler"] +
        0.25*avg["tech"], 2
    )
    return avg
