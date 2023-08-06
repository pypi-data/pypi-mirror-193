from ...block import Block
from ..table import Table
from typing import List

class DataFrameTable(Table):

    def __init__(self, table_df, caption:str, notes:List[str]=[], show_index:bool=False):
        super(DataFrameTable, self).__init__(caption, notes)

        self.table_df = table_df
        self.show_index = show_index

    def as_html_figure_content(self):

        return self.table_df.to_html(index=self.show_index, render_links=True, escape=False)