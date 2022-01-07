s10={1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,18,19}
s11={1,2,4,5,6}
s1={1,2,3}
print(f's1 is subset of s10: {s1.issubset(s10)}')
print(f's10 is superset of s1:{s10.issuperset(s1)}')
print("-------------------------------------")
print(f's1 is subset of s11: {s1.issubset(s11)}')
print(f's11 is superset of s1:{s11.issuperset(s1)}')