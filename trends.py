def trending(slst):
    occurrences = {}
    maxoccr = 0
    for phrase in slst:
        if phrase in occurrences:
            occurrences[phrase] += 1
            if occurrences[phrase] > maxoccr:
                maxoccr = occurrences[phrase]
        else:
            occurrences[phrase] = 0
    trends = []
    for key in occurrences.keys():
        if occurrences[key] == maxoccr:
            trends.append(key)
    ordered = []
    for phrase in slst:
        if phrase in trends and not phrase in ordered:
            ordered.append(phrase)
    return ordered
