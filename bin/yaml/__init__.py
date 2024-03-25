import pathlib

from discopy.frobenius import Diagram

from bin.py.lisp import lisp_f
from bin.py.files import file_diagram, files_f
from composing import glue_all_diagrams


def shell_main(file_names):
    # TODO cuando levanto archivos del filesystem
    # usar IO entre las llamadas.
    # solo al final hacer como Haskell corre el IO en el momento.
    # se necesita implementar !file o tags de un search path.
    file_diagrams = []
    for file_name in file_names:
        path = pathlib.Path(file_name)
        fd = file_diagram(path.open())
        Diagram.to_gif(fd, path=str(path.with_suffix('.gif')))
        file_diagrams.append(fd)
    rep_d = glue_all_diagrams(file_diagrams)
    rep_d = lisp_f(rep_d)
    rep_d = files_f(rep_d)
    return rep_d
