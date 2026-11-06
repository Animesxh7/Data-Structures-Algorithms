class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        st = []
        for i in asteroids:
            while st and st[-1]>0 and i<0:
                if st[-1]>abs(i):
                    break
                elif st[-1]<abs(i):
                    st.pop()
                else:
                    st.pop()
                    break
            else:
                st.append(i)
        return st