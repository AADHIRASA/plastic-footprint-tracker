"""
Plastic Awareness Footprint Calculator
CS50x Final Project

This program asks the user a few questions about their daily
single-use plastic consumption and estimates the associated
CO2 footprint, plastic weight, and decomposition time.

It is meant as an EDUCATIONAL / AWARENESS tool for use in
plastic-awareness campaigns, not as a scientific measurement
instrument. Impact values are rounded, publicly known averages.
"""


# Estimated average environmental impact per single-use item.
# Values are simplified/rounded for educational awareness purposes only.
IMPACT_DATA = {
    "bottles": {
        "label": "Plastic bottles",
        "co2_g": 82.8,       # grams of CO2 to produce one bottle
        "weight_g": 25,       # grams of plastic per bottle
        "decompose_years": 450,
    },
    "bags": {
        "label": "Plastic bags",
        "co2_g": 10.0,
        "weight_g": 5,
        "decompose_years": 20,
    },
    "straws": {
        "label": "Plastic straws",
        "co2_g": 1.5,
        "weight_g": 0.4,
        "decompose_years": 200,
    },
    "cups": {
        "label": "Plastic cups / cutlery",
        "co2_g": 15.0,
        "weight_g": 8,
        "decompose_years": 50,
    },
    "packets": {
        "label": "Plastic packets / wrappers",
        "co2_g": 6.0,
        "weight_g": 3,
        "decompose_years": 100,
    },
}


def get_int(prompt):
    """Repeatedly ask the user for a non-negative whole number until valid."""
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return int(value)
        print("Please enter a whole number of 0 or more.")


def collect_usage():
    """Ask the user how many of each plastic item they used today."""
    print("\nLet's calculate today's single-use plastic footprint!\n")
    usage = {
        "bottles": get_int("How many single-use plastic bottles did you use today? "),
        "bags": get_int("How many plastic bags did you use today? "),
        "straws": get_int("How many plastic straws did you use today? "),
        "cups": get_int("How many plastic cups/cutlery items did you use today? "),
        "packets": get_int("How many plastic packets/wrappers did you use today? "),
    }
    return usage


def calculate_footprint(usage):
    """
    Given a dict of item counts, return a dict with per-item and total
    CO2 (grams), plastic weight (grams), and max decomposition time (years).
    """
    results = {}
    total_co2 = 0.0
    total_weight = 0.0
    max_decompose = 0
    total_items = 0

    for key, count in usage.items():
        data = IMPACT_DATA[key]
        co2 = count * data["co2_g"]
        weight = count * data["weight_g"]

        results[key] = {
            "label": data["label"],
            "count": count,
            "co2_g": co2,
            "weight_g": weight,
        }

        total_co2 += co2
        total_weight += weight
        total_items += count
        if count > 0:
            max_decompose = max(max_decompose, data["decompose_years"])

    results["total"] = {
        "items": total_items,
        "co2_g": total_co2,
        "weight_g": total_weight,
        "max_decompose_years": max_decompose,
    }
    return results


def generate_summary(results):
    """Turn the results dict into a readable summary string."""
    lines = ["\n===== Your Daily Plastic Footprint Summary =====\n"]

    for key, data in results.items():
        if key == "total":
            continue
        if data["count"] > 0:
            lines.append(
                f"{data['label']:<28} x{data['count']:<3} "
                f"-> {data['co2_g']:.1f} g CO2, {data['weight_g']:.1f} g plastic"
            )

    total = results["total"]
    lines.append("\n-------------------------------------------------")
    lines.append(f"Total items used today    : {total['items']}")
    lines.append(f"Estimated CO2 footprint   : {total['co2_g']:.1f} g")
    lines.append(f"Estimated plastic weight  : {total['weight_g']:.1f} g")

    if total["max_decompose_years"] > 0:
        lines.append(
            f"Longest decomposition time: up to {total['max_decompose_years']} years"
        )
    lines.append("-------------------------------------------------")

    if total["items"] == 0:
        lines.append("\nAmazing! You used zero single-use plastic today. Keep it up!")
    elif total["items"] <= 3:
        lines.append("\nGood effort! A few small swaps could get you to zero.")
    else:
        lines.append(
            "\nThat's a fair amount of single-use plastic. Try reusable "
            "alternatives tomorrow: a steel bottle, cloth bag, and metal "
            "straw can eliminate most of this footprint."
        )

    yearly_co2_kg = (total["co2_g"] * 365) / 1000
    lines.append(
        f"\nIf repeated every day, this adds up to about "
        f"{yearly_co2_kg:.1f} kg of CO2 in a year!"
    )

    return "\n".join(lines)


def save_report(summary, filename="plastic_report.txt"):
    """Save the summary text to a file. Returns the filename used."""
    with open(filename, "w") as f:
        f.write(summary)
    return filename


def main():
    usage = collect_usage()
    results = calculate_footprint(usage)
    summary = generate_summary(results)
    print(summary)

    choice = input("\nSave this report to a text file? (y/n): ").strip().lower()
    if choice == "y":
        filename = save_report(summary)
        print(f"Report saved as {filename}")


if __name__ == "__main__":
    main()
