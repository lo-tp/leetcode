from sys import maxint


class Solution(object):
    def sampleStats(self, count):
        maximum, minimum, mode, mode_count, total_count, sum, mean, median = - \
            1, maxint, -1, -1, 0, 0, -1, -1
        for i in xrange(0, 256):
            if count[i]:
                maximum = max(maximum, i)
                minimum = min(minimum, i)
                if count[i] > mode_count:
                    mode_count, mode = count[i], i
                total_count += count[i]
                sum += count[i]*i
        mean = sum/float(total_count)
        if total_count % 2:
            t = (total_count+1)/2
            for i in xrange(0, 256):
                if count[i]:
                    median = i
                    t -= count[i]
                    if t < 1:
                        break
        else:
            t = total_count/2
            for i in xrange(0, 256):
                if count[i]:
                    t -= count[i]
                    median = i
                    if t < 1:
                        break
            if t == 0:
                w = -1
                for k in xrange(median+1, 256):
                    if count[k]:
                        w = k
                        break
                median = (w+median)/2.0
        return [round(float(i),5) for i in [minimum, maximum, mean, median, mode]]

