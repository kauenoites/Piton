def bytes_to_mb(bytes):
    """Converte bytes para megabytes."""
    return bytes / (1024 ** 2)

def calculate_percentage(used_space, total_space):
    """Calcula a porcentagem de uso."""
    return (used_space / total_space) * 100

def generate_report(input_file, output_file):
    """Gera o relatório com base no arquivo de entrada."""
    users_data = []

    with open(input_file, 'r') as file:
        for line in file:
            username, space_used = line.split()
            users_data.append((username, int(space_used)))

    total_space = sum(space for _, space in users_data)
    average_space = total_space / len(users_data)

    with open(output_file, 'w') as report:
        report.write("ACME Inc.               Uso do espaço em disco pelos usuários\n")
        report.write("-" * 72 + "\n")
        report.write("Nr.  Usuário        Espaço utilizado     % do uso\n")

        for i, (username, space_used) in enumerate(sorted(users_data, key=lambda x: x[1], reverse=True), start=1):
            percentage_used = calculate_percentage(space_used, total_space)
            report.write("{:2d}    {:15s}   {:9.2f} MB          {:6.2f}%\n".format(i, username, bytes_to_mb(space_used), percentage_used))

        report.write("\nEspaço total ocupado: {:.2f} MB\n".format(bytes_to_mb(total_space)))
        report.write("Espaço médio ocupado: {:.2f} MB\n".format(bytes_to_mb(average_space)))

# Chama a função para gerar o relatório
generate_report("usuarios.txt", "relatorio.txt")
