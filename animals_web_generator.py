import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """Structures animal infos in html format."""
    output = ""
    output += (
        "<li class='cards__item'>\n"
        f"<div class='card__title'>{animal_obj['name']}</div>\n"
        "<p class='card__text'>"
        f"<strong>Diet:</strong> {animal_obj['characteristics']['diet']}<br/>\n"
        f"<strong>Location:</strong> {animal_obj['locations'][0]}<br/>\n"
    )
    if animal_obj['characteristics'].get('type', 0) != 0:
        output += f"<strong>Type:</strong> {animal_obj['characteristics']['type']}<br/>\n</p></li>\n"
    else:
        output += "</p></li>\n"
    return output


def main():
    animals_data = load_data('animals_data.json')
    output = ""
    for animal in animals_data:
        output += serialize_animal(animal)

    with open("animals_template.html", "r") as f:
        data = f.read()

    data = data.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w") as f:
        f.write(data)


if __name__ == "__main__":
    main()