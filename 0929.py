import arcade
my_window = arcade.open_window(1000, 900, "Graph Paper")
arcade.set_background_color(arcade.color.DARK_BYZANTIUM)
arcade.start_render()
for xlocation in range(50, 1000, 80):
    arcade.draw_line(xlocation, 50, xlocation, 900, arcade.color.LIGHT_CORNFLOWER_BLUE, 5)
for ylocation in range(50, 900, 80):
    arcade.draw_line(50, ylocation, 1000, ylocation, arcade.color.BUFF, 5)
arcade.finish_render()

arcade.run()