import arcade

arcade.open_window(800, 800, "Pumpkin Face")
arcade.set_background_color(arcade.color.DEEP_SPACE_SPARKLE)

arcade.start_render()
arcade.draw_circle_filled(400,400,300, arcade.color.PUMPKIN)
arcade.draw_arc_outline(400, 300, 400, 100, arcade.color.LAVENDER, -180,0,10)
arcade.finish_render()




arcade.run()