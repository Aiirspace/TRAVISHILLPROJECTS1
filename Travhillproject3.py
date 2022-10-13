import arcade

arcade.open_window(400,400,"Big Boy")
arcade.set_background_color(arcade.color.DIAMOND)

arcade.start_render()
arcade.draw_line(100,10,100,160,arcade.color.DEEP_SPACE_SPARKLE,4)
arcade.draw_line(250,10,250,160,arcade.color.DEEP_SPACE_SPARKLE,4)
arcade.draw_lrtb_rectangle_filled(100,250,300,160,arcade.color.DEEP_SPACE_SPARKLE)
arcade.draw_circle_outline(175,340,40,arcade.color.DEEP_SPACE_SPARKLE)
arcade.draw_triangle_filled(75,250,75,300,100,300,arcade.color.DEEP_SPACE_SPARKLE)
arcade.draw_arc_filled(270,250,100,100,arcade.color.DEEP_SPACE_SPARKLE,60,330)


arcade.finish_render()








arcade.run()