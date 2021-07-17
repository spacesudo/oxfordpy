
# oxfordpy
[![GitHub issues](https://img.shields.io/github/issues/spacesudo/oxfordpy)](https://github.com/spacesudo/oxfordpy/issues)
[![GitHub forks](https://img.shields.io/github/forks/spacesudo/oxfordpy)](https://github.com/spacesudo/oxfordpy/network)
[![GitHub stars](https://img.shields.io/github/stars/spacesudo/oxfordpy)](https://github.com/spacesudo/oxfordpy/stargazers)
[![GitHub license](https://img.shields.io/github/license/spacesudo/oxfordpy)](https://github.com/spacesudo/oxfordpy/blob/master/LICENSE.txt)

oxfordpy is a python library for the [oxford dictionary API](https://developer.oxforddictionaries.com/).


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install oxfordpy.

>Installation using pip

```bash
pip install oxfordpy
```
>Installation from source

```bash
git clone https://github.com/spacesudo/oxfordpy.git
cd oxfordpy
python setup.py
```

## Usage

```python
from oxfordpy import oxfordpy

dictionary = oxfordpy.Oxford()

search = dictionary.entries("example") #search for "example"

print(search)

```

## Configuration
To configure the library pass your configurations to the *oxfordpy()* class.
```python
from oxfordpy import oxfordpy
oxford = oxfordpy.Oxford(app_id = "<your id>",app_key = "<your key>",timeout = (2,6)) #timeout should be a tuple
```

## Common Issues

>Authentification error

Please now that the api key and id used for this package is for test purpose only.
Some features of the API are not accessible with a Developer API credentials.

*If you face any other issue please kindly let me know*



## Roadmap
*Please know that this library is still under development*

Future updates of this library will have advanced features and probably use other dictionary API like Meriam Webster support and others

*while this library is production ready please remember to regularly update the library using ```pip install oxfordpy --upgrade```*

## Social media

You can follow me on:
 
Twitter [@derankem](https://twitter.com/derankem) 

or send a message on telegram [@spacesudo](https://t.me/spacesudo)
 

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
This project is licensed under the  [MIT](https://choosealicense.com/licenses/mit/) License. 
