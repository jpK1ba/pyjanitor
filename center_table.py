from IPython.display import HTML

def center_table(df):
    '''
    Accepts a dataframe and displays the dataframe centered in the notebook.
    '''
    display(HTML('<center>' + df.to_html() + '</center>'))