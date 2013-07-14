import random


def get_404_message():
    candidates = []

    candidates.append("""
    You tried to run away but I found you! It's time to go <a href="/">home</a>.
    """)

    candidates.append("""
    Oops! My bad yo.  It appears I haven't created this page yet.<br>
    Navigate 'back' on your browser or click <a href="/">here</a>.
    """)

    candidates.append("""
    <em>
        IF YOU'VE MADE IT TO THIS PAGE, SOMETHING TERRIBLE HAS HAPPENED, AND I'VE<br>
        BEEN FORCED TO FLEE THE COMFORT OF THE COVETED CORNER TABLE AT BARNES & NOBLE.
    </em>
    <br>
    <br>
    My fishing <a href="/">home</a> in Cinque Terre may be my last safe haven; meet me there. Put a pot of coffee on, will ya?
    """)

    index = random.randint(0, len(candidates) - 1)

    return candidates[index]
