import anki_vector

import time

with anki_vector.Robot(enable_nav_map_feed=True, show_3d_viewer=True) as robot:
    time.sleep(5)
