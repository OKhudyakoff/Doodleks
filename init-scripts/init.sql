-- Создаем пользователя, если он еще не существует
-- Создание пользователя
CREATE USER vizov WITH PASSWORD 'vizov';

-- Создание схемы
CREATE SCHEMA vizov;

-- Назначение привилегий на схему пользователю
GRANT ALL PRIVILEGES ON SCHEMA vizov TO vizov;

-- Установка схемы по умолчанию для пользователя
ALTER USER vizov SET search_path TO vizov;
