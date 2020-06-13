from image_crawler import crawling


# print("------ sky image crawling ------")  # ----------------
# path = 'Images/Sky/'
#
# keyword = 'sky+800x600+wallpaper'
# crawling(keyword, path, 0)
#
# keyword = 'sky+800x600+white'
# crawling(keyword, path, 50)
#
# keyword = 'sky+800x600+blue'
# crawling(keyword, path, 100)
# print('\n')


# print("------ sea image crawling ------")  # ----------------
# path = 'Images/Sea/'
#
# keyword = 'sea+800x600+picture'
# crawling(keyword, path, 0)
#
# keyword = 'sea+800x600+wallpaper'
# crawling(keyword, path, 50)
#
# keyword = 'sea+800x600+ocean'
# crawling(keyword, path, 100)
# print('\n')


print("------ mountain image crawling ------")  # ----------------
path = 'Images/Mountain/'

keyword = 'mountain+800x600'
crawling(keyword, path, 0)

keyword = 'mountain+800x600+wallpaper'
crawling(keyword, path, 50)

keyword = 'mountain+800x600+photo'
crawling(keyword, path, 100)
print('\n')
