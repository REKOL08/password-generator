# Generador de Contraseñas Seguras

Herramienta web para crear contraseñas robustas, completamente del lado del cliente. No envía datos a ningún servidor.

## Demo

Abre `index.html` directamente en tu navegador — no necesita servidor.

## Características

- Longitud ajustable de 8 a 64 caracteres
- Selección de tipos de caracteres: mayúsculas, minúsculas, números y símbolos
- Garantiza al menos un carácter de cada tipo activo (sin contraseñas con gaps)
- Barra de fortaleza con niveles: Muy débil → Muy fuerte
- Botón de copiar al portapapeles
- 100% offline, sin dependencias externas

## Algoritmo

La generación usa dos pasos:

1. **Garantía mínima**: se toma un carácter aleatorio de cada conjunto activo
2. **Relleno aleatorio**: se completa hasta la longitud deseada desde el pool combinado
3. **Shuffle Fisher-Yates**: se mezcla el arreglo para evitar patrones predecibles

## Criterios de fortaleza

| Puntos | Nivel       |
|--------|-------------|
| 0–1    | Muy débil   |
| 2      | Débil       |
| 3–4    | Regular / Buena |
| 5      | Fuerte      |
| 6      | Muy fuerte  |

Los puntos se asignan por: longitud ≥ 12, longitud ≥ 20, presencia de mayúsculas, minúsculas, números y símbolos.

## Estructura

```
password-generator/
└── index.html    # App completa en un solo archivo
└── README.md
```

## Stack

- HTML5 / CSS3 / JavaScript vanilla
- Sin frameworks ni dependencias
- Compatible con cualquier navegador moderno

## Parte de

Este proyecto forma parte del repositorio [REKOL08](https://github.com/REKOL08) como ejercicio de la lista **50 proyectos para desarrolladores — Principiante**.
