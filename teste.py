import pyodbc 
# STRING DE CONEXÃO AO BANCO
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
connection_string = (
    "DRIVER={SQL Server};"
    "SERVER=192.168.3.25;"
    "DATABASE=caio_db;"
    "ENCRYPT=no;"
    "UID=sa;"
    "PWD=SqlServer2022!;"
    "AUTOCOMMIT = True"
)

# EXIBE SE FOI CONECTADO
connection = pyodbc.connect(connection_string)
print("Connection success, done.")

# EXECUTANDO QUERYS
cursor = connection.cursor()

# SE EM SUA QUERY TIVER 'ASPAS' SIMPLES, USE "ASPAS" DUPLAS NO COMMAND ABAIXO, OU VICE-VERSA:
# command_create_db = f"""CREATE DATABASE caio_db3"""
# cursor.execute(command_create_db)
# cursor.commit()
# SE O COMANDO ENVIADO AO DATABASE FOR DE ALTERAÇÃO UTILIZAR O cursor.commit()
command_use_db = f"""USE caio_db"""
command_use_db = f"""GO"""
command_create_tbl = f"""
IF NOT EXISTS (
	SELECT 1
	FROM sys.tables
	WHERE name = 'vendas'
	AND type = 'U'
	)
BEGIN
   CREATE TABLE vendas (
     id_venda INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
     cliente VARCHAR(255), 
     produto VARCHAR(255), 
     data_venda DATE, 
     preco DECIMAL(12, 2), 
     quantidade INT,
     )
END"""
cursor.execute(command_create_tbl)
cursor.commit()


# VARIAVIES PARA ADD OS VALORES, NO COMANDO ABAIXO:
cliente = "Caio"
produto = "Computador"
data_venda = "GetDate()"
preco = 7680
quantidade = 1

#SE EM SUA QUERY TIVER 'ASPAS' SIMPLES, USE "ASPAS" DUPLAS NO COMMAND ABAIXO, OU VICE-VERSA:
command_user = f"""use caio_db"""
cursor.execute(command_user)
command = f"""INSERT INTO Vendas( cliente, produto, data_venda, preco, quantidade)
VALUES
    ('{cliente}', '{produto}', {data_venda}, {preco}, {quantidade})"""

cursor.execute(command)
cursor.commit()