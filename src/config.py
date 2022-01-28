track_x_left = 423
track_y = 640
track_width = 75
track_count = 4


def get_track_position(index: int):
  x = track_x_left + (track_width * index)
  return (x, track_y)


TrackLocations = list(map(get_track_position, range(track_count)))
