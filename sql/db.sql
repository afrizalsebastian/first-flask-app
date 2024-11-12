DROP DATABASE IF EXISTS inti_corp_pretest;
CREATE DATABASE inti_corp_pretest;

USE inti_corp_pretest;

DROP TABLE IF EXISTS employees;

CREATE TABLE employees (
  id INT PRIMARY KEY AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50),
  position VARCHAR(50),
  age INT NOT NULL,
  birthdate DATE NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(25) UNIQUE NOT NULL
);

INSERT INTO employees (first_name, last_name, email, phone_number, position, birthdate, age) VALUES
('Pegawai', 'Satu', 'pegawaisatu@mail.com', '082180802240', 'Software Engineer', '2002-10-04', 22),
('Pegawai', 'Dua', 'pegawaidua@mail.com', '082188882552', 'Backend Engineer', '2001-08-05', 23);
