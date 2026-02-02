import sqlite3

DB_PATH = "../banco/netguardian.db"

print("--NETGUARDIAN--\n")
print("\n--Escolha uma opção--")
print("\n1 - Consulta por IP")
print("\n2 - Consulta por ameaça")

def consultar_ip():
    ip = input("Digite o IP: ").strip()

    try:
        conexao = sqlite3.connect(DB_PATH)
        print(f"Resposta do banco: OK")
        cursor = conexao.cursor()
    except sqlite3.Error as e:
        print(f"Erro: {e}")

def consultar_ameaça():     