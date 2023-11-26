def translate(type, row, direction):
    if type == "horizontal":
        if row == 0:
            if direction == 0:
                return "U"
            elif direction == 1:
                return "U'"

        elif row == 1:
            if direction == 0:
                return "E'"
            elif direction == 1:
                return "E"

        elif row == 2:
            if direction == 0:
                return "D'"
            elif direction == 1:
                return "D"

    elif type == "vertical":
        if row == 0:
            if direction == 0:
                return "L'"
            elif direction == 1:
                return "L"

        elif row == 1:
            if direction == 0:
                return "M'"
            elif direction == 1:
                return "M"

        elif row == 2:
            if direction == 0:
                return "R"
            elif direction == 1:
                return "R'"

    elif type == "side":
        if row == 0:
            if direction == 0:
                return "F"
            elif direction == 1:
                return "F'"

        elif row == 1:
            if direction == 0:
                return "S"
            elif direction == 1:
                return "S'"

        elif row == 2:
            if direction == 0:
                return "B'"
            elif direction == 1:
                return "B"