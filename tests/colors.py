# Define table borders and colors 
# create a table summary
index = pd.MultiIndex.from_tuples([("Type", ''), ("alpha", "x"), 
                           ("alpha", "y"),
                           ("alpha","z"),
                            ("beta", '')])

data = [['a', 'b', 'c', 'd'],
        [1, 2, 3, 4], 
        [5, 6, 7, 8], 
        [9, 10, 11, 12],
        [13, 14, 15, 16]]

table = pd.DataFrame(data = data, 
                      index = index,
                      columns =  pd.MultiIndex.from_product([['data'], ['', ' ', '  ', '   ']]))

# set styles
header = {'selector': 'th', 'props': 
          [('background-color', '#00008b'), ('color', 'white'), ('text-align', 'center'), ('vertical-align', 'centre'), ('font-weight', 'bold')]}

header_level0 = {'selector': 'th.col_heading.level0', 'props': [('font-size', '15px')]}

index = {'selector': 'th.row_heading', 'props': 
         [('background-color', '#5b9bd5'), ('color', 'white'), ('text-align', 'center'), ('font-weight', 'bold')]}

top_row = {'selector': 'td.data.row0', 'props': 
         [('background-color', '#5b9bd5'), ('color', 'white'), ('text-align', 'center'), ('font-weight', 'bold')]}

borders_bottom1 = {'selector': '.row0', 'props': 
                  [('border-bottom', '1px solid #00008b'), ('border-top', '1px solid #00008b')]}

borders_bottom2 = {'selector': '.row_heading.level0.row1', 'props': 
                  [('border-bottom', '1px solid #00008b')]}

borders_bottom3 = {'selector': '.row3', 'props': 
                  [('border-bottom', '1px solid #00008b')]}

borders_bottom4 = {'selector': '.row1', 'props': 
                  [('border-bottom', '1px dashed #00008b')]}

borders_bottom5 = {'selector': '.row2', 'props': 
                  [('border-bottom', '1px dashed #00008b')]}

borders_right = {'selector': '.row_heading.level1', 'props': 
                 [('border-right', '1px solid #00008b')]}

# apply styles
table = table.style.set_table_styles([header, header_level0, index, top_row, borders_bottom1, borders_bottom2, borders_bottom3, borders_bottom4, borders_bottom5, borders_right])

#table