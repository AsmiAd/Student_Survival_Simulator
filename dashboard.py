from graphics import Canvas

CANVAS_WIDTH = 700
CANVAS_HEIGHT = 400

BAR_WIDTH = 300
BAR_HEIGHT = 25


def draw_bar(canvas, x, y, label, value):

    canvas.create_text(
        x,
        y,
        label,
        "black",
        14
    )

    canvas.create_rectangle(
        x + 120,
        y - 10,
        x + 120 + BAR_WIDTH,
        y + 15,
        "white",
        "black"
    )

    fill_width = value * 3

    canvas.create_rectangle(
        x + 120,
        y - 10,
        x + 120 + fill_width,
        y + 15,
        "green",
        "green"
    )

    canvas.create_text(
        x + 450,
        y,
        str(value),
        "black",
        14
    )


def show_dashboard(player, week):

    canvas = Canvas(
        CANVAS_WIDTH,
        CANVAS_HEIGHT
    )

    canvas.create_text(
        350,
        30,
        "STUDENT SURVIVAL SIMULATOR",
        "blue",
        20
    )

    canvas.create_text(
        350,
        60,
        f"Week {week}",
        "black",
        16
    )

    draw_bar(
        canvas,
        50,
        120,
        "Grades",
        player.grades
    )

    draw_bar(
        canvas,
        50,
        170,
        "Health",
        player.health
    )

    draw_bar(
        canvas,
        50,
        220,
        "Stress",
        player.stress
    )

    draw_bar(
        canvas,
        50,
        270,
        "Happiness",
        player.happiness
    )