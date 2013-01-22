from fswrap import File
from gitbot.lib.s3 import Bucket
import yaml

HERE = File(__file__).parent


def __dump_and_upload_result(name, data):
    result = HERE.child_file('result.log')
    with open(result.path, 'a') as f:
        f.write('*********' + name + '************')
        f.write(yaml.dump(data))
        f.write('*********' + name + '************')
    b = Bucket(data['bucket'],
                aws_access_key_id=data['access_key'],
                aws_secret_access_key=data['secret'])
    b.make()
    b.add_file(result)


def api(data):
    __dump_and_upload_result('api', data)


def www(data):
    __dump_and_upload_result('www', data)


def all(data):
    __dump_and_upload_result('all', data)
