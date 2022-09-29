import arcade

comp_151_window = arcade.open_window(1000, 800, "Lots of shapes")
arcade.set_background_color(arcade.color.CRIMSON)


arcade.start_render()
arcade.draw_line_strip([(20,30), (200,30), (300, 200), (200, 300), (20,40)],
                       arcade.color.AQUAMARINE, 5)
arcade.draw_lrtb_rectangle_outline(320, 420, 350, 50, arcade.color.FERN_GREEN, 10)
arcade.draw_lrtb_rectangle_filled(450,550, 450,50, arcade.color.AMBER)
arcade.draw_xywh_rectangle_outline(600,50,100,300, arcade.color.ASPARAGUS, 7)
arcade.draw_xywh_rectangle_filled(400, 150, 400, 100, arcade.color.FULVOUS)
arcade.draw_circle_filled(150,450,75, arcade.color.AMARANTH_PINK)
arcade.draw_circle_outline(150,450,100,arcade.color.CITRINE, 8)
arcade.draw_triangle_filled(820, 700, 1000, 700, 910, 500, arcade.color.LAVENDER_ROSE)
arcade.draw_triangle_outline(820, 700, 650, 750, 500, 450, arcade.color.HEART_GOLD)
arcade.draw_arc_filled(400, 700, 100, 100, arcade.color.AQUAMARINE, 30, 340)
arcade.draw_arc_outline(550,700, 100,100, arcade.color.BUFF, -180,0, 7)
arcade.draw_parabola_filled(800,200,1000,300, arcade.color.AMBER)
arcade.finish_render()




arcade.run()