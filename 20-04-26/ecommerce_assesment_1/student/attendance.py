import csv

def load_attendance(filename):
    data = []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            data.append({
                "name": row["name"],
                "days_present": int(row["days_present"]),
                "total_days": int(row["total_days"])
            })

    return data


def calculate_attendance_percentage(attendance):
    percentage_dict = {}

    for a in attendance:
        percent = (a["days_present"] / a["total_days"]) * 100
        percentage_dict[a["name"]] = percent

    return percentage_dict