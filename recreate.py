def hex_to_bytes(hex_string):
    return bytes.fromhex(hex_string)

def create_binary_file(hex_file_path, output_file_path):
    try:
        # Lecture du fichier hexadécimal
        with open(hex_file_path, 'r') as hex_file:
            hex_data = hex_file.read().replace('\n', '')

        # Conversion des valeurs hexadécimales en octets
        binary_data = hex_to_bytes(hex_data)

        # Écriture des octets dans le fichier binaire
        with open(output_file_path, 'wb') as bin_file:
            bin_file.write(binary_data)

        print(f"Le fichier '{output_file_path}' a été créé avec succès.")

    except FileNotFoundError:
        print("Le fichier hexadécimal spécifié n'existe pas.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

# Exemple d'utilisation
hex_file_path = 'hex-in-text.'  # Remplacez cela par le chemin de votre fichier hexadécimal
output_file_path = 'file-created.'

create_binary_file(hex_file_path, output_file_path)
