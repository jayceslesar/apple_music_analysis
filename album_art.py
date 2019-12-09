import io
from collections import Counter


def get_art(name):
    import coverpy
    import html
    coverpy = coverpy.CoverPy()
    limit = 1
    result = coverpy.get_cover(name, limit)
    return result.artwork(200)


def requests_image(name):
    from PIL import Image
    import requests
    i = requests.get(get_art(name)).content
    image = Image.open(io.BytesIO(i))
    return image


def compute_top_image_color(name):
    img = requests_image(name)
    width, height = img.size
    colors = []
    for x in range(0, width):
        for y in range(0, height):
            r, g, b = img.getpixel((x, y))
            colors.append(str(r) + ' ' + str(g) + ' ' + str(b))
    top_color = Counter(colors).most_common(1)[0][0].split()
    return 'rgb(' + top_color[0] + ', ' + top_color[1] + ', ' + top_color[2] + ')'
