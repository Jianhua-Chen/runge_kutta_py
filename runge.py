import sys

# sets B = A;
def populate_array(DIM, A, B):
    for i in range(0,DIM):
        B[i] = A[i]
# sums the arrays
def sum_array(DIM, y, s,c):
    for k in range(0,DIM):
        s[k] = y[k] + c*s[k]

def runge_drive(DIM, t0,tf, y0,function, err, result):
    magdif =0;
    tstep = t0;
    yf = [0] * DIM
    yfp =[0] * DIM
    populate_array(DIM,y0,yf)
    populate_array(DIM,y0,yfp)
    N = 3
    while True:
        h = (tf-t0)/(N-1)
        for i in range(1,N):
            tstep = t0+(i-1)*h
            k1 = [function(q,tstep,yf) for q in range(0,DIM)]
            k2 = [function(q,tstep+0.5*h,[y+(h/2)*x for y,x in zip(yf,k1)]) for q in range(0,DIM)]
            k3 = [function(q,tstep+0.5*h,[y+(h/2)*x for y,x in zip(yf,k2)]) for q in range(0,DIM)]
            k4 = [function(q,tstep+1.0*h,[y+h*x for y,x in zip(yf,k3)]) for q in range(0,DIM)]
            ystep =[(h/6)*(k1[s]+2*(k2[s]+k3[s])+k4[s]) for s in range(0,DIM)]
            sum_array(DIM, ystep,yf,1.0)
        magdif = abs(yf[0]-yfp[0])/max([abs(yf[0]),abs(yfp[0])])
        for k in range(1,DIM):
            magdif += abs(yf[k]-yfp[k])/max([abs(yf[k]),abs(yfp[k])])
        populate_array(DIM, yf, yfp)
        N = 2*N
        populate_array(DIM,y0,yf)
        if magdif < err:
            break
    populate_array(DIM,yfp,result)
