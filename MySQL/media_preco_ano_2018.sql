/*Calculando a media da coluna preço do ano de 2018*/
select avg(Preco) from informacoes
where ddata like '%%/%%/2018';
