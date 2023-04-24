# Descrição(PT-BR)
Foram executados alguns comandos básicos de Docker em um terminal local conectando servidor web Nginx, criando um ambiente isolado para rodar o sistema operacional Ubuntu, bem como criando um banco de dados no ambiente MySQL Workbench.

# Description(ENG)
It were executed some Docker basic commands in a local terminal connecting the Nginx web server, creating an isolated envirinment for running Ubuntu operational system as well as creating a database on MySQL Workbench environment.

# Descripción(ESP)
Fueran ejecutados algunos comandos básicos de Docker en un terminal local conectando el servicio web Nginx, creando un entorno aislado para ejecutar el sistema operacional Ubuntu, bien como creando un banco de datos en el entorno MySQL Workbench.


Figura ilustrativa de um código em Dockerfile usando o Visual Studio. This picture shows a Dockerfile code using the Visual Studio. Figura que muestra un código Dockerfile usando el Visual Studio.


## Conteúdo do repositório(PT-BR)
+ 1.containers_ativos.png - Figura que mostra os containers ativos no diretório local.  
+ 2.imagens_criadas.png - Figura que mostra quais imagens estão no diretório local.
+ 3.primeiro_container_imagem.png - Figura que mostra como fazer o container hello-world.
+ 4.primeiro_container_imagem.png - Figura que mostra o container hello-world no diretório local.
+ 5.especificar_nome_container.png - Figura que mostra como renomear o container hello-world.
+ 6.especificar_nome_container.png - Figura que mostra os containers hello-world(original e renomeado) no diretório local.
+ 7.remover_container.png - Figura que mostra como remover o container original hello-world.
+ 8.container_ubuntu_iterativo.png - Figura que mostra como criar um container iterativo do Ubuntu rodando em ambiente isolado. 
+ 9.container_nginx_background.png - Figura que mostra como criar um container do servidor web Nginx rodando em background 
+ 10.acessar_nginx_habilitar_terminal.png - Figura que mostra como acessar o servidor web Nginx pelo terminal habilitado.
+ 11.porta_local_porta_container.png - Figura que mostra como vincular uma porta da máquina local com a porta do container Nginx.
+ 12.nginx_navegador.png - Figura que mostra como acessar o servidor Nginx pelo navegador.
+ 13.removendo_container_nginx.png - Figura que mostra como remover containers em execução.
+ 14.baixar_imagem_mysql_pro_docker.png - Figura que mostra como baixar imagem do MySQL para o ambiente Docker.
+ 15.criar_container_mysql.png - Figura que mostra como criar container de banco de dados MySQL no Docker. 
+ 16.verificar_conexao_mysql_workbench.png - Figura que serve para verificar a conexão com o MySQL Workbench.
+ 17.verificar_bancodados_mysql_workbench.png - Figura que serve para verificar no MySQL Workbench o banco de dados criado pelo terminal.
+ 18.parar_container_mysql_wil.png - Figura que mostra como parar o container de banco de dados mysql_wil.
+ 19.dockerfile_ubuntu_curl.png - Código em Dockerfile no Visual Studio que serve para criar uma imagem curl no Ubuntu. 
+ 20.dockerfile_ubuntu_curl.png - Figura que mostra como construir aplicação curl no Ubuntu.
+ 21.ubuntu_curl_image.png - Figura que mostra a imagem Ubuntu-curl no diretório local.
+ 22.curl_ubuntu_ambiente_isolado.png - Figura que mostra como rodar a aplicação curl no Ubuntu em ambiente isolado.
+ 23.construir_imagem.png - Figura que mostra quais imagens estão no diretório local.
+ 24.construir_imagem.png - Figura que mostra como construir nova imagem hello-world com a tag v1.
+ 25.login_dockerhub.png - Figura que mostra como fazer login no Dockerhub via terminal.
+ 26.fazendo_push_imagem.png - Figura que mostra como fazer push da imagem hello-world:v1 para o Dockerhub via terminal.
+ 27.conferir_dockerhub_push_da_imagem.png - Figura que mostra a imagem hello-world:v1 que foi subida para o Dockerhub.
+ 28.ultima_versao_imagem.png - Figura que mostra como converter a imagem hello-world:v1 para a última versão da imagem hello-world:latest.
+ 29.fazendo_push_imagem_latest.png - Figura que mostra como fazer o push da imagem hello-world:latest para o Dockerhub via terminal.
+ 30.conferir_dockerhub_push_image_latest.png - Figura que mostra a imagem hello-world:latest que foi subida para o Dockerhub.

## Repository content(ENG)
+ 1.containers_ativos.png - This picture shows the active containers in the local directory. 
+ 2.imagens_criadas.png - This picture shows wich images are in the local directory.
+ 3.primeiro_container_imagem.png - This picture shows how to make the hello-world container.
+ 4.primeiro_container_imagem.png - This picture shows the hello-world container in the local directory.
+ 5.especificar_nome_container.png - This picture shows how to rename the hello-world container.
+ 6.especificar_nome_container.png - This picture shows the hello-world(original and renamed) containers in the local directory.
+ 7.remover_container.png - This picture how to remove the original hello-world container.
+ 8.container_ubuntu_iterativo.png - This picture shows how to create an interactive container from Ubuntu running on isolated environment.
+ 9.container_nginx_background.png - This picture shows how to create a container on Nginx web server running in background.
+ 10.acessar_nginx_habilitar_terminal.png - This picture shows how to access the Nginx web server by the terminal enable. 
+ 11.porta_local_porta_container.png - This picture shows how to link a port from the local machine with the port of the Nginx container.
+ 12.nginx_navegador.png - This picture shows how to access the Nginx server by the browser.
+ 13.removendo_container_nginx.png - This picture shows how to remove the containers in execution.
+ 14.baixar_imagem_mysql_pro_docker.png - This picture shows how to download the MySQL image to Docker environment.
+ 15.criar_container_mysql.png - This picture shows how to create MySQL database container in the Docker.
+ 16.verificar_conexao_mysql_workbench.png - This picture serves to check the conection with the MySQL Workbench.
+ 17.verificar_bancodados_mysql_workbench.png - This picture serves to check on MySQL Workbench the database created by the terminal.
+ 18.parar_container_mysql_wil.png - This picture shows how to stop the mysql_wil database container.
+ 19.dockerfile_ubuntu_curl.png - The Dockerfile code made on Visual Studio app that serves to create a curl image on Ubuntu. 
+ 20.dockerfile_ubuntu_curl.png - This picture shows how to build curl application on Ubuntu.
+ 21.ubuntu_curl_image.png - This picture shows the Ubuntu-curl image in the local directory.
+ 22.curl_ubuntu_ambiente_isolado.png - This picture shows how to run the curl application on Ubuntu in isolated environment.
+ 23.construir_imagem.png - This picture shows which images are in the local directory.
+ 24.construir_imagem.png - This picture shows how to build a new hello-world image with v1 tag.
+ 25.login_dockerhub.png - This picture shows how to make login on Dockerhub site via terminal.
+ 26.fazendo_push_imagem.png - This picture shows how to make push of the hello-world:v1 image to Dockerhub site via terminal.
+ 27.conferir_dockerhub_push_da_imagem.png - This picture shows the hello-world:v1 that was uploaded to Dockerhub site.
+ 28.ultima_versao_imagem.png - This picture shows how to convert the hello-world:v1 image to the last version of the hello-world:latest image.
+ 29.fazendo_push_imagem_latest.png - This picture shows how to make the hello-world:latest image push to Dockerhub site via terminal.
+ 30.conferir_dockerhub_push_image_latest.png - This picture shows the hello-world:latest image that was uploaded to Dockerhub site.

## Contenido del repositório(ESP)
+ 1.containers_ativos.png - Figura que muestra los containers activos en el directório local. 
+ 2.imagens_criadas.png - Figura que muestra que imágenes están en el directório local.
+ 3.primeiro_container_imagem.png - Figura que muestra como hacer el container hello-world.
+ 4.primeiro_container_imagem.png - Figura que muestra el container hello-world en el directório local.
+ 5.especificar_nome_container.png - Figura que muestra como cambiar el nombre del container hello-world.
+ 6.especificar_nome_container.png - Figura que muestra los containers hello-world()original y nombre cambiado) en el directório local.
+ 7.remover_container.png - Figura que muestra como eliminar el container hello-world.
+ 8.container_ubuntu_iterativo.png - Figura que muestra como crear un container iterativo del Ubuntu ejecutando en ambiente aislado.
+ 9.container_nginx_background.png - Figura que muestra como crear un container del servicio web Nginx ejecutando en background.
+ 10.acessar_nginx_habilitar_terminal.png - Figura que muestra como acceder el servício web Nginx por el terminal habilitado.
+ 11.porta_local_porta_container.png - Figura que muestra como vincular una puerta de la máquina local con la puerta del container Nginx.
+ 12.nginx_navegador.png - Figura que muestra como acceder el servicio Nginx por el browser.
+ 13.removendo_container_nginx.png - Figura que muestra como eliminar los containers en ejecución.
+ 14.baixar_imagem_mysql_pro_docker.png - Figura que muestra como bajar imágen del MySQL para el ambiente Docker.
+ 15.criar_container_mysql.png - Figura que muestra como crear container de banco de datos MySQL en el Docker.
+ 16.verificar_conexao_mysql_workbench.png - Figura que sirve para verificar la conección con el MySQL Workbench.
+ 17.verificar_bancodados_mysql_workbench.png - Figura que sirve para verificar en el MySQL Workbench el banco de datos creado por el terminal.
+ 18.parar_container_mysql_wil.png - Figura que muestra como parar el container de banco de datos mysql_wil. 
+ 19.dockerfile_ubuntu_curl.png - Código en Dockerfile en el Visual Studio que sirve para crear una imágen curl en el Ubuntu.
+ 20.dockerfile_ubuntu_curl.png - Figura que muestra como construir una aplicación curl en el Ubuntu.
+ 21.ubuntu_curl_image.png - Figura que muestra la imágen Ubuntu-curl en el directório local.
+ 22.curl_ubuntu_ambiente_isolado.png - Figura que muestra como ejecutar la aplicación curl Ubuntu en ambiente aislado.
+ 23.construir_imagem.png - Figura que muestra que imágenes están en el directório local.
+ 24.construir_imagem.png - Figura que muestra como construir una nueva imágen hello-world con la tag v1.
+ 25.login_dockerhub.png - Figura que muestra como hacer login en el sitio Dockerhub via terminal.
+ 26.fazendo_push_imagem.png - Figura que muestra como hacer push de la imágen hello-world:v1 para el sitio Dockerhub via terminal.
+ 27.conferir_dockerhub_push_da_imagem.png - Figura que muestra la imágen hello-world:v1 que ha sido subida para el sitio Dockerhub. 
+ 28.ultima_versao_imagem.png - Figura que muestra como convertir la imágen hello-world:v1 para la ultima versión de la imágen hello-world:latest.
+ 29.fazendo_push_imagem_latest.png - Figura que muestra como hacer el push de la imágen hello-world:latest para el sitio Dockerhub via terminal.
+ 30.conferir_dockerhub_push_image_latest.png - Figura que muestra la imágen hello-world:latest que ha sido subida para el sitio Dockerhub.
