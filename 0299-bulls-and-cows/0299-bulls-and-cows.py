class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0

        secret_hash = [0] * 10
        guess_hash = [0] * 10

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                secret_hash[int(secret[i])] += 1
                guess_hash[int(guess[i])] += 1

        for i in range(10):
            cows += min(secret_hash[i], guess_hash[i])

        return str(bulls) + "A" + str(cows) + "B"