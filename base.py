
import math

class Base:
	def __init__(self,base,symbols_map):
		'''
			A robust and very generalized class for representing numbers in different bases
		'''
		self.base = base
		self.symbols_map = symbols_map
		self.symbols_r_map = dict(zip(self.symbols_map.values(),self.symbols_map.keys()))
		
	@classmethod
	def construct(cls, base):
		'''
			This function returns a Base object given an integer value for base
		'''
		b=base
		l_str = 'abcdefghijklmnopqrstuvwxyz~!@#$%^&*()_+{}[];,./?'
		lst = [str(i) for i in range(10)]+ [a for a in l_str]
		return Base(b,dict(zip([i for i in lst[:b]],[i for i in range(b)])))

	def to_base10(self,value):
		'''
			This function converts the given value in self.base to base10
		'''
		r_ = ''
		v_str = list(reversed(str(value)))
		v= 0
		for i in range(len(v_str)):
			v+=((self.base)**i)*self.symbols_map[v_str[i]]
		return v

	def from_b10(self,value):
		'''
			This function returns a str of in base self.base
		'''
		if value!=0:
			r_len = math.ceil(math.log(value)/math.log(self.base))
		else:
			r_len=1
		t_d_vs = [] # this list contains the values of no of multiples of self.base that correspond to tens, hundreds, and thousands etc. for base10
		r_val = value #remainder
		for i in reversed(range(1,r_len+1)):
			v1,r_val = r_val//self.base**i,r_val%self.base**i # no of multiples,remaider
			t_d_vs.append(v1)
		t_d_vs.append(r_val)
		r_str = ''
		for v in t_d_vs:
			r_str=r_str+self.symbols_r_map[v]
		return r_str

