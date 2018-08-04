'''This program tells the number that user has guessed.'''
def main():
    """guess my number"""
    m_n = 50
    h_n = 100
    l_n = 0
    g_n = 0
    i_n = 'l'
    while(i_n != 'c'):
        print(m_n)
        i_n = input("Enter 'h' if guess is too high,'l' if its too low.'c' to indicate I guessed correctly")
        if(i_n == 'h'):
            h_n = m_n
            m_n = (h_n + l_n) // 2
        elif(i_n == 'l'):
            l_n = m_n
            m_n = (h_n + l_n) // 2
    print('your guess number is :',m_n)
if __name__== "__main__":
    main()
