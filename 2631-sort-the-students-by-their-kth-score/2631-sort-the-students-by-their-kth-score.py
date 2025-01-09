class Solution(object):
    def sortTheStudents(self, score, k):
        score.sort(key=lambda x: -x[k])
        return score
        