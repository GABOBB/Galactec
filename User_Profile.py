class User():
    def __init__(self,Nombre,Usuario,correo,foto,nave,musica):
        self.N = Nombre
        self.U = Usuario
        self.C = correo
        self.F = foto
        self.n = nave
        self.M = musica
        
    def get_NMBR(self):
        return self.N
    def set_NMBR(self,N):
        self.N = N
        
    def get_USR(self):
        return self.U
    def set_USR(self,U):
        self.U = U
        
    def get_CRR(self):
        return self.C
    def set_CRR(self,crr):
        self.C = crr

    def get_Ft(self):
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