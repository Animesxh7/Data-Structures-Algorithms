class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        st = []
        for ch in tokens:
            if ch.lstrip('-').isdigit():
                st.append(int(ch))
            else:
                b = st.pop()
                a = st.pop()
                if ch == '+':
                    st.append(a+b)
                elif ch == '-':
                    st.append(a-b)
                elif ch == '*':
                    st.append(a*b)
                elif ch == '/':
                    st.append(int(a/b))
        return st[-1]
                

