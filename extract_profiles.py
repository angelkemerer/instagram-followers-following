import json


def extract_profiles_from_json(json_file, output_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    profiles = []

    # Verifica si el archivo JSON es una lista de objetos
    if isinstance(data, list):
        for item in data:
            string_list_data = item.get('string_list_data', [])
            for profile in string_list_data:
                profile_name = profile.get('value')
                if profile_name:
                    profiles.append(profile_name)

    # Guarda los nombres de perfil en el archivo de salida
    with open(output_file, 'w') as file:
        for profile in profiles:
            file.write(profile + '\n')


# Uso del script
input_json_file = 'followers.json'  # Reemplaza con el nombre de tu archivo JSON
output_txt_file = 'followers.txt'  # Nombre del archivo de salida

extract_profiles_from_json(input_json_file, output_txt_file)
