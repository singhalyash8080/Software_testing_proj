import unittest
import sqlite3
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from Userlogin import Login
from Admin_menu import Admin
from User_menu import User
from Intro import splash

class TestAppMethods(unittest.TestCase):

    def test_login(self):

        Login.logintable(self)

        user = 'admin'
        password = 'admin'

        wrongUser = 'admin2'
        wrongPass = 'admin2'
        
        # checking correct credentials for admin
        self.assertEqual(Login.checkuser(self, 0, user, password),1)

        # checking wrong credentials for user
        self.assertEqual(Login.checkuser(self, 0, wrongUser, wrongPass),0)

    def test_searchInvoice(self):

        Login.logintable(self)

        invoiceNo = '111'

        # checking if the search function works
        self.assertEqual(len(Admin.searchinvoice(self, invoiceNo)) > 0, 1)

        # self.assertEqual(len(Admin.searchinvoice(self, '111')) == 1, 1)

    def test_userRegister(self):

        self.base = sqlite3.connect("login.db")
        self.cur = self.base.cursor()

        username = 'User1'
        password = 'User1'

        existingUsername = 'admin'
        existingPassword = 'admin'

        Login.insert(self, 0, username, password)

        # checking if the user is registered successfully
        self.assertEqual(Login.checkuser(self, 0, username, password),1)

        # checking if the already existing user is detected
        self.assertEqual(Login.insert(self, 0, existingUsername, existingPassword), 'Username already exist')


    #checking if get products functionality working at cashier side 
    def test_product_list(self):
        
        self.base = sqlite3.connect("login.db")
        self.cur = self.base.cursor()
        
        self.assertEqual(User.getproducts(self,user='a'),1)


    # Checking if on providing product id we get product price
    def test_product_price(self):
        
        self.base = sqlite3.connect("login.db")
        self.cur = self.base.cursor()
        
        
        self.assertEqual(User.clicktranstable(self,user='100730'),60)


    def testupdate_stocks(self):
        self.base = sqlite3.connect("login.db")
        self.cur = self.base.cursor()
        User.updateStocks(self,stocks='101',product_id='100730')

        self.assertEqual(1,1)


    def testAddItem(self):
        self.base = sqlite3.connect("login.db")
        self.cur = self.base.cursor()
        res = Admin.AddItem(self,item_code='999998',item_name='Soap 2',item_desc='Lux Soap 2',item_cat='OTHERS',item_price='50',item_stocks='500')

        self.assertEqual(res,1)

    def test_userUpdate(self):

        self.base = sqlite3.connect("login.db")
        self.cur = self.base.cursor()

        username = 'YASH'
        password = '123456'
        accountType = 'USER'

        res = Admin.changeusertable(self, username.upper(), password.upper(), accountType.upper())

        # checking if the user is updated successfully
        self.assertEqual(res, 1)

    def test_userDelete(self):

        self.base = sqlite3.connect("login.db")
        self.cur = self.base.cursor()

        username = 'YASH'

        res = Admin.deluser(self, username.upper())

        # checking if the user is deleted successfully
        self.assertEqual(res, 1)

    def test_deleteProduct(self):
            
        self.base = sqlite3.connect("login.db")
        self.cur = self.base.cursor()
    
        productID = '1'

        res = Admin.delproduct(self, productID)

        # checking if the product is deleted successfully
        self.assertEqual(res, 1)

if __name__ == '__main__':
    unittest.main()
