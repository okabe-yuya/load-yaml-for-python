# load-yaml-for-python
defined variants in yaml file, this script can load these and get 
you defined any yaml file in directory
this class load all yaml file and use for Variant(string or number(integer)) in python grammer

## argument
- dir_name => parent directory you put yaml file
- extension => target extension(default = yml)
- dir_symbol => decided to symbol for serach path

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

if yaml method return values is None
dir_name or path is wrong!!!!!! please check again
