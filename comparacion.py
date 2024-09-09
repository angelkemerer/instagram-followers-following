def compare_lists(following_file, followers_file, output_file):
    # Leer los archivos de texto y obtener las listas de nombres de perfil
    with open(following_file, 'r') as file:
        following_profiles = set(line.strip() for line in file)

    with open(followers_file, 'r') as file:
        followers_profiles = set(line.strip() for line in file)

    # Encontrar perfiles que están en following_profiles pero no en followers_profiles
    not_followed_back = following_profiles - followers_profiles

    # Escribir los resultados en el archivo de salida
    with open(output_file, 'w') as file:
        for profile in sorted(not_followed_back):
            file.write(profile + '\n')


# Uso del script
following_file = 'following.txt'
followers_file = 'followers.txt'
output_file = 'no_me_siguen.txt'
compare_lists(following_file, followers_file, output_file)
