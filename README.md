# Supermarket-Cashier
## Welcome to Andi’s Supermarket Cashier Program
The Cashier Program is a system for self-service cashiers that enables them to input items, their prices, and the quantity ordered into a table, and subsequently provides the total amount to be paid.

### Program Flow:
1. Users create a transaction on the program, one transaction at a time.
2. Users add product name, quantity and price in a single input
3. Users might change the product name, quantity and price without affecting each other (they might change the name without the quantities)
4. Users might delete products from the transaction list
5. Users might reset all the transaction and start from the beginning

### Code Explanation
#### 1. Importing Libraries

!['Importing Libraries'](Docs/1.png)

These codes import necessary libraries to make the coding experience easier. Datetime library enables users to generate current date and time of the transaction. Pandas is used to make data tabulation easier. Psycopg2, sqlalchemy and urllib.parse are tools to support data transfer from python to database

#### 2. Creating object from Transaction Class

!['Creating object from Transaction Class'](Docs/2.png)

This code initialize an object created from ‘Transaction’ class. It prints concurrent number of transaction and the date when the transactions were made.

!['Creating object from Transaction Class2'](Docs/3.png)


#### 3. Adding product

!['Adding product'](Docs/4.png)

‘add_product’ method enables users to add product name with the quantities and price. The inputs of this method are the product name, quantity and price.. These input will be transformed into dictionary 

!['Adding product2'](Docs/5.png)

#### 4. Edit/customize order

There are several method which enable users to edit their order: update_product_name, update_product_qty, update_product_price, delete_product and reset_transaction.

##### update_product_name

!['update_product_name'](Docs/6.png)

Users can input what product to be changed and the new product name in this method. 

!['update_product_name2'](Docs/7.png)


##### update_product_qty

!['update_product_qty'](Docs/8.png)

Users can input the product which quanitites need to be updated and the expected quantity

!['update_product_qty2'](Docs/9.png)

##### update_product_price

!['update_product_price'](Docs/10.png)

Users can input the product and the new price update

!['update_product_price2'](Docs/11.png)

##### delete_product

!['delete_product'](Docs/12.png)

Users can delete one product at a time with this method from the transaction list

!['delete_product2'](Docs/13.png)

##### reset_transaction

!['reset_transaction'](Docs/14.png)

Users can delete whole product in transaction and start over. Number of total transaction will be reduced by 1 since there are less number of transaction now

!['reset_transaction2'](Docs/15.png)

#### 5. Checking Order

!['checking_order'](Docs/16.png)

This method transform dictionary into tabular data so user can see their summary of transaction better. 

!['checking_order2'](Docs/17.png)

#### 6. Checking Out

!['Checking_Out'](Docs/18.png)

This method applies discount to users transaction based on the predetermined rules. 

If the product total price > 500000, 7% discount is applied

If the product total price > 300000, 6% discount is applied

If the product total price > 200000, 5% discount is applied

All products within the transaction will be transferred to postgresql database using psycopg2 and sql alchemy library. In this code, connection strings are hidden so make sure to put the information in this format 

"postgresql://[user[:password]@][netloc][:port][/dbname]"

This is the table which has been inputted to pgAdmin 4

!['pgadmin4'](Docs/19.png)








