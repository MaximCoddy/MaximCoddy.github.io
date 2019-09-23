import re
from bs4 import BeautifulSoup

methods = ['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find',
		   'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier',
		   'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip',
		   'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition',
		   'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill',
		   'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort',
		   'clear', 'copy', 'fromkeys', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values', 'dict', 'print',
		   'len', 'float','bool', 'list', 'tupple', 'range', 'close', 'write', 'input', 'acos', 'acosh', 'asin', 'asinh', 'atan',
		   'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'erf', 'erfc', 'exp', 'expm1', 'fabs',
		   'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf',
		   'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pow',
		   'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'randint', 'pprint', 'open', 'log', 'console', 'sdahkhadk']
operations = ['assert','as','with','from','>=', '<=', '+=', '==','-', '**','+', '*', '//', '%', 'if','while', 'for', 'return', 'else', 'elif', 'break','pass','continue']

def repl(m): 
	return '<span class="purple">' + m[0] + '</span>'
def yellow(m):
	return '<span class="yellow">' + m[0] + '</span>'
def red(m):
	return '<span class="red">' + m[0] + '</span>'
def f_name(m):
	d, n = m[0].split(' ')
	return f'<span class="blue">{d}</span> <span class="green">{n}</span>'
def reddy(m):
	s = m[0].split('=')
	return f'{s[0]}<span class="red">=</span>{s[1]}'
def orange(m):
	s = m[0][:-1]
	return f'<span class="orange">{s}</span><'


with open('hw_js1.html', 'r', encoding='utf-8') as f:
	fs = BeautifulSoup(f.read(), 'html.parser')
	codes = [c for c in fs.find_all('p', {'class': 'code'})]
	for file in fs.select('p[class=code]'):
		try:
			file.contents = re.sub(r'\w{1}=\S', reddy, file.contents)
			file.contents = re.sub(r'stream<', orange, file.contents)
			file.contents = re.sub(r'end<', orange, file.contents)
			file.contents = re.sub(r'sep<', orange, file.contents)
			file.contents = re.sub(r'file.contents<', orange, file.contents)
			for o in operations:
				#s = f' {o} '
				#file.contents = re.sub(s, red, file.contents)  
				file.contents.contents = file.contents.replace(f'{o} ', f'<span class="red">{o} </span>')
			for m in methods:
				file.contents = file.contents.replace(f'{m}(', f'<span class="blue">{m}</span>(')
				#s = f'{m}('
				#file.contents = re.sub(s, blue, file.contents)  
			file.contents = re.sub(r'[-+]?\d+\.?\d*', repl, file.contents)
			file.contents = re.sub(r' / ', red, file.contents)
			file.contents = re.sub(r'\n', '\n<br>\n', file.contents)
			file.contents = re.sub(r'\s{1}=\s{1}', red, file.contents)
			file.contents = re.sub(r'(\x20\x20\x20\x20)', '&nbsp;&nbsp;&nbsp;&nbsp;', file.contents)
			file.contents = re.sub(r'(\'.*?\')', yellow, file.contents)
			file.contents = re.sub(r'(def \w+)', f_name, file.contents)
			file.contents = re.sub(r'True|False', repl, file.contents)
			file.contents = re.sub(r'from ', red, file.contents)
			file.contents = re.sub(r' in ', red, file.contents)
			file.contents = re.sub(r'import ', red, file.contents)
			file.contents = file.contents.replace('def', '<span class="green">def</span>')
		except:
			pass
print()