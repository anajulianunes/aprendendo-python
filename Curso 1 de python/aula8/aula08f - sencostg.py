import math
ang = float(input('Type the angle: '))
rad = math.radians(ang)
print('O cosseno do angulo {} é {:.2f};\nO seno do angulo {} é {:.2f};'.format(ang, math.cos(rad), ang, math.sin(rad)))
print('A tangente do angulo {} é {:.2f}'.format(ang, math.tan(rad)))
