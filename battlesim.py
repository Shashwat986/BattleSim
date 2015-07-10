import random
from collections import defaultdict

matching = defaultdict(int,{
	('P','K'):3,
	('K','G'):3,
	('G','L'):3,
	('L','P'):3,
	('K','P'):-3,
	('G','K'):-3,
	('L','G'):-3,
	('P','L'):-3
})

def dieroll(n):
	return sum([random.randrange(6) + 1 for i in range(n)])

class Player(object):
	def __init__(self,tough,sta,stre,coun):
		self.t = tough
		self.stam = sta
		self.stre = stre
		self.coun = coun
		self.HP = tough * 6 * 4
		self.degree = 1
	
	def move(self):
		s = random.randrange(5 + 10*self.degree + 1)
		d = 5 + 10*self.degree - s
		t = random.choice(['P','K','L','G'])
		return s,d,t
	
	def status(self):
		if self.HP > self.t * 6 * 3: return 0
		if self.HP > self.t * 6 * 2: return 2
		if self.HP > self.t * 6 * 1: return 4
		if self.HP > self.t * 6 * 0: return 6

class Fight(object):
	def __init__(self, p1,p2):
		self.underdog = (p1.t + p2.t + p1.stam + p2.stam) * 6
		self.p1 = p1
		self.p2 = p2
	def calcdmg(self,p1,p2):
		atk_ = dieroll(p1.stre) + s1 + matching[(t1,t2)]
		def_ = dieroll(p2.coun) + s2
		
		if atk_ > def_ :
			p2.HP -= d1

	def fight(self):
		ctr = 1
		p1 = self.p1
		p2 = self.p2
		while (p1.HP > 0 and p2.HP > 0):
			s1,d1,t1 = p1.move()
			s2,d2,t2 = p2.move()
			
			# 1's attack
			atk_ = dieroll(p1.stre) + s1 + matching[(t1,t2)]
			def_ = dieroll(p2.coun) + s2
			if atk_ > def_ :
				p2.HP -= d1
			
			# 2's attack
			atk_ = dieroll(p2.stre) + s2 + matching[(t2,t1)]
			def_ = dieroll(p1.coun) + s1
			if atk_ > def_ :
				p1.HP -= d2

			p1.HP += dieroll(p1.stam)
			p2.HP += dieroll(p2.stam)
			
			a = dieroll(1)
			if a > 4:
				if dieroll(1) > p1.status():
					p1.degree += 1
			if a == 1:
				if dieroll(1) > 3:
					p1.degree -= 1
				else:
					p1.degree -= 2
			
			a = dieroll(1)
			if a > 4:
				if dieroll(1) > p2.status():
					p2.degree += 1
			if a == 1:
				if dieroll(1) > 3:
					p2.degree -= 1
				else:
					p2.degree -= 2
			
			if p1.degree < 0: p1.degree = 0
			if p2.degree < 0: p2.degree = 0
			
			#print "Turn {}: P1 HP = {}; P2 HP = {}".format(ctr,p1.HP, p2.HP)
			ctr += 1
		#print "Player {} Wins!".format(1 if p1.HP > p2.HP else 2)
		return 1 if p1.HP > p2.HP else 2, ctr

ctr = 0
ctrc = 0
for i in range(1000):
	p1 = Player(2,4,2,2)
	p2 = Player(2,3,2,3)
	
	f=Fight(p1,p2)
	p,c = f.fight()
	ctr += p
	ctrc += c

print ctr * 1.0/1000
print ctrc * 1.0/1000

























