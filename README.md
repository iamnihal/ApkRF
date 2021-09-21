<h1 align="center">ApkRF: Android Package Reconnaissance Framework</h1>

[![version](https://img.shields.io/badge/version-1.0-red)](https://www.github.com/iamnihal/ApkRF)
[![python](https://img.shields.io/badge/python-3.8.10-blue.svg?logo=python&labelColor=yellow)](https://www.python.org/downloads/)
[![django](https://img.shields.io/badge/django-3.2.7-blue.svg?logo=django&labelColor=grey)](https://www.python.org/downloads/)
[![platform](https://img.shields.io/badge/platform-osx%2Flinux%2Fwindows-green.svg)](https://github.com/iamnihal/warf/)
  <br />

<p align="center">
<img src="https://user-images.githubusercontent.com/37813784/134226704-6974293f-6224-4c3c-b218-c4f32ac5cbca.gif" width="300" height="300" />
</p>
  


![ApkSF](https://user-images.githubusercontent.com/37813784/134228960-566dae2b-d853-401c-8eb6-df2de3f2bb39.png)

## Live: [Soon]

```
ApkRF is a Reconnaissance Framework for APK files. It uses "apkleaks" in the Back-end
which decompiles the APK and look for interesting informations inside it.
```

### Installation

1) Create a virtualenv:
```
$ python3 -m venv <virtual env path>
```
2) Activate the virtualenv you have just created:
```
$ source <virtual env path>/bin/activate
```
3) Clone this repository:
```
$ git clone https://github.com/iamnihal/ApkRF.git
````
4) Install the requirements:
```
$ pip install -r requirements.txt
```
5) Apply migrations:
```
$ python manage.py migrate
```
6) Run the server:
```
$ python manage.py runserver
```

and load the app at http://127.0.0.1:8000


> :warning: Warning:-  **Change SECRET_KEY in settings.py for the security purpose. To generate your own SECRET_KEY, use this:-**
```
python -c "import secrets; print(secrets.token_urlsafe())"
```
 
<!-- CONTRIBUTING -->
## Contributing

Any contributions you make are **greatly appreciated**.

<!-- LICENSE -->
## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements and Credits
[apkleaks](https://github.com/dwisiswant0/apkleaks):- dwisiswant0
