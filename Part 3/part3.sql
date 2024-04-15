CREATE TABLE clients (
  `client_id` int NOT NULL ,
  `entity_type` VARCHAR(255) NULL,
  `entity_year_established` date,
  PRIMARY KEY (`client_id`));
LOAD DATA LOCAL INFILE 'C:/Users/nhuma/Downloads/Technical Test/Clients.csv'
INTO TABLE clients
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS (`client_id`,`entity_type`,`entity_year_established`);

CREATE TABLE payments (
  `transaction_id` int NOT NULL ,
  `contract_id` int NOT NULL,
  `client_id` int NOT NULL,
  `payment_amt` decimal(13,4),
  `payment_code` varchar(255),
   `transaction_date` datetime,
  PRIMARY KEY (`transaction_id`));
LOAD DATA LOCAL INFILE 'C:/Users/nhuma/Downloads/Technical Test/Payments.csv'
INTO TABLE payments
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS (`transaction_id`, `contract_id`, `client_id`,`payment_amt`,`payment_code`,`transaction_date`);
ALTER TABLE payments
ADD FOREIGN KEY(client_id) REFERENCES clients(client_id);

SELECT client_id, sum(payment_amt), entity_type
from payments, clients
where clients.client_id = payments.client_id
group by clients.entity_type
order by sum(payment_amt) desc limit 20;

SELECT clients.client_id, entity_type, sum(payment_amt) as total_payment,
DENSE_RANK() OVER( ORDER BY entity_type ) as Ranking
FROM clients, payments
WHERE clients.client_id = payments.client_id and year(transaction_date) = 2018
GROUP BY client_id
order by total_payment desc limit 20;