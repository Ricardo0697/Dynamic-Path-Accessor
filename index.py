import json

def get_dict_value(dct, path):
    keys = path.split('.')
    try:
        # Traverse the dictionary based on the keys in the path
        for key in keys:
            dct = dct[key]
        return str(dct)  # Convert to string to match the expected return type
    except (KeyError, TypeError):
        return None

def get_res(s, paths):
    final_dict = ""
    for x in s:
        final_dict += x
    final_dict = json.loads(final_dict)
    result = []
    for path in paths : 
        res = get_dict_value(final_dict, path)
        if res is None : 
            result.append("None")
        else:
            result.append(res)
    return result

if __name__ == '__main__':
    # Object representation
    s = ['{"car": {"wheels": 2, "gears": 5}}']

    # Input for the paths
    paths_count = int(input().strip())
    paths = [input() for _ in range(paths_count)]

    # Getting the result
    result = get_res(s, paths)

    # Printing the result
    for res in result:
        print(res)