#os.path isn't installed
from os.path import join

path_segment_1 = "/Home/User"
path_segment_2 = "Codecademy/videos"
path_segment_3 = "cat_videos/surprised_cat.mp4"

# join all three of the paths here!
#print(join(path_segment_1, path_segment_2, path_segment_3))

def myjoin(*args):
  joined_args = ''
  for arguments in args:
    joined_args += join(arguments)
  
  return joined_args