from typing import List


class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        tasks.sort()
        dp = {}
        stack = [(tasks, 0, False)]
        while stack:
            options, total, flag = stack.pop()
            key = str(options + [total])
            if key not in dp:
                if not options:
                    dp[key] = 0
                if flag:
                    dp[key] = 15
                    for i in range(0, len(options)):
                        nextOptions = options[:i] + options[i + 1 :]
                        nextKey = str(
                            nextOptions
                            + [
                                total - options[i]
                                if total >= options[i]
                                else sessionTime - options[i]
                            ]
                        )
                        dp[key] = min(
                            dp[key], dp[nextKey] + (1 if total < options[i] else 0)
                        )
                else:
                    stack.append((options, total, True))
                    for i in range(0, len(options)):
                        nextOptions = options[:i] + options[i + 1 :]
                        stack.append(
                            (
                                nextOptions,
                                (sessionTime if options[i] > total else total)
                                - options[i],
                                False,
                            )
                        )
        return dp[str(tasks + [0])]
