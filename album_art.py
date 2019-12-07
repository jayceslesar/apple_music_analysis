def get_art(name):
    import coverpy
    coverpy = coverpy.CoverPy()
    limit = 1
    result = coverpy.get_cover(name, limit)
    return result.artwork(200)
