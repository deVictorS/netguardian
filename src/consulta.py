import sqlite3

DB_PATH = "../banco/netguardian.db"

class Consulta:

    @staticmethod
    def consultar_ip():
        ip = input("Digite o IP a ser verificado (x.x.x.x): ").strip()

        try:
            conexao = sqlite3.connect(DB_PATH)
            print(f"Resposta do banco: OK")
            cursor = conexao.cursor()

            query = "SELECT tipo_ameaca, data_coleta, fonte_dados FROM ameacas WHERE ip_address = ?"
            cursor.execute(query, (ip,))

            resultado = cursor.fetchone()

            print("-" * 35)
            if resultado:
                print("Pesquisando. . .\n")
                print(f"ALERTA! IP {ip} encontrado no banco!")
                print(f"\nTipo: {resultado[0]}")
                print(f"\nDetectado em: {resultado[1]}")
                print(f"\nFonte: {resultado[0]}")
            else:
                print(f"O {ip} não possui registros de ameaça")
            print("-" * 35)

            conexao.close()

        except sqlite3.Error as e:
            print(f"Erro: {e}")

    @staticmethod
    def consultar_ameaca():
        ameaca = input("Digite a ameaça a ser verificada Ou '0' para voltar: ").strip()
        if ameaca == "0":
            return

        try:
            conexao = sqlite3.connect(DB_PATH)
            print(f"Resposta do banco: OK")
            cursor = conexao.cursor()

            query = "SELECT ip_address,tipo_ameaca, data_coleta, status, fonte_dados FROM ameacas WHERE tipo_ameaca LIKE ?"
            cursor.execute(query, (f"%{ameaca}%",))

            resultado = cursor.fetchall()

            print("-" * 35)
            if resultado:
                print("Pesquisando. . .\n")
                print(f"Informações sobre {ameaca}\n")
                for linha in resultado:
                    print(f"IP {linha[0]}")
                    print(f"Ameaça: {linha[1]}")
                    print(f"Detectado em: {linha[2]}")
                    print(f"Status: {linha[3]}")
                    print(f"Fonte: {linha[4]}")
                    print("-" * 35)
            else:
                print(f"Nenhum registro encontrado")
            print("-" * 35)

            conexao.close()

        except sqlite3.Error as e:
            print(f"Erro: {e}")    

def menu():
    while True: 
        print("\n--NETGUARDIAN--")
        print("--Escolha uma opção--")
        print("1 - Consulta por IP")
        print("2 - Consulta por ameaça")
        print("0 - Sair")

        opcao = input("Selecione: ")

        if opcao == "1":
            Consulta.consultar_ip()

        elif opcao == "2":
            Consulta.consultar_ameaca()

        elif opcao == "0":
            print("Encerrando. . .")
            break
        
        else:
            print("Opção inválida, tente novamente")
            
menu()