import album_art
my_string = "RATCHET SATURN GIRL Aminé"


def fix(text):
    wierd = "ŠŽšžŸÀÁÂÃÄÅÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖÙÚÛÜÝàáâãäåçèéêëìíîïðñòóôõöùúûüýÿ"
    wierd_list = list(wierd)
    wierd_map = "SZszYAAAAAACEEEEIIIIDNOOOOOUUUUYaaaaaaceeeeiiiidnooooouuuuyy"
    wierd_map_list = list(wierd_map)
    list_string = list(text)
    for c in range(len(list_string)):
        if list_string[c] in wierd_list:
            list_string[c] = wierd_map_list[wierd_list.index(list_string[c])]
    fixed = ""
    for c in list_string:
        fixed += c
    return fixed
