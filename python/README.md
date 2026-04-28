# Generador de Contraseñas — Python CLI

Versión de línea de comandos del generador. Sin dependencias externas, usa solo la librería estándar de Python.

## Requisitos

- Python 3.7+

## Uso

### Modo interactivo

```bash
python generator.py
```

El programa te guía paso a paso con valores por defecto.

### Modo flags

```bash
# longitud 24, configuración por defecto (mayúsculas + minúsculas + números)
python generator.py --length 24

# incluir símbolos
python generator.py --length 32 --symbols

# sin números, con símbolos
python generator.py --no-numbers --symbols

# solo minúsculas y números, longitud 12
python generator.py --no-upper --length 12
```

## Flags disponibles

| Flag | Alias | Descripción |
|------|-------|-------------|
| `--length N` | `-l N` | Longitud (8-64). Default: 16 |
| `--no-upper` | — | Excluir mayúsculas |
| `--no-lower` | — | Excluir minúsculas |
| `--no-numbers` | — | Excluir números |
| `--symbols` | `-s` | Incluir símbolos (!@#$...) |
| `--version` | `-v` | Mostrar versión |
| `--help` | `-h` | Mostrar ayuda |

## Algoritmo

1. Garantiza al menos un carácter de cada tipo activo
2. Rellena hasta la longitud deseada desde el pool combinado
3. Shuffle Fisher-Yates para eliminar patrones predecibles

## Autor

**REKOL08** · [github.com/REKOL08](https://github.com/REKOL08)
