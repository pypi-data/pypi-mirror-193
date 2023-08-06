from random import randint
from .dialetos import DialetoMiguxes

import re


def __camelizar(s: str) -> str:

    """
    Aleatoriza a capitalização dos caracteres de uma string.

    Parameters
    ----------
    s: str
        String para ser aleatorizada.

    Returns
    -------
    str_camelizada: str
        String com a capitalização de seus caracteres aleatorizados.

    Example
    -------
    >>> __camelizar("mithrandir")
    'MIThRANDIR'
    """

    str_minuscula = [*s.lower()]
    str_camelizada = map(lambda x: x if randint(0, 1) else x.upper(), str_minuscula)
    return ''.join(str_camelizada)


def miguxar(s: str, dialeto: DialetoMiguxes = DialetoMiguxes.MIGUXES_ARCAICO) -> str:

    """
    "Miguxa" uma string.

    Parameters
    ----------

    s: str
        String para ser miguxada

    dialeto: DialetoMiguxes, optional
        O dialeto de miguxês para ser aplicado na string (o 'default' é o miguxês arcaico).

    Returns
    -------

    string_miguxada: str
        A string após ser miguxada.

    Example
    -------
    >>> miguxar("Chorar por uma pessoa que esta morta não é tão triste quanto chorar por uma pessoa que ainda vive mas que a perdemos para sempre.",
    ...             DialetoMiguxes.MIGUXES_MODERNO)
    'xorah por 1 pessoa ke esta morta nau eh tau tristi qtu xorah por 1 pessoa ke ainda vivi mas ke a perdemus p sempre......'
    """

    regexes = DialetoMiguxes.pegar_regex_por_dialeto(dialeto)

    string_miguxada = s.lower()

    for pattern, repl in regexes:
        string_miguxada = re.sub(pattern, repl, string_miguxada)

    if dialeto == DialetoMiguxes.NEO_MIGUXES:
        string_miguxada = re.sub(r'x', 'xXx', s)
        string_miguxada = re.sub(r'ss', 'XX', s)
        string_miguxada = __camelizar(s)
    return string_miguxada
