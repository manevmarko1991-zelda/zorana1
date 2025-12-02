import csv

ZIPCODE_FILE = "zipcode.txt"


def load_zipcodes(filename):
    """Read zipcode.txt and return a list of dicts with the useful fields."""
    data = []
    with open(filename, "r", encoding="latin1", newline="") as f:
        reader = csv.reader(f)
        header = next(reader, None)  # read header if there is one

        for row in reader:
            # skip empty lines
            if not row:
                continue

            # 🔹 FIX ENCODING HERE (repair ThÃ¼ringen -> Thüringen etc.)
            fixed = [cell.encode("latin1").decode("utf-8", errors="ignore") for cell in row]

            # make sure we have at least 11 columns
            if len(fixed) < 11:
                continue

            # use FIXED here, not row
            entry = {
                "country":       fixed[0],
                "plz":           fixed[1],
                "city":          fixed[2],
                "state":         fixed[3],
                "state_code":    fixed[4],
                "district":      fixed[7],
                "district_code": fixed[8],
                "latitude":      fixed[9],
                "longitude":     fixed[10],
            }
            data.append(entry)
    return data


def search_by_plz(data, plz):
    matches = [e for e in data if e["plz"] == plz]

    if not matches:
        print("No entries found for this postal code.")
        return

    print(f"\nResults for PLZ {plz}:")
    for e in matches:
        print("----------------------------------------")
        print(f"City:           {e['city']}")
        print(f"State:          {e['state']} ({e['state_code']})")
        print(f"District:       {e['district']} (Nr. {e['district_code']})")
        print(f"Latitude:       {e['latitude']}")
        print(f"Longitude:      {e['longitude']}")
    print("----------------------------------------")


def search_by_city(data, city):
    matches = [e for e in data if e["city"].lower() == city.lower()]

    if not matches:
        print("No entries found for this city.")
        return

    # Use first match for district info etc.
    sample = matches[0]
    plz_list = sorted({e["plz"] for e in matches})

    print(f"\nResults for city: {sample['city']}")
    print("----------------------------------------")
    print(f"State:          {sample['state']} ({sample['state_code']})")
    print(f"District:       {sample['district']}")
    print(f"District number:{sample['district_code']}")
    print("Postal codes:")
    for p in plz_list:
        print(f"  - {p}")
    print("----------------------------------------")


def search_by_district(data, district):
    matches = [e for e in data if e["district"].lower() == district.lower()]

    if not matches:
        print("No entries found for this district.")
        return

    sample = matches[0]
    plz_list = sorted({e["plz"] for e in matches})

    print(f"\nResults for district: {sample['district']}")
    print("----------------------------------------")
    print(f"District number: {sample['district_code']}")
    print(f"State:           {sample['state']} ({sample['state_code']})")
    print("Postal codes in this district:")
    for p in plz_list:
        print(f"  - {p}")
    print("----------------------------------------")


def search_by_district_number(data, district_number):
    matches = [e for e in data if e["district_code"] == district_number]

    if not matches:
        print("No entries found for this district number.")
        return

    sample = matches[0]
    plz_list = sorted({e["plz"] for e in matches})

    print(f"\nResults for district number: {district_number}")
    print("----------------------------------------")
    print(f"District:       {sample['district']}")
    print(f"State:          {sample['state']} ({sample['state_code']})")
    print("Postal codes in this district:")
    for p in plz_list:
        print(f"  - {p}")
    print("----------------------------------------")


def main():
    print("Loading zipcode data...")
    data = load_zipcodes(ZIPCODE_FILE)
    print(f"Loaded {len(data)} entries.\n")

    while True:
        print("What do you want to search by?")
        print("  1 - Postal code (PLZ)")
        print("  2 - City")
        print("  3 - District (Landkreis)")
        print("  4 - District number (Landkreisnummer)")
        print("  0 - Exit")

        choice = input("Your choice: ").strip()

        if choice == "0":
            print("Goodbye!")
            break

        elif choice == "1":
            plz = input("Enter postal code (PLZ): ").strip()
            search_by_plz(data, plz)

        elif choice == "2":
            city = input("Enter city name: ").strip()
            search_by_city(data, city)

        elif choice == "3":
            district = input("Enter district (Landkreis) name: ").strip()
            search_by_district(data, district)

        elif choice == "4":
            district_number = input("Enter district number (Landkreisnummer): ").strip()
            search_by_district_number(data, district_number)

        else:
            print("Invalid choice, please try again.")

        print()  # empty line
        again = input("Do you want to search again? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break
        print()  # extra empty line before next menu


if __name__ == "__main__":
    main()
