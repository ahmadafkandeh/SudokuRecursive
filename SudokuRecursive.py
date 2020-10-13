# SudokuRecursive
#Recursive sudoku solver in Python
#Source code:

# Hi, this is a sudoku solver application based on Jadi Mirmirani's video
# I just created a prettier UI.
# Ahmad Afkandeh (Arta)
# Jadi's Website: www.jadi.net
# video: https://www.youtube.com/watch?v=EWNyZGyEPHc

from array import *
import collections
class sudoku:
	def __init__(self):
		self.chart = [
		[5, 3, 0, 0, 7, 0, 0, 0, 0],
		[6, 0, 0, 1, 9, 5, 0, 0, 0],
		[0, 9, 8, 0, 0, 0, 0, 6, 0],
		[8, 0, 0, 0, 6, 0, 0, 0, 3],
		[4, 0, 0, 8, 0, 3, 0, 0, 1],
		[7, 0, 0, 0, 2, 0, 0, 0, 6],
		[0, 6, 0, 0, 0, 0, 2, 8, 0],
		[0, 0, 0, 4, 1, 9, 0, 0, 5],
		[0, 0, 0, 0, 8, 0, 0, 7, 9]]
		self.Draw()
		
	def printFirstHorizLine(self):
		print('┌' , end='')
		for i in range (0,9*2+5 ):
			if int((i+1)%8) == 0 and i<8*3:
				print('┬',end='')
			else:
				print('―',end='')
		print('┐')
	def printTerminatorHorizLine(self):
		print('└' , end='')
		for i in range (0,9*2+5 ):
			if int((i+1)%8) == 0 and i<8*3:
				print('┴',end='')
			else:
				print('―',end='')
		print('┘')
	def printInternalHorizLine(self):
		print('├',end='')
		for i in range (0,9*2+5 ):
			if int((i+1)%8) == 0 and i<8*3:
				print('┼',end='')
			else:
				print('―',end='')
		print('┤')
		
	def Draw(self):
		self.printFirstHorizLine()
		for y in range (0,9):
			for x in range (0,9):
				if(int(x%3) == 0):
					print('|',end=' ')
				print (self.chart[y][x] , end = " ")
			
			if(int((y+1)%3) == 0 and y<8):
				print('|')
				self.printInternalHorizLine()
			else:
				print('|')
		self.printTerminatorHorizLine()
	def findFree(self):
		Point = collections.namedtuple('Point', ['x', 'y'])
		
		for y in range (0,9):
			for x in range (0,9):
				if ( self.chart[y][x] == 0 ):
					return Point(x,y)
		return Point(-1,-1);
		
	def isValid(self, n , x, y):
		#print(" n : {}, x : {} , y: {}".format(n, x, y))
		for i in range (0,9):
			if ( self.chart[i][x] == n or self.chart[y][i] == n ):
				return False
		x_Square = int(x/3) * 3
		y_Square = int(y/3) * 3
		for j in range (y_Square, y_Square +3):
			for i in range (x_Square, x_Square +3):
				if (self.chart[j][i] == n):
					return False
		return True
	
	def solve(self):
		var= self.findFree()
		x= var[0]
		y = var[1]
		#print (var)
		if (x == -1):
			return True
		for i in range (1,9+1):
			if( self.isValid(i,x,y)):
				self.chart[y][x] = i
				if(self.solve()):
					return True
				self.chart[y][x] = 0
		return False

if __name__=="__main__":
	var = sudoku()
	print('Solved table:')
	var.solve()
	var.Draw()


