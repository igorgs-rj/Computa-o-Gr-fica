from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import*

r=1.0
h=3.0
n=input("Qual o numero de lados da base da piramide?")
ang=(2*pi)/n

vertices=[[0,h,0]]
linhas=[]
faces=[]
aux=[]

for i in range(0,n):
    c0 = r * cos(ang * i)
    c1 = r * sin(ang * i)
    vertices += [[c0, -h / 2, c1]]

linhas +=[[0, 1]]
linhas +=[[1, n]]
for i in range(2,n+1):
    linhas += [[i-1, i]]
    linhas += [[0, i]]

for i in range(1,n):
    faces += [[i + 1, i, 0]]

faces+=[[n, 1, 0]]
for i in range(1, n + 1):
    aux += [i]
faces += [aux]


#print(vertices)
#print(linhas)
#print(faces)



cores = ((1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 1, 1), (0, 0, 1), (1, 0, 1), (0.5, 1, 1), (1, 0, 0.5),(1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 1, 1), (0, 0, 1))


def Pol():
    glBegin(GL_TRIANGLES)
    i = 0
    for face in faces:
        #glColor3fv(cores[i])   # cor para cada face
        for vertex in face:
            glColor3fv(cores[vertex])   #cor para cada vertice
            glVertex3fv(vertices[vertex])
        i = i + 1
    glEnd()

    glColor3fv((0, 0.5, 0))
    glBegin(GL_LINES)
    for linha in linhas:
        for vertice in linha:
            glVertex3fv(vertices[vertice])
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glRotatef(5, 1, 3, 0) #rota o cubo quanto esta rotando(2) em relacao ao vetor 130
    Pol()
    glutSwapBuffers()

def timer(i):
    glutPostRedisplay() #redesenha a janela
    glutTimerFunc(50, timer, 1) #ao passar esse tempo


# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800, 600) #define a dimensao do janela
glutCreateWindow("Pol")  #nome da janela
glutDisplayFunc(display)  #funcao de callback para repintar a tela
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0., 0., 0., 1.)
gluPerspective(45, 800.0 / 600.0, 0.1, 50.0) #modifica a pespectiva
glTranslatef(0.0, 0.0, -10) #translacao da cena no eixo x ,y ,z
glRotatef(45, 1, 1, 1)       #
glutTimerFunc(50, timer, 1) #redesenha a janela ao chamar a funcao timer
glutMainLoop()
