/*Contando a quantidade de um determinado produto registrado em 2018*/
select count(*) as 'Quantidade' from informacoes 
where produtoID = '003128f981470c3e5a2e7445e4a771cd3'
and ddata like '%%/%%/2018';