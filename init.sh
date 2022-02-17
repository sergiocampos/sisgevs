#!/bin/bash
echo 'Criando imagem docker'
docker-compose up -d
echo 'Inserindo dados'
docker-compose exec db psql -U postgres -d postgres -f /insert/insert.sql