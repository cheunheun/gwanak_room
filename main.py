import streamlit as st
from sqlmanager import SQLManager
import dataprocessor as dp

if __name__ == '__main__':
    '''# hi'''
    stn_name, db_filter, search_filter = dp.input_filter()
    dp.print_filtered_result(SQLManager('data.db'), stn_name, db_filter, search_filter)
