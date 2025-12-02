# lab02.py
# Lab 2 - Containters


def main():
    points = {}

    with open("score2.txt", "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) < 5:
                continue
            
            first = parts[2]
            last = parts[3]
            score = int(parts[4])
            name = f"{first} {last}"


            points[name] = points.get(name, 0) + score

    max_points = max(points.values())
    winner = [name for name, total in points.items() if total == max_points]

    print("Winners(s):")
    for winner in winner:
        print(f"{winner} with {max_points} points")

if __name__ == "__main__":
    main()