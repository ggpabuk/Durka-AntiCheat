# Durka Anti - Cheat

#### Features
- Easy to use
- Configuration file
- ~~Dirty code~~

#### Configuration
| Config Option	  | Value Type    | Description  	                                  |
| --------------- | ------------- | ----------------------------------------------- |
| process         | string        | The process followed by anti-cheat              |
| delay           | float         | Delay between checks                            |
| debug           | bool          | Enables debug mode (disable before compilation) |
| ~~hard_mode~~ (in dev)      | bool          | Enables or disables additional protection levels (recommended) |

#### How to use
1. Download [this](https://github.com/ggpabuk/Durka-AntiCheat/releases/latest) and install cx_freeze (`pip install cx_freeze` (`pip3 install cx_freeze` on Linux))
1. Change the configuration file (`config.yaml`) for your project
1. Run `py setup.py build` (`python3 setup.py build` on Linux)
1. Congratulations, you compiled anti-cheat, now go to the `build` directory. The anti-cheat will be in the `exe.xxx` directory

#### Durka meme
![Durka Ebat](https://cs10.pikabu.ru/post_img/big/2020/02/14/1/1581637383127016272.png "Durka Ebat")
