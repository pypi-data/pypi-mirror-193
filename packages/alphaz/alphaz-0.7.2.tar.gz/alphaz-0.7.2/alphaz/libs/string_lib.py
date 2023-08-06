import re, string, encodings, warnings
from typing import List


def is_number(txt):
    try:
        a = float(txt)
        return True
    except:
        return False


def is_upper(word):
    return all(c in string.ascii_uppercase for c in list(word))


def sort_words(words_dict):
    return {
        x[0]: x[1]
        for x in sorted(words_dict.items(), key=lambda item: item[1], reverse=True)
    }


def is_carac(test):
    string_check = re.compile("[@_!#$%^€&*()<>?/\|}{~:]")

    if string_check.search(test) == None:
        return False
    else:
        return True


def get_words(txt):
    pm = re.findall(r"\([^()]*\)", txt)
    for p in pm:
        txt = txt.replace(p, "")

    words = txt.split()

    words_out = []
    for x in words:
        x = x.lower()
        if is_carac(x):
            continue
        if "." in x:
            continue
        if "+" in x:
            continue
        if "-" in x:
            continue
        if "'" in x:
            continue
        if "," in x:
            continue
        if ";" in x:
            continue
        if "<" in x:
            continue
        if ">" in x:
            continue
        if "·" in x:
            continue
        if "[" in x:
            continue
        if x == "est":
            continue
        if x == "le":
            continue
        if x == "est":
            continue
        if x == "des":
            continue
        if x == "les":
            continue
        if len(x) == 1:
            continue
        if len(x) == 2:
            continue
        if is_number(x):
            continue

        words_out.append(x)
    return words_out


black_list = [
    "cp037",
    "utf_16_be",
    "cp1252",
    "hz",
    "ascii",
    "utf_32",
    "cp500",
    "cp1140",
    "gb2312",
    "euc_jis_2004",
    "cp865",
    "ptcp154",
    "cp860",
    "cp437",
    "koi8_r",
    "cp1256",
    "cp863",
    "cp1125",
    "gbk",
    "iso8859_11",
    "mac_iceland",
    "mac_latin2",
    "iso8859_8",
    "iso2022_jp_ext",
    "mac_greek",
    "big5hkscs",
    "cp949",
    "cp866",
    "mac_turkish",
    "iso2022_jp_2",
    "mac_roman",
    "cp1250",
    "cp950",
    "kz1048",
    "shift_jisx0213",
    "cp1258",
    "cp1253",
    "big5",
    "cp932",
    "cp852",
    "quopri_codec",
    "bz2_codec",
    "iso2022_jp_1",
    "euc_kr",
    "cp862",
    "cp858",
    "cp861",
    "tis_620",
    "cp869",
    "cp855",
    "shift_jis_2004",
    "cp775",
    "cp1026",
    "zlib_codec",
    "utf_16",
    "cp1254",
    "iso8859_7",
    "cp850",
    "iso8859_6",
    "shift_jis",
    "utf_16_le",
    "utf_32_be",
    "mac_cyrillic",
    "cp273",
    "mbcs",
    "uu_codec",
    "utf_32_le",
    "cp1251",
    "iso2022_kr",
    "cp857",
]


def universal_decode(txt, encodings_methods=[], blacklist=[]):
    encodings_methods.extend(list(set(encodings.aliases.aliases.values())))

    result = txt
    for encoding_method in encodings_methods:
        if encoding_method not in blacklist:
            try:
                result = txt.decode(encoding_method)
                return result
            except:
                pass
    return result


def universal_decodes(txt, encodings_methods=[], blacklist=[]):
    encodings_methods.extend(list(set(encodings.aliases.aliases.values())))

    results = {}
    for encoding_method in encodings_methods:
        if encoding_method not in blacklist:
            try:
                results[encoding_method] = txt.decode(encoding_method)
            except:
                pass
    return results


def python_case(txt):
    txt = txt.replace(" ", "_")
    txt = re.sub("[^a-zA-Z0-9_ \n\.]", "", txt)
    return txt.lower()


def pascal_case(txt):
    output = ""

    for el in txt.split("_"):
        output += el.lower().capitalize()
    output = re.sub("[^a-zA-Z0-9 \n\.]", "", output)
    return output


def camel_case(txt):
    output = ""
    i = 0
    for el in txt.split("_"):
        if i == 0:
            output += el.lower()
        else:
            output += el.lower().capitalize()
        i += 1

    return output


def levenshtein(mot1: str, mot2: str) -> int:
    # todo: change
    ligne_i = [k for k in range(len(mot1) + 1)]
    for i in range(1, len(mot2) + 1):
        ligne_prec = ligne_i
        ligne_i = [i] * (len(mot1) + 1)
        for k in range(1, len(ligne_i)):
            cout = int(mot1[k - 1] != mot2[i - 1])
            ligne_i[k] = min(
                ligne_i[k - 1] + 1, ligne_prec[k] + 1, ligne_prec[k - 1] + cout
            )
    return ligne_i[len(mot1)]


def found_best_match(word: str, words: List[str], threshold: int = None) -> str:
    if len(words) == 0:
        return None, 0
    matchs = [
        (word in w) / abs(len(word) - len(w) if len(word) != len(w) else 0.5)
        for w in words
    ]
    max_value = max(matchs)
    if threshold is not None and max_value < threshold:
        return None, max_value
    return words[matchs.index(max_value)], max_value


def to_list(o):
    if o is None:
        return []
    if type(o) == list:
        return o
    if len(o) == 0:
        return []
    if len(o) < 2:
        return [o]
    if o[0] == "[":
        o = o[1:]
    if o[-1] == "]":
        o = o[:-1]

    output = []
    for el in o.split(","):
        el = el.strip()
        if el.startswith("'"):
            el = el[1:]
        elif el.startswith("\"'"):
            el = "'" + el[2:]

        if el.endswith("'"):
            el = el[:-1]
        elif el.endswith("'\""):
            el = el[:-2] + "'"
        output.append(el)
    return output


def escape_ansi(line):
    ansi_escape = re.compile(r"(\x9B|\x1B\[)[0-?]*[ -/]*[@-~]")
    return ansi_escape.sub("", str(line))


def remove_accents(old):
    """
    Removes common accent characters, lower form.
    Uses: regex.
    """
    new = old.lower()
    new = re.sub(r"[àáâãäå]", "a", new)
    new = re.sub(r"[èéêë]", "e", new)
    new = re.sub(r"[ìíîï]", "i", new)
    new = re.sub(r"[òóôõö]", "o", new)
    new = re.sub(r"[ùúûü]", "u", new)
    return new
