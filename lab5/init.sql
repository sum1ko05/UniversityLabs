CREATE TABLE IF NOT EXISTS orders(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    model VARCHAR(100) NOT NULL,
    amount INT,
    assembly_included TINYINT(1),
    delivery VARCHAR(50)
);
