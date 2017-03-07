# Tempel.BOI

Catatan re-deployment http://tempel.blankonlinux.or.id

---------------------------------------------------------------------

## Dependensi:
* Python 2.6.6
* Django 1.2.5
* Pygments
* SQLite3

---------------------------------------------------------------------

## Instalasi

Jalankan perintah:

```sh
$ cd $HOME
$ git clone https://github.com/yyuu/pyenv.git ~/.pyenv
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
$ echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
```

* Bila tidak bisa, ganti `.bash_profile` dengan `.bashrc`

Reload shell, lalu jalankan perintah instalasi Python 2.6.6.

```sh
$ pyenv install 2.6.6
```

Set versi python menjadi 2.6.6 dengan menggunakan Pyenv

```sh
$ pyenv versions
* system (set by /home/username/.pyenv/version)
  2.6.6
$ pyenv shell 2.6.6
$ python --version
Python 2.6.6
```

Pasang virtualenv melalui pip dan buat lingkungan virtual lalu aktifkan.

```sh
$ pip install virtualenv
$ virtualenv venv01
$ source venv01/bin/activate
```

Fork & Clone Project ini kedalam direktori `tempel`

```sh
$ git clone https://github.com/usernameFork/tempel-boi.git tempel
```

Atau Unduh revisi terakhir dari dev.blankonlinux.or.id

```sh
$ bzr branch http://dev.blankonlinux.or.id/browser/infrastruktur/tempel
```

Pasang django dan pustaka yang dibutuhkan

```sh
$ pip install -r requirements.txt
```

Coba jalankan dalam virtualenv shell

```sh
$ cd tempel
$ python manage.py runserver
```

---------------------------------------------------------------------

Happy hacking!
