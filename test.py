#print(__file__)

#folder path
import os
dirname = (os.path.dirname(__file__), '..')
#print(dirname)

ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__),'..'))

#print(os.path.join(ROOT, 'data'))

print(type(ROOT +'/data' +'.pdb'))
