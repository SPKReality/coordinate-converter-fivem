import re

def convert_to_vector3(input_text):
    pattern = r"\{x = ([\d\.-]+),\s*y = ([\d\.-]+),\s*z = ([\d\.-]+)\}"
    matches = re.findall(pattern, input_text)
    vector3_entries = [f"vector3({x}, {y}, {z})," for x, y, z in matches]
    return "\n".join(vector3_entries)

def save_to_file(content, filename="output.txt"):
    with open(filename, "w") as file:
        file.write(content)


if __name__ == "__main__":
    print("Select the speed limit zone for these coordinates:")
    print("1. 60mph Zone")
    print("2. 80mph Zone")
    print("3. 120mph Zone")

    zone_choice = input("Enter the number corresponding to the speed limit zone: ").strip()

    zone_map = {
        "1": "60mph Zone",
        "2": "80mph Zone",
        "3": "120mph Zone"
    }

    if zone_choice not in zone_map:
        print("Invalid choice. Defaulting to '60mph Zone'.")
        zone_choice = "1"
    selected_zone = zone_map[zone_choice]

    print(f"You selected: {selected_zone}")
    print("Paste your coordinates in the format {x = value, y = value, z = value}. Type 'DONE' on a new line to finish.")
    
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "DONE":
            break
        lines.append(line)

    raw_input = "\n".join(lines)

    formatted_output = convert_to_vector3(raw_input)
    filename = f"output_{selected_zone.replace(' ', '_').lower()}.txt"
    save_to_file(formatted_output, filename)
    
    print("\nConverted coordinates:")
    print(formatted_output)
    print(f"\nThe output has been saved to '{filename}'.")
