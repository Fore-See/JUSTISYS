# ForeSeeProject
The Best Team

/* Export CSV file */
SELECT *
FROM lawbank.money
INTO OUTFILE 'C:\Users\Davis\Desktop\money2.csv'
FIELDS ENCLOSED BY '"' TERMINATED BY ';' ESCAPED BY '"'
LINES TERMINATED BY '\r\n';

/* Import CSV file */
LOAD DATA INFILE 'D:/money.csv' 
INTO TABLE lawbank.money
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
