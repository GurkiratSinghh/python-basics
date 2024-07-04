/* Triggers
Triggers are special types of stored procedures that are automatically executed or fired when certain events occur. They can be used to enforce business rules, maintain data integrity, and automatically update or validate data.

1. Trigger to Update Payment Status after an Order is Completed
Purpose: This trigger automatically updates the payment status to 'completed' once the corresponding order is marked as completed.

Explanation:

AFTER UPDATE: This specifies that the trigger will be executed after an update operation on the orders table.
FOR EACH ROW: This means the trigger will execute once for each row that is updated.
IF NEW.status = 'completed': Checks if the new status of the order is 'completed'.
UPDATE payment: Updates the status field in the payment table to 'completed' for the corresponding order.

DELIMITER //
CREATE TRIGGER update_payment_status_after_order
AFTER UPDATE ON orders
FOR EACH ROW
BEGIN
    IF NEW.status = 'completed' THEN
        UPDATE payment
        SET status = 'completed'
        WHERE order_id = NEW.order_id;
    END IF;
END //
DELIMITER ;

2. Trigger to Check Delivery Agent Availability before Inserting an Order
Purpose: This trigger checks if a delivery agent is available before assigning them to a new order.

Explanation:

BEFORE INSERT: This specifies that the trigger will be executed before an insert operation on the orders table.
DECLARE available_orders INT: Declares a variable to store the count of orders the delivery agent is currently assigned to.
SELECT COUNT(*) INTO available_orders FROM orders WHERE da_id = NEW.da_id: Counts the number of orders currently assigned to the delivery agent.
IF available_orders >= 1 THEN: Checks if the delivery agent is already assigned to at least one order.
SIGNAL SQLSTATE '45000': Raises an error if the delivery agent is unavailable.

DELIMITER //
CREATE TRIGGER check_delivery_agent_availability_before_order
BEFORE INSERT ON orders
FOR EACH ROW
BEGIN
    DECLARE available_orders INT;
    SELECT COUNT(*) INTO available_orders FROM orders WHERE da_id = NEW.da_id;
    IF available_orders >= 1 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Delivery agent is currently unavailable';
    END IF;
END //
DELIMITER ;

3. Trigger to Update Customer's Address after an Order is Placed
Purpose: This trigger updates the customer's address after an order is placed.

Explanation:

AFTER INSERT: This specifies that the trigger will be executed after an insert operation on the orders table.
UPDATE customers SET addr = NEW.addr WHERE customer_id = NEW.customer_id: Updates the customer's address to the new address provided in the order.

DELIMITER //
CREATE TRIGGER update_customer_address_after_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE customers
    SET addr = NEW.addr
    WHERE customer_id = NEW.customer_id;
END //
DELIMITER ;

TCL Commands
Transaction Control Language (TCL) commands manage transactions in a database to ensure data integrity. Transactions are sequences of operations performed as a single logical unit of work.

1. Save Command Permanently (Commit)
Purpose: This sequence of commands ensures that the changes made to the database are saved permanently.

Explanation:

START TRANSACTION: Begins a new transaction.
INSERT INTO ...: Inserts new records into the orders and payment tables.
COMMIT: Saves all changes made during the transaction permanently.

START TRANSACTION;
INSERT INTO orders (order_id, customer_id, da_id, total) VALUES (1006, 106, 1, 250);
INSERT INTO payment (payment_id, order_id, amount, mode, status) VALUES (4, 1006, 250, 'upi', 'completed');
COMMIT;

2. Rollback to Previous Command
Purpose: This sequence of commands demonstrates how to discard changes made during a transaction.

Explanation:

START TRANSACTION: Begins a new transaction.
INSERT INTO ...: Inserts a new record into the orders table.
ROLLBACK: Discards all changes made during the transaction.

START TRANSACTION;
INSERT INTO orders (order_id, customer_id, da_id, total) VALUES (1007, 107, 2, 300);
ROLLBACK;

3. Create Savepoint and Rollback to Savepoint
Purpose: This sequence of commands shows how to create a savepoint within a transaction and roll back to that savepoint if needed.

Explanation:

START TRANSACTION: Begins a new transaction.
INSERT INTO ...: Inserts new records into the orders and payment tables.
SAVEPOINT order_insert: Creates a savepoint named order_insert.
ROLLBACK TO order_insert: Rolls back the transaction to the order_insert savepoint, discarding subsequent changes.

START TRANSACTION;
INSERT INTO orders (order_id, customer_id, da_id, total) VALUES (1008, 108, 3, 350);
SAVEPOINT order_insert;
INSERT INTO payment (payment_id, order_id, amount, mode, status) VALUES (5, 1008, 350, 'credit', 'in process');
ROLLBACK TO order_insert;

Views
Views are virtual tables created by querying data from one or more tables. They simplify complex queries and enhance data security by restricting access to specific data.

1. View that Displays Customers with Their Corresponding Orders
Purpose: This view shows customer information along with their order details.

Explanation:

SELECT c.customer_id, c.customer_name, o.order_id, o.total: Selects customer ID, customer name, order ID, and total.
FROM customers c JOIN orders o ON c.customer_id = o.customer_id: Joins the customers and orders tables based on the customer ID.

CREATE VIEW CustomerOrders AS
SELECT c.customer_id, c.customer_name, o.order_id, o.total
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id;

2. Create or Replace View to Show Payment Details with Order and Customer Information
Purpose: This view combines payment details with related order and customer information.

Explanation:

SELECT p.payment_id, p.order_id, o.customer_id, c.customer_name, c.age, c.addr, p.amount, p.mode, p.status: Selects payment ID, order ID, customer ID, customer name, age, address, payment amount, mode, and status.
FROM payment p JOIN orders o ON p.order_id = o.order_id JOIN customers c ON o.customer_id = c.customer_id: Joins the payment, orders, and customers tables based on their respective relationships.

CREATE OR REPLACE VIEW PaymentOrderCustomerDetails AS
SELECT p.payment_id, p.order_id, o.customer_id, c.customer_name, c.age, c.addr, p.amount, p.mode, p.status
FROM payment p
JOIN orders o ON p.order_id = o.order_id
JOIN customers c ON o.customer_id = c.customer_id;

3. Drop View if It Exists
Purpose: This command removes a view if it exists in the database.

Explanation:

DROP VIEW IF EXISTS PaymentOrderCustomerDetails: Drops the PaymentOrderCustomerDetails view if it exists.

DROP VIEW IF EXISTS PaymentOrderCustomerDetails;

By implementing these triggers, TCL commands, and views, you can enhance the functionality and data integrity of your Zomato database. 
Triggers automate critical updates and checks, TCL commands manage transactions to ensure data consistency, and views simplify complex queries and restrict access to sensitive information.
*/
