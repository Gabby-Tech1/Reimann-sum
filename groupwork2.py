def m_ln(x, n):
    length = (x-1)/n
    points = [1]
    curr, number = 1, 1
    
    while number <= n:
        points.append(round(curr + length, 2))
        curr = curr + length
        number += 1
        
        final_answer = 0
    for i in range(1, len(points)):
        value = length * 1/((points[i-1] + points[i])/2)
        final_answer += value
        
    return final_answer

ans = m_ln(10, 100)
print(ans)