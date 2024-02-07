import urllib.parse

def webEmbed(title = None, description = None, thumbnail = None, color = None, bigimg = False):
    spoilerhack = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| _ _ _ _ _ _"
    baseurl = "https://embed.xpg.lol/embed"
    url = baseurl
    first = True
    if title:
        if first:
            url += f"?title={urllib.parse.quote(title)}"
        else:
            url += f"&title={urllib.parse.quote(title)}"
        first = False
    if description:
        if first:
            url += f"?description={urllib.parse.quote(description)}"
        else:
            url += f"&description={urllib.parse.quote(description)}"
        first = False
    if thumbnail:
        if first:
            url += f"?thumbnail={urllib.parse.quote(thumbnail)}"
        else:
            url += f"&thumbnail={urllib.parse.quote(thumbnail)}"
        first = False
    if color:
        if first:
            url += f"?color={urllib.parse.quote(color)}"
        else:
            url += f"&color={urllib.parse.quote(color)}"
        first = False
    if bigimg == True:
        if first:
            url += f"?bigimg=true"
        else:
            url += f"&bigimg=true"
    else:
        if first:
            url += f"?bigimg=false"
        else:
            url += f"&bigimg=false"
        first = False

    return f"{spoilerhack}{url}"
