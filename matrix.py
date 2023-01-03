def read(r,c,mat):
    # For user input 
    for i in range(r): # for loop for row entries 
        a =[] 
        for j in range(c): # for loop for column entries 
            a.append(int(input())) 
            mat.append(a) # store complete row in matirx
def dis(r,c,mat):
    # For printing the matrix 
    for i in range(r): 
        for j in range(c): 
            print(mat[i][j], end = " ") 
    print() 
def add(r,c,mat1,mat2):
    res=[] # resultant matrix
    for i in range(r):
        a=[] # array
        for j in range(c):
            a.append(mat1[i][j]+mat2[i][j])
            res.append(a)
    print("Resultant addition is as follows:")
    dis(r,c,res)
def mul(r1,c1,r2,c2,mat1,mat2):
    res=[]
    for i in range(r1):
        a=[]
        for j in range(c2):
            sum=0
            for k in range(c1):
                sum=sum+mat1[i][k]*mat2[k][j]
                a.append(sum)
                res.append(a)
    print("Resultant multiplication is as follows:")
    dis(r1,c2,res)
def transpose(r,c,mat):
    res=[]
    for i in range(c):
        a=[]
        for j in range(r):
            a.append(mat[j][i])
            res.append(a)
     
    dis(c,r,res)
def main():
    r1 = int(input("Enter the number of rows of first matrix:")) 
    c1 = int(input("Enter the number of columns of first matrix:"))
    r2 = int(input("Enter the number of rows of second matrix:")) 
    c2 = int(input("Enter the number of columns of second matrix:"))
     
    # Declare two matrices
    mat1 = []
    mat2 = []
     
    print("Enter the entries rowwise of first matrix:") 
    read(r1,c1,mat1)
    print("Enter the entries rowwise of second matrix:")
    read(r2,c2,mat2)
    print("First matrix is as follows:") 
    dis(r1,c1,mat1)
    print("Second matrix is as follows:")
    dis(r2,c2,mat2)
     
    if(r1==r2 and c1==c2):
        add(r1,c1,mat1,mat2)
    else:
        print("\n Addition is not possible")
    
    if(c1==r2):
        mul(r1,c1,r2,c2,mat1,mat2)
    else:
        print("\n Multiplication is not possible")
    print("Resultant transpose of first matrix is as follows:") 
    transpose(r1,c1,mat1)
    print("Resultant transpose of second matrix is as follows:")
    transpose(r2,c2,mat2)
 
main()
