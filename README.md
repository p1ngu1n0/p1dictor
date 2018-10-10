# P1dictor

Genera diccionarios .lst

## Instalacion

En el directorio instala los paquetes necesarios con:

```sh
pip3 install -r requeriments.txt
```

Si no tienes pip3 ejecuta en Debian:

```sh
# apt-get install python3-pip
```

### Ejecucion

Para ejecutarlo escribe:

```sh
python3 p1dictor.py -h
```

Esto nos devolvera las opcciones del script:

```ascii
usage: p1dic.py [-h] -n NUM -c CHAR -o OUTPUT

p1dictor.py create by p1ngu1n0

optional arguments:
  -h, --help            show this help message and exit
  -n NUM, --num NUM     Numero de caracteres
  -c CHAR, --char CHAR  Caracteres a usar
  -o OUTPUT, --output OUTPUT
                        Nombre de salida
```
### Ejemplo

```sh
python3 p1dictor.py -n 4 -c 0123456789 -o pin
```

Esto generaria un archivo llamado pin de 4 digitos empezando por:

0000
0001
0002
0003
00...

## Autor

@_p1ngu1n0_

