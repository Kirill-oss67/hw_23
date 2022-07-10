from flask_restx import abort


def make_query(cnd, val, file_list):
    if cnd == "filter":
        res = filter(lambda x: val in x, file_list)
        return res
    if cnd == "map":
        try:
            val = int(val)
            res = [x.split()[val] for x in file_list]
            return res
        except:
            return abort(400)
    if cnd == "unique":
        res = list(set(file_list))
        return res
    if cnd == 'sort':
        reverse = val == 'desc'
        res = sorted(file_list, reverse=reverse)
        return res
    if cnd == "limit":
        try:
            val = int(val)
            res = list(file_list)[:val]
            return res
        except:
            return abort(400)
