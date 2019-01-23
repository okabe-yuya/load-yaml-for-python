# load-yaml-for-python
pythonでymlファイルにi18nextみたく変数を置きたかったので作った

## argument
- dir_name => ymlファイルを格納している一番親のディレクトリ
- extension => ファイルの拡張子(default=yml)
- dir_symbol => ファイルのパスのシンボル(default=@)

## how to use and example
-yml
  - test.yml(test: hello)
  - Foo
    - bar.yml(test: good)

1. you make this class of instance,
  yml = YamlConverte("yml")
2. use yaml method and attribute yaml path
  get[test.yml in test]: yml.yaml("test.test")
  get[bar.yml in test]: yml.yaml("Foo:bar.test")

## あれ値が返ってこない(None)
- 指定している親ディレクトリの名前が違うか、同じものがある可能性
- ファイルのパスが間違っている
- シンボル記号が間違っている など
