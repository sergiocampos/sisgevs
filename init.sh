#!/bin/bash
echo '#### Criando imagem docker ####'
docker-compose up -d --build
sleep 10
echo '#### Copiando o insert.sql ####'
docker cp ./dados/sql_insert/insert_dados.sql sisgevs-db-1:/tmp
echo '##### Inserindo dados ####'
docker-compose exec db psql -U postgres -d postgres -f /tmp/insert_dados.sql
echo '#### limpando arquivos ####'
docker-compose exec db rm /tmp/insert_dados.sql
