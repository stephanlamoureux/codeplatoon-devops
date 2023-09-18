-- 1. List all the account names (first name and last name) along with their email addresses.
SELECT first_name, last_name, email FROM accounts;

-- 2. Find the total number of accounts in the dataset.
SELECT count(account_id) FROM accounts;

-- 3. Retrieve the accounts with a salary greater than $60,000.
SELECT * FROM accounts WHERE salary > 60000;

-- 4. List the unique states present in the dataset.
SELECT DISTINCT state FROM accounts;

-- 5. Find the average age of the account holders.
SELECT avg(age) FROM accounts;

-- 6. Show the accounts with a city of 'New York'.
SELECT * FROM accounts WHERE city = 'New York';

-- 7. Find the highest salary among the accounts.
SELECT first_name, last_name, MAX(salary) FROM accounts;

-- 8. List the accounts in descending order of their ages.
SELECT * FROM accounts ORDER BY age DESC;

-- 9. Retrieve the accounts with a password that starts with '1b9'.
SELECT * FROM accounts WHERE password like '1b9%';

-- 10. Count the number of accounts in each state and display the result in descending order of count.
SELECT state, COUNT(*) as num_per_state FROM accounts GROUP BY state ORDER BY num_per_state DESC;