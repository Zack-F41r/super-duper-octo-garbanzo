CREATE DATABASE IF NOT EXISTS testdb;
USE testdb;

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- usuario / permisos (por si no se usan variables)
CREATE USER IF NOT EXISTS 'appuser'@'%' IDENTIFIED BY 'appuserpass';
GRANT ALL PRIVILEGES ON testdb.* TO 'appuser'@'%';
FLUSH PRIVILEGES;
