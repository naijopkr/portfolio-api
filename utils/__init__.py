def get_prop(path: list, target: [dict, list]):
    out = target.copy()
    for key in path:
        try:
            out = out[key]
        except:
            return None
    else:
        return out
