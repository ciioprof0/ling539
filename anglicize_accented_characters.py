import re

def anglicize_accented_characters(original_text):
    """
    Convert accented characters in a string to their Anglicized (non-accented)
    equivalents while preserving the original case.

    This function replaces accented Latin characters in the input text with
    their closest US-ASCII counterparts. It handles both uppercase and lowercase
    accented characters separately to maintain the case of each character in the
    original text.

    Args:
        original_text (str): The string to be processed. It can contain extended
        ASCII and Unicode accented characters in both uppercase and lowercase.

    Returns:
        str: A new string with all accented characters replaced by their
        Anglicized US-ASCII equivalents, preserving the original case.

    Example Usage:
        original_text = "Café São Paulo – Łódź, České Švýcarsko"
        anglicized_text = anglicize_accented_characters(original_text)

        print(original_text)  # Output: "Café São Paulo – Łódź, České Švýcarsko"
        print(anglicized_text)  # Output: "Cafe Sao Paulo – Lodz, Ceske Svyacarsko"
    """
    replacements = [
        (r'[àáâäãåā]', 'a'), (r'[ÀÁÂÄÃÅĀ]', 'A'),
        (r'[æ]', 'ae'), (r'[Æ]', 'AE'),
        (r'[çćč]', 'c'), (r'[ÇĆČ]', 'C'),
        (r'[đď]', 'd'), (r'[ĐĎ]', 'D'),
        (r'[ğģ]', 'g'), (r'[ĞĢ]', 'G'),
        (r'[èéêëēėę]', 'e'), (r'[ÈÉÊËĒĖĘ]', 'E'),
        (r'[ìíîïīįĩ]', 'i'), (r'[ÌÍÎÏĪĮĨ]', 'I'),
        (r'[łľĺ]', 'l'), (r'[ŁĽĹ]', 'L'),
        (r'[ñńň]', 'n'), (r'[ÑŃŇ]', 'N'),
        (r'[òóôöõøōœ]', 'o'), (r'[ÒÓÔÖÕØŌŒ]', 'O'),
        (r'[œ]', 'oe'), (r'[Œ]', 'OE'),
        (r'[ùúûüūųũ]', 'u'), (r'[ÙÚÛÜŪŲŨ]', 'U'),
        (r'[řŗ]', 'r'), (r'[ŘŖ]', 'R'),
        (r'[śšş]', 's'), (r'[ŚŠŞ]', 'S'),
        (r'ß', 'ss'), (r'ẞ', 'SS'),
        (r'[ťţț]', 't'), (r'[ŤŢȚ]', 'T'),
        (r'[ýÿ]', 'y'), (r'[ÝŸ]', 'Y'),
        (r'[źžż]', 'z'), (r'[ŹŽŻ]', 'Z'),
    ]

    anglicized_text = ""

    for pattern, replacement in replacements:
        anglicized_text = re.sub(pattern, replacement, original_text)

    return anglicized_text

# Example usage
original_text = "Café São Paulo – Łódź, České Švýcarsko"
anglicized_text = anglicize_accented_characters(original_text)

print("Original Text:", original_text)
print("Modified Text:", anglicized_text)