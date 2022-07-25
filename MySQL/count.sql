use cadastro;
select carga, count(nome) from cursos
group by carga;