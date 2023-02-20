import pyodbc

# CONEXAO AO DATABASE
connection_string = (
    "Driver={SQL Server};"
    "Server=localhost;"
    "Database=caio_db;"
)

# EXIBE SE FOI CONECTADO
connection = pyodbc.connect(connection_string)
print("Connection success, done.")

# EXECUTANDO QUERYS
cursor = connection.cursos()

# VARIAVIES PARA ADD OS VALORES, NO COMANDO ABAIXO:
id_venda = 2
cliente = "Caio"
produto = "Computer"
data_venda = "GetDate()"
preco = 7680
quantidade = 1


# SE EM SUA QUERY TIVER 'ASPAS' SIMPLES, USE "ASPAS" DUPLAS NO COMMAND ABAIXO, OU VICE-VERSA:
command = f"""INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
VALUES
    ({id_venda}, '{cliente}', '{produto}', {data_venda}, {preco}, {quantidade})"""

cursor.execute(command)

#CASO O COMANDO ENVIADO AO DATABASE FOR DE ALTERAÇÃO, EXECUTE O COMMIT:
cursor.commit()