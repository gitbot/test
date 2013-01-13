from fswrap import File
from gitbot.lib.s3 import Bucket
import yaml

HERE = File(__file__).parent


def __dump_and_upload_result(name, data):
    result = HERE.child_file('result.log', 'a')
    with open(result.path) as f:
        f.write('*********' + name + '************')
        f.write(yaml.dump(data))
        f.write('*********' + name + '************')
    b = Bucket(data.bucket)
    b.make()
    b.add_file(result)


def api(data):
    __dump_and_upload_result('api', data)


def www(data):
    __dump_and_upload_result('www', data)


def all(data):
    __dump_and_upload_result('all', data)
