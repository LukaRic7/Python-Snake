def darken_hex(hex_color:str, percent:float) -> str:
    """
    **Darken HEX color by given pct.**
    
    *Parameters*:
    - `hex_color` (str): Starting color
    - `percent` (float): Percentage to darken
    
    *Returns*:
    - (str): The darkened color in HEX format.
    """

    hex_color = hex_color.lstrip('#')

    # Convert hex to RGB
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)

    # Calculate darkening factor
    factor = 1 - (percent / 100)

    # Apply factor and clamp values
    r = max(0, min(255, int(r * factor)))
    g = max(0, min(255, int(g * factor)))
    b = max(0, min(255, int(b * factor)))

    # Convert back to hex
    return "#{:02X}{:02X}{:02X}".format(r, g, b)

def darken_rgb(rgb:tuple[int], percent:float) -> tuple[int]:
    """
    **Darken RGB color by given pct.**
    
    *Parameters*:
    - `rgb` (tuple[int]): Starting color
    - `percent` (float): Percentage to darken
    
    *Returns*:
    - (tuple[int]): The darkened color in RGB format.
    """

    r, g, b = rgb

    # Clamp input just in case
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))

    # Darkening factor
    factor = 1 - (percent / 100)

    # Apply and clamp
    r = max(0, min(255, int(r * factor)))
    g = max(0, min(255, int(g * factor)))
    b = max(0, min(255, int(b * factor)))

    return (r, g, b)