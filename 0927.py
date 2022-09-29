import arcade

my_window = arcade.open_window(1000,900,"Graph Paper")
arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)
arcade.start_render()
for xloc in range(50, 1000, 80):
    arcade.draw_line(xloc, 50, xloc, 900, arcade.color.BOSTON_UNIVERSITY_RED,5)
for yloc in range(500, 30, 100):
    arcade.draw_line(xloc, yloc, xloc, yloc, arcade.color.CELADON_GREEN,5)
arcade.finish_render()



arcade.run()