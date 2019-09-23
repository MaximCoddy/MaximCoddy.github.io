import re
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
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
		   'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pow', 'random', 'parseInt',
		   'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'randint', 'pprint', 'open', 'log', 'console', 'assasasa']
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
	for file in fs.find_all('p', {'class': 'code'}):
			text = file.contents[0]
			if text.find('//') != -1:
				comment = '<span class="grey">' + text[text.find('//'):]+'</span>'
				text = text[:text.find('//')]
				
			else:
				comment = ''
			text = re.sub(r'\w{1}=\S', reddy, text)

			text = re.sub(r'stream<', orange, text)
			text = re.sub(r'end<', orange, text)
			text = re.sub(r'sep<', orange, text)
			text = re.sub(r'text<', orange, text)
			for o in operations:
				#s = f' {o} '
				#text = re.sub(s, red, text)  
				text = text.replace(f'{o} ', f'<span class="red">{o} </span>')
			for m in methods:
				text = text.replace(f'{m}(', f'<span class="blue">{m}</span>(')
				#s = f'{m}('
				#text = re.sub(s, blue, text)  
			text = re.sub(r'[-+]?\d+\.?\d*', repl, text)
			text = re.sub(r' / ', red, text)
			text = re.sub(r'\n', '\n<br>\n', text)
			text = re.sub(r'\s{1}=\s{1}', red, text)
			text = re.sub(r'(\x20\x20\x20\x20)', '&nbsp;&nbsp;&nbsp;&nbsp;', text)
			text = re.sub(r'(\'.*?\')', yellow, text)
			text = re.sub(r'(def \w+)', f_name, text)
			text = re.sub(r'true|false', repl, text)
			text = re.sub(r'from ', red, text)
			text = re.sub(r' in ', red, text)
			text = re.sub(r'import ', red, text)
			text = text.replace('var', '<span class="blue">var</span>')
			text = text.replace('console', '<span class="blue">console</span>')
			text = text + comment
			a = fs.new_tag('p')
			a['class'] = 'code'
			a.string = text
			file.replaceWith(a)
html = fs.prettify()
html = html.replace('&gt;', '>')
html = html.replace('&lt;', '<')
with open('out.html', 'wb') as f:

	f.write(html.encode('utf-8'))
