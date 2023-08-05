import sys

import yarl

from ...const import APP_BASE_HOST, APP_SECURE_SCHEME
from ...core import HttpCore
from ...exception import TiebaServerError
from ...helper import log_success, parse_json
from ...request import pack_form_request, send_request


def parse_body(body: bytes) -> None:
    res_json = parse_json(body)
    if code := int(res_json['error_code']):
        raise TiebaServerError(code, res_json['error_msg'])


async def request(http_core: HttpCore, fid: int, tid: int, pid: int, is_hide: bool) -> bool:
    data = [
        ('BDUSS', http_core.account._BDUSS),
        ('forum_id', fid),
        ('is_hide', str(int(is_hide))),
        ('post_id', pid),
        ('thread_id', tid),
    ]

    request = pack_form_request(
        http_core,
        yarl.URL.build(scheme=APP_SECURE_SCHEME, host=APP_BASE_HOST, path="/c/c/thread/setPrivacy"),
        data,
    )

    __log__ = f"tid={tid}"

    body = await send_request(request, http_core.network, read_bufsize=1024)
    parse_body(body)

    log_success(sys._getframe(1), __log__)
    return True
