# Kard Private Api
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0)
![](https://komarev.com/ghpvc/?username=ghrlt-py-kard&color=brightgreen&label=Repository%20views)  
Python wrapper of Kard Private Api
<br>

Made with the help of the awesome open-source tool [HTTP Toolkit](https://httptoolkit.tech/) for trafic sniffing ❤️


## Installation
`pip install pyKard`

## Usage
```python
from kard_private_api import Kard

myKard = Kard()
myKard.authenticate(forceApiAuth=False)

...
```

That's all! You're all setup to play with Kard private API.<br>
I recommend you to start with some of the examples [here](https://github.com/ghrlt/kard-private-api/tree/master/examples).


## FAQ
### How does it login to my Kard account?

On your first (or clean) login, the library will generate a unique vendor identifier that will be linked to your session. <br>
Then, a request will be made to Kard, which in return will either ask for an OTP code or your PIN code. 

Once successfully authenticated, we have access to an `accessToken` and a `refreshToken` which are your account sesame. These as well as your vendor identifier are saved on your computer for later use.

### Where my credentials are saved?

By default, they are saved in a file named `.kard-login_YOURPHONENUMBER-settings.json` located in your home directory. <br>
(`C:\\Users\%username%\` on Windows or `~` on Linux/MacOs)


## License

This repository and all of its content is under the [GNU GPLv3](https://github.com/ghrlt/kard-private-api/blob/master/LICENSE) license.


## Disclaimer
This software is provided as is, I shall not, and will not be liable for any misuse or unauthorised use, leading or not to damage to any third-party.
