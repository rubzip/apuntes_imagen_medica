#!/usr/bin/env bash
#
# compile.sh
# Script cómodo para compilar los apuntes de una carpeta a HTML y PDF.
#
# Uso:
#   ./compile.sh <CARPETA> [-o DIRECTORIO_SALIDA] [--name NOMBRE_FICHERO] [opciones]
#
# Ejemplos:
#   ./compile.sh Fisica/Tema_1
#   ./compile.sh 1
#   ./compile.sh Fisica/Tema_1 -o dist
#   ./compile.sh Fisica/Tema_1 -o dist --name Apuntes_UF1
#

set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
PYTHON_BIN="$(which python3)"

if [ -z "$1" ]; then
    echo "=========================================================="
    echo " Compilador de Apuntes - Imagen y Diagnóstico Clínico"
    echo "=========================================================="
    echo "Uso: ./compile.sh <CARPETA> [-o DIRECTORIO_SALIDA] [--name NOMBRE_FICHERO] [opciones]"
    echo ""
    echo "Argumentos:"
    echo "  CARPETA                 Ruta de la carpeta a compilar (ej. 'Fisica/Tema_1' o '1')"
    echo "  -o, --output DIR        Directorio donde guardar el HTML y PDF (se crea si no existe)"
    echo "  -n, --name NOMBRE       Nombre de los ficheros (por defecto: nombre de la carpeta)"
    echo ""
    echo "Ejemplos:"
    echo "  ./compile.sh Fisica/Tema_1"
    echo "  ./compile.sh 1 -o dist"
    echo "  ./compile.sh Fisica/Tema_1 -o dist --name Apuntes_UF1"
    echo ""
    exit 1
fi

if [ -f "$DIR/pdf_compiler/compilar_tema.py" ]; then
    COMPILADOR="$DIR/pdf_compiler/compilar_tema.py"
else
    COMPILADOR="$DIR/compilar_tema.py"
fi

"$PYTHON_BIN" "$COMPILADOR" "$@"
