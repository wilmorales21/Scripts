/*Selecionar a coluna produtoID e ddata da tabela informacoes
e filtrar dados por ano*/
select produtoID,ddata from informacoes
where ddata like '%%/%%/2018';
