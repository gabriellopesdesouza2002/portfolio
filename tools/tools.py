def convert_bytes_to(tamanho: int|float):
    """Converte os bytes para
    
    >>> B = Byte

    >>> K = Kilo

    >>> M = Mega

    >>> G = Giga

    >>> T = Tera

    >>> P = Peta

    
    ### Utiliza-se a base 1024 ao invés de 1000

    Use:
        >>> tamanho_do_arquivo_em_bytes = os.path.getsize('C:\\MeuArquivo.txt')
        >>> print(tamanho_do_arquivo_em_bytes)
        >>>> 3923 
        >>> print(convert_bytes(tamanho_do_arquivo))
        >>>> '3.83 K'

    Args:
        tamanho (int|float): Tamanho do arquivo em bytes, pode ser utilizado o os.path.getsize(file)

    Returns:
        str: Valor do tamanho em B; K; M; G; T; P -> 
    """
    base = 1024
    kilo = base # K
    mega = base ** 2 # M
    giga = base ** 3 # G
    tera = base ** 4 # T
    peta = base ** 5 # P
    
    # se o tamanho é menor que kilo (K) é Byte
    # se o tamanho é menor que mega (M) é Kb
    # se o tamanho é menor que giga (G) é MB e assim por diante
    
    if isinstance(tamanho, (int, float)):
        pass
    else:
        print('Tentando converter o valor do parâmetro tamanho...')
        try:
            tamanho = float(tamanho)
        except ValueError as e:
            if 'could not convert string to float' in str(e):
                print(f'Não foi possível converter o tamanho ++ {tamanho} ++ para float!')
                return 'ValueError'
    if tamanho < kilo:
        tamanho = tamanho
        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'K'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'M'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'G'
    elif tamanho < peta:
        tamanho /= tera
        texto = 'T'
    else:
        tamanho /= peta
        texto = 'P'
        
    tamanho = round(tamanho, 2)
    
    return f'{tamanho} {texto}'.replace('.', ',')