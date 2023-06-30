if __name__ == '__main__':
    sentence = list(map(str, input().split()))
    length = len(sentence)
    word = ''
    for i in range(length-1, -1 , -1):
        word += sentence[i]+ " "
    print(word)
    
