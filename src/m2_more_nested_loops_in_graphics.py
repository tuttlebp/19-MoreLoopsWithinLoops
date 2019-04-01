"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Brett Tuttle.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    run_test_draw_upside_down_wall()


def run_test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Upside-down wall, Tests 1 and 2')

    rectangle = rg.Rectangle(rg.Point(125, 230), rg.Point(155, 250))
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(375, 175), rg.Point(425, 225))
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()


def draw_upside_down_wall(rectangle, n, window):
    """
    See   MoreWalls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" on the given window, where:
      -- The BOTTOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is nonnegative.
    """
    # -------------------------------------------------------------------------
    # TODO: 2. Implement and test this function.
    #     Some tests are already written for you (above).
    # -------------------------------------------------------------------------
    start_x = rectangle.get_upper_left_corner().x
    start_y = rectangle.get_upper_left_corner().y
    end_x = rectangle.get_lower_right_corner().x
    end_y = rectangle.get_lower_right_corner().y
    width = rectangle.get_width()
    height = rectangle.get_height()
    rectangle.attach_to(window)
    window.render(.1)

    for k in range(1, n):
        for j in range(k + 1):
            point1 = rg.Point(start_x - (j * width/2), start_y - (j * height))
            point2 = rg.Point(end_x - (j * width/2), end_y - (j*height))
            new_rectangle = rg.Rectangle(point1, point2)
            new_rectangle.attach_to(window)

            for h in range(j + 1):
                new_rectangle1 = rg.Rectangle(rg.Point(point1.x + (width * h), point1.y),
                                              rg.Point(point2.x + (width * h), point2.y))
                new_rectangle1.attach_to(window)
        window.render(.1)


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
