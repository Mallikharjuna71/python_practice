

import re
def matching(s):
    ex = r'^([a-zA-Z0-9_\-]+)@([a-zA-Z0-9]+)\.([a-zA-Z]{3})$'
    print(bool(re.search(ex, s)))