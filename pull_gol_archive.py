def grid_maker():
  global grid, reproduction_list, series, side, list_length
  grid = []
  cell_x = 0
  cell_y = 0
  list_length = df_meta['Length'][0]
  series = df_meta['Series'][0]
  side = df_meta['Side'][0]
  for i in range(list_length):
      grid.append((series, list_length, side, int(reproduction_list[i]),
                    int(cell_x + i % side), int(cell_y - i//side), 
                    int((cell_x + i % side) + 1), int(cell_y - i//side), 
                    int((cell_x + i % side) + 1), int((cell_y - i//side) - 1),
                    int(cell_x + i % side), int((cell_y - i//side) - 1),
                    int((cell_x + i % side) - 1), int((cell_y - i//side) - 1),
                    int((cell_x + i % side) - 1), int((cell_y - i//side)),
                    int((cell_x + i % side) - 1), int((cell_y - i//side) + 1),
                    int((cell_x + i % side)), int((cell_y - i//side) + 1),
                    int((cell_x + i % side) + 1), int((cell_y - i//side) + 1)))
