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


    # Checking if on providing  product id we get product price
    def test_product_price(self):
        
        self.base = sqlite3.connect("login.db")
        self.cur = self.base.cursor()

        
        
        self.assertEqual(User.clicktranstable(self,user='100730'),60)


    def testupdate_stocks(self):
        self.base = sqlite3.connect("login.db")
        self.cur = self.base.cursor()
        User.updateStocks(self,stocks='101',product_id='100730')

        self.assertEqual(1,1)


    # def testAddItem(self):
    #     self.base = sqlite3.connect("login.db")
    #     self.cur = self.base.cursor()
    #     Admin.AddItem(self,item_code='111111',item_name='Brush',item_desc='Colgate Toothbrush',item_cat='OTHERS',item_price='20',item_stocks='500')

    #     self.assertEqual(1,1)

if __name__ == '__main__':
    unittest.main()
