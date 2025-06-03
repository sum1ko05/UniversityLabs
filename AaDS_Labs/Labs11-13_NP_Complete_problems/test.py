from graph_color import min_colors
from backpack import max_value_backpack
from packing import max_items_packed


if True:
    graph = {
        '0': ['1', '2'],
        '1': ['0', '2', '3'],
        '2': ['0', '1', '3'],
        '3': ['1', '2']
    }
    pallete_size, coloring = min_colors(graph)
    print(f"Min pallete size: {pallete_size}")
    print(f"Colored graph: {coloring}")
if True:
    print(f"Max value backpack: {max_value_backpack(10, [2, 3, 5, 7], [10, 15, 20, 25], 4)}")
if True:
    print(f"Max items packed: {max_items_packed([4, 5, 2, 1, 3], 6)}")
