import re


ora_sft_map = {
    'YYYY': '%Y',
    'YY': '%y',
    'MM': '%m',
    'MONTH': '%B',
    'MON': '%b',
    'DDD': '%j',
    'DD': '%d',
    'DY': '%a',
    'DAY': '%A',
    'HH24': '%H',
    'HH12': '%I',
    'HH': '%I',
    'MI': '%M',
    'SSSS': '%f',
    'SS': '%S',
    'AM': '%p',
    'PM': '%p',
    'TZD': '%Z',
    'TZR': '%z',
    'TZ': '%Z',
}

sft_ora_map = {v: k for k, v in ora_sft_map.items()}



def ora_to_sft(ora_mask: str) -> str:
    if ora_mask:
        ora_mask = ora_mask.upper()
        mask_elems = '|'.join(list(ora_sft_map.keys()))
        pattern = re.compile(fr'({mask_elems})')
        result = re.sub(pattern, lambda x: ora_sft_map[x.group()], ora_mask)
        return result
    else:
        return ''


def sft_to_ora(sft_mask: str) -> str:
    if sft_mask:
        mask_elems = '|'.join(list(sft_ora_map.keys()))
        pattern = re.compile(fr'({mask_elems})')
        result = re.sub(pattern, lambda x: sft_ora_map[x.group()], sft_mask)
        return result
    else:
        return ''
