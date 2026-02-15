-- I included the code to create the table just in case if needed -- 

CREATE TABLE IF NOT EXISTS tickets (
  ticketno INT PRIMARY KEY,
  price DECIMAL(10,2) NOT NULL,
  validdate DATE NOT NULL
);

INSERT INTO tickets (ticketno, price, validdate) VALUES
(1111, 15.00, '2026-12-31'),
(2222, 25.00, '2026-12-31'),
(3333, 35.00, '2026-12-31'),
(4444, 10.00, '2026-03-15'),
(5555, 12.50, '2026-06-01'),
(6666, 18.00, '2026-08-20'),
(7777, 22.00, '2025-12-31'),
(8888, 30.00, '2026-11-01'),
(9999, 40.00, '2024-01-01'),
(1001, 9.99,  '2026-12-31'),
(1002, 8.50,  '2026-09-09'),
(1003, 14.25, '2026-10-10'),
(1004, 19.75, '2026-07-07'),
(1005, 16.00, '2026-05-05'),
(1006, 11.00, '2026-04-04');

