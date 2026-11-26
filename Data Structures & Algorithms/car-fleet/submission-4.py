class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        a = sorted(list(zip(position,speed)),key = lambda x: x[0],reverse = True)
        position = [a[i][0] for i in range(len(a))]
        speed = [a[i][1] for i in range(len(a))]
        print(position,speed)
        steps = [(target-position[i]) / speed[i] for i in range(len(position))]
        print(steps)
        ans = 0
        while steps:
            ans += 1
            head = steps[0]
            steps = steps[1:]
            stack = [head]
            next_steps = []
            for step in steps:
                if step > head:
                    next_steps.append(step)
                # print(next_steps,head)
            steps = next_steps
            print(steps)
        return ans