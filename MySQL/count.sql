use cadastro;
select carga, count(nome) from cursos      # A função de agregação count vai contar quantos cursos tem a mesma carga horaria
group by carga;
