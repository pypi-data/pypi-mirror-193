

class ServerType:
    LOCAL = 0
    PROXY = 1
    REMOTE = 2


class BodyType:
    JSON = 0
    BYTE = 1
    STRING = 2


class HTTPMethod:
    GET = "get"
    POST = "post"
    PUT = "put"
    DELETE = "delete"
    HEAD = "head"
    OPTIONS = "options"
    PATCH = "patch"


class EC2State:

    PENDING = 0
    RUNNING = 1
    STOPPING = 2
    STOPPED = 3
    TERMINATING = 4
    TERMINATED = 5
