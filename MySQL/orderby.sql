use cadastro;
select nome,ano,descricao from cursos
where ano in ('2014','2016','2018')     # Vai ordenar o nome, o ano e a descriç
order by ano;
describe cursos;
