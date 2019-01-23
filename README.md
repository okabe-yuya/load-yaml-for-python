# load-yaml-for-python
pythonでymlファイルにi18nextみたく変数を置きたかったので作った

## argument
- dir_name => ymlファイルを格納している一番親のディレクトリ
- extension => ファイルの拡張子(default=yml)
- dir_symbol => ymlファイルの上階層にディレクトリがある場合に使用するシンボル(default=:)

## 使い方と例
### フォルダ階層
- yml
  - test.yml(test: hello)
  - Foo
    - bar.yml(test: good)

1. クラスのインスタンスを作成
  yml = YamlConverte("yml")
  
2. yamlメゾットに以下のようにパスを指定。親ディレクトリがある場合はFoo:のように指定
  // get[test.yml in test] (no parent directory)
      yml.yaml("test.test")
  // get[bar.yml in test] (exist parent directory)
      yml.yaml("Foo:bar.test")

## あれ値が返ってこない(None)
- 指定している親ディレクトリの名前が違うか、同じものがある可能性
- ファイルのパスが間違っている
- シンボル記号が間違っている など
