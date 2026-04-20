def load_visits(filename):
    visits = []

    with open(filename, "r") as file:
        for line in file:
            name = line.strip()   
            visits.append(name)

    return visits


def analyze_visits(visits):
    total_visits = len(visits)

    unique_visitors = set(visits)

    visit_count = {}

    for v in visits:
        visit_count[v] = visit_count.get(v, 0) + 1

    # most frequent visitor
    most_frequent = max(visit_count, key=visit_count.get)

    return total_visits, unique_visitors, visit_count, most_frequent