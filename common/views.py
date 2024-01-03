
# Create your views here.

def get_offset_limit_page(page):
    LIMIT = 7
    page_prev = page - 1
    page_next = page + 1
    if page <= 1:
        page = 1
        page_prev = 1
    OFFSET = page * LIMIT - LIMIT
    return OFFSET, LIMIT, page, page_prev, page_next

