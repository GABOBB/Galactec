import os

class User():
    '''def __init__(self, N, P):
        self.N = N
        self.P = P'''
        
    def __init__(self,N,U,P,C,F,n,M):
        self.N = N
        self.U = U
        self.C = C
        self.F = F
        self.n = n
        self.M = M
        self.P = P
    
    def chageAD(self, User):
        self.N = User.get_NMBR()
        self.U = User.get_USR()
        self.C = User.get_CRR()
        self.P = User.get_PSSWRD()
        
    '''def __init__(self, nombre, user, mail, psswrd):
        self.N = nombre
        self.U = user
        self.C = mail
        self.P = psswrd
        
                
    def __init__(self):
        self.N = 'Nombre'
        self.U = 'Usuario'
        self.C = 'Correo@gmail.com'
        self.F = None #os.path.join('Auxiliares','defecto.jpg')
        self.n = None
        self.M = None'''
        
    def get_NMBR(self):
        return self.N
    def set_NMBR(self,N):
        self.N = N
        
    def get_PSSWRD(self):
        return self.P
    def set_PSSWRD(self,P):
        self.P = P
        
    def get_USR(self):
        return self.U
    def set_USR(self,U):
        self.U = U
        
    def get_CRR(self):
        return self.C
    def set_CRR(self,crr):
        self.C = crr

    def get_FT(self):
        return self.F
    def set_FT(self,F):
        self.F = F
        
    def get_NV(self):
        return self.n
    def set_NV(self,n):
        self.n = n
    
    def get_MSC(self):
        return self.M
    def set_MSC(self,M): 
        self.M = M