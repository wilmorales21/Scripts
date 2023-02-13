use basededados;
load data infile '/etc/mysql/mysqlfiles/planilha.csv'
into table informacoes
fields terminated by ','
lines terminated by '\r\n'
ignore 1 rows
(ID,produtoID,clienteID,Desconto,Preco,Quantidade,IDarmazenado,ddata);
select * from informacoes;