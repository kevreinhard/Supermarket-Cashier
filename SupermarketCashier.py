#!/usr/bin/env python
# coding: utf-8

# In[2]:


''' 

This code represents a class to provide transactional cashier system in a supermarket.
There are several necessary libraries such as datetime, pandas, psycopg, sqlalchemy.
Pandas is used to make data tabulation easier
psycopg2 and sqlalchemy are libraries to make connection/interaction with database
Kindly install these libraries to proceed

'''
#Import libraries
from datetime import datetime
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
#from urllib.parse import quote 

class Transaction():
    '''
    Transaction class contains every method to perform transactional cashier system.
    Each transaction must be represented by an object, for example
    
    trx_1 = Transaction()
    This means that we have created object "trx_1" out of Transaction() class.
    total_transactions is a counter of how much transactions held
    
    '''
    
    total_transactions = 0
    
    def __init__(self):
        ''' Inits all inherent attributes for an object made out of Transaction class'''
        self.product = {}
        Transaction.total_transactions += 1
        self.transaction_number = Transaction.total_transactions
        self.time = datetime.now().strftime("%A, %d %B %Y %H:%M:%S")
        print(f"Welcome to Andi's Supermarket! This is Transaction number {self.transaction_number} of your purchase on {self.time}")
        
    def add_product(self, product_name, product_qty, product_price):
        '''Add a key-value pair to item dictonary with product_name as a key,
            and list containing product_qty and product_price as value.
        Examples:
            >>> trx_1 = Transaction()
            
            >>> t1.add_item('Ketoprak', 3, 60000)
            You have succesfully added 3 ketoprak to the cart!
            {'ketoprak': [3, 20000]}
            
            >>> trx_1.add_product('Bakso',2,15000)
            You have succesfully added 2 bakso to the cart!
            {'ketoprak': [3, 20000], 'bakso': [2, 15000]}
            
        Args:
            product_name (str): Ordered product name
            product_qty (int): Ordered product qty
            product_price (int): Ordered product price (per pcs)
            
        Returns:
            product (dict): Dictionary with this format
                (product_name:[product_qty, product_price]).
                All product name is formatted to lower case and strip (no space between words)
        '''
        try:
            product_name = product_name.lower().replace('_',' ').strip()
            product_qty = int(product_qty)
            product_price = int(product_price)
            self.product[product_name] = []
            self.product[product_name].append(product_qty)
            self.product[product_name].append(product_price)
            print(f"You have succesfully added {product_qty} {product_name} to the cart!")
            return self.product
        except (ValueError, AttributeError, NameError):
            print('Kindly recheck your orders! Please input the proper format')
        
    def update_product_name(self, product_name, update_product_name):
        '''Changing dictionary key (product_name)
        Examples:
            >>> trx_1 = Transaction()
            
            >>> t1.add_item('Ketoprak', 3, 60000)
            You have succesfully added 3 ketoprak to the cart!
            {'ketoprak': [3, 20000]}
            
            >>> trx_1.add_product('Bakso',2,15000)
            You have succesfully added 2 bakso to the cart!
            {'ketoprak': [3, 20000], 'bakso': [2, 15000]}
            
            >>> trx_1.update_product_name('Ketoprak','kentang')
            You have succesfully changed ketoprak to kentang!
            {'bakso': [2, 15000], 'kentang': [3, 20000]}
        Args:
            product_name (str): Product key/name which need to be changed
            update_product_name (str): The new product name
            
        Returns:
            product (dict): Updated dictionary
            (update_product_name:[product_qty, product_price]).
                
        '''
        try:
            product_name = product_name.lower().replace('_',' ').strip()
            update_product_name = update_product_name.lower().replace('_',' ').strip()
            self.product[update_product_name] = self.product.pop(product_name)
            print(f"You have succesfully changed {product_name} to {update_product_name}!")
            return self.product
        except KeyError:
            print(f'You have not put {product_name} into your transactions. Please check again!')
    
    def update_product_qty(self, product_name, update_product_qty):
        '''
        Changing dictionary value (product_qty)
        Examples:
            >>> trx_1 = Transaction()
            
            >>> t1.add_item('Ketoprak', 3, 60000)
            You have succesfully added 3 ketoprak to the cart!
            {'ketoprak': [3, 20000]}
            
            >>> trx_1.add_product('Bakso',2,15000)
            You have succesfully added 2 bakso to the cart!
            {'ketoprak': [3, 20000], 'bakso': [2, 15000]}
            
            >>> trx_1.update_product_name('Ketoprak','kentang')
            You have succesfully changed ketoprak to kentang!
            {'bakso': [2, 15000], 'kentang': [3, 20000]}
            
            >>> trx_1.update_product_qty('kentang',5)
            kentang quantities has successfully updated
            {'bakso': [2, 15000], 'kentang': [5, 20000]}
            
        Args:
            product_name (str): Product key/name which need to be changed
            update_product_qty (str): The new product quantity
            
        Returns:
            product (dict): Updated dictionary
            (product_name:[update_product_qty, product_price]).
    
        '''
        try:
            product_name = product_name.lower().replace('_',' ').strip()
            update_product_qty = int(update_product_qty)
            self.product[product_name][0] = update_product_qty
            print(f'{product_name} quantities has successfully updated')
            return self.product
        except (TypeError, ValueError, NameError):
            print('Please check again your inputs!')
        except KeyError:
            print('The item that you want to change is not available')
    
    def update_product_price(self, product_name, update_product_price):
        '''
        Changing dictionary value (product_price)
        Examples:
            >>> trx_1 = Transaction()
            >>> t1.add_item('Ketoprak', 3, 60000)
            You have succesfully added 3 ketoprak to the cart!
            {'ketoprak': [3, 20000]}
            
            >>> trx_1.add_product('Bakso',2,15000)
            You have succesfully added 2 bakso to the cart!
            {'ketoprak': [3, 20000], 'bakso': [2, 15000]}
            
            >>> trx_1.update_product_name('Ketoprak','kentang')
            You have succesfully changed ketoprak to kentang!
            {'bakso': [2, 15000], 'kentang': [3, 20000]}
            
            >>> trx_1.update_product_qty('kentang',5)
            kentang quantities has successfully updated
            {'bakso': [2, 15000], 'kentang': [5, 20000]}
            
            >>> trx_1.update_product_price('Bakso',25000)
            bakso price has been changed to 25000
            {'bakso': [2, 25000], 'kentang': [5, 20000]}
            
        Args:
            product_name (str): Product key/name which need to be changed
            update_product_price (str): The new product price
            
        Returns:
            product (dict): Updated dictionary
            (product_name:[product_qty, update_product_price]).
    
        ''' 
        try:
            product_name = product_name.lower().replace('_',' ').strip()
            update_product_price = int(update_product_price)
            self.product[product_name][1] = update_product_price
            print(f'{product_name} price has been changed to {update_product_price}')
            return self.product
        except (TypeError, ValueError, NameError):
            print('Please check again your inputs!')
        except KeyError:
            print('The item that you want to change is not available')
    
    def delete_product(self, product_name):
        '''
        Remove a key-value pair in product dictionary
        Examples:
            >>> trx_1 = Transaction()
            >>> t1.add_item('Ketoprak', 3, 60000)
            You have succesfully added 3 ketoprak to the cart!
            {'ketoprak': [3, 20000]}
            
            >>> trx_1.add_product('Bakso',2,15000)
            You have succesfully added 2 bakso to the cart!
            {'ketoprak': [3, 20000], 'bakso': [2, 15000]}
            
            >>> trx_1.update_product_name('Ketoprak','kentang')
            You have succesfully changed ketoprak to kentang!
            {'bakso': [2, 15000], 'kentang': [3, 20000]}
            
            >>> trx_1.update_product_qty('kentang',5)
            kentang quantities has successfully updated
            {'bakso': [2, 15000], 'kentang': [5, 20000]}
            
            >>> trx_1.update_product_price('Bakso',25000)
            bakso price has been changed to 25000
            {'bakso': [2, 25000], 'kentang': [5, 20000]}
            
            >>> trx_1.delete_product('kentang')
            kentang has been deleted
            {'bakso': [2, 25000]}
            
        Args:
            product_name (str): Product key/name which need to be deleted
            
        Returns:
            product (dict): Updated dictionary of the deleted product
    
        ''' 
        try:
            product_name = product_name.lower().replace('_',' ').strip()
            del self.product[product_name]
            print(f'{product_name} has been deleted')
            return self.product
        except KeyError:
            print('The product that you want to delete does not exist!')
    
    def reset_transaction(self, param1=None):
        '''
        Reset all products that have been appended on the Product dictionary
        Examples:
            >>> trx_1 = Transaction()
            >>> t1.add_item('Ketoprak', 3, 60000)
            You have succesfully added 3 ketoprak to the cart!
            {'ketoprak': [3, 20000]}
            
            >>> trx_1.add_product('Bakso',2,15000)
            You have succesfully added 2 bakso to the cart!
            {'ketoprak': [3, 20000], 'bakso': [2, 15000]}
            
            >>> trx_1.update_product_name('Ketoprak','kentang')
            You have succesfully changed ketoprak to kentang!
            {'bakso': [2, 15000], 'kentang': [3, 20000]}
            
            >>> trx_1.update_product_qty('kentang',5)
            kentang quantities has successfully updated
            {'bakso': [2, 15000], 'kentang': [5, 20000]}
            
            >>> trx_1.update_product_price('Bakso',25000)
            bakso price has been changed to 25000
            {'bakso': [2, 25000], 'kentang': [5, 20000]}
            
            >>> trx_1.reset_transaction()
            All products has been deleted
            {}
            
        Args: None
            
        Returns: 
            product = {} (Empty dictionary)
    
        ''' 
        self.product={}
        Transaction.total_transactions -= 1
        print('All products has been deleted')
        print(self.product)
        
    def check_order(self, param1=None):
        '''
        Convert the Product dictionary into a table
        
        Args: None
        
        Returns: df (dataframe) --> A tabulate data which contains Product, Quantity, Price, Total Price column
        
        '''
        try:
            dict_list = [{'Product': key, 'Quantity': val[0], 'Price': val[1], 'Total Price': val[0]*val[1]} for key, val in self.product.items()]
            self.df = pd.DataFrame(dict_list)
            print("Your transactions are ready below. Please check again!\n")
            print(self.df)
        except ValueError:
            print('Your transaction list is empty')
    
    def checkout(self, param1=None):
        '''
        Calculate final price of the products after discount adjustment on certain conditions
        
        Args: None
        
        Returns: 
            Final Price = Sum of Final_Price column on the Dataframe (df) as Final Price
            
            Transaction table =  Return a table consists of Product, Quantity, Price, Total_Price, Discount, Final_Price
        
        '''
        def calculate_discount(price):
            if price > 500_000:
                return 0.07 * price
            elif price > 300_000:
                return 0.06 * price
            elif price > 200_000:
                return 0.05 * price
            else:
                return 0
            
        try:
            self.df['Discount'] = self.df['Total Price'].apply(calculate_discount)
            self.df['Final_Price'] = self.df['Total Price'] - self.df['Discount']
            print(f"Your final price for this transaction is {self.df['Final_Price'].sum()}\n")
            print(self.df)
            
            conn_string = 'connection_string' #classified
            db = create_engine(conn_string)
            conn = db.connect()
            self.df.to_sql(name='andi_cashier', schema='public', con=conn, if_exists='replace', index=False)
            conn = psycopg2.connect(conn_string)
            conn.autocommit = True
            cursor = conn.cursor()
            
        except (ValueError, AttributeError):
            print('Your transaction list is empty!')

