from load_yml import YamlLoader
import datetime

def sample():
    y = YamlLoader("yml")
    aaa = "okabe"
    print(y.yaml(f'test.foo.bar@{aaa}'))
    print(y.yaml(f'test.foo.tmp'))
    print(y.yaml(f'test.foo.ymd@{aaa}'))
    print(y.yaml(f'test:utils.util.hello@{aaa}'))
    print(datetime.date.today().strftime(y.yaml(f'test.format.ymd')))

if __name__=='__main__':
    sample()