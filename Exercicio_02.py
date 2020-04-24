import sqlite3
conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute('''CREATE TABLE exercicio1_breno(id integer,nome text not null,email text,primary key (id) )'''
                )

c.execute("INSERT INTO exercicio1_breno VALUES (1,'BRENO GUSTAVO','breno@123.com')")

c.execute('''SELECT * 
                FROM sqlite_master AS m, pragma_table_info(m.name)
                WHERE tbl_name = 'exercicio1_breno'
            ''')

for row in c.fetchall():
    print('----------------- tabelas ----------------')
    print('Nomes dos campos: ', row[6])
    print('Primary Key: ', row[10])
    print('Permite nulo? : ', row[8])

conn.commit()
conn.close()
