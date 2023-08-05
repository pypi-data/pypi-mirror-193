import string

cut_mapping = {
    "Ideal": 4,
    "Premium": 3,
    "Very Good": 2,
    "Good": 1,
    "Fair": 0,
}

color_mapping = {
    color_grade: value for value, color_grade in enumerate(string.ascii_uppercase[3:])
}

clarity_mapping = {
    "IF": 7,
    "VVS1": 6,
    "VVS2": 5,
    "VS1": 4,
    "VS2": 3,
    "SI1": 2,
    "SI2": 1,
    "I1": 0,
}

mappings = [cut_mapping, color_mapping, clarity_mapping]
