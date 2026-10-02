#!/usr/bin/env bash
#
# compilar.sh
# Script cómodo para compilar los apuntes de un tema a un único PDF.
#
# Uso:
#   ./compilar.sh Tema_1
#   ./compilar.sh 1
#

set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
PYTHON_BIN="$(which python3)"

if [ -z "$1" ]; then
    echo "=========================================================="
    echo " Compilador de Apuntes - Imagen y Diagnóstico Clínico"
    echo "=========================================================="
    echo "Uso: ./compilar.sh <TEMA> [opciones]"
    echo ""
    echo "Ejemplos:"
    echo "  ./compilar.sh 1"
    echo "  ./compilar.sh Tema_1"
    echo "  ./compilar.sh Tema_1 -o Apuntes_Tema_1.pdf"
    echo ""
    exit 1
fi

if [ -f "$DIR/pdf_compiler/compilar_tema.py" ]; then
    COMPILADOR="$DIR/pdf_compiler/compilar_tema.py"
else
    COMPILADOR="$DIR/compilar_tema.py"
fi

"$PYTHON_BIN" "$COMPILADOR" "$@"
