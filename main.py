from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.properties import ListProperty, ObjectProperty, DictProperty
from kivymd.uix.label import Label
from kivymd.uix.dropdownitem import MDDropDownItem
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDFloatingActionButton, MDRectangleFlatIconButton
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivy.uix.scrollview import ScrollView
from kivymd.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.picker import MDDatePicker
from datetime import date
import sqlite3

Window.size = (300, 500)


class CommitteeApp(MDApp):
    previous_date = ObjectProperty()

    def build(self):
        screen = Screen()
        # code = Builder.load_string(helper_code)
        # screen.add_widget(code)
        layout = BoxLayout()

        self.bottom_bar = MDBottomNavigation()
        bottom_bar1  = Builder.load_string("""
MDBottomNavigationItem:
    name:'first'
    icon:'book'
            
    MDToolbar:
        id:toolbar
        text:"Monthly Overview"
        pos_hint:{"top":1}

    ScrollView:
        Screen:
            MDCard:
                size_hint: None, None
                size: "280dp", "180dp"
                pos_hint:{"center_x":0.5, "center_y":0.75}
                padding:"8dp"
                
                MDLabel:
                    text:"TITLE"
                
                MDSeparator:
                    height:"1dp"
                    
            MDCard:
                size_hint: None, None
                size: "280dp", "180dp"
                pos_hint:{"center_x":0.5, "center_y":0.25}
                padding:"8dp"
                
                MDLabel:
                    text:"TITLE"
                
                MDSeparator:
                    height:"1dp"
                    
            MDFloatingActionButton:
                icon:'plus'
                pos_hint:{"center_x":0.86, "center_y":0.1}

        """)

        #2nd tab starts here
        bottom_bar2 = MDBottomNavigationItem(name="table", icon="table")
        table = MDDataTable(rows_num=20, column_data=[
            ("S No.", dp(10)),
            ("Name", dp(26)),
            ("EMI", dp(15)),
            ("Amount Paid", dp(20)),
            ("Balance", dp(13))], row_data=[
            ("1", "", "", "", ""),
            ("2", "", "", "", ""),
            ("3", "", "", "", ""),
            ("4", "", "", "", ""),
            ("5", "", "", "", ""),
            ("6", "", "", "", ""),
            ("7", "", "", "", ""),
            ("8", "", "", "", ""),
            ("9", "", "", "", ""),
            ("10", "", "", "", ""),
            ("11", "", "", "", ""),
            ("12", "", "", "", ""),
            ("13", "", "", "", ""),
            ("14", "", "", "", ""),
            ("15", "", "", "", ""),
            ("16", "", "", "", ""),
            ("17", "", "", "", ""),
            ("18", "", "", "", ""),
            ("19", "", "", "", ""),
            ("20", "", "", "", ""),
        ])
        bottom_bar2.add_widget(table)
        #2nd Tab End

        # bottom_bar3 = MDBottomNavigationItem(name="edit", icon='account-edit')
        self.bottom_bar3 = Builder.load_string("""
MDBottomNavigationItem:
    name:"edit"
    icon:"account-edit"
    
    MDToolbar:
        title:"New Entry"
        pos_hint:{"top":1}
    
    BoxLayout:
        pos_hint:{"center_x":0.31, "center_y":0.75}
        size_hint_x:0.5
        size_hint_y:0.1
        MDLabel:
            text:"Name"
            font_style:'Body1'
    MDTextField:
        id:name
        pos_hint:{"center_x":0.6, "center_y":0.755}
        size_hint_x:None
        width:200
        hint_text:"Enter Name"
        required:True
        
    BoxLayout:
        pos_hint:{"center_x":0.28, "center_y":0.55}
        size_hint_x:0.5
        size_hint_y:0.1
        MDLabel:
            text:"Paid Amt"
            font_style:'Body1'
    MDTextField:
        id:amount
        pos_hint:{"center_x":0.61, "center_y":0.555}
        size_hint_x:None
        width:200
        hint_text:"Enter Paid Amount"
        helper_text:"Only Enter Numbers"
        required:True
        
    MDRectangleFlatButton:
        pos_hint:{"center_x":0.28, "center_y":0.35}
        id:date_label
        text:"CHOOSE DATE"
        on_release:
            app.choose_date()
            
        
    BoxLayout:
        pos_hint:{"center_x":0.75, "center_y":0.35}
        size_hint_x:0.4
        MDLabel:
            id:date_label
            
        
    MDRaisedButton:
        text: "SUBMIT"
        pos_hint:{"center_x":0.5, "center_y":0.15}
        on_release:app.new_entry()
        """)


        self.bottom_bar.add_widget(bottom_bar1)
        self.bottom_bar.add_widget(bottom_bar2)
        self.bottom_bar.add_widget(self.bottom_bar3)
        layout.add_widget(self.bottom_bar)
        screen.add_widget(layout)

        return screen

    def new_entry(self):
        name = self.bottom_bar3.ids.name.text
        amount = self.bottom_bar3.ids.amount.text
        date = self.bottom_bar3.ids.date_label.text
        print(name)

        conn = sqlite3.connect("maindb.db")
        cur = conn.cursor()

        month="january"
        cur.execute("INSERT INTO january VALUES (?,?,?)", (name, amount, date))
        cur.execute("SELECT amount FROM january WHERE Name='abc'")
        print(cur.fetchall())
        snackbar = Snackbar(text="Data Updated")
        snackbar.show()

    def get_date(self, date):
        '''
        :type date: <class 'datetime.date'>
        '''


    def choose_date(self):
        date = MDDatePicker(self.set_previous_date).open()

    def set_previous_date(self, date_obj):
        self.previous_date = date_obj
        self.bottom_bar3.ids.date_label.text = str(date_obj)

    # def on_start(self):
    #     conn = sqlite3.connect("maindb.db")
    #     cur = conn.cursor()
    #
    #     insert = "INSERT INTO january VALUES('abc', 12, 'abcd')"
    #     select_amt = "SELECT amount FROM %s"
    #     cur.execute(insert)
    #     cur.execute(select_amt, '%s' 'january')

if __name__ == "__main__":
    CommitteeApp().run()